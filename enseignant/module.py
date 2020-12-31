from fonction import * 
from systeme.systeme_cardio import *
from systeme.systeme_digestif import *
from systeme.systeme_endocrinologique import *
from systeme.systeme_genital import *
from systeme.systeme_hematopoietique import *
from systeme.systeme_nerveux import *
from systeme.systeme_ophtalmique import *
from systeme.systeme_pulmonaire import *
from systeme.systeme_sphere import *
from systeme.systeme_urinaire import *
from parametres.parametres_vitaux import *
from parametres.complementaire import *
from parametres.parametre_entropometrique import *
from traitement.traitement import *
from diagnostic.diagnostics import *
from random import randrange


def identification():
    """ Dans cette première fonction nous récupérons l'identifiant, le nom, l'age et le sexe du aptient """
    
    # ON RECUPERE L'IDENTIFIANT' DU PATIENT
    ID = randrange(99999)

    # ON RECUPERE LE NOM DU PATIENT
    Nom = input("Entrez le nom du patient : ")

    # ON RECUPERE L'AGE DU PATIENT
    age_max =200
    age = 0
    while age <= 0 or age > age_max :
        age = input("VEUILLEZ ENTRER L'AGE DU PATIENT : ")
        try :
            age = int(age)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UN NOMBRE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UN NOMBRE POUR INDIQUER L'AGE DU PATIENT")
            age = 0
        if age < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIIVE! VEUILLEZ ENTRER UN AGE VALIDE ")
        elif age > age_max  :
            print("DESOLE VOUS NE POUVEZ AVOIR UN AGE SUPERIEUR A ",age_max," ANS")
    
    # ON RECUPERE LE SEXE DU PATIENT
    sexe = Sexe()

    identifiant ={
        "Identifiant":ID,
        "Nom":Nom,
        "Age":age,
        "Sexe":sexe
    }
    return identifiant



def Symptome():
    """ Cette methode permet de returner les symptômes du patient"""
    liste_symptome  = []

    ajouter_symptome = True
    while ajouter_symptome== True:
        symptome = input("VEUILLEZ INDIQUER LES SYMPTOMES DU PATIENT : ")
        liste_symptome.append(symptome)
        
        rajouter = input("PRESENTE T-IL D'AUTRES SYMPTOMES? REPONDEZ PAR O/n : ")
        if rajouter == 'O' or rajouter == 'o':
            ajouter_symptome = True
        else:
            ajouter_symptome = False

    return liste_symptome 

def Contexte():
    """Cette fonction permet de récupérer les données permettant de spécifier le contexte social du patient """
    # ON RECUPERE LE STATUS DU PATIENT
    status = Status()

    # ON RECUPERE LE METIER DU PATIENT
    metier = input("VEUILLEZ INDIQUER LE METIER DU PATIENT : \n")

    # ON RECUPERE LA RELIGION DU PATIENT
    religion = input("VEUILLEZ INDIQUER LA RELIGION DU PATIENT : \n")

    # ON RECUPERE L'ETHNIE DU PATIENT
    ethnie = input("VEUILLEZ INDIQUER L'ETHNIE DU PATIENT : \n")

    # ON RECUPERE LA RESIDENCE DU PATIENT
    residence = input("VEUILLEZ INDIQUER LA RESIDENCE DU PATIENT : \n")

    # ON RECUPERE LE NOM DU CONJOINT DU PATIENT
    if status == "MARIE" or status ==  "FIANCE":
        personne = input("VEUILLEZ INDIQUER LE NOM DU CONJOINT : \n")
    elif status =="CELIBATAIRE" or status == "AUTRE":
        personne = input("VEUILLEZ INDIQUER LE NOM DE LA PERSONNE AVEC QUI VOUS VIVEZ : \n")

    # ON RECUPERE LE NUMERO DE TELEPHONE DU PATIENT
    telephone = randrange(999999999)

    contexte_social ={
        "status matrimonial":status,
        "metier": metier,
        "religion": religion,
        "ethnie":ethnie,
        "residence":residence,
        "conjoint ou autre personne": personne,
        "telephone":telephone
    }

    return contexte_social



