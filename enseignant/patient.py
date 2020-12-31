from module import *
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
import json
import os


with open("donées.json", "a") as file:

    print("BIENVENUE DANS LE MODULE DE CREATION DU PATIENT VIRTUEL \n")

    print("******************************************************* \n")
    print("\n")

    print("POUR COMMENCER VEUILLEZ INDIQUER LE NOM, L'AGE ET LE SEXE DU PATIENT")

    identifiant = identification()
    sexe = identifiant["Sexe"]

    print("\n")

    print("VEUILLEZ DEFINIR LE CONTEXTE SOCIAL DU PATIENT \n")

    contexte = Contexte()


    print("\n")
    print("PRESENTEZ LES SYMPTOMES DU PATIENT \n")

    symptome = Symptome()

    print("\n")
    print("PRESENTEZ L'HISTOIRE DE LA MALADIE DU PATIENT \n")

    histoire = Histoire()


    print("\n")
    print("PRESENTEZ LES DIFFERENTS ANTECEDENTS DU PATIENT \n")

    antecedent = Antecedent(sexe)

    print("\n")
    print("PRESENTEZ LES ENQUETES SUR LES  DIFFERENTS SYSTEMES DU PATIENT \n")

    enquete = enquetes_systemique()

    print("\n")
    print("PRESENTEZ LES PARAMETRES DU PATIENT \n")

    parametre = Parametre()

    print("\n")
    print("PRESENTEZ LES EXAMENS EFFECTES SUR LES  DIFFERENTS SYSTEMES DU PATIENT \n")

    examens = Examens()

    print("\n")
    print("PRESENTEZ LES DIAGNOSTIC DU PATIENT \n")

    diagnostics = Diagnostic()

    print("\n")
    print("PRESENTEZ LES EXAMENS COMPLEMENTAIRES DU PATIENT \n")

    complementaire = Examen_complementaire()


    print("\n")
    print("PRESENTEZ LE TRAITEMENT DU PATIENT DU PATIENT \n")

    Traitement = traitements()

    Patient = {
        "Identification":identifiant
        "Contexte social":contexte,
        "Symptomes du patient":symptome,
        "Histoire de la maldie":histoire,
        "Antecedent du patient":antecedent,
        "Enquetes systemique":enquete,
        "Parametres du patient":parametre,
        "Examens du patient":examens,
        "Diagnostic du patient":diagnostics,
        "Examens complementaires":complementaire,
        "Traitement du patient":Traitement
    },

    json.dump(Patient, file, skipkeys=True, indent=4)
    
    file.close()

os.system("pause")


