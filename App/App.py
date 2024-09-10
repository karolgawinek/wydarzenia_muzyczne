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
        print("8. Zakończ")

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
            print("Kończymy program.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")


if __name__ == "__main__":
    main()