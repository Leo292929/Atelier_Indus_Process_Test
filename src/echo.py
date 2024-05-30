from locale import getlocale
from datetime import datetime


liste_mot_francais = {"matin": ["bonjour", "bonne journée"], "soir": ["bonsoir", "bonne soirée"], "bien dit": "Bien dit"}
liste_mot_anglais = {"matin": ["good morning", "Have a good day"], "soir": ["good evening", "good night"], "bien dit": "Well Said"}

language = {"fr_FR": liste_mot_francais, "en_US": liste_mot_anglais}

system_language = getlocale()[0]

liste_mot = language[system_language]

heure_actuelle = datetime.now().time().hour


def est_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    return s == s[::-1]


def echo():
    if heure_actuelle < 12:
        print(liste_mot["matin"][0])
    else:
        print(liste_mot["soir"][0])

    while True:
        user_input = input("\n")

        if user_input.lower() == 'exit':
            if heure_actuelle < 12:
                print(liste_mot["matin"][1])
            else:
                print(liste_mot["soir"][1])
            break

        elif est_palindrome(user_input):
            print(liste_mot["bien dit"])

        else:
            print(user_input[::-1])


if __name__ == "__main__":
    echo()
