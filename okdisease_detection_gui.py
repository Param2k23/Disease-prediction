import tkinter as tk
from tkinter import messagebox
import main

# Function to handle button click event for disease detection
def detect_button_clicked():
    # Change button text to "Loading"
    detect_button.config(text="Loading...")
    window.update()

    # Get selected symptoms
    symptoms = entry_symptoms.get()

    # Perform disease detection and update labels
    process_disease_detection(symptoms)

# Function to perform disease detection and update labels
def process_disease_detection(symptoms):
    # Perform disease detection
    dtc = main.main()
    name = main.start(dtc, symptoms)
    print("name gui : "+name)
    description = main.desc(name)
    print("description gui : "+description)
    precaution1, precaution2, precaution3 = main.precaution(name)
    
    # Update labels with results
    name_label.config(text="Name of Disease : "+name)
    description_label.config(text="Description : "+description)
    precaution_label.config(text="Precaution 1 : "+precaution1+"\nPrecaution 2 : "+precaution2+"\nPrecaution 3 : "+precaution3)

    # Change button text back to "Detect"
    detect_button.config(text="Detect")

# Function to navigate to the input page
def start_button_clicked():
    front_page_frame.pack_forget()
    input_page_frame.pack()

# Create main window
window = tk.Tk()
window.title("Human Body Disease Detection")

# Create front page frame
front_page_frame = tk.Frame(window, bg="#f08080")  # Light Coral
front_page_frame.pack(fill=tk.BOTH, expand=True)

# Front page content
title_label = tk.Label(front_page_frame, text="Welcome to Disease Detection", font=("Arial", 30), bg="#f08080")  # Light Coral
title_label.pack(pady=50)

start_button = tk.Button(front_page_frame, text="Get Started", command=start_button_clicked, font=("Arial", 20), bg="#2f4f4f", fg="white", padx=30, pady=15)  # Dark Slate Gray
start_button.pack(pady=20)

# Create input page frame
input_page_frame = tk.Frame(window, bg="#bc8f8f")  # Rosy Brown

# Symptoms input text box
entry_symptoms_label = tk.Label(input_page_frame, text="Enter Symptoms (separated by commas):", font=("Arial", 20), bg="#bc8f8f")  # Rosy Brown
entry_symptoms_label.pack(pady=20)
entry_symptoms = tk.Entry(input_page_frame, width=70, font=("Arial", 16))
entry_symptoms.pack(pady=10)

# Create detect button
detect_button = tk.Button(input_page_frame, text="Detect Disease", command=detect_button_clicked, font=("Arial", 20), bg="#2f4f4f", fg="white", padx=30, pady=15)  # Dark Slate Gray
detect_button.pack(pady=30)

# Result label
name_label = tk.Label(input_page_frame, text="", font=("Arial", 20), wraplength=700, bg="#bc8f8f")  # Rosy Brown
name_label.pack(pady=20)

# Precaution label
description_label = tk.Label(input_page_frame, text="", font=("Arial", 20), wraplength=700, bg="#bc8f8f", fg="red")  # Rosy Brown
description_label.pack(pady=20)

precaution_label = tk.Label(input_page_frame, text="", font=("Arial", 20), wraplength=700, bg="#bc8f8f", fg="red")  # Rosy Brown
precaution_label.pack(pady=20)

# Hide input page initially
input_page_frame.pack_forget()

# Run the main event loop
window.mainloop()
