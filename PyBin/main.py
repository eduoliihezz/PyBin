import os
from colorama import Fore

def login():
    login_acc = input(f'[{Fore.BLUE}*{Fore.RESET}] Desea utilizar otra cuenta? (Y/N): ')
    if login_acc == 'N':
        os.system('python main_login.py')
    else:
        os.system('python temp_login.py')

login()