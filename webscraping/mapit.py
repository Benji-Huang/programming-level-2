# mapit.py -  launches a map in a
# browser using an address from the command line

import webbrowser, sys, pyperclip

# If there are no aruguments, use args as address
# If there are no arguments, grab from grab from clipboord

# Factor
prefix = "https://www.google.com/maps/place/"

if len(sys.argv) > 1:
    address= " ".join(sys.argv[1:])

else:
    address = pyperclip.paste()

# Factor
webbrowser.open(prefix + address)
