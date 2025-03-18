import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import mysql.connector
from mysql_connection import create_connection

def take_test(user_id):
    
    def fetch_questions(subject, num_questions=30):
        """Fetch random MCQs from the database based on subject."""
        conn = create_connection()
        if conn:
            try:
                cursor = conn.cursor(dictionary=True)
                query = """SELECT question_id, question, option_a, option_b, option_c, option_d, correct_option 
                           FROM question_bank 
                           WHERE LOWER(subject) = LOWER(%s) AND correct_option IS NOT NULL
                           ORDER BY RAND() LIMIT %s"""
                cursor.execute(query, (subject, num_questions))
                questions = cursor.fetchall()
                return questions
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
                return []
            finally:
                cursor.close()
                conn.close()
        return []

    def start_test(subject):
        """Launches the test window with structured layout (Only MCQs)."""
        if subject == "Full Test (PCM)":
            questions = fetch_questions("Physics", 30) + fetch_questions("Chemistry", 30) + fetch_questions("Maths", 30)
        else:
            questions = fetch_questions(subject, 90)

        if not questions:
            messagebox.showerror("Error", f"No MCQs available for {subject}.")
            return

        test_window = tk.Toplevel(root)
        test_window.title(f"{subject} Mock Test")
        test_window.geometry("1000x600")

        user_answers = [None] * len(questions)
        current_question = 0
        buttons = []
        start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Frames for Layout
        left_frame = tk.Frame(test_window, width=250)
        left_frame.pack(side="left", fill="y", padx=20, pady=20)

        top_frame = tk.Frame(test_window)
        top_frame.pack(fill="both", side="top", padx=20, pady=20)

        # Scrollable Right Frame
        right_frame = tk.Frame(test_window, width=250)
        right_frame.pack(side="right", fill="y", anchor="n", padx=20, pady=20)

        canvas = tk.Canvas(right_frame)
        scrollbar = tk.Scrollbar(right_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Timer
        time_left = 10800  # 3-hour test
        timer_label = tk.Label(top_frame, text=f"Time Left: {time_left // 60} min", font=("Arial", 16), fg="red")
        timer_label.pack(pady=10)

        def update_timer():
            nonlocal time_left
            if time_left > 0:
                time_left -= 1
                mins, secs = divmod(time_left, 60)
                if test_window.winfo_exists():  # Ensure window still exists
                    timer_label.config(text=f"Time Left: {mins:02}:{secs:02}")
                    test_window.after(1000, update_timer)
            else:
                if test_window.winfo_exists():
                    messagebox.showinfo("Time's Up", "Your time is up! Test has ended.")
                    submit_test(user_id, questions, option_widgets, user_answers, start_time, submit_btn)  # Auto-submit
                    test_window.destroy()  # Close the test window

        update_timer()

        # Question Label
        question_label = tk.Label(left_frame, text="", font=("Arial", 16), wraplength=700, pady=20)
        question_label.pack()

        # Answer Options (Inside Left Frame)
        selected_answer = tk.StringVar()
        option_widgets = []

        for i in range(len(questions)):
            opt1 = tk.Radiobutton(left_frame, text="", variable=selected_answer, value="", font=("Arial", 14), anchor="w")
            opt2 = tk.Radiobutton(left_frame, text="", variable=selected_answer, value="", font=("Arial", 14), anchor="w")
            opt3 = tk.Radiobutton(left_frame, text="", variable=selected_answer, value="", font=("Arial", 14), anchor="w")
            opt4 = tk.Radiobutton(left_frame, text="", variable=selected_answer, value="", font=("Arial", 14), anchor="w")
            option_widgets.append([opt1, opt2, opt3, opt4])
        
        bottom_frame = tk.Frame(left_frame)  

        save_btn = tk.Button(bottom_frame, text="Save Answer", font=("Arial", 14), bg="#4682B4", fg="white",
                            padx=10, pady=5, command=lambda: save_answer())
        submit_btn = tk.Button(bottom_frame, text="Submit Test", font=("Arial", 14), bg="green", fg="white", padx=10, pady=5,
                            command=lambda: submit_test(user_id, questions, option_widgets, user_answers, start_time, submit_btn))

        save_btn.pack(side="left", padx=10)
        submit_btn.pack(side="right", padx=10)

        def load_buttons():
            """Loads the bottom frame with Save and Submit buttons."""
            bottom_frame.pack(fill="x", pady=20)

        # Subject Sections & Navigation Buttons
        def add_subject_section(subject_name, start_idx):
            subject_label = tk.Label(scrollable_frame, text=f"{subject_name} Section", font=("Arial", 14, "bold"))
            subject_label.pack(pady=5)

            frame = tk.Frame(scrollable_frame)
            frame.pack()

            for i in range(6):
                row_frame = tk.Frame(frame)
                row_frame.pack()
                for j in range(5):
                    q_num = start_idx + (i * 5 + j)
                    if q_num < len(questions):
                        btn = tk.Button(row_frame, text=str(q_num + 1), width=5, font=("Arial", 12),
                                        command=lambda q=q_num: load_question(q))
                        btn.pack(side="left", padx=5, pady=5)
                        buttons.append(btn)

        if subject == "Full Test (PCM)":
            add_subject_section("Physics", 0)
            add_subject_section("Chemistry", 30)
            add_subject_section("Maths", 60)
        else:
            add_subject_section(subject, 0)

        def update_navigation():
            """Updates button colors for saved answers."""
            for i, btn in enumerate(buttons):
                btn.config(relief="raised", bg="SystemButtonFace")
                if user_answers[i]:
                    btn.config(bg="lightgreen")  # Answer saved
                if i == current_question:
                    btn.config(relief="sunken", underline=True)  # Current question

        def load_question(idx):
            """Loads question into UI."""
            nonlocal current_question
            current_question = idx
            q = questions[idx]
            question_label.config(text=f"Q{idx + 1}: {q['question']}")
            selected_answer.set(user_answers[idx] if user_answers[idx] else " ")
            for widget_set in option_widgets:
                for widget in widget_set:
                    widget.pack_forget()
                    bottom_frame.pack_forget() 
                
                    # Unpack all option widgets
            for j, opt in enumerate(['option_a', 'option_b', 'option_c', 'option_d']):
                option_widgets[idx][j].config(text=q[opt], value=q[opt])
                option_widgets[idx][j].pack(fill="x", padx=10, pady=5)
                
            
            # Load buttons after options
            left_frame.update_idletasks()
            load_buttons()
                
            update_navigation()

        def save_answer():
            """Saves user's answer."""
            user_answers[current_question] = selected_answer.get()
            update_navigation()
        

        load_question(0)
        

    def save_mock_test(question_ids):
        """Insert test_id into mock_test and return the generated test_id."""
        conn = create_connection()

        if conn:
            try:
                cursor = conn.cursor()

                # Insert a new row in mock_test to generate a test_id
                query = "INSERT INTO mock_test (question_id) VALUES (%s)"
                values = [(qid,) for qid in question_ids]

                cursor.executemany(query, values)
                conn.commit()

                # Get the generated test_id
                cursor.execute("SELECT LAST_INSERT_ID()")
                test_id = cursor.fetchone()[0]

                return test_id  # Return the generated test_id
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
                return None
            finally:
                cursor.close()
                conn.close()

    def save_test_result(test_id, user_id, start_time, end_time, score):
        """Insert into attempt_test only after test_id exists in mock_test."""
        conn = create_connection()

        if conn:
            try:
                cursor = conn.cursor()

                # Ensure test_id exists in mock_test before inserting into attempt_test
                cursor.execute("SELECT test_id FROM mock_test WHERE test_id = %s", (test_id,))
                if not cursor.fetchone():
                    messagebox.showerror("Database Error", f"test_id {test_id} does not exist in mock_test")
                    return

                query_attempt = """
                    INSERT INTO attempt_test (test_id, user_id, start_time, end_time, score)
                    VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(query_attempt, (test_id, user_id, start_time, end_time, score))

                conn.commit()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    def update_performance(user_id):
        """Updates the performance table with the best score, average score, and total tests from the mock_test table."""
        conn = create_connection()

        if conn:
            try:
                cursor = conn.cursor()

                # Fetch best score, average score, and total tests from mock_test table
                cursor.execute("""
                    SELECT MAX(score), AVG(score), COUNT(*) 
                    FROM attempt_test 
                    WHERE user_id = %s
                """, (user_id,))
                result = cursor.fetchone()

                if result:
                    best_score, avg_score, total_tests = result

                    if best_score is not None and avg_score is not None:
                        # Check if the user already has a record in performance table
                        cursor.execute("SELECT user_id FROM performance WHERE user_id = %s", (user_id,))
                        existing_record = cursor.fetchone()

                        if existing_record:
                            # Update existing record
                            cursor.execute("""
                                UPDATE performance 
                                SET best_score = %s, average_score = %s, total_tests = %s 
                                WHERE user_id = %s
                            """, (best_score, avg_score, total_tests, user_id))
                        else:
                            # Insert new record
                            cursor.execute("""
                                INSERT INTO performance (user_id, best_score, average_score, total_tests) 
                                VALUES (%s, %s, %s, %s)
                            """, (user_id, best_score, avg_score, total_tests))

                        conn.commit()
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()

    # Submit Test Function
    def submit_test(user_id, questions, option_widgets, user_answers, start_time, submit_btn):
        """Handles test submission, highlights correct/incorrect answers, and stores results."""
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        score = 0

        question_ids = [q['question_id'] for q in questions]
        test_id = save_mock_test(question_ids)

        if test_id:
            for i, q in enumerate(questions):
                correct_answer = q['correct_option']
                user_answer = user_answers[i] if i < len(user_answers) else None

                for j, opt in enumerate(['option_a', 'option_b', 'option_c', 'option_d']):
                    option_text = q[opt]
                    option_widget = option_widgets[i][j]

                    if option_text == correct_answer:
                        option_widget.config(fg="green")

                    if user_answer == option_text:
                        if user_answer == correct_answer:
                            option_widget.config(text=f" ✅  {option_text}")
                            score += 4
                        elif user_answer != correct_answer and user_answer == option_text:
                            option_widget.config(text=f" ❌  {option_text}")
                            score -= 1

                    option_widget.config(state="disabled")

            submit_btn.config(state="disabled")
            save_test_result(test_id, user_id, start_time, end_time, score)
            messagebox.showinfo("Test Completed", f"Your Score: {score} / {len(questions) * 4}")
            update_performance(user_id)

    root = tk.Tk()
    root.title("JEE Mock Test")
    root.geometry("600x400")

    tk.Label(root, text="Select a Test", font=("Arial", 18, "bold")).pack(pady=20)

    tk.Button(root, text="Full Test (PCM)", font="Arial 14", bg="#4682B4", fg='white',
              command=lambda: start_test("Full Test (PCM)")).pack(pady=10)

    tk.Button(root, text="Physics Test", font="Arial 14", bg="#4682B4", fg='white',
              command=lambda: start_test("Physics")).pack(pady=10)

    tk.Button(root, text="Chemistry Test", font="Arial 14", bg="#4682B4", fg='white',
              command=lambda: start_test("Chemistry")).pack(pady=10)

    tk.Button(root, text="Maths Test", font="Arial 14", bg="#4682B4", fg='white',
              command=lambda: start_test("Maths")).pack(pady=10)

    root.mainloop()

