# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv

url = 'https://mojim.com/twh109122.htm'
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'html.parser')
block = soup.find_all('dd', 'hb2')
block2 = soup.find_all('dd','hb3')

songs = []
def writeFile(i):
        j = i.get('href')
        sub_resp = requests.get("https://mojim.com" + j)
        sub_soup = BeautifulSoup(sub_resp.text, 'html.parser')
        name = sub_soup.find('dt','fsZx2')
        lyric = sub_soup.find_all('dd','fsZx3', 'br/')
        print(lyric)
        print(name)
        try:
            name = name.text
        except:
            name = None
        try:
            lyric = lyric.text
        except:
            lyric = None
        return name, lyric

for i in block: 
    song_left = i.find_all('span','hc3')
    for j in song_left:
        sl = j.find_all('a')
        for k in sl:
            tmp = {}
            name, lyric = writeFile(k)
            tmp['Name'] = name
            tmp['Lyric'] = lyric
            songs.append(tmp)

    song_right = i.find_all('span','hc4')
    for j in song_right:
        sr = j.find_all('a')
        for k in sr:
            tmp = {}
            name, lyric = writeFile(k)
            tmp['Name'] = name
            tmp['Lyric'] = lyric
            songs.append(tmp)
        
for i in block2: 
    song_left = i.find_all('span','hc3')
    for j in song_left:
        sl = j.find_all('a')
        for k in sl:
            tmp = {}
            name, lyric = writeFile(k)
            tmp['Name'] = name
            tmp['Lyric'] = lyric
            songs.append(tmp)
                
    song_right = i.find_all('span','hc4')
    for j in song_right:
        sr = j.find_all('a')
        for k in sr:
            tmp = {}
            name, lyric = writeFile(k)
            tmp['Name'] = name
            tmp['Lyric'] = lyric
            songs.append(tmp)

print(len(songs))
df = pd.DataFrame(songs)
file ='./lyrics/田馥甄' + '.csv'
df.to_csv(file, encoding = 'utf-8')