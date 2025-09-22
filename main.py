
"""Code qui teste si une chaîne de caractères est un palindrome"""
#### Fonction secondaire



def normaliser_accents(chaine):
    """Remplace les accents/ligatures par leurs équivalents ASCII."""
    chaine = chaine.lower()
    mapping = str.maketrans({
        #espace
        " ": "",
        #ponctuation
        ",": "", "-": "","'": "", ":": "","!": "","?": "",".": "",
        # minuscules
        "é": "e", "è": "e", "ê": "e", "ë": "e",
        "à": "a", "â": "a", "ä": "a", "á": "a", "ã": "a",
        "î": "i", "ï": "i", "í": "i", "ì": "i",
        "ô": "o", "ö": "o", "ó": "o", "ò": "o", "õ": "o",
        "ù": "u", "û": "u", "ü": "u", "ú": "u",
        "ç": "c", "ñ": "n",
        "œ": "oe", "æ": "ae",
    })
    return chaine.translate(mapping)

def ispalindrome(p):
    """Dis si une chaîne de caractère p est un palindrome"""
    s = normaliser_accents(p)
    return s == s[::-1]



if __name__ == "__main__":
    tests = [
        "Ésope reste ici et se repose",
        "Noël a trop par rapport à Léon",
        "Céçi n'est pas un palindrome",
        "été",
        "Kayak",
        "Engage le jeu que je le gagne",
    ]
    for s in tests:
        print(f"{s!r} -> {ispalindrome(s)}")









def main():
    """Fait quelques appels sur différentes chaînes de caractères"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
