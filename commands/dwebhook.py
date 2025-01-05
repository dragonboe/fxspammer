import requests
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate

def delete_webhook():
    dwebhook = input(Colorate.Horizontal(Colors.blue_to_red, "Webhook URL: "))
    response = requests.delete(dwebhook)
    
    if response.status_code == 204:
        print(Colorate.Horizontal(Colors.blue_to_red, "Deleted webhook successfully!"))
    elif response.status_code == 404:
        print(Colorate.Horizontal(Colors.blue_to_red, "Error: Webhook doesn't exist"))
    else:
        print(Colorate.Horizontal(Colors.blue_to_red, f"Error occurred: {response.status_code}"))

if __name__ == "__main__":
    delete_webhook()
