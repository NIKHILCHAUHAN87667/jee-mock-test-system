import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector
from mysql_connection import create_connection  # Import database connection
import csv

def create_rounded_button(parent, text, command, color, y_pos):
    """Function to create rounded buttons."""
    button = tk.Button(parent, text=text, command=command, bg=color, fg="white",
                       font=("Arial", 12, "bold"), relief="flat", bd=0, width=20, height=2)
    button.place(relx=0.5, y=y_pos, anchor="center")
    return button
def add_question():
    """Function to add a question to the database."""
    root = tk.Tk()
    root.title("Add Question")
    root.geometry("500x500")
    root.configure(bg="#D3D3D3")

    tk.Label(root, text="ADD QUESTION", font=("Arial", 18, "bold"), bg="#D3D3D3").pack(pady=30)

    # Entry fields
    tk.Label(root, text="Subject:", font=("Arial", 12), bg="#D3D3D3").pack()
    subject_entry = tk.Entry(root, font=("Arial", 12))
    subject_entry.pack(pady=5)

    tk.Label(root, text="Question:", font=("Arial", 12), bg="#D3D3D3").pack()
    question_entry = tk.Entry(root, font=("Arial", 12))
    question_entry.pack(pady=5)

    tk.Label(root, text="Option A:", font=("Arial", 12), bg="#D3D3D3").pack()
    option_a_entry = tk.Entry(root, font=("Arial", 12))
    option_a_entry.pack(pady=5)

    tk.Label(root, text="Option B:", font=("Arial", 12), bg="#D3D3D3").pack()
    option_b_entry = tk.Entry(root, font=("Arial", 12))
    option_b_entry.pack(pady=5)

    tk.Label(root, text="Option C:", font=("Arial", 12), bg="#D3D3D3").pack()
    option_c_entry = tk.Entry(root, font=("Arial", 12))
    option_c_entry.pack(pady=5)

    tk.Label(root, text="Option D:", font=("Arial", 12), bg="#D3D3D3").pack()
    option_d_entry = tk.Entry(root, font=("Arial", 12))
    option_d_entry.pack(pady=5)

    tk.Label(root, text="Correct Option:", font=("Arial", 12), bg="#D3D3D3").pack()
    correct_option_entry = tk.Entry(root, font=("Arial", 12))
    correct_option_entry.pack(pady=5)

    tk.Label(root, text="Diagram:", font=("Arial", 12), bg="#D3D3D3").pack()
    diagram_entry = tk.Entry(root, font=("Arial", 12))
    diagram_entry.pack(pady=5)

def delete_question():
    """Function to delete a question from the database."""
    root = tk.Tk()
    root.title("Delete Question")
    root.geometry("500x500")
    root.configure(bg="#D3D3D3")

    tk.Label(root, text="DELETE QUESTION", font=("Arial", 18, "bold"), bg="#D3D3D3").pack(pady=30)

    # Entry field
    tk.Label(root, text="Question ID:", font=("Arial", 12), bg="#D3D3D3").pack()
    question_id_entry = tk.Entry(root, font=("Arial", 12))
    question_id_entry.pack(pady=5)

    # Button
    delete_button = create_rounded_button(root, "DELETE", None, "#D62828", 200)

    root.mainloop()
    
    # Add the delete logic here


def admin_dashboard():
    """Admin Dashboard UI"""
    root = tk.Tk()
    root.title("Admin Dashboard")
    root.geometry("500x500")
    root.configure(bg="#D3D3D3")

    tk.Label(root, text="ADMIN DASHBOARD", font=("Arial", 18, "bold"), bg="#D3D3D3").pack(pady=30)

    # Buttons
    create_rounded_button(root, "ADD QUESTION", add_question, "#1E90FF", 120)
    create_rounded_button(root, "DELETE QUESTION", delete_question, "#D62828", 180)
    create_rounded_button(root, "UPLOAD QUESTION BANK", upload_question_bank, "#32CD32", 240)
    create_rounded_button(root, "EXIT", root.quit, "#20B2AA", 300)

    root.mainloop()

def upload_question_bank():
    """Function to upload questions from a CSV file into the database."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    
    if not file_path:
        return  # User canceled file selection
    
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row

            conn = create_connection()
            if conn:
                cursor = conn.cursor()
                query = """INSERT INTO question_bank 
                           (subject, question, option_a, option_b, option_c, option_d, correct_option, diagram) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

                for row in csv_reader:
                    if len(row) != 8:  # Ensure correct column count
                        messagebox.showerror("Error", "CSV format incorrect!")
                        return
                    
                    cursor.execute(query, row)

                conn.commit()
                cursor.close()
                conn.close()
                
                messagebox.showinfo("Success", "Questions uploaded successfully!")
    except Exception as e:
        messagebox.showerror("Upload Error", f"Error processing file: {str(e)}")

# Run the admin dashboard














    

