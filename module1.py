import csv



def tableau(data): 
    print(f"{'Nom':<5}|  {'Categorie':<20}|  {'nom ':<70}| {'prix':<12}")
    print("-" * 120)
    for ligne in data:
        print(f"{ligne[0]:<5}|  {ligne[1]:<20}|  {ligne[2]:<70}| {ligne[3]:<12}")

def afficher_menu():
    global plat
    with open('C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv',
              'r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)  # sauter 
        menu = []
        data = []
        for plat in lecteur:
            if len(plat) < 4:
                continue
            ligne = (plat[0], plat[1], plat[2], plat[3])  #id, cat, nom, prix
            data.append(ligne)
            menu.append(plat)
        tableau(data)
        return menu
def prendre_commande():
    commande = []
    while True:  
        plat = input("Entrez le numero du plat que vous souhaitez commander (ou '0' pour quitter) : ")
        if plat == '0':
            print("Commande termieée.")
            break
        if not plat.isdigit():
            print("Entree invalide. Veuillez entrer uniquement des chiffres.")
            continue
        plat = int(plat)
        if plat <= 0 or plat > 260:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 260.")
            continue

        commande.append(plat)
        print(f"'{plat}' ajoute à la commande.")  # corrigé "ajouter" -> "ajouté" et meilleur français
    return commande
def calculer_total(commande):
    total = 0
    t = 0
    with open('C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv',
              'r', encoding='utf-8') as fichier:
        lecteur = csv.reader(fichier)
        next(lecteur)  # sauter
        for plat in lecteur:
            if len(plat) < 4:
                continue
            if int(plat[0]) in commande:
                t += float(plat[3])
        t2 = t*1.15
        total = round(t2, 2)
    return total
def recu(total,commande):
    with open('C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\recu.txt', 'w') as fichier:
        fichier.write("Voici votre commande : \n")
        for plat in commande:
            fichier.write(f"{plat}\n")
        fichier.write(f"Le total de votre commande est : {total} $\n")
        print("Recu enregistré dans le fichier 'recu.txt'.")

#debug and main
Y= 1
X = 0
if X == 1:#debug
    with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r', encoding='utf-8') as f:
     r = csv.reader(f)
     for row in r:
       print(row)

if Y == 1: #main
    print("plat")
    menu = afficher_menu()
    c = prendre_commande()
    total = calculer_total(c)
    recu(total,c)
    print("votre total est", total, " $")


