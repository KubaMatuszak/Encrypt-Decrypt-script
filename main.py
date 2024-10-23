import tkinter as tk
from tkinter import filedialog

# Dict to map letters with numbers
lowercase_dict = {chr(i): i - 97 for i in range(97, 123)}
uppercase_dict = {chr(i): i - 65 for i in range(65, 91)}

# Dicts to map numbers to letters again :)
reverse_lowercase_dict = {v: k for k, v in lowercase_dict.items()}
reverse_uppercase_dict = {v: k for k, v in uppercase_dict.items()}

root = tk.Tk()
root.withdraw()

def file_loader():
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


## ENCRYPTING SECTION !!!
def cesar_encrypt(text, num):
    coded_string = ''
    for c in text:
        if c.isupper():
            # Mapping shifted value back to letter and adding it to a new string
            shifted_value = (uppercase_dict[c] + num) % 26
            coded_string += reverse_uppercase_dict[shifted_value]
        elif c.islower():
            # Mapping shifted value back to letter and adding it to a new string
            shifted_value = (lowercase_dict[c] + num) % 26
            coded_string += reverse_lowercase_dict[shifted_value]
        else:
            # Keep non-alphabetic characters unchanged
            coded_string += c

    return coded_string

## DECRYPTING SECTION ( TO DO )
def cesar_decrypt(text, num):
    coded_string = ''
    for c in text:
        if c.isupper():
            # Mapping shifted value back to letter and adding it to a new string
            shifted_value = (uppercase_dict[c] - num) % 26
            coded_string += reverse_uppercase_dict[shifted_value]
        elif c.islower():
            # Mapping shifted value back to letter and adding it to a new string
            shifted_value = (lowercase_dict[c] - num) % 26
            coded_string += reverse_lowercase_dict[shifted_value]
        else:
            # Keep non-alphabetic characters unchanged
            coded_string += c

    return coded_string
def file_saver(txt):
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


print('Podaj liczbę znaków, o które mam przesunąć tekst')
num = int(input())
print('Wybierz plik txt do wczytania')
txt_to_save = cesar_encrypt(file_loader(), num)
print('Wybierz gdzie zapisać zaszyfrowany plik')
file_saver(txt_to_save)