def Histoire():
    """ Cette methode recupère l'histoire de la maladie du patient"""

    #ON RECUPERE LA DATE DE DEBUT DES TOUS PREMIERS SYMPTOMES
    date_debut = input("INDIQUEZ A QUAND REMONTE LES TOUS PREMIERS SYMPTOMES : ")

    #ON RECUPERE LES SYMPTOMES
    symptomes = Symptome()

    #ON RECUPERE LA FREQUENCE
    frequence = input("INDIQUEZ LA FREQUENCE DES SYMPTOME :  ")

    # ON INDIQUE L'ACTION POSEE POUR ATTENUER LES SYMPTOMES
    action = input(" INDIQUEZ L'ACTION QUI A ETE POSEE POUR ATTENUER LES SYMPTOMES : ")

    # ON INDIQUE LA DATE DE L'ACTION POSEE POUR ATTENUER LES SYMPTOMES
    quand = input("QUAND EST CE QUE L'ACTION A ETE POSE :  ")

    # ON INDIQUE LE LIEU DE L'ACTION POSEE POUR ATTENUER LES SYMPTOMES
    ou = input("OU EST CE QUE L'ACTION A ETE POSEE")

    # ON INDIQUE L'EVOLUTION DE LA MALADIE
    evolution = input("EXPLIQUEZ L'EVOLUTION DE LA MALADIE")

    histoire = {
        "La date de debut de la maladie":date_debut,
        "les symptomes":symptomes,
        "la frequence des symptomes":frequence,
        "action posee pour attenuer les symptomes":action,
        "la date de l'action":quand,
        "le lieu de l'action":ou,
        "l'evolution de la maladie":evolution
    }

    return histoire



def Antecedent(sexe):
    """ Cette méthode permet de récupéré les antécedents du patient """
  
    mode = mode_vie()
    medical = medicale()
    chirugies = chirugicale()
    immune = Immuno_allergique()
    toxi = Toxicologie()
    famille = Familiaux()
    genico =Genico_obs(sexe)

    liste_antécédent = [mode, medical, chirugies, immune, toxi, famille, genico]

    return liste_antécédent



def enquetes_systemique():
    cardio = systeme_cardio()
    digestif = systeme_digestif()
    endocrine = systeme_endo()
    genital = systeme_geni()
    hematopoiet = systeme_hema()
    nerveux = systeme_nerv()
    ophtalmique = systeme_oph()
    pulmonaire = systeme_pul()
    sphere = systeme_sphere()
    urinaire = systeme_urinaire()


    liste_enquete = [cardio, digestif, endocrine, genital, hematopoiet, nerveux, ophtalmique, pulmonaire, sphere, urinaire]

    return liste_enquete



def Parametre():
    print(" PARAMETRES VITAUX DU PATIENT \n")
    tension = tension_arterille()
    fre_card = frequence_card()
    fre_resp = frequence_resp()
    temperature = Temperature()
    saturation = Saturation_Ox()
    
    vitaux = {
        "Nom": "Parametres vitaux",
        "Tension":tension,
        "Frequence cardiaque":fre_card,
        "Frequence Respiratoire":fre_resp,
        "Temperature":temperature,
        "Saturation en Oxigene":saturation
    }

    print(" PARAMETRES ENTROPOMETRIQUE DU PATIENT \n")

    poids = Poids()
    taille = Taille()
    indice = Indice_masse()
    circon = Circonference()

    entro = {
        "Nom": "Parametres Entropometrique",
        "Poids":poids,
        "Taille":taille,
        "Indice de masse":indice,
        "Circonference Abdominale":circon
    }

    liste_parametre = [vitaux, entro]

    return liste_parametre



def Examens():
    cardio = Examen_cardio()
    digestif = Examen_digestif()
    endocrine = Examen_endo()
    genital = Examen_geni()
    hematopoiet = Examen_hema()
    nerveux = Examen_nerv()
    ophtalmique = Examen_oph()
    pulmonaire = Examen_pul()
    sphere = Examen_sphere()
    urinaire = Examen_urinaire()

    liste_examen= [cardio, digestif, endocrine, genital, hematopoiet, nerveux, ophtalmique, pulmonaire, sphere, urinaire]

    return liste_examen


def Diagnostic():
    Hypo = hypothese()

    Hypothese = {
        "Titre":"Hypotheses de Diagnostic",
        "Details":Hypo
    }

    trav= diag_travail()

    travail = {
        "Titre":"Diagnostic de travail",
        "Details":trav
    }

    liste_diagnostic = [Hypothese, travail]

    return liste_diagnostic



def Examen_complementaire():
    print(" PRESENTATION DES EXAMENS COMPLEMENTAIRES DU PATIENT \n")
    complementaire = Complementaire()

    return complementaire


def traitements():
    traitement = Traitement()

    return traitement


