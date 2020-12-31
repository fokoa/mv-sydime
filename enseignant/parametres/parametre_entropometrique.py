

def Taille():
    """ Cette methode permet de returner LA TAILLE d'un patiente"""

    taille = -1
    while taille < 0 :
        taille = input("VEUILLEZ INDIQUER LA TAILLE DU PATIENT :")
        try :
            taille = float(taille)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA TAILLE DU PATIENT")
            taille = -1
        if taille < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return taille


def Poids():
    """ Cette methode permet de returner Le poids d'un patiente"""

    poids = -1
    while poids < 0 :
        poids = input("VEUILLEZ INDIQUER LE POIDS DU PATIENT :")
        try :
            poids = float(poids)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LE POIDS DU PATIENT")
            poids = -1
        if poids < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return poids



def Indice_masse():
    """ Cette methode permet de returner L'indice de masse corporelle d'un patient"""

    indice = -1
    while indice < 0 :
        indice = input("VEUILLEZ INDIQUER LE POIDS DU PATIENT :")
        try :
            indice = float(indice)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LE POIDS DU PATIENT")
            indice = -1
        if indice < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return indice



def Circonference():
    """ Cette methode permet de returner La circonférence abdominale d'un patient"""

    circonference = -1
    while circonference < 0 :
        circonference = input("VEUILLEZ INDIQUER LE POIDS DU PATIENT :")
        try :
            circonference = float(circonference)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LE POIDS DU PATIENT")
            circonference = -1
        if circonference < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return circonference


