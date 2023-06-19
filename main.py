import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from QAsystem import QAsystem

def send_message():
    user_input = input_box.get().strip()
    if not user_input:
        return

    display_message(user_input, "user")
    response = QAsystem(user_input)
    # response = test()
    display_message(response, "bot")
    input_box.delete(0, tk.END)

def display_message(message, sender):
    chat_log.configure(state='normal')

    if sender == "user":
        tag = "user_tag"
        color = "blue"
        justify = "left"
        lmargin1 = 50  # Padding on the right side
        rmargin = 30  # Padding on the left side
        bg=None

        # # Load the user icon image
        # if not hasattr(chat_log, 'user_icon'):
        #     chat_log.user_icon = PhotoImage(file="user.png")
        # chat_log.window_create(tk.END, window=tk.Label(chat_log, image=chat_log.user_icon, bg=bg))
        
        # user_icon = Image.open("user.png")
        # user_icon = user_icon.resize((30, 30))  # Resize the image to desired dimensions
        # user_icon = ImageTk.PhotoImage(user_icon)
        # chat_log.image_create(tk.END, image=user_icon)
        # chat_log.image = user_icon  # Store a reference to prevent garbage collection
    else:
        tag = "bot_tag"
        color = "green"
        justify = "left"
        lmargin1 = 30  # Padding on the left side
        rmargin = 50  # Padding on the right side
        bg = "light blue"
        
        icon = Image.open("bot.png")
        icon = icon.resize((30, 30))  # Resize the image to desired dimensions
        icon = ImageTk.PhotoImage(icon)
        chat_log.image_create(tk.END, image=icon)
        chat_log.image = icon  # Store a reference to prevent garbage collection

    chat_log.tag_configure(tag, foreground=color, background=bg, justify=justify, lmargin1=lmargin1, rmargin=rmargin)

    formatted_message = f"{message}\n"
    chat_log.insert(tk.END, formatted_message, tag)

    chat_log.configure(state='disabled')
    chat_log.see(tk.END)

def test():
    print("Hello")
    return None

# button hover
def on_button_enter(event):
    send_button.config(bg="#C38154", fg="white")

def on_button_leave(event):
    send_button.config(bg="#D6CDA4", fg="black")

window = tk.Tk()
window.title("Chatbot")
window.geometry("500x500")

window.configure(bg='#1C6758')

label = tk.Label(window, text="MAKANAN MALAYSIA", bg='#1C6758', fg='white', font=("Helvetica", 20, "bold"))
label.pack(pady=10)

chat_log = tk.Text(window, height=20, width=80)
chat_log.configure(state='disabled')
chat_log.pack(padx=10, pady=10)

input_box = tk.Entry(window, width=40)
input_box.pack(padx=10, pady=10)

send_button = tk.Button(window, text="SEND", command=send_message, width=8, height=2, font=font.Font(size=10, weight="bold"))
send_button.config(bg="#D6CDA4", fg="black")
send_button.pack(pady=10)

send_button.bind("<Enter>", on_button_enter)
send_button.bind("<Leave>", on_button_leave)

window.mainloop()
