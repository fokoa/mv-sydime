

def tension_arterille():
    """ Cette methode permet de recuperer le tension arterielle d'un patient"""

    tension = -1
    while tension < 0 :
        tension = input("VEUILLEZ INDIQUER LA TENSION ARTERIELLE DU PATIENT :")
        try :
            tension = float(tension)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA TENSION DU PATIENT")
            tension = -1
        if tension < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")
    
    return tension



def frequence_card():
    """ Cette methode permet de recuperer la frequence cardiaque d'un patient"""

    frequence_c = -1
    while frequence_c < 0 :
        frequence_c = input("VEUILLEZ INDIQUER LA FREQUENCE CARDIAQUE DU PATIENT :")
        try :
            frequence_c = float(frequence_c)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA FREQUENCE CARDIAQUE DU PATIENT")
            frequence_c = -1
        if frequence_c< 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")
    
    return frequence_c
    


def frequence_resp():
    """ Cette methode permet de recuperer la frequence respiratoire d'un patient"""

    frequence_r = -1
    while frequence_r < 0 :
        frequence_r = input("VEUILLEZ INDIQUER LA FREQUENCE RESPIRATOIRE DU PATIENT :")
        try :
            frequence_r = float(frequence_r)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA FREQUENCE RESPIRATOIRE  DU PATIENT")
            frequence_r = -1
        if frequence_r< 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")
    
    return frequence_r



def Temperature():
    """ Cette methode permet de recuperer le temperature d'un patient"""

    temperature = -1
    while temperature < 0 :
        temperature = input("VEUILLEZ INDIQUER LA TEMPERATURE DU PATIENT :")
        try :
            temperature = float(temperature)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA TEMPERATURE  DU PATIENT")
            temperature = -1
        if temperature < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")
    
    return temperature



def Glycemie():
    """ Cette methode permet de recuperer la glycemie d'un patient"""

    glycemie = -1
    while glycemie < 0 :
        glycemie = input("VEUILLEZ INDIQUER LA GLYCEMIE DU PATIENT :")
        try :
            glycemie = float(glycemie)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA GLYCEMIE DU PATIENT")
            glycemie = -1
        if glycemie < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return glycemie



def Saturation_Ox():
    """ Cette methode permet de recuperer la saturation en oxigene d'un patient"""

    saturation = -1
    while saturation < 0 :
        saturation = input("VEUILLEZ INDIQUER LA SATURATION EN OXIGENE DU PATIENT :")
        try :
            saturation = float(saturation)
        except ValueError :
            print("DESOLE MAIS LA VALEUR ENTRE N'EST PAS UNE VALEUR NUMERIQUE MAIS UN MOT\n")
            print("VEUILLEZ ENTRER UNE VALEUR NUMERIQUE POUR INDIQUER LA SATURATION EN OXIGENE DU PATIENT")
            saturation = -1
        if saturation < 0 :
            print("DESOLE MAIS LA VALEUR ENTRE EST NEGATIVE ! VEUILLEZ ENTRER UNE VALEUR A PARTIR DE 0 ")

    return saturation


