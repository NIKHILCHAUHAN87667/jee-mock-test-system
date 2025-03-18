import tkinter as tk
from mysql_connection import create_connection
import bcrypt
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox
from student_dashboard import student_window  # Import the student_window function
from admin import admin_dashboard

def on_entry_click(event, entry, default_text):
    """Function to remove placeholder text on click."""
    if entry.get() == default_text:
        entry.delete(0, tk.END)
        entry.config(fg="black")

def on_focus_out(event, entry, default_text):
    """Function to restore placeholder text if empty."""
    if not entry.get():
        entry.insert(0, default_text)
        entry.config(fg="gray")

def login(name_frame, email_frame, password_frame, role_var,root1):
    
    # Get user input
    name = name_frame.get()
    email = email_frame.get()
    password = password_frame.get()
    role = role_var.get()

    # Validate input fields
    if name and email and password and role:
        conn = create_connection()  # Function to establish database connection
        if conn:
            try:
                cursor = conn.cursor()

                # Query to fetch the hashed password from the database
                cursor.execute("SELECT password,user_id FROM user WHERE email = %s", (email,))
                stored_hash = cursor.fetchone()

                

                if stored_hash:
                    # Verify password using bcrypt
                    if bcrypt.checkpw(password.encode('utf-8'), stored_hash[0].encode('utf-8')):
                        messagebox.showinfo("Success", "Login successful!")
                        if role == "Student":
                        # Open the student dashboard window and pass the name
                            root1.withdraw()
                            student_window(name,user_id=stored_hash[1])
                            
                                
                        else:
                            root1.withdraw()
                            admin_dashboard()
                            
                            
                    else:
                        messagebox.showerror("Error", "Incorrect password.")
                else:
                    messagebox.showerror("Error", "Email not found.")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Connection Error", "Could not connect to the database.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

    return None  # Return None if login fails








def signup(entry_name_signup, entry_email_signup, entry_password_signup, role_var_signup):
    name = entry_name_signup.get()
    email = entry_email_signup.get()
    password = entry_password_signup.get()
    role = role_var_signup.get()

    if name and email and password and role :
        conn = create_connection()
        if conn:
            try:
                cursor=conn.cursor()

                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                cursor.execute("INSERT INTO user (name, email, password, role) VALUES (%s, %s, %s, %s)", (name,email,hashed_password,role) )

                conn.commit()

                messagebox.showinfo("Success", "Signup successful!")

                entry_name_signup.delete(0, tk.END)
                entry_email_signup.delete(0, tk.END)
                entry_password_signup.delete(0, tk.END)

            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error: {err}")
            finally:
                cursor.close()
                conn.close()
        else:
            messagebox.showerror("Connection Error", "Could not connect to the database.")
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

    # Here you would add the code to insert the user data into the database
    print(f"Signup successful! Name: {name}, Email: {email}, Password: {password}, Role: {role}")
    messagebox.showinfo("Success", f"Registration Successful for {role}")

