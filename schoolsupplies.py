himikali = 5.80
markeri = 7.20
preparat = 1.20
paketh = int(input())
paketm = int(input())
litrip = int(input())
namalenie = int(input()) / 100

cena = paketh * himikali + paketm * markeri + litrip * preparat
finalnacena = cena - cena * namalenie
print(finalnacena)
