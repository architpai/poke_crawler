from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import re
import numpy as np
from urllib.request import urlopen

url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon"
html = urlopen(url)
soup = BeautifulSoup(html , 'html.parser')

number = []
name = []
type_1 = []
type_2 = []

all_tables = soup.find_all(class_='wikitable')
for table in all_tables:
    pokemon = table.find_all('tr')
    for entry in pokemon:
        values = entry.find_all("td")
        if len(values) > 0:
            if values[0].text is not None:
                number.append(values[0].text.rstrip())
            if values[2].text is not None:
                name.append(values[2].text.rstrip())
            if values[3].text is not None:
                type_1.append(values[3].text.rstrip())
            if values[4].text is not None:
                type_2.append(values[4].text.rstrip())

cdata = {"number": number, "name": name, "type1": type_1, "type2":type_2}
print(cdata)
df = pd.DataFrame(data=cdata)
df.to_csv("pokedex.csv", header=True, index=False)