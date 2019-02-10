from tkinter import *
from tkinter import messagebox
import SimpleQIWI

#api_q = StringVar()

#api_q_entry = Entry(textvariable=api_q)

def show_message_api():
    api = message.get()
    return api

def show_message():
	messagebox_showinfo("Donate", text="Спасибо от автора за рубль!")

def donate(token_otp, number_otp):
	api = QApi(token = token_otp, phone = number_otp)
	api.pay(account = "79999606624", amount = 1, comment = "Donat from my qiwi program")
	show_message()
	

root = Tk()
root.wm_iconbitmap("qiwi.ico")
root.title("Переводы QiWi by Vitaliy 2019")
root.geometry('400x400')

def exit():
	root.quit()

message = StringVar()


message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
message_entry.insert(0, "Введите QiWi API")

# Кнопки

message_button = Button(text="Произвести переводы", command=show_message_api)
message_button.place(relx=.5, rely=.5, anchor="c")

button1 = Button(root, text="Выход", command=exit)
button1.place(x = 180, y = 360)
button1.bind()

donate_button = Button(root, text="Отблагодарить автора рублём", command=donate)
donate_button.place(x = 120, y = 340)
donate_button.bind()

root.mainloop()