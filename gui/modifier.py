from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import json
import os

data_file = json.load(open('./my_data.json'))

modifier_window = Tk()
modifier_window.geometry('1200x600')
modifier_window.title("Projet PR215")


def selection():
    try:
        int(code_txt.get())
    except:
        messagebox.showwarning(
            'Erreur', 'Veuillez saisir un code dans le champ requis')
        return "Erreur : code non saisi"

    code = code_txt.get()

    if code in data_file:
        trv.insert("", END, values=(
            code,
            data_file[code]['nom'],
            data_file[code]['capital'],
            data_file[code]['population'],
            data_file[code]['langue'],
            data_file[code]['superficie'],
            data_file[code]['independance'],
            data_file[code]['president'],
            data_file[code]['pib']
        ))
        saisi_code.delete(0, END)
        saisi_code.insert(0, "")
    else:
        messagebox.showwarning('Erreur', 'Pays inexistant ou code incorrect!')


def retourarriere():
    modifier_window.destroy()
    os.system("python main.py")


canvas = Canvas(modifier_window, width=1200, height=600, bg="#263D42")
canvas.grid(columnspan=2)

frame = Frame(modifier_window, bg="#6AADB6", padx=70, pady=30)
frame.grid(row=0, column=0, columnspan=3)

frame1 = Frame(frame, bg="#6AADB6", padx=70, pady=30)
frame1.grid(row=2, column=0, columnspan=3)

tete = Label(frame, text="Veuillez saisir le code d'un pays: ",
             bg="#263D42", fg="white", padx=10, pady=5)
tete.grid(row=0, column=1, pady=10)

trv = ttk.Treeview(frame1, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"),
                   show='headings', height=3)
trv.grid(row=0, column=0)
s = ttk.Style()
style = ttk.Style(modifier_window)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#263D42", foreground="white")

trv.heading('#1', text="Code", anchor='center')
trv.column('#1', width=80, anchor='center')
trv.heading('#2', text="Nom", anchor='center')
trv.column('#2', width=80, anchor='center')
trv.heading('#3', text="Capitale", anchor='center')
trv.column('#3', width=80, anchor='center')
trv.heading('#4', text="Population", anchor='center')
trv.column('#4', width=80, anchor='center')
trv.heading('#5', text="Langue", anchor='center')
trv.column('#5', width=80, anchor='center')
trv.heading('#6', text="Superficie", anchor='center')
trv.column('#6', width=80, anchor='center')
trv.heading('#7', text="Independance", anchor='center')
trv.column('#7', width=80, anchor='center')
trv.heading('#8', text="President", anchor='center')
trv.column('#8', width=80, anchor='center')
trv.heading('#9', text="PIB", anchor='center')
trv.column('#9', width=80, anchor='center')

code_txt = StringVar()
saisi_code = Entry(frame, font=("Arial", 10),
                   textvariable=code_txt, width=20, borderwidth=8)
saisi_code.grid(row=1, column=1, pady=10)

entrer = Button(frame, text="Entrer", padx=10,
                pady=10, fg="white", bg="#263D42", command=lambda: selection())
entrer.grid(row=3, column=0, padx=10, pady=10)

modifier_btn = Button(frame, text="Modifier", padx=10,
                      pady=10, fg="white", bg="#263D42")
modifier_btn.grid(row=3, column=1, pady=10)

retour = Button(frame, text="Retour", padx=10, pady=10,
                fg="white", bg="#263D42", command=lambda: retourarriere())
retour.grid(row=3, column=2, padx=10, pady=10)

modifier_window.mainloop()
