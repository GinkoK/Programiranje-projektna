import re
import requests
import json

sep = 'TV (Continuing)'
count = 0

vzorec = (
    r'<div class="seasonal-anime js-seasonal-anime" .*?'
    r'data-genre="'
    r'(?P<zanri>.*?)'
    r'"><div>.*?'
    r'class="link-title">'
    r'(?P<naslov>.*?)'
    r'</a></h2>'
    r' .*?<a href="/anime/producer/\d*/.*?" '
    r'title=".*?">'
    r'(?P<studio>.*?)'
    r'</a>'
    r'.*?'
    r'.*?<span>'
    r'(?P<dolzina>.*?)'
    r'\s+.*?'
    r'<span class="source">'
    r'(?P<vir>.*?)'
    r'</span>'
    r'.*?id="'
    r'(?P<id>.*?)'
    r'">'
    r'.*?<div class="info">\W+'
    r'(?P<tip>.*?)'
    r'\s+'
    r'.*?<span class="member fl-r" title="Members">\D+'
    r'(?P<stevilo>.*?)'
    r'\s+'
    r'.*?title="Score">\W+'
    r'(?P<ocena>.*?)'
    r'\s+'
)

serije = []

for leto in range(2000, 2022):
    for sezona in ['winter', 'spring', 'summer', 'fall']:
        url = (
            'https://myanimelist.net/anime/season/'
            f'{leto}/{sezona}'
        )
        r= requests.get(url)
        html = r.text
        nov = html.split(sep, 1)[0]
        vsebina = nov.replace('\n', '').replace('          -', '<a href="/anime/producer/69/Dummy" title="Dummy">-</a>')
        for zadetek in re.finditer(vzorec, vsebina):
            serije.append(zadetek.groupdict())
            count += 1
        print(count)

with open('serije.json', 'w', encoding='utf-8') as f:
    json.dump(serije, f, indent=2)
