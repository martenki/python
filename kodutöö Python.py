# 6. Salakeel
# sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# kasutaja sisestab tavalise sõna, mis muudetakse salakeeleks - 1p
# kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# kood kommenteeritud - 1p
def loo_salakeel(sona: str) -> str:
    """
    Muudab tavalise sõna salakeelde.
    Näide: 'mari' -> 'maoaroroi'
    """
    tulemus = ""
    for taht in sona:
        tulemus += taht + "o" + taht
    return tulemus


def tolgi_salakeel(salasona: str) -> str:
    tulemus = ""
    i = 0
    while i < len(salasona):
        tulemus += salasona[i]
        i += 3
    return tulemus


def pea():
    print("SALAKEEL")
    print("Kas soovid luua uut salakeelt või tõlkida olemasolevat?")
    valik = input("Sisesta '1' kui soovid salakeelt LUUA, või '2' kui soovid TÕLKIDA: ").strip()

    if valik == "1":
        sona = input("Sisesta tavaline sõna, mille tahad muuta salakeelde: ").strip().lower()
        salasona = loo_salakeel(sona)
        print(f"Sinu sõna salakeeles on: {salasona}")

    elif valik == "2":
        salasona = input("Sisesta salakeeles sõna, mida soovid tõlkida: ").strip().lower()
        sona = tolgi_salakeel(salasona)
        print(f"Sinu sõna tavalises keeles on: {sona}")

    else:
        print("Viga: palun vali '1' või '2'.")


if __name__ == "__main__":
    pea()
    

# 5. Emaili kontroll
# kasutaja sisestab 3 kaugushüppe tulemust - 1p
# sinu programm leiab ning väljastab parima ja keskmise tulemuse - 2p
# programmi dialoog kasutajaga on arusaadav ja üheselt mõistetav - 1p
# kood kommenteeritud - 1p
def loe_tulemus(nr: int) -> float:
    while True:
        toor = input(f"Sisesta {nr}. hüppe tulemus (meetrites): ").strip().replace(",", ".")
        try:
            tulemus = float(toor)
            if tulemus <= 0:
                print("Viga: tulemus peab olema positiivne arv.")
                continue
            return tulemus
        except ValueError:
            print("Viga: palun sisesta arvuline väärtus, nt 5.72")


def pea():
    print("KAUGUSHÜPPE PROGRAMM")
    print("Palun sisesta oma kolme hüppe tulemused (meetrites).")
    print("Näide: 5.83 või 6,12\n")
    tulemused = [loe_tulemus(i) for i in range(1, 4)]
    parim = max(tulemused)
    keskmine = sum(tulemused) / len(tulemused)
    print("\nTulemused:")
    print(f"Sinu hüpped: {tulemused[0]:.2f} m, {tulemused[1]:.2f} m, {tulemused[2]:.2f} m")
    print(f"Parim hüpe: {parim:.2f} meetrit")
    print(f"Keskmine hüpe: {keskmine:.2f} meetrit")

if __name__ == "__main__":
    pea()

# 4. Emaili kontroll
# kasutaja lisab emaili kujul enimi.pnimi@server.com - 1p
# programm kontrollib kas email on sisestatud õigesti - vähemalt @-märgi kontroll - 1p
# programm tükeldab selle ja väljastab lause: ‘Tere enimi, sinu email on server serveris ja domeeniks on sul com’ - 1p
# kasutajalt küsitud küsimused on selgelt üheselt mõistetavad - 1p
# kood kommenteeritud - 1p
def loe_email() -> str:
    while True:
        email = input("Sisesta oma e-posti aadress (kujul enimi.pnimi@server.com): ").strip()
        if email.count("@") == 1:
            vasak, parem = email.split("@")
            if vasak and parem:
                return email
        print("Viga: palun sisesta kehtiv aadress, mis sisaldab täpselt ühte '@' märki (nt enimi.pnimi@server.com).")

def eralda_osad(email: str) -> tuple[str, str, str]:
    vasak, parem = email.lower().split("@", 1)
    enimi = vasak.split(".", 1)[0] if vasak else ""
    server = parem.split(".", 1)[0] if parem else ""
    domeen = parem.split(".")[-1] if parem else ""

    return enimi, server, domeen

def pea():
    print("EMAILI KONTROLL")
    print("Palun sisesta aadress kujul enimi.pnimi@server.com.\n")

    email = loe_email()
    enimi, server, domeen = eralda_osad(email)
    print(f"Tere {enimi}, sinu email on {server} serveris ja domeeniks on sul {domeen}")

if __name__ == "__main__":
    pea()


# 3. täringud
# kuvatakse korrektne arusaadav küsimus ja hiljem vastus - 1p
# kasutaja võistleb kahe täringuga arvuti vastu - 1p
# kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale - 2p
# kood kommenteeritud - 1p
import random
DICE_SIDES = 6
ALGNE_KASUTAJA_RAHA = 100
ALGNE_ARVUTI_RAHA  = 100

def veereta_2_taringut() -> tuple[int, list[int]]:
    """Veeretab 2 täringut ja tagastab (summa, [t1, t2])."""
    t1 = random.randint(1, DICE_SIDES)
    t2 = random.randint(1, DICE_SIDES)
    return t1 + t2, [t1, t2]
def loe_panuse_sisend(max_summa: int) -> int:
    """
    Küsib kasutajalt panust (täisarv eurodes).
    Lubatud vahemik: 1 .. max_summa. Sisestus '0' lõpetab mängu.
    Vale sisendi korral kuvatakse veateade ja küsitakse uuesti.
    """
    while True:
        toor = input(f"Vali oma panus (1..{max_summa}) või 0 lõpetamiseks: ").strip()
        if toor.isdigit():
            panus = int(toor)
            if panus == 0:
                return 0
            if 1 <= panus <= max_summa:
                return panus
        print("Viga: palun sisesta täisarv vahemikus 1..{0} või 0 lõpetamiseks.".format(max_summa))


