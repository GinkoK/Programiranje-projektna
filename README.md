# Programiranje-projektna
Projektna naloga za programiranje

Analiza animiranih televizijskih serij

Analiziral bom animirane serije, ki so začele izhajati po letu 2000 na spletnih straneh
[MAL] https://myanimelist.net/anime/season/{leto}/{letni čas} (npr. /2021/winter)

Za vsako serijo bom zajel:
- naslov
- studio
- dolžino
- vir
- žanre
- opis
- oceno
- število ljudi, ki so ga dodali na seznam

Delovne hipoteze:
- Ali žanr vpliva na ocene in popularnost?
- Ali lahko iz dolžine ali vsebine naslova ugotovimo vir?
- Ali je ocena odvisna od vira?
- Ali studii delajo raznolike serije glede na žanr, ali se specializirajo za določene žanre?
- Ali se spreminja delež virov glede na čas?


Zaenkrat imam tri CSV datoteke, ena osnovna ki vsebuje podatke iz jsona (serije.csv), studii.csv ki iidentificira studije s posameznimi identitetami za lažjo obdelavo podatkov, ter zanri.csv, ki vsakii seriji pripiše žanre.
