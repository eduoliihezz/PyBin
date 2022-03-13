# 📄| PyBin

Python scripts that connects Python with Pastebin, giving you the option to upload a Paste with an account or anonymously.

## 🛠| Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
In this case, the only requirement that we need is `Colorama`

```bash
pip install colorama
```
Go to `main_login.py` file and edit:
```python
username = 'PasteBin Username' # Line 9
passwd = 'PasteBin Password' # Line 10

key = 'PasteBin Developer APIKey' # Line 14
user_key = 'PasteBin User APIKey' # Line 15
```
If you need help with the Developer or User keys, go to the [Pastebin Wiki](https://pastebin.com/doc_api#1).

## ⚙| Usage
Run the `main.py` file. It's a menu for the `main_login.py` or the `temp_login.py`
```bash
python main.py
```
```python
def login():
    # Ask your for use the "main account" or a Temporal Login.
    login_acc = input(f'[{Fore.BLUE}*{Fore.RESET}] Desea utilizar otra cuenta? (Y/N): ')
    if login_acc == 'N':
        os.system('python main_login.py')
    else:
        os.system('python temp_login.py')

login()
```
`main_login.py`
```python
# PasteBin Title
t_title = input(f'{Fore.YELLOW} [?] {Fore.RESET} Titulo del PasteBin: ')
# PasteBin Content (ex. Hello World)
text = input(f'{Fore.YELLOW} [?] {Fore.RESET} Contenido del Paste: \n [{Fore.GREEN}>{Fore.RESET}] ')
# PasteBin Expiration of the Paste (Default Never)
expiration = "N"
# PasteBin Privacity (Default Public)
privacity = '0'
os.system("cls")

# Shows the info of the paste.
print(f'{Fore.GREEN} [+] {Fore.RESET} El titulo del Paste es: {t_title}')
print(f'{Fore.GREEN} [+] {Fore.RESET} El contenido del Paste es: {text}')
print(f'{Fore.GREEN} [+] {Fore.RESET} La expiración se ha establecido como -Nunca-, y la privacidad en -Publico-. Por Defecto')
print('========================================')
```
`temp_login.py`
```python
# Ask for the Username of PasteBin
username = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu nombre de Usuario: ')
# PasteBin Password
passwd = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu contraseña: ')
os.system("cls")

# Developer And User APIKey
key = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce your Developer API key: ')
user_key = input(f'{Fore.YELLOW} [?] {Fore.RESET} Introduce tu User Key: ')
```

## 🤝| Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[APACHE 2.0](https://choosealicense.com/licenses/apache-2.0/)