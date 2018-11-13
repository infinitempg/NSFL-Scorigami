
from bs4 import BeautifulSoup
import requests

"""
THINGS TO DO:
 - make it all one function (that way I can merge the files)
    - just use an if or something lol
 - make it collect more information for a json file
    - can still split off for the normal txt file as well (but if in one file won't need to)
"""

def get_season(num):
    print('Season',num)
    if num < 10:
        strnum = '0'+str(num)
    elif num >= 10:
        strnum = str(num)
    url = "http://sim-football.com/indexes/NSFLS"+strnum+"/GameResults.html"
    page = requests.get(url)

    soup = BeautifulSoup(page.text,'html.parser')

    test = soup.find_all('tr')[145:]

    sresults = []

    n = 0
    w = 0

    try:
        while n + 1 <= len(test):
            team1 = test[n].find_all('td')
            team1list = []
            for item in team1:
                team1list.append(item.get_text())

            team2 = test[n+1].find_all('td')
            team2list = []
            for item in team2:
                team2list.append(item.get_text())
            gresults = [int(team1list[-1]),int(team2list[-1])]
            gresults.sort()
            sresults.append(gresults)
            n += 8
            w += 1
            if w%2 == 0:
                n += 1
            if w%4 == 0:
                n += 1
            if w == 56:
                n += 1
    except ValueError:
        del(sresults[-1])
        pass
    return sresults

s9 = get_season(9)
s8 = get_season(8)
s7 = get_season(7)
s6 = get_season(6)
s5 = get_season(5)
s4 = get_season(4)
s3 = get_season(3)

## GETTING SEASON 2 BECAUSE WHY

print('Season 2')
url = "http://sim-football.com/indexes/NSFLS02/GameResults.html"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

test = soup.find_all('tr')[137:]

sresults = []

n = 0
w = 0

while n + 1 <= 303:
    team1 = test[n].find_all('td')
    team1list = []
    for item in team1:
        team1list.append(item.get_text())

    team2 = test[n+1].find_all('td')
    team2list = []
    for item in team2:
        team2list.append(item.get_text())
    gresults = [int(team1list[-1]),int(team2list[-1])]
    gresults.sort()
    sresults.append(gresults)
    n += 8
    w += 1
    if w%2 == 0:
        n += 1
    if w%4 == 0:
        n += 1
    if w == 56:
        n += 1

n = 307
w = 0
while n + 1 <= len(test):
    team1 = test[n].find_all('td')
    team1list = []
    for item in team1:
        team1list.append(item.get_text())

    team2 = test[n+1].find_all('td')
    team2list = []
    for item in team2:
        team2list.append(item.get_text())
    gresults = [int(team1list[-1]),int(team2list[-1])]
    gresults.sort()
    sresults.append(gresults)
    n += 8
    w += 1
    if w%2 == 0:
        n += 1
    if w%4 == 0:
        n += 1
    if w == 19:
        break

n = 474
w = 0
while n + 1 <= len(test):
    team1 = test[n].find_all('td')
    team1list = []
    for item in team1:
        team1list.append(item.get_text())

    team2 = test[n+1].find_all('td')
    team2list = []
    for item in team2:
        team2list.append(item.get_text())
    gresults = [int(team1list[-1]),int(team2list[-1])]
    gresults.sort()
    sresults.append(gresults)
    n += 8
    w += 1
    if w%2 == 0:
        n += 1
    if w%4 == 0:
        n += 1
    if w == 2:
        break

n = 492
w = 0
while n + 1 <= len(test):
    team1 = test[n].find_all('td')
    team1list = []
    for item in team1:
        team1list.append(item.get_text())

    team2 = test[n+1].find_all('td')
    team2list = []
    for item in team2:
        team2list.append(item.get_text())
    gresults = [int(team1list[-1]),int(team2list[-1])]
    gresults.sort()
    sresults.append(gresults)
    n += 8
    w += 1
    if w%2 == 0:
        n += 1
    if w%4 == 0:
        n += 1
    if w == 19:
        break

s2 = sresults
sresults = []

### SEASON ONE

print("Season 1")
url = "http://sim-football.com/indexes/NSFLS01/GameResults.html"
page = requests.get(url)

soup = BeautifulSoup(page.text,'html.parser')

test = soup.find_all('tr')[113:]

sresults = []

n = 0
w = 0
k = 0
while n + 1 <= len(test):
    team1 = test[n].find_all('td')
    team1list = []
    for item in team1:
        team1list.append(item.get_text())

    team2 = test[n+1].find_all('td')
    team2list = []
    for item in team2:
        team2list.append(item.get_text())
    gresults = [int(team1list[-1]),int(team2list[-1])]
    gresults.sort()
    sresults.append(gresults)
    n += 8
    w += 1
    k += 1
    if k%2 == 0:
        n += 1
    if w%3 == 0:
        n += 2
        k = 0
    if w == 56:
        n += 1

s1 = sresults
sresults = []

allseasons = s1+s2+s3+s4+s5+s6+s7+s8
#allseasons.sort()

text = open('allscores.txt','w')
for item in allseasons:
    text.write(str(item[0])+"\t"+str(item[1])+"\n")
text.close()
