from datetime import date, datetime, timedelta

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    def get_ar(self):
        return self.ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam, kavefozo):
        super().__init__(ar=10000, szobaszam=szobaszam)
        self.kavefozo = kavefozo

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, erkely):
        super().__init__(ar=15000, szobaszam=szobaszam)
        self.erkely = erkely

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = {}

    def add_room(self, szoba):
        self.szobak.append(szoba)

    def book_room(self, szobaszam, foglalasi_datum):
        if foglalasi_datum < date.today():
            return "Nem lehet múltbeli dátumra foglalni."

        if foglalasi_datum in self.foglalasok:
            if szobaszam in self.foglalasok[foglalasi_datum]:
                return "A szoba már foglalt ezen a napon."
            else:
                self.foglalasok[foglalasi_datum].append(szobaszam)
        else:
            self.foglalasok[foglalasi_datum] = [szobaszam]

        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                return f"A szoba sikeresen lefoglalva. Ár: {szoba.get_ar()}"

    def delete_booking(self, szobaszam, foglalasi_datum):
        if foglalasi_datum < date.today():
            return "Nem lehet múltbeli foglalást törölni."

        if foglalasi_datum in self.foglalasok and szobaszam in self.foglalasok[foglalasi_datum]:
            self.foglalasok[foglalasi_datum].remove(szobaszam)
            if not self.foglalasok[foglalasi_datum]:
                del self.foglalasok[foglalasi_datum]
            return "A foglalás törölve."
        else:
            return "Nincs ilyen foglalás."

    def booking_list(self):
        return self.foglalasok

class Foglalas:
    def __init__(self, szalloda):
        self.szalloda = szalloda

# Rendszer inicializálása
szalloda = Szalloda("Grand Hotel")

# Szobák hozzáadása a szállodához
szalloda.add_room(EgyagyasSzoba(101,"Nincs"))
szalloda.add_room(EgyagyasSzoba(102,"Van"))
szalloda.add_room(KetagyasSzoba(201,"Van"))

# Előzetes foglalások
szalloda.book_room(101, date.today() + timedelta(days=1))
szalloda.book_room(102, date.today() + timedelta(days=2))
szalloda.book_room(201, date.today() + timedelta(days=3))
szalloda.book_room(101, date.today() + timedelta(days=4))
szalloda.book_room(102, date.today() + timedelta(days=5))

# UI
def ui(szalloda):
    while True:
        print("1. Szoba foglalása")
        print("2. Foglalás törlése")
        print("3. Összes foglalás listázása")
        print("4. Kilépés")
        choice = input("Válasszon egy lehetőséget: ")

        if choice == "1":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            foglalasi_datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            foglalasi_datum = datetime.strptime(foglalasi_datum_str, "%Y-%m-%d").date()
            print(szalloda.book_room(szobaszam, foglalasi_datum))
        elif choice == "2":
            szobaszam = int(input("Adja meg a szobaszámot: "))
            foglalasi_datum_str = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            foglalasi_datum = datetime.strptime(foglalasi_datum_str, "%Y-%m-%d").date()
            print(szalloda.delete_booking(szobaszam, foglalasi_datum))
        elif choice == "3":
            foglalasok = szalloda.booking_list()
            for datum, szobak in foglalasok.items():
                print(f"{datum}: {', '.join(map(str, szobak))}")
        elif choice == "4":
            break
        else:
            print("Érvénytelen választás. Próbálja újra.")

ui(szalloda)
