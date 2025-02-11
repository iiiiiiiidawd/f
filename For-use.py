import requests
import colorama
import ctypes
import random
import threading
from colorama import Fore

colorama.init(autoreset=True)

# Set console title
ctypes.windll.kernel32.SetConsoleTitleW(
    "[Rec.Net Username Checker] by irtco | irtco#0702 | https://discord.gg/ytrT83ghMp"
)

# Display banner
print(f"""{Fore.MAGENTA}
 _____________________________________________________________________________
/                                                                             \\
|                      {Fore.LIGHTBLUE_EX}Rec.Net Username Checker by irtco{Fore.MAGENTA}                      |
\\_____________________________________________________________________________/
/                                                                             \\
|                              {Fore.LIGHTBLUE_EX}Discord: irtco#702{Fore.MAGENTA}                              |
\\_____________________________________________________________________________/
/                                                                             \\
|                        {Fore.LIGHTBLUE_EX}https://discord.gg/ytrT83ghMp{Fore.MAGENTA}                        |
\\_____________________________________________________________________________/
""")

num = input(f"Length? ")
ABC = 'abcdefghijklmnopqrstuvwxyz123456789_-.'
valid_count = 0

AUTH_TOKEN = "your_authorization_token_here"
HEADERS = {
    "Authorization": f"Bearer {AUTH_TOKEN}"
}

def main():
    while True:
        username = "".join(random.choice(ABC) for _ in range(int(num)))
        response = requests.get(f"https://accounts.rec.net/account?username={username}", headers=HEADERS)

        if response.status_code == 404:
            print(f"{Fore.GREEN} {username} is available!")
            with open("valid.txt", "a+") as file:
                file.write(username + "\n")
        else:
            print(f"{Fore.RED} {username} is taken.")

threads = []
for _ in range(7):
    t = threading.Thread(target=main)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
