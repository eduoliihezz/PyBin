import requests
import os
from colorama import Fore, Style, init
init(autoreset=True)

########## Declaramos variables ##########

# Variables del Login
username = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu nombre de Usuario: ')
passwd = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu contraseña: ')
os.system("cls")

# Variables del "Paste"
key = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce your Developer API key: ')
user_key = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu User Key: ')
t_title = input(f'{Fore.YELLOW} [?] {Fore.RESET} Titulo del PasteBin: ')
text = input(f'{Fore.YELLOW} [?] {Fore.RESET} Contenido: \n [{Fore.GREEN}>{Fore.RESET}] ')
expiration = "N"
privacity = '0'
os.system("cls")

print(f'{Fore.GREEN} [+] {Fore.RESET} El titulo del Paste es: {t_title}')
print(f'{Fore.GREEN} [+] {Fore.RESET} El contenido del Paste es: {text}')
print(f'{Fore.GREEN} [+] {Fore.RESET} La expiración se ha establecido como -Nunca-, y la privacidad en -Publico-. Por Defecto')
print('========================================')
########## FIN Variables ##########

login_data = {
    'api_dev_key': key,
    'api_user_name': username,
    'api_user_password': passwd
    }
data = {
    'api_option': 'paste',
    'api_dev_key': key,
    'api_paste_code':text,
    'api_paste_name':t_title,
    'api_paste_expire_date': expiration,
    'api_user_key': user_key,
    'api_paste_private': privacity,
    'api_paste_format': 'text'
    }

login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)
print(f'{Fore.BLUE} [~] {Fore.RESET} Login status: ', login.status_code if login.status_code != 200 else "OK/200")
print(f'{Fore.BLUE} [~] {Fore.RESET} User token: ', login.text)
data['api_user_key'] = login.text

r = requests.post("https://pastebin.com/api/api_post.php", data=data)
print(f'{Fore.BLUE} [~] {Fore.RESET} Paste send: ', r.status_code if r.status_code != 200 else "OK/200")
print(f'{Fore.BLUE} [~] {Fore.RESET} Paste URL: ', r.text)
print('========================================')