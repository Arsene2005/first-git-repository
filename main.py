first_name = input("Entrez votre prénom : ")
last_name = input("Entrez votre nom : ")
print("Bonjour,", first_name, last_name)

age = input("Entrez votre âge : ")
print("Vous avez", age, "ans.")

rom datetime import datetime

current_year = datetime.now().year
birth_year = current_year - int(age)
print("Vous êtes né(e) en", birth_year)