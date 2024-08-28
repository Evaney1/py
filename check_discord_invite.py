import requests

def check_discord_invite(invite_link):
    url = f"https://discord.com/api/v9/invites/{invite_link}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            invite_info = response.json()
            print("Der Invite-Link ist gültig.")
            print(f"Servername: {invite_info['guild']['name']}")
            print(f"Channel: {invite_info['channel']['name']}")
            print(f"Kanal-ID: {invite_info['channel']['id']}")
        elif response.status_code == 404:
            print("Der Invite-Link ist ungültig oder abgelaufen.")
        elif response.status_code == 403:
            # Statuscode 403 kann auf mehrere Probleme hinweisen.
            response_json = response.json()
            message = response_json.get('message', '')
            if message == 'Invites are disabled for this server':
                print("Die Einladungen auf diesem Server sind pausiert oder deaktiviert.")
            elif message == 'Invite could not be accepted':
                print("Die Einladung kann nicht angenommen werden. Möglicherweise ist der Invite-Link abgelaufen oder gesperrt.")
            elif message == 'You are banned from this server':
                print("Du wurdest von diesem Server gebannt.")
            else:
                print(f"Zugriff verweigert: {message}")
        else:
            print(f"Unbekannter Fehler: {response.status_code}")
    except requests.RequestException as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    invite_link = input("Gib den Discord Invite-Link ein: ")
    invite_code = invite_link.split('/')[-1]
    check_discord_invite(invite_code)
