import tkinter as tk

def inscription():
    pseudo = entry_pseudo.get()
    mdp = entry_mdp.get()
    email = entry_email.get()

    # Afficher les données sur le terminal
    print("Pseudo:", pseudo)
    print("Mot de passe:", mdp)
    print("Email:", email)

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Inscription")

# Créer et placer les widgets dans la fenêtre
label_pseudo = tk.Label(fenetre, text="Nom:")
label_pseudo.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

entry_pseudo = tk.Entry(fenetre)
entry_pseudo.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(fenetre, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_email = tk.Entry(fenetre)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_mdp = tk.Label(fenetre, text="Mot de passe:")
label_mdp.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

entry_mdp = tk.Entry(fenetre, show="*")
entry_mdp.grid(row=1, column=1, padx=10, pady=5)



bouton_inscription = tk.Button(fenetre, text="Inscription", command=inscription)
bouton_inscription.grid(row=3, column=0, columnspan=2, pady=10)

# Lancer la boucle principale
fenetre.mainloop()