def prindi_seis(kasutaja: int, arvuti: int) -> None:
    print(f"\nSinu raha: {kasutaja} € | Arvuti raha: {arvuti} €")


def voor(kasutaja: int, arvuti: int) -> tuple[int, int, bool]:
    max_panustatav = min(kasutaja, arvuti)
    if max_panustatav <= 0:
        return kasutaja, arvuti, False

    print("\n— UUS VOOR —")
    prindi_seis(kasutaja, arvuti)

    panus = loe_panuse_sisend(max_panustatav)
    if panus == 0:
        return kasutaja, arvuti, False
    kasutaja -= panus
    arvuti -= panus
    pott = panus * 2
    k_summa, k_taringud = veereta_2_taringut()
    a_summa, a_taringud = veereta_2_taringut()
    print(f"Sina veeretasid: {k_taringud[0]} ja {k_taringud[1]} -> summa {k_summa}")
    print(f"Arvuti veeretas: {a_taringud[0]} ja {a_taringud[1]} -> summa {a_summa}")

    if k_summa > a_summa:
        kasutaja += pott
        print(f"Võitsid vooru! Võtad laual oleva {pott} € endale.")
    elif a_summa > k_summa:
        arvuti += pott
        print(f"Arvuti võitis vooru ja võtab {pott} € endale.")
    else:
        kasutaja += panus
        arvuti += panus
        print("Viik! Panused tagastati, keegi potti ei saanud.")

    prindi_seis(kasutaja, arvuti)
    if kasutaja > 0 and arvuti > 0:
        vastus = input("Kas mängime veel ühe vooru? (j/e): ").strip().lower()
        return kasutaja, arvuti, (vastus == "j")
    else:
        return kasutaja, arvuti, False


def pea():
    """Peafunktsioon: tervitab, selgitab reeglid ja juhib voorusid."""
    print("TÄRINGUD: Kasutaja vs Arvuti")
    print("Reeglid: veeretate mõlemad 2 täringut, suurem summa võidab panga (pott = 2 × panus).")
    print("Viigi korral makstakse panused tagasi. Sisesta panus täisarvuna eurodes.\n")

    kasutaja = ALGNE_KASUTAJA_RAHA
    arvuti = ALGNE_ARVUTI_RAHA

    jatka = True
    while jatka:
        kasutaja, arvuti, jatka = voor(kasutaja, arvuti)
    print("\nMäng lõppenud.")
    if kasutaja > arvuti:
        print(f"Tubli! Lõppskoor: sina {kasutaja} € vs arvuti {arvuti} € – jäid plussi.")
    elif arvuti > kasutaja:
        print(f"Kahjuks arvuti jäi ette: sina {kasutaja} € vs arvuti {arvuti} €.")
    else:
        print(f"Viik rahas: mõlemal {kasutaja} €.")


if __name__ == "__main__":
    pea()


# 2. Eurokalkuraator - koosta programm, mis kalkuleerib valuuta vastavalt kasutaja soovile EUR->EEK või EEK->EUR
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# kuvatakse veateade, kui kasutaja tegi valiku valesti - 1p
# küsitakse valuuta kogust ja tehakse arvutused - 2p
# kood kommenteeritud - 1p

KURSS = 15.6466
def loe_arvuline_sisend(kusimus: str) -> float:
    while True:
        toor = input(kusimus).strip().replace(",", ".")
        try:
            kogus = float(toor)
            if kogus < 0:
                print("Viga: kogus ei tohi olla negatiivne. Proovi uuesti.")
                continue
            return kogus
        except ValueError:
            print("Viga: palun sisesta arvuline väärtus (nt 12.5).")

def pea():
    print("EUROKALKULAATOR")
    print("Vali suund:")
    print("  1) EUR -> EEK")
    print("  2) EEK -> EUR")
    valik = input("Sisesta valiku number (1 või 2): ").strip()
    if valik == "1":
        eur = loe_arvuline_sisend("Sisesta summa eurodes (EUR): ")
        eek = eur * KURSS
        print(f"{eur:.2f} EUR = {eek:.2f} EEK (kurss {KURSS})")
    elif valik == "2":
        eek = loe_arvuline_sisend("Sisesta summa kroonides (EEK): ")
        eur = eek / KURSS
        print(f"{eek:.2f} EEK = {eur:.2f} EUR (kurss {KURSS})")

    else:
        print("Viga: vale valik. Palun käivita programm uuesti ja vali '1' või '2'.")
if __name__ == "__main__":
    pea()



# 1. Koosta programm, mis kontrollib, kas kasutaja poolt sisestatud arv on paaris või paaritu
# kuvatakse korrektne arusaadav küsimus ja vastus - 1p
# eelnev kontroll, kas kasutaja ei lisanud arvu või pani nulli - 1p
# kood mis teavitab paaris või paaritust arvust - 1p
# kuvatakse programmi pealkiri - 1p
# kood kommenteeritud - 1p

print("=== Paaris või Paaritu Arvu Kontrollija ===")
sisend = input("Sisesta arv: ")
if sisend == "":
    print("Sa ei sisestanud ühtegi arvu")
else:
    try:
        arv = int(sisend)
        if arv == 0:
            print("Null ei ole paaris ega paaritu")
        elif arv % 2 == 0:
            print(f"Arv {arv} on paaris")
        else:
            print(f"Arv {arv} on paaritu")
    except ValueError:
        print("Palun sisesta ainult täisarv, mitte tekst")
