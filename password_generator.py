import tkinter as tk
import random
import string
import sys
import subprocess

texts = {
    'en': {
        'title': "Password Generator",
        'length_label': "Enter password length:",
        'generate_button': "Generate Password",
        'invalid_input': "Invalid input: ",
        'password_field': "Generated Password",
        'quit_button': "Quit",
        'include_letters': "Include letters",
        'include_numbers': "Include numbers",
        'include_special': "Include special characters"
    },
    'ar': {
        'title': "مولد كلمات المرور",
        'length_label': "أدخل طول كلمة المرور:",
        'generate_button': "توليد كلمة مرور",
        'invalid_input': "مدخل غير صالح: ",
        'password_field': "كلمة المرور المولدة",
        'quit_button': "خروج",
        'include_letters': "تشمل الحروف",
        'include_numbers': "تشمل الأرقام",
        'include_special': "تشمل الرموز الخاصة"
    }
}

def generate_password(length, use_letters, use_numbers, use_special):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "No characters selected!"
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(length_entry.get())
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        use_letters = letter_var.get()
        use_numbers = digit_var.get()
        use_special = special_var.get()
        password = generate_password(length, use_letters, use_numbers, use_special)
        password_var.set(password)
    except ValueError as e:
        password_var.set(f"{texts[lang]['invalid_input']}{e}")

def change_language(new_lang):
    global lang
    lang = new_lang
    title_label.config(text=texts[lang]['title'])
    length_label.config(text=texts[lang]['length_label'])
    generate_button.config(text=texts[lang]['generate_button'])
    password_entry.config(placeholder=texts[lang]['password_field'])
    quit_button.config(text=texts[lang]['quit_button'])
    letter_check.config(text=texts[lang]['include_letters'])
    digit_check.config(text=texts[lang]['include_numbers'])
    special_check.config(text=texts[lang]['include_special'])

def quit_app():
    root.quit()

# Tkinter GUI
root = tk.Tk()
lang = 'en'
root.title(texts[lang]['title'])
root.geometry("400x350")

bg_color = "#e8f0f2"  # Light blue-gray background
button_color = "#3498db"  # Soft blue
text_color = "#333333"  # Dark gray
entry_bg_color = "#ffffff"  # White for entry fields
button_hover_color = "#2980b9"  # Slightly darker blue for hover effect
quit_button_color = "#f44336"  # Red color for the Quit button
quit_button_hover_color = "#d32f2f"  # Darker red for hover effect

root.configure(bg=bg_color)

font_title = ("Helvetica", 16)
font_label = ("Helvetica", 12)
font_button = ("Helvetica", 10)
font_check = ("Helvetica", 12)

title_label = tk.Label(root, text=texts[lang]['title'], bg=bg_color, fg=text_color, font=font_title)
title_label.pack(pady=10)

length_label = tk.Label(root, text=texts[lang]['length_label'], bg=bg_color, fg=text_color, font=font_label)
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=10, bg=entry_bg_color, fg=text_color, borderwidth=2, relief="solid", font=font_label)
length_entry.pack(pady=5)

letter_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

letter_check = tk.Checkbutton(root, text=texts[lang]['include_letters'], variable=letter_var, bg=bg_color, fg=text_color, selectcolor=bg_color, font=font_check)
letter_check.pack(anchor=tk.W, padx=20, pady=2)

digit_check = tk.Checkbutton(root, text=texts[lang]['include_numbers'], variable=digit_var, bg=bg_color, fg=text_color, selectcolor=bg_color, font=font_check)
digit_check.pack(anchor=tk.W, padx=20, pady=2)

special_check = tk.Checkbutton(root, text=texts[lang]['include_special'], variable=special_var, bg=bg_color, fg=text_color, selectcolor=bg_color, font=font_check)
special_check.pack(anchor=tk.W, padx=20, pady=2)

generate_button = tk.Button(root, text=texts[lang]['generate_button'], command=on_generate, bg=button_color, fg="white", relief="flat", font=font_button)
generate_button.pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=40, bg=entry_bg_color, fg=text_color, borderwidth=2, relief="solid", font=font_label)
password_entry.pack(pady=5)

en_button = tk.Button(root, text="English", command=lambda: change_language('en'), bg="#f0f0f0", fg=text_color, relief="flat", font=font_button)
en_button.pack(side=tk.LEFT, padx=10, pady=10)

ar_button = tk.Button(root, text="العربية", command=lambda: change_language('ar'), bg="#f0f0f0", fg=text_color, relief="flat", font=font_button)
ar_button.pack(side=tk.RIGHT, padx=10, pady=10)

quit_button = tk.Button(root, text=texts[lang]['quit_button'], command=quit_app, bg=quit_button_color, fg="white", relief="flat", font=font_button)
quit_button.pack(pady=10)

def on_enter(e):
    e.widget.config(bg=button_hover_color)

def on_leave(e):
    e.widget.config(bg=button_color)

def on_enter_quit(e):
    e.widget.config(bg=quit_button_hover_color)

def on_leave_quit(e):
    e.widget.config(bg=quit_button_color)

generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)
quit_button.bind("<Enter>", on_enter_quit)
quit_button.bind("<Leave>", on_leave_quit)

root.mainloop()

# PyInstaller Integration
if getattr(sys, 'frozen', False):
    # The application is running in a bundle
    pass
else:
    # The application is running live, we could offer a bundling option
    if len(sys.argv) > 1 and sys.argv[1] == '--build':
        # Command to build the executable
        print("Building the executable...")
        subprocess.call([
            sys.executable, '-m', 'PyInstaller', '--onefile', '--windowed', '--name', 'PasswordGenerator', __file__
        ])
        print("Build complete!")
