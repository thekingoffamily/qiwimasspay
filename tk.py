from tkinter import *
from tkinter import messagebox
import pyqiwi


root = Tk()
root.wm_iconbitmap("qiwi.ico")
root.title("Переводы QiWi by Vitaliy 2019")
root.geometry('400x400')


def exit():
	root.quit()


api = StringVar()
api_ent = Entry(textvariable=api)
api_ent.insert(0, 'Укажите QiWi API')
tel = StringVar()
tel_ent = Entry(textvariable=tel)
tel_ent.insert(0, 'Ваш номер QiWi')
api_ent.pack()
tel_ent.pack()

def donate():
	token = api.get()
	phone = tel.get()
	wallet = pyqiwi.Wallet(token=token, number=phone)
	wallet.send('99', recipient='79999606624', amount=1, comment='Донат с программы qiwimasspay')
	messagebox.showinfo("Donate", "Спасибо от автора за рубль!")

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

message_button = Button(text="Произвести переводы", command=quit)
message_button.place(relx=.5, rely=.5, anchor="c")

button1 = Button(root, text="Выход", command=exit)
button1.place(x = 180, y = 360)
button1.bind()

donate_button = Button(root, text="Отблагодарить автора рублём", command=donate)
donate_button.place(x = 120, y = 340)
donate_button.bind()

root.mainloop()