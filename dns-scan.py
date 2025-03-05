import requests
import fade
import colorama
from colorama import Fore


def scan():
    ascii_art = '''
██▄      ▄      ▄▄▄▄▄       █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
█  █      █    █     ▀▄     █    █   █ █   █ █▄█     █  █   █ 
█   █ ██   █ ▄  ▀▀▀▀▄       █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █  █  ▀▄▄▄▄▀        ███▄ ▀████ ▀████ █  █ █   █ █     
███▀  █  █ █                    ▀              █  █▄ ▄█  █    
      █   ██                                  ▀    ▀▀▀    ▀   
                                                            '''
    print(fade.purplepink(ascii_art))
    choice = input(Fore.LIGHTMAGENTA_EX+"enter the link to scan : ")
    api = "https://api.hackertarget.com/dnslookup/?q=" + choice
    res = requests.get(api)
    results = res.text
    print()
    print(results)
    print()
    input("Press enter for exit..")
    
scan()

