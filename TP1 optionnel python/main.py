# algorithmie et programmation 1 - TP1

# 1 Introduction

#Les TPs s'eectueront en mode Terminal, sans utiliser d'IDE1.
#Une fois connecte a votre compte 2, ouvrez un Terminal.
#Creez ensuite un dossier Python, qui contiendra tous vos scripts de Python ce semestre, puis un sous-
#dossier TP1.
#Une fois dans ce dossier, lancez la commande Python3 pour utiliser la calculatrice Python
#[bonzon@pc529-1:~]$ mkdir Python
#[bonzon@pc529-1:~]$ cd Python
#[bonzon@pc529-1:~/Python]$ mkdir TP1
#[bonzon@pc529-1:~/Python/TP1]$ cd TP1
#[bonzon@pc529-1:~/Python/TP1]$ Python3


# exercice 5 - le magicien
print('exo 5 :')
# 1
nbentier = int(input('pensez à un nombre entier :'))
resultat = nbentier * 5
ajout = int(resultat) + 7
multiple =  int(ajout) * 4
ajout2 =  int(multiple) + 6
magie =  int(ajout2) * 5
print('1')
print('annonce : ', magie)

# 2
print('2')
print('je pense pouvoir deviner l entier initial à partir du résultat précédent :')
magiemagie = magie/5
magiemagie2 = magiemagie - 6
magiemagie3 = magiemagie2/4
magiemagie4 = magiemagie3 - 7
magiemagie5 = magiemagie4/5
print()
print('l entier initial est :', magiemagie5)

# exercice 6 :

# 1
print('exercice 6 :')
a = 4
b = -2
x=1
print('ax + b = 0')
f = a*x + b
b = a*x
b /= a*x
print('x est égal à :', b)