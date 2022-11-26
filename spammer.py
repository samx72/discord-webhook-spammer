import os
from termcolor import colored
from discord_webhook import DiscordWebhook
import time

os.system("cls")

print(colored("""

░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""", "cyan"))



web = input("webhook url: ")
msg = input("message: ")
t = int(input("time in seconds between messages: "))

webhook = DiscordWebhook(url=web, content=msg)

input(colored("to start click enter", "green"))

print(colored("loading..  :)", "green"))

os.system("cls")
print(colored("to stop just close the window", "red"))

while (True):
    response = webhook.execute()