# Function to open the Login Window
# Store image references globally or inside the function
def create_login_window():
    root.withdraw()  # Close the main window
    root1 = tk.Toplevel()
    root1.title("Login UI")
    root1.geometry("900x600")
    root1.configure(bg="black")

    # Create Canvas
    canvas = tk.Canvas(root1, width=900, height=600, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    # Load and place the left panel image
    left_image = Image.open("login_image2.png").resize((450, 600))
    left_photo = ImageTk.PhotoImage(left_image)
    canvas.create_image(0, 0, anchor="nw", image=left_photo)

    # Right Panel
    canvas.create_rectangle(450, 0, 900, 600, fill="black")

    # Profile Icon
    profile_image = Image.open("user.png").resize((80, 80))
    profile_photo = ImageTk.PhotoImage(profile_image)
    canvas.create_image(675, 100, anchor="center", image=profile_photo)

    # Sign In Text
    canvas.create_text(675, 160, text="Sign In", fill="white", font=("Arial", 18, "bold"))

    # Username Input Box
    username_entry = tk.Entry(root1, width=30, font=("Arial", 12))
    username_entry.place(x=560, y=200, height=35)
    username_entry.insert(0, "Username")
    username_entry.config(fg="gray")
    username_entry.bind("<FocusIn>", lambda event: on_entry_click(event, username_entry, "Username"))
    username_entry.bind("<FocusOut>", lambda event: on_focus_out(event, username_entry, "Username"))

    # Email Input Box
    email_entry = tk.Entry(root1, width=30, font=("Arial", 12))
    email_entry.place(x=560, y=260, height=35)
    email_entry.insert(0, "Email")
    email_entry.config(fg="gray")
    email_entry.bind("<FocusIn>", lambda event: on_entry_click(event, email_entry, "Email"))
    email_entry.bind("<FocusOut>", lambda event: on_focus_out(event, email_entry, "Email"))

    # Password Input Box
    password_entry = tk.Entry(root1, width=30, font=("Arial", 12), show="*")
    password_entry.place(x=560, y=320, height=35)
    password_entry.insert(0, "Password")
    password_entry.config(fg="gray")
    password_entry.bind("<FocusIn>", lambda event: on_entry_click(event, password_entry, "Password"))
    password_entry.bind("<FocusOut>", lambda event: on_focus_out(event, password_entry, "Password"))

    # Role Selection (Radio Buttons)
    role_var = tk.StringVar()
    role_var.set("Student")  # Default role

    student_radio = tk.Radiobutton(root1, text="Student", variable=role_var,selectcolor="black", value="Student", bg="black", fg="white", font=("Arial", 12))
    student_radio.place(x=560, y=380)

    admin_radio = tk.Radiobutton(root1, text="Admin", variable=role_var,selectcolor="black", value="Admin", bg="black", fg="white", font=("Arial", 12))
    admin_radio.place(x=680, y=380)

    # Login Button
    def create_rounded_button(canvas, x, y, width, height, radius, text, command):
    # Draw the rounded rectangle background
        button_bg = canvas.create_arc(x, y, x + 2 * radius, y + 2 * radius, start=90, extent=90, fill="#007BFF", outline="#007BFF")
        arc2 = canvas.create_arc(x + width - 2 * radius, y, x + width, y + 2 * radius, start=0, extent=90, fill="#007BFF", outline="#007BFF")
        arc3 = canvas.create_arc(x, y + height - 2 * radius, x + 2 * radius, y + height, start=180, extent=90, fill="#007BFF", outline="#007BFF")
        arc4 = canvas.create_arc(x + width - 2 * radius, y + height - 2 * radius, x + width, y + height, start=270, extent=90, fill="#007BFF", outline="#007BFF")

        # Draw the main button body
        button_rect1 = canvas.create_rectangle(x + radius, y, x + width - radius, y + height, fill="#007BFF", outline="#007BFF")
        button_rect2 = canvas.create_rectangle(x, y + radius, x + width, y + height - radius, fill="#007BFF", outline="#007BFF")

        # Draw button text
        button_text = canvas.create_text(x + width / 2, y + height / 2, text=text, font=("Arial", 12, "bold"), fill="white")

        # Function to simulate button press
        def on_click(event):
            command()

        # Function to change color on hover
        def on_hover(event):
            for item in [button_bg, arc2, arc3, arc4, button_rect1, button_rect2]:
                canvas.itemconfig(item, fill="#0056b3", outline="#0056b3")

        def on_leave(event):
            for item in [button_bg, arc2, arc3, arc4, button_rect1, button_rect2]:
                canvas.itemconfig(item, fill="#007BFF", outline="#007BFF")

        # Bind events to all button parts
        for item in [button_bg, arc2, arc3, arc4, button_rect1, button_rect2, button_text]:
            canvas.tag_bind(item, "<Button-1>", on_click)
            canvas.tag_bind(item, "<Enter>", on_hover)
            canvas.tag_bind(item, "<Leave>", on_leave)

    

    # Create the rounded login button
    create_rounded_button(canvas, 610, 440, 180, 40, 10, "LOGIN", lambda: login(username_entry, email_entry, password_entry, role_var,root1))

    
      # Increased padding for better spacing

    

    

    # Sign Up Text
    sign_up_label = tk.Label(root1, text="No account yet? Sign Up NOW", fg="lightblue",font="lucida 14 underline", bg="black", cursor="hand2")
    sign_up_label.bind("<Button-1>", lambda e: open_signup_window())
    sign_up_label.place(x=600, y=520)

    root1.mainloop()

 # Start the Tkinter main loop






# Function to open the Signup Window
def open_signup_window(event=None):
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("800x600")
    signup_window.configure(bg="#333333")

    # Title
    tk.Label(signup_window, text="REGISTER YOURSELF!", font=("lucida", 18), bg="#333333", fg="light blue").pack(pady=20)

    # Name Field
    tk.Label(signup_window, text="Name:", bg="#333333", fg="white", font=("lucida", 12)).pack(anchor="w", padx=50, pady=5)
    entry_name_signup = tk.Entry(signup_window, font=("Arial", 12), relief="sunken")
    entry_name_signup.pack(padx=50, fill="x")

    # Email Field
    tk.Label(signup_window, text="Email:", bg="#333333", fg="white", font=("lucida", 12)).pack(anchor="w", padx=50, pady=5)
    entry_email_signup = tk.Entry(signup_window, font=("lucida", 12), relief="sunken")
    entry_email_signup.pack(padx=50, fill="x")

    # Password Field
    tk.Label(signup_window, text="Password:", bg="#333333", fg="white", font=("lucida", 12)).pack(anchor="w", padx=50, pady=5)
    entry_password_signup = tk.Entry(signup_window, show="*", font=("lucida", 12), relief="sunken")
    entry_password_signup.pack(padx=50, fill="x")

    # Role Selection
    role_var_signup = tk.StringVar()
    role_var_signup.set("student")

    tk.Label(signup_window, text="Role:", bg="#333333", fg="white", font=("lucida", 12)).pack(anchor="w", padx=50, pady=5)
    tk.Radiobutton(signup_window, text="Student", bg="#333333", fg="white", font=("lucida", 12),selectcolor="#333333", value="student", variable=role_var_signup).pack(anchor="w", padx=70)
    tk.Radiobutton(signup_window, text="Admin", bg="#333333", fg="white", font=("lucida", 12),selectcolor="#333333", value="admin", variable=role_var_signup).pack(anchor="w", padx=70)

    # Submit Button
    tk.Button(
        signup_window, 
        text="Submit", 
        font=("lucida", 18), 
        bg="green", 
        fg="white", 
        relief="sunken",
        cursor="hand2",
        command=lambda: signup(entry_name_signup, entry_email_signup, entry_password_signup, role_var_signup)
    ).pack(pady=20)

# Function to create rounded button
def create_rounded_button(parent, text, color, command):
    # Button dimensions (increased size)
    width, height = 180, 50  # Larger buttons
    radius = 10  # Radius for rounded corners

    # Create canvas for the button
    button_canvas = tk.Canvas(parent, width=width, height=height,cursor="hand2", bg="#FFFAFA", bd=0, highlightthickness=0)

    # Draw the button with subtly rounded corners
    button_canvas.create_oval(0, 0, 2 * radius, 2 * radius, fill=color, outline=color)  # Top-left corner
    button_canvas.create_oval(width - 2 * radius, 0, width, 2 * radius, fill=color, outline=color)  # Top-right corner
    button_canvas.create_oval(0, height - 2 * radius, 2 * radius, height, fill=color, outline=color)  # Bottom-left corner
    button_canvas.create_oval(width - 2 * radius, height - 2 * radius, width, height, fill=color, outline=color)  # Bottom-right corner
    button_canvas.create_rectangle(radius, 0, width - radius, height, fill=color, outline=color)  # Top rectangle
    button_canvas.create_rectangle(0, radius, width, height - radius, fill=color, outline=color)  # Center rectangle

    # Add button text
    button_canvas.create_text(width // 2, height // 2, text=text, font=("lucida", 16, "bold"), fill="white")  # Larger text

    # Bind the click event to the button
    button_canvas.bind("<Button-1>", lambda e: command())
    button_canvas.pack(side="left", padx=15)  # Increased padding for better spacing

# Main Window
root = tk.Tk()
root.title("Mock Test System")
root.geometry("800x600")
root.configure(bg="#FFFAFA")  # Set the background color to Snow

# Title Label
tk.Label(root, text="WELCOME TO MOCK TEST SYSTEM", font=("lucida", 20, "bold"), bg="#FFFAFA", fg="#1C1C1C").pack(pady=50)

# Adding an Image between the title and the buttons
try:
    img = tk.PhotoImage(file="online-learning-concept.png").subsample(2, 2)  # Adjust subsample to scale down the image
    image_label = tk.Label(root, image=img, bg="#FFFAFA")
    image_label.pack(pady=20)
except tk.TclError:
    tk.Label(root, text="Image Not Found", font=("lucida", 12), bg="#FFFAFA", fg="red").pack(pady=20)

# Frame for Buttons
button_frame = tk.Frame(root, bg="#FFFAFA")
button_frame.pack(pady=20)

# Create rounded buttons side by side
create_rounded_button(button_frame, "Login", "#1E90FF", create_login_window)
create_rounded_button(button_frame, "Signup", "#32CD32", lambda: open_signup_window())

root.mainloop()









