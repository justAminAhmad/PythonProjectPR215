"""
module principale du programme
"""
from tkinter import *
import os


def main():
    # Les differentes fonctions de navigations du programme
    def entrer():
        root.destroy()
        os.system("python gui/ajouter.py")

    def afficher():
        root.destroy()
        os.system("python gui/afficher.py")

    def rechercher():
        root.destroy()
        os.system("python gui/rechercher.py")

    def modifier():
        root.destroy()
        os.system("python gui/modifier.py")

    def supprimer():
        root.destroy()
        os.system("python gui/supprimer.py")

    # creation d'une fenetre d'interface pour le menu principal
    root = Tk()
    root.title("Projet PR215")

    # creation d'un canvas comportant un frame qui enfin tiendra tous les elements du menu
    canvas = Canvas(root, width=600, height=500, bg='#263D42')
    canvas.grid(columnspan=2)

    frame = Frame(root, bg="#6AADB6", padx=80, pady=20)

    tete = Label(frame, text="Veuillez choisir une option",
                 bg="#263D42", fg="white", borderwidth=10, padx=70, pady=5)

    # creation des boutons
    ajouter_btn = Button(frame, text="Ajouter", padx=55,
                         pady=20, fg="white", bg='#263D42', command=lambda: entrer())

    afficher_btn = Button(frame, text="Afficher", padx=40,
                          pady=20, fg="white", bg='#263D42', command=lambda: afficher())

    rechercher_btn = Button(frame, text="Rechercher", padx=41,
                            pady=20, fg="white", bg='#263D42', command=lambda: rechercher())

    modifier_btn = Button(frame, text="Modifier", padx=39,
                          pady=20, fg="white", bg='#263D42', command=lambda: modifier())

    supprimer_btn = Button(frame, text="Supprimer", padx=115,
                           pady=20, fg="white", bg='#263D42', command=lambda: supprimer())

    quitter_btn = Button(frame, text="Quitter", padx=20,
                         pady=10, fg="white", bg='#263D42', command=lambda: exit())

    # Les fonctions grid permettant de placer les differents composants
    frame.grid(row=0, column=0, columnspan=2)
    tete.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    ajouter_btn.grid(row=1, column=0, padx=5, pady=5)
    afficher_btn.grid(row=1, column=1, padx=5, pady=5)
    rechercher_btn.grid(row=2, column=0, padx=5, pady=5)
    modifier_btn.grid(row=2, column=1, padx=5, pady=5)
    supprimer_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    quitter_btn.grid(row=4, column=1, pady=5)

    # l'execution de notre fenetre
    root.mainloop()


if __name__ == "__main__":
    main()
