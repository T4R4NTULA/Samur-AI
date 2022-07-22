from colorama import init #collors
import os #for console clearing
init()
#Console Clear definiton for different Operation Systems 
def clearscreen():
    os.system('cls' if os.name=='nt' else 'clear')
#main Script
def run_SamurAI():
    #intro
    print('\033[31m')
    print('  ██████  ▄▄▄       ███▄ ▄███▓ █    ██  ██▀███         ▄▄▄       ██▓ ')
    print('▒██    ▒ ▒████▄    ▓██▒▀█▀ ██▒ ██  ▓██▒▓██ ▒ ██▒      ▒████▄    ▓██▒ ')
    print('░ ▓██▄   ▒██  ▀█▄  ▓██    ▓██░▓██  ▒██░▓██ ░▄█ ▒      ▒██  ▀█▄  ▒██▒ ')
    print('  ▒   ██▒░██▄▄▄▄██ ▒██    ▒██ ▓▓█  ░██░▒██▀▀█▄        ░██▄▄▄▄██ ░██░ ')
    print('▒██████▒▒ ▓█   ▓██▒▒██▒   ░██▒▒▒█████▓ ░██▓ ▒██▒       ▓█   ▓██▒░██░ ')
    print('▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░░ ▒░   ░  ░░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░       ▒▒   ▓▒█░░▓   ')
    print('░ ░▒  ░ ░  ▒   ▒▒ ░░  ░      ░░░▒░ ░ ░   ░▒ ░ ▒░        ▒   ▒▒ ░ ▒ ░ ')
    print('░  ░  ░    ░   ▒   ░      ░    ░░░ ░ ░   ░░   ░         ░   ▒    ▒ ░ ')
    print('      ░        ░  ░       ░      ░        ░                 ░  ░ ░   ')
    print('                                                   Tool Kit for Skids')
    #end of intro
    print('\033[39m') #color
    #choise
    print('1) DDos ') #website Attacking
    print('2) Camera Hacking') #Hacking Cameras
    print('3) Spammer') #Spamming Text
    print('99) leave')
    command = input('Your Choise : ')
    if int(command) == 1 :
        import AddCommand   #my script
        input('Press enter To return : ')
    elif int(command) == 2 : 
        import AddCommand1 #Found Script in Github
        input('Press enter To return : ')
    elif int(command) == 3 :
        import AddCommand2 #my script
        input('Press enter To return : ')
    elif int(command) == 99 :
        exit() 
    else : 
        input('Option Not Found! Try Again! :')
    clearscreen() 
while True:
    run_SamurAI()