import os
import subprocess
import sys
sys.dont_write_bytecode = True
import time

import colorama
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate

init()

options = """
                        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                        ┃      Made by .fridge.         ┃     Skidding Since '23        ┃
                        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        ┃  [1] Webhook Spammer          ┃  [2] Webhook Deleter          ┃
                        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        ┃  [3] FX Webhook Spammer       ┃  [4] CBT Webhook Spammer      ┃
                        ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
                        ┃  [5] FX Discord               ┃  [6] Uncover It Discord       ┃
                        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

def banner():
    banner_text = """
                ███████╗██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                ██╔════╝╚██╗██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                █████╗   ╚███╔╝     ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
                ██╔══╝   ██╔██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                ██║     ██╔╝ ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                ╚═╝     ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                  
"""
    print(Colorate.Vertical(Colors.blue_to_red, banner_text, 1))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title FX SPAMMER                                                                                                                                                                                                                         Made By Fridge")
    banner()
    print(Colorate.Vertical(Colors.blue_to_red, options, 1))
    while True:
        user_input = Write.Input(f"\n\n [Select Option] : ", Colors.blue_to_red, interval=0.03)
        user_input = user_input.lower()
    
        if user_input == "1":
            subprocess.run(["python", "commands/webhook.py"])
            time.sleep(1.9)
            main()
        elif user_input == "":
            print("Error enter something")
            time.sleep(0.7)
            main()
        elif user_input == "2":
            subprocess.run(["python", "commands/dwebhook.py"])
            time.sleep(1.9)
            main()
        elif user_input == "3":
            subprocess.run(["python", "commands/fxwebhook.py"])
            time.sleep(1.9)
            main()
        elif user_input == "4":
            subprocess.run(["python", "commands/webhookcbt.py"])
            time.sleep(10)
            main()
        elif user_input == "5":
            print(Colorate.Horizontal(Colors.blue_to_red, ("FX Discord : https://discord.gg/TaAFW8UDa2"), 5))
            time.sleep(10)
            main()
        elif user_input == "6":
            print(Colorate.Horizontal(Colors.blue_to_red, ("Uncover It Discord : https://discord.gg/2zUZWqsmgm"), 5))
            time.sleep(10)
            main()
        
        elif user_input == "exit":
            sys.exit()
        else:
            print(Fore.RED +"Error 404: Command not found")
            time.sleep(0.7)
            main()

if __name__ == "__main__":
    main()