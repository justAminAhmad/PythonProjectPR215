from tkinter import *
from tkinter import messagebox
import os
import json

entrer_window = Tk()
entrer_window.geometry('800x600')
entrer_window.title("Projet PR215")


data_file = json.load(open('./my_data.json'))


def ajout_pays():
    # fonction permettant d'enregistrer une nouvelle donnee
    global data_file
    try:
        # recuperation des donnees entres en int
        int(code_txt.get())
        int(population_txt.get())
        int(superficie_txt.get())
        int(jour_txt.get())
        int(mois_txt.get())
        int(annee_txt.get())
        int(pib_txt.get())
    except:
        # exeption permettant de retourner une erreur si 
        # les donnees recu ne sont pas des entiers
        messagebox.showwarning(
            'Erreur', 'Veuillez remplir les champs correctement')
        return "Erreur : Veuillez remplir les champs correctement"

    # recuperation du code du pays
    code = int(code_txt.get())
    if str(code) in data_file:
        # test de l'existance du pays dans la database
        messagebox.showwarning('Erreur', 'Code existe deja')
        return "Erreur 807"

    nom = nom_txt.get()
    capitale = capitale_txt.get()
    population = int(population_txt.get())
    langue = langue_txt.get()
    superficie = int(superficie_txt.get())

    jour = int(jour_txt.get())
    mois = int(mois_txt.get())
    annee = int(annee_txt.get())
    if((jour not in range(0, 31)) or (mois not in range(1, 13)) or (annee not in range(1800, 2021))):
        # test si la date est entree correctement
        messagebox.showwarning('Erreur', 'Erreur Date')
        return "Erreur Date"

    president = president_txt.get()
    pib = int(pib_txt.get())

    if((nom == "") or (capitale == "") or (langue == "") or (president == "")):
        # test si les champs sont bien remplis
        messagebox.showwarning(
            'Erreur', 'Veuillez remplir les champs correctement')
        return "Veuillez remplir les champs"

    data_file[code] = {
        "nom": nom,
        "capital": capitale,
        "population": population,
        "langue": langue,
        "superficie": superficie,
        "independance": str(jour)+"-"+str(mois)+"-"+str(annee),
        "president": president,
        "pib": pib
    }
    out_file = open("./my_data.json", 'w')
    json.dump(data_file, out_file, indent=5)
    out_file.close()
    messagebox.showinfo('title', 'success')
    data_file = json.load(open("./my_data.json"))
    clear_entries()
    return "success"


def clear_entries():
    # fonction permettant de vider les champs pour etre utiliser à nouveau
    saisi_code.delete(0, END)
    saisi_code.insert(0, "")
    saisi_nom.delete(0, END)
    saisi_nom.insert(0, "")
    saisi_capitale.delete(0, END)
    saisi_capitale.insert(0, "")
    saisi_population.delete(0, END)
    saisi_population.insert(0, "")
    saisi_lang.delete(0, END)
    saisi_lang.insert(0, "")
    saisi_superficie.delete(0, END)
    saisi_superficie.insert(0, "")
    saisi_jour.delete(0, END)
    saisi_jour.insert(0, "")
    saisi_mois.delete(0, END)
    saisi_mois.insert(0, "")
    saisi_annee.delete(0, END)
    saisi_annee.insert(0, "")
    saisi_presi.delete(0, END)
    saisi_presi.insert(0, "")
    saisi_pib.delete(0, END)
    saisi_pib.insert(0, "")


def retourarriere():
    entrer_window.destroy()
    os.system("python main.py")


canvas = Canvas(entrer_window, width=800, height=600, bg="#263D42")
canvas.grid(columnspan=2)

frame = Frame(entrer_window, bg="#6AADB6", padx=20, pady=20)
frame.grid(row=0, column=0, columnspan=3)

frame_label = Frame(frame, bg="#6AADB6", padx=20, pady=20)
frame_label.grid(row=1, column=1)

frame_saisis = Frame(frame, bg="#6AADB6", padx=20, pady=20)
frame_saisis.grid(row=1, column=2, columnspan=3)

frame_date = Frame(frame_saisis, bg="#6AADB6", padx=2, pady=2)
frame_date.grid(row=7, column=0, columnspan=3)

tete = Label(frame, text="Pour enregistrer un nouvel pays \nVeuillez remplir les champs suivants: ",
             bg="#263D42", fg="white", padx=150, pady=5)
