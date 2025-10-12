import values as vls


def isMorse(text:str):

    return text[0] in (".","-")

def NormalToMorse(text:str):

    info = vls.morse_alphabet

    text = text.upper()

    new_text = ""

    for letter in text:

        new_text += info[letter]+" "

    return new_text

def MorseToNormal(text:str):

    info = vls.alphabet

    letters = text.split(" ")

    new_text = ""

    for letter in letters:

        
         new_text += info[letter]

    return new_text
