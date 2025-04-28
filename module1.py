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
            ligne = (plat[0], plat[1], plat[2], plat[3])  # (ID, Cat�gorie, Nom, Prix)
            data.append(ligne)
            menu.append(plat)
        # Fin de la boucle for : on peut maintenant appeler tableau et retourner
        tableau(data)
        return menu
def prendre_commande():
    commande = []
    while True:  # Corrigé "wwhile" -> "while"
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



#debug
Y= 1
X = 0

with open(r"C:\\Users\\23cha\\Documents\\GitHub\\projet-debug\\menu.csv", 'r', encoding='utf-8') as f:
    r = csv.reader(f)
    for row in r:
        if X == 1:
            print(row)

if Y == 1:
    print("plat")
    menu = afficher_menu()
    c = prendre_commande()
#variables

#c = Conard()

#main