tete.grid(row=0, columnspan=4, pady=15)

lbl = Label(frame_label, text="code international", padx=10,
            pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl.grid(row=1, sticky=W, padx=10, pady=5)

lbl1 = Label(frame_label, text="Nom du pays", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl1.grid(row=2, sticky=W, padx=10, pady=5)

lbl2 = Label(frame_label, text="Capitale", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl2.grid(row=3, sticky=W, padx=10, pady=5)

lbl3 = Label(frame_label, text="Population", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl3.grid(row=4, sticky=W, padx=10, pady=5)

lbl4 = Label(frame_label, text="Langue officielle", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl4.grid(row=5, sticky=W, padx=10, pady=5)

lbl5 = Label(frame_label, text="Superficie", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl5.grid(row=6, sticky=W, padx=10, pady=5)

lbl6 = Label(frame_label, text="Date d’indépendance", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl6.grid(row=7, sticky=W, padx=10, pady=5)

lbl7 = Label(frame_label, text="Président", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl7.grid(row=8, sticky=W, padx=10, pady=5)

lbl8 = Label(frame_label, text="PIB", padx=10,
             pady=5, borderwidth=3, bg="#263D42", fg="white")
lbl8.grid(row=9, sticky=W, padx=10, pady=5)


code_txt = StringVar()
saisi_code = Entry(frame_saisis, textvariable=code_txt, font=("Arial", 10), width=40,
                   borderwidth=5)
saisi_code.grid(row=1, sticky=W, padx=10, pady=7)

nom_txt = StringVar()
saisi_nom = Entry(frame_saisis, textvariable=nom_txt, font=("Arial", 10), width=40,
                  borderwidth=5)
saisi_nom.grid(row=2, sticky=W, padx=10, pady=7)

capitale_txt = StringVar()
saisi_capitale = Entry(frame_saisis, textvariable=capitale_txt, font=("Arial", 10), width=40,
                       borderwidth=5)
saisi_capitale.grid(row=3, sticky=W, padx=10, pady=7)

population_txt = StringVar()
saisi_population = Entry(frame_saisis, textvariable=population_txt, font=("Arial", 10), width=40,
                         borderwidth=5)
saisi_population.grid(row=4, sticky=W, padx=10, pady=7)

langue_txt = StringVar()
saisi_lang = Entry(frame_saisis, textvariable=langue_txt, font=("Arial", 10), width=40,
                   borderwidth=5)
saisi_lang.grid(row=5, sticky=W, padx=10, pady=7)

superficie_txt = StringVar()
saisi_superficie = Entry(frame_saisis, textvariable=superficie_txt, font=("Arial", 10), width=40,
                         borderwidth=5)
saisi_superficie.grid(row=6, sticky=W, padx=10, pady=7)

jour_txt = StringVar()
saisi_jour = Entry(frame_date, textvariable=jour_txt, font=("Arial", 10), width=10,
                   borderwidth=5)
saisi_jour.grid(row=0, column=0, sticky=W, padx=10, pady=7)

mois_txt = StringVar()
saisi_mois = Entry(frame_date, textvariable=mois_txt, font=("Arial", 10), width=10,
                   borderwidth=5)
saisi_mois.grid(row=0, column=1, sticky=W, padx=10, pady=7)

annee_txt = StringVar()
saisi_annee = Entry(frame_date, textvariable=annee_txt, font=("Arial", 10), width=10,
                    borderwidth=5)
saisi_annee.grid(row=0, column=2, sticky=W, padx=10, pady=7)

president_txt = StringVar()
saisi_presi = Entry(frame_saisis, textvariable=president_txt, font=("Arial", 10), width=40,
                    borderwidth=5)
saisi_presi.grid(row=8, sticky=W, padx=10, pady=7)

pib_txt = StringVar()
saisi_pib = Entry(frame_saisis, textvariable=pib_txt, font=("Arial", 10), width=40,
                  borderwidth=5)
saisi_pib.grid(row=9, sticky=W, padx=10, pady=7)


enregistrer = Button(frame, text="Enregistrer", padx=30,
                     pady=5, fg="white", bg="#263D42", command=lambda: ajout_pays())
enregistrer.grid(row=2, column=2)

retour = Button(frame, text="Retour", padx=10,
                pady=5, fg="white", bg="#263D42", command=lambda: retourarriere())
retour.grid(row=2, column=3)

entrer_window.mainloop()
