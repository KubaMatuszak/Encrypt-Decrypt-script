import tkinter as tk
from tkinter import filedialog

class FileMan:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def file_load(self):
        file_path = filedialog.askopenfilename(
            title="Select a Text File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )

        if file_path:
            print(f"Selected file: {file_path}")

            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                return text

        else:
            print("No file selected.")

    def file_save(self, txt):
        file_path = filedialog.asksaveasfilename(
            title="Save Text File",
            defaultextension=".txt",  # Default extension
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]  # File types
        )

        # Check if a file was selected
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(txt)  # Write the string to the file
            print(f"File saved as: {file_path}")
        else:
            print("Save operation was cancelled.")