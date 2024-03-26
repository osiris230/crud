import mysql.connector as mysql

#Établir un connexion à la base de données
mydb = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database ='crud')

def create_user(nom, email):
    cursor = mydb.cursor()
    cursor.execute("""
        INSERT INTO utilisateurs (nom, email)
        VALUES (%s,%s)
    """, (nom, email))
    mydb.commit()

def read_users():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    for(id, nom, email) in cursor:
        print(f"ID: {id}, NOM: {nom}, Email: {email}")

def update_user(id, email):
    cursor = mydb.cursor()
    cursor.execute("UPDATE utilisateurs SET email=%s WHERE id=%s", (email, id))
    mydb.commit()

def delete_user(id):
    cursor = mydb.cursor()
    cursor.execute("DELETE FROM utilisateurs WHERE id = %s", (id,))
    mydb.commit()

def saisie():
    nom=input("Entrez votre nom : ")
    email=input("Entrez votre adresse e-mail : ")
    create_user(nom, email)

def menu():
    while True:
        print("\nMenu:")
        print("1. Ajouter un utilisateur")
        print("2. Afficher les utilisateurs")
        print("3. Mettre à jour un utilisateur")
        print("4. Supprimer un utilisateur")
        print("5. Quitter")
        choix = input("Entrez votre choix (1-5): ")

        if choix == '1':
            nom = input("Entrez votre nom complet : ")
            email = input("Entrez votre adresse e-mail : ")
            create_user(nom, email)
        elif choix == '2':
            read_users()
        elif choix == '3':
            id = input("Entrez l'ID de l'utilisateur à mettre à jour : ")
            email = input("Entrez le nouvel email : ")
            update_user(id, email)
        elif choix == '4':
            id = input("Entrez l'ID de l'utilisateur à supprimer : ")
            delete_user(id)
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Choix non valide. Veuillez réessayer.")

menu()
#create_user("John Dope", "john.dope@example.com")
#read_users()
#update_user(2, 'emicheldev@gmail.com')
#delete_user(2)
#saisie()