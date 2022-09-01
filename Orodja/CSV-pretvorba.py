import json
import Orodja as o

with open('serije.json') as json_file:
    serije = json.load(json_file)

o.zapisi_csv(serije, ['id', 'naslov', 'studio', 'zanri', 'dolzina', 'vir', 'tip', 'stevilo', 'ocena'], 'serije.csv')

zanri = []

studii = []

obdelani_studiji = set()

id = 1

for serija in serije:
    niz_zanrov = serija['zanri']
    if niz_zanrov != "":
        seznam_zanrov = niz_zanrov.split(",")
        vsi_zanri = list(map(int, seznam_zanrov))
        for zanr in vsi_zanri:
            zanri.append({'serija': serija['id'], 'zanr': zanr})
    if serija['studio'] not in obdelani_studiji and serija['studio'] != "-":
        obdelani_studiji.add(serija['studio'])
        studii.append({'id': id, 'studio': serija['studio']})
        id += 1

o.zapisi_csv(zanri, ['serija', 'zanr'], 'zanri.csv')
o.zapisi_csv(studii, ['id', 'studio'], 'studii.csv')


