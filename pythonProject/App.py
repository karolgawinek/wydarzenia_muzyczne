# Listy globalne
koncerty = []
# Strukutura Koncertu
# nowy_koncert = {
#     "id": znajdz_nowe_id(koncerty),
#     "nazwa": nazwa,
#     "data": data,
#     "lokalizacja": lokalizacja,
#     "współrzędne": (wsp_x, wsp_y),
#     "zespoły": [],
#     "klienci": []
# }
zespoly = []
#Struktura zespoołu
# {      "id": znajdz_nowe_id(zespoly),
#         "nazwa": nazwa,
#         "gatunek": gatunek,
#         "koncerty": []
#     }
klienci = []
#Struktura klienta
# "id": znajdz_nowe_id(klienci),
# "imie": imie,
# "nazwisko": nazwisko,
# "email": email


# Funkcja do tworzenia koncertu
def stworz_koncert():
    nazwa = input("Podaj nazwę koncertu: ")
    data = input("Podaj datę koncertu (YYYY-MM-DD): ")
    lokalizacja = input("Podaj lokalizację koncertu: ")
    wsp_x = float(input("Podaj współrzędną geograficzną X: "))
    wsp_y = float(input("Podaj współrzędną geograficzną Y: "))

    nowy_koncert = {
        "id": znajdz_nowe_id(koncerty),
        "nazwa": nazwa,
        "data": data,
        "lokalizacja": lokalizacja,
        "współrzędne": (wsp_x, wsp_y),
        "zespoły": [],
        "klienci": []
    }

    # Wywołanie funkcji do dodawania zespołów do koncertu
    dodaj_zespol_do_koncertu(nowy_koncert)

    # Wywołanie funkcji do dodawania klientów do koncertu
    dodaj_klienta_do_koncertu(nowy_koncert)

    return nowy_koncert


# Funkcja do wyświetlania koncertów
def wyswietl_koncerty():
    if not koncerty:
        print("Brak koncertów do wyświetlenia.")
        return

    for koncert in koncerty:
        print("\n" + "=" * 40)
        print(f"ID Koncertu: {koncert['id']}")
        print(f"Nazwa: {koncert['nazwa']}")
        print(f"Data: {koncert['data']}")
        print(f"Lokalizacja: {koncert['lokalizacja']}")
        print(f"Współrzędne: X={koncert['współrzędne'][0]}, Y={koncert['współrzędne'][1]}")
        print("\nZespoły na tym koncercie:")

        if koncert['zespoły']:
            for zespol_id in koncert['zespoły']:
                zespol = next((z for z in zespoly if z['id'] == zespol_id), None)
                if zespol:
                    print(f"  - {zespol['nazwa']} (Gatunek: {zespol['gatunek']}, ID: {zespol['id']})")
        else:
            print("  Brak zespołów przypisanych do tego koncertu.")

        print("\nKlienci, którzy zakupili bilety:")

        if koncert['klienci']:
            for klient_id in koncert['klienci']:
                klient = next((k for k in klienci if k['id'] == klient_id), None)
                if klient:
                    print(f"  - {klient['imie']} {klient['nazwisko']} (Email: {klient['email']}, ID: {klient['id']})")
        else:
            print("  Brak klientów przypisanych do tego koncertu.")

        print("=" * 40)


