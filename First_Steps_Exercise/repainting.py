nailonzam = 1.50
boqzal = 14.50
razreditelzal = 5.00
torbichki = 0.40

nailon = int(input()) + 2
boq = int(input())
boyafinal = boq + boq * 0.10
razreditel = int(input())
maistori = int(input())

materiali = nailonzam * nailon + boqzal * boyafinal + razreditelzal * razreditel + torbichki
maistoricena = maistori * (materiali * 0.30)
cena = materiali + maistoricena

print(cena)

