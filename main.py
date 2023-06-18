import tkinter as tk
from QAsystem import QAsystem

def send_message():
    user_input = input_box.get().strip() 
    if not user_input:
        return  
        
    display_message(user_input, "user")  
    response = QAsystem(user_input)
    display_message(response, "bot")  
    input_box.delete(0, tk.END)  

def display_message(message, sender):
    chat_log.configure(state='normal')  
    chat_log.insert(tk.END, f"{sender}: {message}\n")  
    chat_log.configure(state='disabled') 
    chat_log.see(tk.END)  

    
window = tk.Tk()
window.title("Chatbot")
window.geometry("500x500")

label = tk.Label(window, text="Makanan Malaysia", font=("Helvetica", 16, "bold"))
label.pack(pady=10)

chat_log = tk.Text(window, height=20, width=60)
chat_log.configure(state='disabled') 
chat_log.pack(padx=10, pady=10)

input_box = tk.Entry(window, width=60)
input_box.pack(padx=10, pady=10)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=10)

window.mainloop()