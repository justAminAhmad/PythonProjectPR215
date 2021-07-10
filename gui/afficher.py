import sys
from tkinter import *
import tkinter.ttk as ttk
import os
import json

# creation de la fenetre interface
afficher_window = Tk()
afficher_window.geometry('1200x500')
afficher_window.title("Projet PR215")

# recuperation de notre fichier de donnée
data_file = json.load(open('./my_data.json'))


def insert_data(data):
    # fonction d'entrer de données
    for i in data:
        trv.insert("", "end", values=(
            i,
            data[i]['nom'],
            data[i]['capital'],
            data[i]['population'],
            data[i]['langue'],
            data[i]['superficie'],
            data[i]['independance'],
            data[i]['president'],
            data[i]['pib']
        ))


def retourarriere():
    # fonction de retour vers le menu principale
    afficher_window.destroy()
    os.system("python ./main.py")


canvas = Canvas(afficher_window, width=1200, height=500, bg="#263D42")

frame = Frame(afficher_window, bg="#6AADB6", padx=80, pady=20)

tete = Label(frame, text="Liste des pays enregistrés",
             bg="#263D42", fg="white", padx=150, pady=5)

# creation d'une treeview pour afficher nos donnees
trv = ttk.Treeview(frame, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7",
                                   "#8", "#9"), show='headings', height='10')
style = ttk.Style(afficher_window)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#263D42", foreground="white")

# gestion des headings de notre treeview
trv.heading('#1', text="Code", anchor='center')
trv.column('#1', width=100, anchor='center')
trv.heading('#2', text="Nom", anchor='center')
trv.column('#2', width=100, anchor='center')
trv.heading('#3', text="Capitale", anchor='center')
trv.column('#3', width=100, anchor='center')
trv.heading('#4', text="Population", anchor='center')
trv.column('#4', width=100, anchor='center')
trv.heading('#5', text="Langue", anchor='center')
trv.column('#5', width=100, anchor='center')
trv.heading('#6', text="Superficie", anchor='center')
trv.column('#6', width=100, anchor='center')
trv.heading('#7', text="Date d'independance", anchor='center')
trv.column('#7', width=140, anchor='center')
trv.heading('#8', text="President", anchor='center')
trv.column('#8', width=100, anchor='center')
trv.heading('#9', text="PIB", anchor='center')
trv.column('#9', width=100, anchor='center')

retour = Button(frame, text="retour", padx=30,
                pady=20, fg="white", bg="#263D42", command=lambda: retourarriere())


# grid pour le placement des elements
canvas.grid(columnspan=2)
frame.grid(row=0, column=0, columnspan=2)
tete.grid(row=0, columnspan=3, padx=10, pady=15)
trv.grid(row=1, column=1)
retour.grid(row=2, column=1)

insert_data(data_file)

afficher_window.mainloop()
