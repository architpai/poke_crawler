# Introduction
The goal while writing this particular web crawler was to crawl and extract all pokemons released yet along with basic information such as their types(some have dual typing)and pokedex entry numbers.
This data can later be used to find pokemons which are strong or weak against each other based on type.
# Methodology
Before begining the scraping it was important to understand the underlying structure of the webpage and to codify the information using xpaths for both understanding and telling the program what to look for while crawling. To understand the page structure, Chrome browser developer tools was used. After quickly glancing over the html structure the use of classes in the html tags was apparent, these classes are precise what enabled easy of crawling and extraction of the webpage. The following information is scraped from the page:
1. Pokedex number
2. Name of the Pokemon
3. Primary Typing
4. Secondary Typing
The data was scraped off of "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon". The webpage has a table indexing all released pokemon in different tables.
Normally it would be quite easy to extract information based on the class or id of the elements but in this specific webpage no such class declaration was used hence a different method was used to scrape the data.
```
url = "https://pokemon.fandom.com/wiki/List_of_Pok%C3%A9mon"
html = urlopen(url)
soup = BeautifulSoup(html , 'html.parser')
```

Above we open the url and pass it in to BeautifulSoup Object to access the HTML.
```
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
```
Next due to the structure we start by accessing and storing all the tables in the variable table_date ,
then iterating over each table we look for all the table rows <tr> within said table.
Every row represent a particular pokemon and hence by accessing table data <td> of each <tr> we have the information that we need.
Because we studied the structure of the table we know that name is stored in the Third <td> and so on.
Once the data is extracted and saved in a dictionary we simply pass it to a dataframe we is then saved as a .csv file
 ```
cdata = {"number": number, "name": name, "type1": type_1, "type2":type_2}
print(cdata)
df = pd.DataFrame(data=cdata)
df.to_csv("pokedex.csv", header=True, index=False)
 ```
