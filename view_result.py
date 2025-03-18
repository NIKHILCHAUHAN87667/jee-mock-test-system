import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import mysql.connector
import csv
from mysql_connection import create_connection

# Function to calculate percentile
def get_jee_percentile(score):
    score_percentile_map = [
        (300, 281, 100, 99.99989145),
        (280, 271, 99.994681, 99.997394),
        (270, 263, 99.990990, 99.994029),
        (262, 250, 99.977205, 99.988819),
        (250, 241, 99.960163, 99.975034),
        (240, 231, 99.934980, 99.956364),
        (230, 221, 99.901113, 99.928901),
        (220, 211, 99.851616, 99.893732),
        (210, 201, 99.795063, 99.845212),
        (200, 191, 99.710831, 99.782472),
        (190, 181, 99.597399, 99.688579),
        (180, 171, 99.456939, 99.573193),
        (170, 161, 99.272084, 99.431214),
        (160, 151, 99.028614, 99.239737),
        (150, 141, 98.732389, 98.990296),
        (140, 131, 98.317414, 98.666935),
        (130, 121, 97.811260, 98.254132),
        (120, 111, 97.142937, 97.685672),
        (110, 101, 96.204550, 96.978272),
        (100, 91, 94.998594, 96.064850),
        (90, 81, 93.471231, 94.749479),
        (80, 71, 91.072128, 93.152971),
        (70, 61, 87.512225, 90.702200),
        (60, 51, 82.016062, 86.907944),
        (50, 41, 73.287808, 80.982153),
        (40, 31, 58.151490, 71.302052),
        (30, 21, 37.694529, 56.569310),
        (20, 11, 13.495849, 33.229128),
        (10, 0, 0.8435177, 9.6954066)
    ]
    
    for high, low, high_p, low_p in score_percentile_map:
        if high >= score >= low:
            return round(low_p + (high_p - low_p) * (score - low) / (high - low), 6)
    
    return "Invalid Score"

# Export function
def export_to_csv(test_history):
    """Exports test history data to a CSV file."""
    if not test_history:
        messagebox.showwarning("Export Failed", "No test history available to export.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                             filetypes=[("CSV Files", "*.csv")],
                                             title="Save CSV File")
    if not file_path:
        return  

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Test ID", "Start Time", "End Time", "Score", "Percentile"])  
            for row in test_history:
                writer.writerow([row["test_id"], row["start_time"], row["end_time"], row["score"], row["percentile"]])

        messagebox.showinfo("Export Successful", f"Test history exported successfully!\nSaved at: {file_path}")
    
    except Exception as e:
        messagebox.showerror("Export Error", f"Failed to export CSV\nError: {e}")

# View test history
def view_test_history(user_id):
    """Fetch, display test history, and allow export as CSV."""
    conn = create_connection()
    if not conn:
        messagebox.showerror("Database Error", "Failed to connect to the database!")
        return

    try:
        cursor = conn.cursor(dictionary=True)

        query = """
            SELECT at.test_id, at.start_time, at.end_time, at.score 
            FROM attempt_test at
            JOIN mock_test mt ON at.test_id = mt.test_id
            WHERE at.user_id = %s
            ORDER BY at.start_time DESC
        """
        cursor.execute(query, (user_id,))
        test_history = cursor.fetchall()

        if not test_history:
            messagebox.showinfo("Test History", "No test records found for this user.")
            return

        # Calculate percentile dynamically
        for row in test_history:
            row["percentile"] = get_jee_percentile(row["score"])

        # Tkinter Window
        history_window = tk.Toplevel()
        history_window.title("Test History")
        history_window.geometry("800x400")

        # Title Label
        tk.Label(history_window, text="Test History", font=("Arial", 18, "bold")).pack(pady=10)

        # Create Table
        columns = ("Test ID", "Start Time", "End Time", "Score", "Percentile")
        tree = ttk.Treeview(history_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=130)

        for row in test_history:
            tree.insert("", "end", values=(row["test_id"], row["start_time"], row["end_time"], row["score"], row["percentile"]))

        tree.pack(padx=10, pady=10, fill="both", expand=True)

        # Export Button
        export_button = tk.Button(history_window, text="Export to CSV", font=("Arial", 12, "bold"), 
                                  bg="green", fg="white", padx=10, pady=5, 
                                  command=lambda: export_to_csv(test_history))
        export_button.pack(pady=10)

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")

    finally:
        cursor.close()
        conn.close()
