import sys
import requests
import json

def get_fivem_server_info(ip, port):
    url = f"http://{ip}:{port}/info.json"
    players_url = f"http://{ip}:{port}/players.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        server_info = response.json()

        players_response = requests.get(players_url)
        players_response.raise_for_status()
        players_info = players_response.json()

        # UTF-8 Encoding setzen
        sys.stdout.reconfigure(encoding='utf-8')

        print("Server Information:")
        print(json.dumps(server_info, indent=4))

        print("\nConnected Players:")
        for player in players_info:
            print(f"ID: {player['id']}, Name: {player['name']}, Ping: {player['ping']} ms")
    
    except requests.exceptions.RequestException as e:
        print(f"Fehler beim Abrufen der Informationen: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Verwendung: python script.py <Server-IP> <Server-Port>")
        sys.exit(1)
    
    ip = sys.argv[1]
    
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Der Server-Port muss eine Zahl sein.")
        sys.exit(1)

    get_fivem_server_info(ip, port)
