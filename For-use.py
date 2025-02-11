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

AUTH_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImljMVpGMXJ2dXYtbU9SMnBPX214dWNJcHpTOCIsInR5cCI6ImF0K2p3dCIsIng1dCI6ImljMVpGMXJ2dXYtbU9SMnBPX214dWNJcHpTOCJ9.eyJuYmYiOjE3MzkyNDIyNzksImV4cCI6MTczOTI0NTg3OSwiaXNzIjoiaHR0cHM6Ly9hdXRoLnJlYy5uZXQiLCJjbGllbnRfaWQiOiJyZWNuZXQiLCJyb2xlIjoid2ViQ2xpZW50Iiwic3ViIjoiMTIyMjY5MzMiLCJhdXRoX3RpbWUiOjE3MzkyNDIyNzksImlkcCI6ImxvY2FsIiwianRpIjoiNkYwM0I5NzhCQjM0QzBDNkMyRTJFOUNGOEExOEE5RkUiLCJzaWQiOiI2NTZGNzUxMEQ3NEMxNURGOUFFREE4NDFEQ0NBOEMzNCIsImlhdCI6MTczOTI0MjI3OSwic2NvcGUiOlsib3BlbmlkIiwicm4uYXBpIiwicm4uY29tbWVyY2UiLCJybi5ub3RpZnkiLCJybi5tYXRjaC5yZWFkIiwicm4uY2hhdCIsInJuLmFjY291bnRzIiwicm4uYXV0aCIsInJuLmxpbmsiLCJybi5saXN0cyIsInJuLmNsdWJzIiwicm4ucm9vbXMiLCJybi5kaXNjb3ZlcnkiLCJybi5kYXRhIiwicm4ubW9kZXJhdGlvbiIsIm9mZmxpbmVfYWNjZXNzIl0sImFtciI6WyJwd2QiXX0.BDC2-vlINhg9phuJjnKsf0jMohZbA4cxOHEFHEN9iPflufneCF78fADGYfcEVBnxrl-zEh4MEMUmCJJEzp_mxRtj8y34UbRaZFkKg8aEe85-3_HdfozQZoldpRfjv9PgZuKFkF69UvtNijdXcAhGkiO9fsQTI2VyJCyN5CeKkxcfaRL-HkRPihDu3HyzQuDfEEUrj1Tv7CAb0bgaIXIw4OPAX3PIvO1EPOr0yMgcHCoLqBIkPWHkfv1pExBUX2F3XVL2HxqpCoE_DeY97WcSwKaeQHb6Bi8U1JGa3qrjftAlvWN5o9RODrEIZzeSbq1-dcEq5ZnBl4b0bL1OvSrNzg"
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
