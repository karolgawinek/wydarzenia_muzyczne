# Listy globalne
koncerty = []
#Strukutura Koncertu
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
        elif wybor == "8":
            generuj_mape()
        elif wybor == "9":
            print("Kończymy program.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()