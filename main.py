from translater import *
from anim_type import *
from settings import settings


if __name__== "__main__":

    def menu():

        while True:

            msg = input("Message: ")

            new = MorseToNormal(msg) if isMorse(msg) else NormalToMorse(msg)

            typing_animation(new) if settings["animatedTyping"] else print(new)
        
        
    menu()