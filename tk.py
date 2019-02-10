from tkinter import *
from tkinter import messagebox
import SimpleQIWI



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

# инпуты
api = Entry(root)
api.insert(0, 'Укажите QiWi API')
tel = Entry(root)
tel.insert(0, 'Ваш номер QiWi')
api.pack()
tel.pack()

tel1 = Entry(root)
tel1.insert(0, 'Киви 1')
tel1.pack()
tel2 = Entry(root)
tel2.insert(0, 'Киви 2')
tel2.pack()
tel3 = Entry(root)
tel3.insert(0, 'Киви 3')
tel3.pack()
tel4 = Entry(root)
tel4.insert(0, 'Киви 4')
tel4.pack()
tel5 = Entry(root)
tel5.insert(0, 'Киви 5')
tel5.pack()
# Кнопки

message_button = Button(text="Произвести переводы", command=quit)
message_button.place(relx=.5, rely=.5, anchor="c")

button1 = Button(root, text="Выход", command=exit)
button1.place(x = 180, y = 360)
button1.bind()

donate_button = Button(root, text="Отблагодарить автора рублём", command=donate)
donate_button.place(x = 120, y = 340)
donate_button.bind()

root.mainloop()