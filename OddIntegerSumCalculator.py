
n = int(input("Veuillez entrer un entier n : "))
somme = 0.0


for i in range(1, n + 1):
    entier_impairs = 2 * i - 1
    somme += entier_impairs ** 2

print("Voici la somme :", somme)