# Funkcja aktualizująca listę koncertów
def aktualizuj_koncert():
    # Pytanie o ID koncertu
    koncert_id = input("Podaj ID koncertu, który chcesz zaktualizować: ")

    if not koncert_id.isdigit():
        print("Podano nieprawidłowe ID. Spróbuj ponownie.")
        return

    koncert_id = int(koncert_id)
    koncert = next((k for k in koncerty if k['id'] == koncert_id), None)

    if not koncert:
        print("Nie znaleziono koncertu o podanym ID.")
        return

    # Wyświetlenie obecnych informacji o koncertu
    print(f"\nObecne informacje o koncercie '{koncert['nazwa']}':")
    print(f"Nazwa: {koncert['nazwa']}")
    print(f"Data: {koncert['data']}")
    print(f"Lokalizacja: {koncert['lokalizacja']}")
    print(f"Współrzędne: X={koncert['współrzędne'][0]}, Y={koncert['współrzędne'][1]}")

    print("\nObecna lista zespołów:")
    if koncert['zespoły']:
        for zespol_id in koncert['zespoły']:
            zespol = next((z for z in zespoly if z['id'] == zespol_id), None)
            if zespol:
                print(f"  - {zespol['nazwa']} (ID: {zespol['id']})")
    else:
        print("  Brak zespołów przypisanych do tego koncertu.")

    print("\nObecna lista klientów:")
    if koncert['klienci']:
        for klient_id in koncert['klienci']:
            klient = next((k for k in klienci if k['id'] == klient_id), None)
            if klient:
                print(f"  - {klient['imie']} {klient['nazwisko']} (Email: {klient['email']}, ID: {klient['id']})")
    else:
        print("  Brak klientów przypisanych do tego koncertu.")

    # Pytanie o aktualizację poszczególnych pól
    if input(
            f"\nCzy chcesz zaktualizować nazwę koncertu? (obecnie: {koncert['nazwa']}) (tak/nie): ").strip().lower() == 'tak':
        koncert['nazwa'] = input("Podaj nową nazwę koncertu: ")

    if input(
            f"Czy chcesz zaktualizować datę koncertu? (obecnie: {koncert['data']}) (tak/nie): ").strip().lower() == 'tak':
        koncert['data'] = input("Podaj nową datę koncertu (YYYY-MM-DD): ")

    if input(
            f"Czy chcesz zaktualizować lokalizację koncertu? (obecnie: {koncert['lokalizacja']}) (tak/nie): ").strip().lower() == 'tak':
        koncert['lokalizacja'] = input("Podaj nową lokalizację koncertu: ")

    if input(
            f"Czy chcesz zaktualizować współrzędną X? (obecnie: {koncert['współrzędne'][0]}) (tak/nie): ").strip().lower() == 'tak':
        koncert['współrzędne'] = (
            float(input("Podaj nową współrzędną X: ")),
            koncert['współrzędne'][1]
        )

    if input(
            f"Czy chcesz zaktualizować współrzędną Y? (obecnie: {koncert['współrzędne'][1]}) (tak/nie): ").strip().lower() == 'tak':
        koncert['współrzędne'] = (
            koncert['współrzędne'][0],
            float(input("Podaj nową współrzędną Y: "))
        )

    # Aktualizacja listy zespołów
    if input(f"\nCzy chcesz zaktualizować listę zespołów? (tak/nie): ").strip().lower() == 'tak':
        koncert['zespoły'] = []  # Zerowanie aktualnej listy zespołów
        while True:
            zespol_id = input("Podaj ID zespołu do dodania (lub wpisz 'stop' aby zakończyć): ")
            if zespol_id.lower() == 'stop':
                break
            if not zespol_id.isdigit():
                print("Podano nieprawidłowe ID. Spróbuj ponownie.")
                continue
            zespol_id = int(zespol_id)
            zespol = next((z for z in zespoly if z['id'] == zespol_id), None)
            if zespol:
                koncert['zespoły'].append(zespol_id)
                print(f"Zespół {zespol['nazwa']} dodany do koncertu.")
            else:
                print("Nie znaleziono zespołu o podanym ID.")

    # Aktualizacja listy klientów
    if input(f"\nCzy chcesz zaktualizować listę klientów? (tak/nie): ").strip().lower() == 'tak':
        koncert['klienci'] = []  # Zerowanie aktualnej listy klientów
        while True:
            klient_id = input("Podaj ID klienta do dodania (lub wpisz 'stop' aby zakończyć): ")
            if klient_id.lower() == 'stop':
                break
            if not klient_id.isdigit():
                print("Podano nieprawidłowe ID. Spróbuj ponownie.")
                continue
            klient_id = int(klient_id)
            klient = next((k for k in klienci if k['id'] == klient_id), None)
            if klient:
                koncert['klienci'].append(klient_id)
                print(f"Klient {klient['imie']} {klient['nazwisko']} dodany do koncertu.")
            else:
                print("Nie znaleziono klienta o podanym ID.")

    print("Aktualizacja koncertu zakończona.")


