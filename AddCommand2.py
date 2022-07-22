import pyautogui #Controlling keyboard
import time #sleep
print('\033[1;32m')
#intro
print(" +--^----------,--------,-----,--------^-, ")
print(" | |||||||||   `--------'     |          O ")
print(" `+---------------------------^----------| ")
print("   `\_,---------,---------,--------------' ")
print("     / XXXXXX /'|       /' ")
print("    / XXXXXX /  `\    /' ")
print("   / XXXXXX /`-------' ")
print("  / XXXXXX / ")
print(" / XXXXXX / ")
print("(________(                ")
print(" `------'         TARANTULA SPAMMER     ")

y = input ('what you want to spam? :')
times = input('How many times you want to spam:')
print('your attack will start in 5 seconds! prepare!')
time.sleep(5)
for x in range(int(times)) :
    pyautogui.write(str(y)) #Write String
    pyautogui.press('enter') #Press Enter
