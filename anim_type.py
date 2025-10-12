# This section is optional.


# -- Modules -- #

import os
import sys
import time


# -- Functions -- #

def typing_animation(text:str,delay:float=0.05,newline:bool=True)->None:  # Function to print with animation.

    for char in text:              # Loop through each character in the input text
        
        sys.stdout.write(char)     # Write the colored character to stdout without buffering
        
        sys.stdout.flush()         # Flush the output to ensure immediate display
        
        time.sleep(delay)          # Pause for the specified delay time between characters

    if newline: print()            # If newline is True, print a newline to move to the next line

def deleting(charNum:int)->None:    # Function to delete a specified number of characters from the console output
    
    sys.stdout.write(charNum*"\b")  # Move the cursor back by charNum positions using backspace characters
    sys.stdout.write(charNum*" ")   # Overwrite the characters with spaces to clear them from the display
    sys.stdout.write(charNum*"\b")  # Move the cursor back again to the original position after clearing
    sys.stdout.flush()              # Flush the output buffer to ensure the changes are displayed immediately

def clear()->None: # Function to clear the terminal
    
    if os.name == "nt":
        os.system("cls") # Windows
    else:
        os.system("clear") # Linux and Macos