def zarzadzaj_koncertami_zespolu():
    # Pytanie o ID zespołu
    zespol_id = input("Podaj ID zespołu, którego koncerty chcesz zarządzać: ")

    if not zespol_id.isdigit():
        print("Podano nieprawidłowe ID. Spróbuj ponownie.")
        return

    zespol_id = int(zespol_id)
    zespol = next((z for z in zespoly if z['id'] == zespol_id), None)

    if not zespol:
        print("Nie znaleziono zespołu o podanym ID.")
        return

    # Wyświetlanie koncertów dla wybranego zespołu
    koncerty_zespolu = [k for k in koncerty if zespol_id in k['zespoły']]

    if not koncerty_zespolu:
        print("Brak koncertów przypisanych do tego zespołu.")
        return

    print(f"\nKoncerty dla zespołu '{zespol['nazwa']}':")
    for koncert in koncerty_zespolu:
        print(
            f"ID: {koncert['id']}, Nazwa: {koncert['nazwa']}, Data: {koncert['data']}, Lokalizacja: {koncert['lokalizacja']}, Współrzędne: X={koncert['współrzędne'][0]}, Y={koncert['współrzędne'][1]}")

    # Opcje edytowania
    while True:
        akcja = input("\nCo chcesz zrobić? (1 - Edytuj koncert, 2 - Usuń zespół z koncertów, 3 - Wyjdź): ").strip()

        if akcja == '1':
            # Edytowanie koncertu
            koncert_id = input("Podaj ID koncertu do edytowania: ")

            if not koncert_id.isdigit():
                print("Podano nieprawidłowe ID. Spróbuj ponownie.")
                continue

            koncert_id = int(koncert_id)
            koncert = next((k for k in koncerty if k['id'] == koncert_id), None)

            if not koncert or zespol_id not in koncert['zespoły']:
                print("Nie znaleziono koncertu o podanym ID lub zespół nie jest przypisany do tego koncertu.")
                continue

            aktualizuj_koncert()

        elif akcja == '2':
            # Usuwanie zespołu z koncertów
            koncert_id = input("Podaj ID koncertu, z którego chcesz usunąć zespół: ")

            if not koncert_id.isdigit():
                print("Podano nieprawidłowe ID. Spróbuj ponownie.")
                continue

            koncert_id = int(koncert_id)
            koncert = next((k for k in koncerty if k['id'] == koncert_id), None)

            if not koncert or zespol_id not in koncert['zespoły']:
                print("Nie znaleziono koncertu o podanym ID lub zespół nie jest przypisany do tego koncertu.")
                continue

            koncert['zespoły'].remove(zespol_id)
            print(f"Zespół {zespol['nazwa']} został usunięty z koncertu '{koncert['nazwa']}'.")

        elif akcja == '3':
            break

        else:
            print("Nieprawidłowa opcja. Spróbuj ponownie.")


def zarzadzaj_klientami():
    # Wyświetlanie wszystkich klientów dodanych do koncertów
    dodani_klienci = set()
    for koncert in koncerty:
        dodani_klienci.update(koncert['klienci'])

    if dodani_klienci:
        print("\nLista klientów dodanych do koncertów:")
        for klient_id in dodani_klienci:
            klient = next((k for k in klienci if k['id'] == klient_id), None)
            if klient:
                print(f"ID: {klient['id']}, Imię: {klient['imie']}, Nazwisko: {klient['nazwisko']}")
    else:
        print("Brak klientów dodanych do koncertów.")

    # Dodawanie klienta do koncertu
    if input("\nCzy chcesz dodać klienta do koncertu? (tak/nie): ").strip().lower() == 'tak':
        koncert_id = input("Podaj ID koncertu, do którego chcesz dodać klienta: ")

        if not koncert_id.isdigit():
            print("Podano nieprawidłowe ID koncertu. Spróbuj ponownie.")
            return

        koncert_id = int(koncert_id)
        koncert = next((k for k in koncerty if k['id'] == koncert_id), None)

        if not koncert:
            print("Nie znaleziono koncertu o podanym ID.")
            return

        klient_id = input("Podaj ID klienta, którego chcesz dodać: ")

        if not klient_id.isdigit():
            print("Podano nieprawidłowe ID klienta. Spróbuj ponownie.")
            return

        klient_id = int(klient_id)
        klient = next((k for k in klienci if k['id'] == klient_id), None)

        if not klient:
            print("Nie znaleziono klienta o podanym ID.")
            return

        if klient_id not in koncert['klienci']:
            koncert['klienci'].append(klient_id)
            print(f"Klient {klient['imie']} {klient['nazwisko']} został dodany do koncertu.")
        else:
            print("Klient już jest dodany do tego koncertu.")


# Funkcja pomocnicze
# Funkcja do znajdowania najwyższego ID w danej liście
def znajdz_nowe_id(lista):
    if lista:
        return max(item['id'] for item in lista) + 1
    else:
        return 1


def dodaj_zespol_do_koncertu(koncert):
    while True:
        zespol_id = input(
            "Podaj ID zespołu, który chcesz dodać do koncertu (lub wpisz 'stop', aby zakończyć dodawanie zespołów): ")

        if zespol_id.lower() == 'stop':
            break

        if not zespol_id.isdigit():
            print("Podano nieprawidłowe ID. Spróbuj ponownie.")
            continue

        zespol_id = int(zespol_id)
        zespol = next((z for z in zespoly if z['id'] == zespol_id), None)

        if zespol:
            koncert['zespoły'].append(zespol_id)
            zespol['koncerty'].append(koncert['id'])  # Dodajemy ID koncertu do listy koncertów zespołu
            print(f"Zespół {zespol['nazwa']} został dodany do koncertu.")
        else:
            print("Nie znaleziono zespołu o podanym ID.")
            wybor = input("Czy chcesz stworzyć nowy zespół? (tak/nie): ").strip().lower()
            if wybor == 'tak':
                nowy_zespol = stworz_zespol()
                dodaj_zespol(nowy_zespol)
                koncert['zespoły'].append(nowy_zespol['id'])
                nowy_zespol['koncerty'].append(koncert['id'])  # Dodajemy ID koncertu do listy koncertów zespołu
                print(f"Nowy zespół {nowy_zespol['nazwa']} został stworzony i dodany do koncertu.")
            else:
                print("Zespół nie został dodany do koncertu.")


