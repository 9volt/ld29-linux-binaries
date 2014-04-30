import json
import requests
import re

entry_re = re.compile(r"<a href='\?action=(\w+?)&uid=([0-9]+)' rel=\"dofollow\"><img src='([^']*)'><div class='title'><i>(.*?)</i></div>(.*?)</a></div>")

find_links_re = re.compile(r"<p class='links'>(.*?)</p>")
platform_re = re.compile(r"<a href=\"([^\"]*)\" target='_blank' rel=\"nofollow\">(.*?)</a>")

games = []

def games_on_page(url):
    f = requests.get(url)
    if(f.status_code != 200):
        print('failed url grabbing')
    return entry_re.findall(f.text)

game_pages = []

for i in range(105):
    event_name = 'ludum-dare-29'
    entries_url = "http://www.ludumdare.com/compo/{}/?action=preview&etype=&start={}".format(event_name, i*24)
    game_pages += games_on_page(entries_url)

print(len(game_pages))

def cleaner(s):
    oses = ['windows', 'linux', 'osx', 'web', 'os/x']
    for os in oses:
        if os in s.lower():
            return os.replace('/', '')
    return 'other'

for entry in game_pages:
    url = 'http://www.ludumdare.com/compo/ludum-dare-29/?action=preview&uid={}'.format(entry[1])
    f = requests.get(url)
    if f.status_code != 200:
        print('failed game page')
    links = find_links_re.findall(f.text)
    if len(links) > 0:
        r = platform_re.findall(links[0])
        g = {'name':entry[3], 'author':entry[4], 'url':url}
        if len(r) > 0:
            u, t = zip(*r)
            g['binaries'] = list(map(cleaner, t))
            g['binary_url'] = u
        else:
            print("no platforms found {}".format(entry[1]))
        games.append(g)
    else:
        print("could not find links: {}".format(entry[1]))

with open('games.js', 'w') as f:
    f.write("var game_json = '")
    f.write(json.dumps(games).replace("'", "\\'"))
    f.write("';")
