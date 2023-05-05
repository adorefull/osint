import colorama
import webbrowser
from colorama import Fore, Back, Style
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

os.system(f'cls & title osint tool fully coded by @adorefull on github')

# Initialize colorama
colorama.init()

def done():
    clear_screen()
    print('Thanks for using this osint tool, hope u enjoyed')
    input('Press any key to exit')
    exit()
# Define a function to handle the user's choice
def handle_choice(choice):
    if choice == 1:
        url = "https://www.numlookup.com/"
        webbrowser.open_new_tab(url)
        print("Opening the URL:", url)
    if choice == 2:
        url = "https://www.truepeoplesearch.com/"
        webbrowser.open_new_tab(url)
        print("Opening the URL:", url)
    
    if choice == 3:
        url = 'https://whatismyipaddress.com/ip-lookup'
        webbrowser.open_new_tab(url)
        print("Opening the URL:", url)
    if choice == 4:
        url = 'https://www.proxysite.com/'
        webbrowser.open_new_tab(url)
        print("Opening the URL:", url)
    if choice == 5:
        url = 'https://github.com/adorefull'
        webbrowser.open_new_tab(url)
        print("Opening the URL:", url)
    if choice == 6:
        done()
    else:
        print("Invalid option selected.")

# Create a list of options
options = [1, 2, 3, 4, 5]

while True:
    clear_screen()
    # Print the options to the user
    print( Fore.RED + """
    ______________¶¶¶
    _____________¶¶_¶¶¶¶
    ____________¶¶____¶¶¶
    ___________¶¶¶______¶¶
    ___________¶¶¶_______¶¶
    __________¶¶¶¶________¶¶
    __________¶_¶¶_________¶¶                  ╔════════════════════════════════════════════════╗
    __________¶__¶¶_________¶¶____¶¶           ║→ 1 | number lookup.............................║
    __________¶__¶¶__________¶¶¶¶¶¶¶           ║→ 2 | people lookup.............................║
    _________¶¶__¶¶¶______¶¶¶¶¶¶___¶           ║→ 3 | ip lookup.................................║ 
    _________¶¶___¶¶__¶¶¶¶¶¶__¶¶               ║→ 4 | good free proxy...........................║
    _______¶¶_¶____¶¶¶¶________¶¶              ║→ 5 | Credits...................................║
    ______¶¶__¶¶___¶¶__________¶¶              ║→ 6 | Exit......................................║
    _____¶¶____¶¶___¶¶__________¶¶             ╚════════════════════════════════════════════════╝
    ___¶¶_______¶¶___¶¶_________¶¶
    ___¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
    _¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶ 
    ¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶               empowered by um#1414
    ¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
    ________¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
    ______¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
    ______¶¶¶¶¶¶¶¶¶¶¶¶
    ______¶__¶¶_¶¶¶¶¶¶
    _____¶¶______¶___¶
    _____¶¶_____¶¶___¶
    _____¶______¶¶___¶
    ____¶¶______¶¶___¶¶
    ____¶¶______¶¶___¶¶
    ___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    __¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
    __¶¶________¶¶¶____¶¶
    ____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    """ + Style.RESET_ALL )


    # Get the user's choice
    choice = int(input(Fore.RED + "choice? : " + Style.RESET_ALL))

    # Handle the user's choice
    handle_choice(choice)