# Funkcja do dodawania klientów do koncertu
def dodaj_klienta_do_koncertu(koncert):
    while True:
        klient_id = input(
            "Podaj ID klienta, który chcesz dodać do koncertu (lub wpisz 'stop', aby zakończyć dodawanie klientów): ")

        if klient_id.lower() == 'stop':
            break

        if not klient_id.isdigit():
            print("Podano nieprawidłowe ID. Spróbuj ponownie.")
            continue

        klient_id = int(klient_id)
        klient = next((k for k in klienci if k['id'] == klient_id), None)

        if klient:
            koncert['klienci'].append(klient_id)
            print(f"Klient {klient['imie']} {klient['nazwisko']} został dodany do koncertu.")
        else:
            print("Nie znaleziono klienta o podanym ID.")
            wybor = input("Czy chcesz stworzyć nowego klienta? (tak/nie): ").strip().lower()
            if wybor == 'tak':
                nowy_klient = stworz_klienta()
                dodaj_klienta(nowy_klient)
                koncert['klienci'].append(nowy_klient['id'])
                print(
                    f"Nowy klient {nowy_klient['imie']} {nowy_klient['nazwisko']} został stworzony i dodany do koncertu.")
            else:
                print("Klient nie został dodany do koncertu.")


# Funkcje do tworzenia zespołów i klientów
def stworz_zespol():
    nazwa = input("Podaj nazwę zespołu: ")
    gatunek = input("Podaj gatunek zespołu: ")

    return {
        "id": znajdz_nowe_id(zespoly),
        "nazwa": nazwa,
        "gatunek": gatunek,
        "koncerty": []
    }


def stworz_klienta():
    imie = input("Podaj imię klienta: ")
    nazwisko = input("Podaj nazwisko klienta: ")
    email = input("Podaj email klienta: ")

    return {
        "id": znajdz_nowe_id(klienci),
        "imie": imie,
        "nazwisko": nazwisko,
        "email": email
    }


# Funkcje dodające zespoły i klientów do globalnych list
def dodaj_zespol(zespol):
    zespoly.append(zespol)
    print(f"Zespół {zespol['nazwa']} został dodany.")


def dodaj_klienta(klient):
    klienci.append(klient)
    print(f"Klient {klient['imie']} {klient['nazwisko']} został dodany.")


def dodaj_koncert(nowy_koncert):
    koncerty.append(nowy_koncert)
    print(f"Nowy koncert '{nowy_koncert['nazwa']}' został dodany.")



















# Główna funkcja
def main():
    # Mechanizm logowania
    while True:
        haslo = input("Podaj hasło: ")
        if haslo == "koncert":
            print("Hasło poprawne. Witamy w systemie.")
            break
        else:
            print("Nieprawidłowe hasło. Spróbuj ponownie.")

    # Menu główne
    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj koncert")
        print("2. Dodaj zespół")
        print("3. Dodaj klienta")
        print("4. Wyświetl koncerty")
        print("5. Aktualizuj koncert")
        print("6. Zarządzaj zespołami w koncertach")
        print("7. Zarządzaj klientami")
        print("8. Generuj Mape Koncertów")
        print("9. Zakończ")

        wybor = input("Twój wybór: ")

        if wybor == "1":
            nowy_koncert = stworz_koncert()
            dodaj_koncert(nowy_koncert)
        elif wybor == "2":
            nowy_zespol = stworz_zespol()
            dodaj_zespol(nowy_zespol)
        elif wybor == "3":
            nowy_klient = stworz_klienta()
            dodaj_klienta(nowy_klient)
        elif wybor == "4":
            wyswietl_koncerty()
        elif wybor == "5":
            aktualizuj_koncert()
        elif wybor == "6":
            zarzadzaj_koncertami_zespolu()
        elif wybor == "7":
            zarzadzaj_klientami()
        # elif wybor == "8":
        #     generuj_mape()    w budowie
        elif wybor == "9":
            print("Kończymy program.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()