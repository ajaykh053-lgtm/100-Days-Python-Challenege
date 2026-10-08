import random
import time
import tkinter as tk
from tkinter import messagebox

# List of sentences
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and rewarding to learn.",
    "Practice makes perfect in every skill you master.",
    "Technology advances rapidly in our modern digital world.",
    "Coding requires patience, logic, and continuous practice.",
]


class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        self.start_time = 0
        self.target_sentence = ""

        # Title Label
        self.title_label = tk.Label(
            root, text="Tkinter Typing Test", font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=15)

        # Instructions / Target Sentence Label
        self.sentence_label = tk.Label(
            root, text="", font=("Arial", 12), wraplength=550, justify="center"
        )
        self.sentence_label.pack(pady=20)

        # User Entry Field
        self.entry_box = tk.Entry(root, font=("Arial", 14), width=45)
        self.entry_box.pack(pady=15)
        self.entry_box.bind("<Return>", self.finish_test)  # Press Enter to submit

        # Submit / Start Button
        self.action_button = tk.Button(
            root,
            text="Start Test",
            font=("Arial", 12, "bold"),
            command=self.start_test,
            bg="#4CAF50",
            fg="white",
        )
        self.action_button.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=15)

    def start_test(self):
        # Pick a new random sentence
        self.target_sentence = random.choice(SENTENCES)
        self.sentence_label.config(text=self.target_sentence)

        # Reset entry and results
        self.entry_box.delete(0, tk.END)
        self.result_label.config(text="")

        # Enable entry and record start time
        self.entry_box.focus()
        self.start_time = time.time()

        # Change button function to finish or leave it as submit
        self.action_button.config(text="Submit", command=self.finish_test_button)

    def finish_test(self, event=None):
        self.finish_test_button()

    def finish_test_button(self):
        if not self.start_time:
            return

        end_time = time.time()
        user_text = self.entry_box.get()

        # Calculate time and WPM
        time_taken = end_time - self.start_time
        words = len(self.target_sentence.split())
        wpm = (words / time_taken) * 60 if time_taken > 0 else 0

        # Check accuracy
        accuracy = (
            100
            if user_text == self.target_sentence
            else int(
                (
                    len(set(user_text.split()) & set(self.target_sentence.split()))
                    / words
                )
                * 100
            )
        )

        # Display results
        result_text = f"Time: {time_taken:.2f}s | Speed: {wpm:.2f} WPM"
        self.result_label.config(text=result_text)

        # Reset start time
        self.start_time = 0
        self.action_button.config(text="Try Another Sentence", command=self.start_test)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()
