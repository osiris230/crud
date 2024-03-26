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


#create_user("John Dope", "john.dope@example.com")
read_users()
#update_user(2, 'emicheldev@gmail.com')
#delete_user(2)
#saisie()