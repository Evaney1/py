import requests
import sys
import os

# Funktion zur Auflösung des cfx.re-Links
def resolve_cfx_link(cfx_link):
    # Extrahiere den Code nach 'cfx.re/join/'
    if "cfx.re/join/" in cfx_link:
        cfx_code = cfx_link.split("cfx.re/join/")[1]
    else:
        print("Ungültiger Link. Bitte einen vollständigen cfx.re-Link eingeben.")
        return None, None

    # Die URL für die API, die wir anfragen müssen
    api_url = f"https://servers-frontend.fivem.net/api/servers/single/{cfx_code}"

    # User-Agent Header hinzufügen
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Sende eine Anfrage an die API mit dem User-Agent Header
    response = requests.get(api_url, headers=headers)

    # Überprüfe, ob die Antwort erfolgreich war
    if response.status_code == 200:
        server_data = response.json()
        ip = server_data['Data']['connectEndPoints'][0].split(':')[0]
        port = server_data['Data']['connectEndPoints'][0].split(':')[1]
        return ip, port
    elif response.status_code == 403:
        print("Zugriff verweigert: 403. Die API hat die Anfrage blockiert.")
    else:
        print(f"Fehler beim Auflösen des Links: {response.status_code}")
    
    return None, None

# Funktion zum Erstellen von leeren Dateien (beim Start des Programms)
def create_files():
    open("ip.txt", "w").close()
    open("port.txt", "w").close()

# Funktion zum Speichern von IP und Port in Dateien
def save_ip_port(ip, port):
    with open("ip.txt", "w") as ip_file:
        ip_file.write(ip)
    with open("port.txt", "w") as port_file:
        port_file.write(port)

# Hauptfunktion
def main():
    try:
        # Erstelle die Dateien beim Start des Programms
        create_files()

        if len(sys.argv) == 3:
            # Wenn IP-Adresse und Port als Argumente übergeben werden
            ip_address = sys.argv[1]
            port = sys.argv[2]
            print(f"Übergebene IP-Adresse: {ip_address}")
            print(f"Übergebener Port: {port}")
            save_ip_port(ip_address, port)
        else:
            # Andernfalls Link eingeben
            cfx_link = input("Gib den vollständigen CFX-RE Link ein (z.B. https://cfx.re/join/odl8xj): ").strip()
            ip, port = resolve_cfx_link(cfx_link)

            if ip and port:
                print(f"IP-Adresse: {ip}")
                print(f"Port: {port}")

                # IP und Port in Dateien speichern
                save_ip_port(ip, port)
            else:
                print("Konnte die Serverinformationen nicht abrufen.")
    finally:
        # Entferne die cleanup_files Funktion, um die Dateien beim Beenden des Programms nicht zu löschen
        pass

if __name__ == "__main__":
    main()
