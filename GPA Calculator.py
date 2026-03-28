# CGPA Calculator with GUI + Prediction
import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.linear_model import LinearRegression

gpas = []

# Functions

def calculate_gpa():
    try:
        grades = list(map(float, grade_entry.get().split(',')))
        credits = list(map(float, credit_entry.get().split(',')))

        if len(grades) != len(credits):
            messagebox.showerror("Error", "Grades and Credits must match!")
            return

        total_points = sum(g * c for g, c in zip(grades, credits))
        total_credits = sum(credits)

        gpa = total_points / total_credits
        gpas.append(gpa)

        result_label.config(text=f"GPA: {gpa:.2f}")

    except:
        messagebox.showerror("Error", "Invalid input!")


def calculate_cgpa():
    if not gpas:
        messagebox.showerror("Error", "No GPA data!")
        return

    cgpa = sum(gpas) / len(gpas)
    result_label.config(text=f"CGPA: {cgpa:.2f}")


def predict_gpa():
    if len(gpas) < 2:
        messagebox.showerror("Error", "Need at least 2 semesters!")
        return

    X = np.array(range(1, len(gpas)+1)).reshape(-1, 1)
    y = np.array(gpas)

    model = LinearRegression()
    model.fit(X, y)

    next_sem = np.array([[len(gpas)+1]])
    pred = model.predict(next_sem)

    result_label.config(text=f"Predicted GPA: {pred[0]:.2f}")



# GUI Setup

root = tk.Tk()
root.title(" CGPA Calculator")
root.geometry("420x350")
root.configure(bg="#5C5C96")

# Title
title = tk.Label(root, text="CGPA Calculator", font=("Arial", 18, "bold"),
                 bg="#9393aa", fg="white")
title.pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#8bb547", bd=2, relief="ridge")
frame.pack(pady=10, padx=10, fill="both")

# Input fields
tk.Label(frame, text="Grades (e.g. 8,7,9)", bg="#2c2c3e", fg="white").pack(pady=5)
grade_entry = tk.Entry(frame, width=30)
grade_entry.pack(pady=5)

tk.Label(frame, text="Credits (e.g. 3,4,3)", bg="#2c2c3e", fg="white").pack(pady=5)
credit_entry = tk.Entry(frame, width=30)
credit_entry.pack(pady=5)

# Buttons
btn_style = {"width": 20, "bg": "#4CAF50", "fg": "white", "bd": 0, "pady": 5}

tk.Button(root, text="Calculate GPA", command=calculate_gpa, **btn_style).pack(pady=5)
tk.Button(root, text="Calculate CGPA", command=calculate_cgpa, **btn_style).pack(pady=5)
tk.Button(root, text="Predict Next GPA", command=predict_gpa,
          bg="#226CA9", fg="white", width=20, bd=0, pady=5).pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"),
                        bg="#1e1e2f", fg="#FFD700")
result_label.pack(pady=15)

root.mainloop()