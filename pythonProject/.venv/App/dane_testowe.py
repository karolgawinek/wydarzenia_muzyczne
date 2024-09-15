import random

def zaladuj_testowe_dane(koncerty, zespoly, klienci):
    # Generowanie 4 zespołów
    zespoly.extend([
        {"id": 1, "nazwa": "Zespół A", "gatunek" : "Rock","koncerty": []},
        {"id": 2, "nazwa": "Zespół B", "gatunek" : "Hip-hop", "koncerty": []},
        {"id": 3, "nazwa": "Zespół C","gatunek" : "Jazz", "koncerty": []},
        {"id": 4, "nazwa": "Zespół D","gatunek" : "Alternatywa", "koncerty": []}
    ])

    # Generowanie 5 klientów
    klienci.extend([
        {"id": 1, "imie": "Jan", "nazwisko": "Kowalski", "email": "jan.kowalski@example.com", "koncerty": []},
        {"id": 2, "imie": "Anna", "nazwisko": "Nowak", "email": "anna.nowak@example.com", "koncerty": []},
        {"id": 3, "imie": "Piotr", "nazwisko": "Wiśniewski", "email": "piotr.wisniewski@example.com", "koncerty": []},
        {"id": 4, "imie": "Ewa", "nazwisko": "Zielińska", "email": "ewa.zielinska@example.com", "koncerty": []},
        {"id": 5, "imie": "Marek", "nazwisko": "Szymański", "email": "marek.szymanski@example.com", "koncerty": []}

    ])

    # Lista miast w Polsce z przykładowymi współrzędnymi geograficznymi
    miasta = [
        {"nazwa": "Warszawa", "wsp_x": 52.2297, "wsp_y": 21.0122},
        {"nazwa": "Kraków", "wsp_x": 50.0647, "wsp_y": 19.9450},
        {"nazwa": "Wrocław", "wsp_x": 51.1079, "wsp_y": 17.0385},
        {"nazwa": "Gdańsk", "wsp_x": 54.3520, "wsp_y": 18.6466},
        {"nazwa": "Poznań", "wsp_x": 52.4064, "wsp_y": 16.9252},
        {"nazwa": "Łódź", "wsp_x": 51.7592, "wsp_y": 19.4560},
        {"nazwa": "Szczecin", "wsp_x": 53.4285, "wsp_y": 14.5528},
        {"nazwa": "Bydgoszcz", "wsp_x": 53.1235, "wsp_y": 18.0084},
        {"nazwa": "Lublin", "wsp_x": 51.2465, "wsp_y": 22.5684},
        {"nazwa": "Katowice", "wsp_x": 50.2649, "wsp_y": 19.0238}
    ]

    # Generowanie 10 koncertów w losowych miastach
    for i in range(10):
        miasto = random.choice(miasta)
        nowy_koncert = {
            "id": i + 1,
            "nazwa": f"Koncert {miasto['nazwa']}",
            "data": f"2024-0{i+1}-15",  # Przykładowe daty
            "lokalizacja": miasto["nazwa"],
            "współrzędne": (miasto["wsp_x"], miasto["wsp_y"]),
            "zespoły": [],
            "klienci": []
        }
        koncerty.append(nowy_koncert)

    # Dodawanie 2 zespołów do każdego koncertu
    for koncert in koncerty:
        zespoly_do_dodania = random.sample(zespoly, 2)
        for zespol in zespoly_do_dodania:
            koncert['zespoły'].append(zespol['id'])
            zespol['koncerty'].append(koncert['id'])

    # Dodawanie wszystkich klientów do każdego koncertu
    for koncert in koncerty:
        for klient in klienci:
            koncert['klienci'].append(klient['id'])
            klient['koncerty'].append(koncert['id'])

    print("Testowe dane zostały załadowane.")

