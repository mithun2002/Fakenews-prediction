import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
import math
from PIL import Image, ImageTk
import joblib

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

        # Display the result in a message box with animation
        if prediction[0] == 0:
            result = "Fake News"
        else:
            result = "Real News"

        def display_result_animation():
            alert_text.config(text=f"The input text is classified as: {result}")
            for _ in range(10):
                alert_frame.update_idletasks()
                time.sleep(0.1)
                alert_frame.lift()
                alert_frame.update()

        alert_frame = tk.Toplevel(root)
        alert_frame.title("Fake News Detection")
        alert_text = tk.Label(alert_frame, text="", font=("Helvetica", 14))
        alert_text.pack(padx=20, pady=20)
        alert_frame.after(100, display_result_animation)

    else:
        messagebox.showerror("Error", "Please enter text to analyze.")

# Function to rotate text
def rotate_text(angle):
    x = 200 * math.cos(math.radians(angle)) + 300
    y = 100 * math.sin(math.radians(angle)) + 200
    rotating_text.place(x=x, y=y, anchor="center")
    root.after(50, lambda: rotate_text((angle + 1) % 360))

# Create a thread for text rotation
text_rotation_thread = threading.Thread(target=lambda: rotate_text(0))
text_rotation_thread.daemon = True
text_rotation_thread.start()

# Create the main application window
root = tk.Tk()
root.title("Fake News Detection")

# Create a frame for the content
content_frame = ttk.Frame(root)
content_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

# Create a label and entry for entering text
text_label = ttk.Label(content_frame, text="Enter text for analysis:")
text_label.pack(pady=10)
text_entry = ttk.Entry(content_frame, width=50)
text_entry.pack(pady=10)

# Create Analyze and Clear buttons
analyze_button = ttk.Button(content_frame, text="Analyze", command=detect_fake_news)
analyze_button.pack(pady=10)
clear_button = ttk.Button(content_frame, text="Clear", command=lambda: text_entry.delete(0, 'end'))
clear_button.pack(pady=10)

# Create an Exit button
def exit_app():
    root.destroy()

exit_button = ttk.Button(content_frame, text="Exit", command=exit_app)
exit_button.pack(pady=10)

# Create a rotating text
rotating_text = ttk.Label(root, text="Fake News Detection", font=("Helvetica", 16))
rotating_text.place(relx=0.5, rely=0.5, anchor="center")

# Run the Tkinter main loop
root.mainloop()
