import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import Image, ImageTk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import random

# Load the trained model and vectorizer
model = joblib.load('fake_news_detection_model_logistic.pkl')
tfidf_vectorizer = joblib.load('tfidf_vectorizer_logistic.pkl')

# Create a function to perform fake news detection
def detect_fake_news():
    text = text_entry.get()
    if text:
        # Vectorize the input text using the same vectorizer used during training
        text_tfidf = tfidf_vectorizer.transform([text])

        # Make predictions using the loaded model
        prediction = model.predict(text_tfidf)

        # Display the result in a custom message box
        if prediction[0] == 0:
            result = "Fake News"
        else:
            result = "Real News"

        message_label.config(text=f"The input text is classified as: {result}")
    else:
        messagebox.showerror("Error", "Please enter text to analyze.")

# Create the main application window
root = tk.Tk()
root.title("Fake News Detection")

# Create a frame for the content
content_frame = ttk.Frame(root)
content_frame.pack(fill=tk.BOTH, expand=True)

# Load and display a background image
bg_image = Image.open("Background.png")  # Replace with your image file
bg_image = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(content_frame, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create a custom label with styled text
title_label = tk.Label(
    content_frame,
    text="Fake News Detection",
    font=("Helvetica", 24, "bold"),
    fg="white",
    bg="navy",
    pady=10
)
title_label.pack(fill=tk.X)

# Create an entry for entering text
text_entry = ttk.Entry(
    content_frame,
    font=("Helvetica", 14),
    width=50
)
text_entry.pack(pady=20)

# Create an animated button with a hover effect
def on_enter(event):
    analyze_button.config(bg="green")

def on_leave(event):
    analyze_button.config(bg="lightgreen")

analyze_button = tk.Button(
    content_frame,
    text="Analyze",
    font=("Helvetica", 16, "bold"),
    bg="lightgreen",
    fg="white",
    padx=20,
    pady=10,
    command=detect_fake_news
)
analyze_button.pack(pady=10)
analyze_button.bind("<Enter>", on_enter)
analyze_button.bind("<Leave>", on_leave)

# Create a custom message label
message_label = tk.Label(
    content_frame,
    text="",
    font=("Helvetica", 18, "bold"),
    fg="white",
    bg="navy",
    pady=10
)
message_label.pack(fill=tk.X)

# Run the GUI main loop
root.mainloop()
