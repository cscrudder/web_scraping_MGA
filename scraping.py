
import requests
import bs4
import csv
from datetime import date
today = date.today()

def headline_grabber():
    res = requests.get('https://www.hispantv.com/ultimas-noticias')
    if res.status_code == requests.codes.ok:
        body = bs4.BeautifulSoup(res.text, 'html.parser')
        headlines = []
        for headline in body.find_all("h3"):
            headlines.append(headline.text)
        for i in headlines:
            if 'Titulares más destacados de HispanTV' in i:
                headlines.remove(i)
    else:
        #send me an email or do something so we know it didn't work
        print("Oops there was a problem with the webpage.")
    return headlines

def existing_grabber():
    knownLines = open('headline_data.csv', 'r')
    csvOb = csv.DictReader(knownLines)
    existing_headlines = []
    for i in csvOb:
        if i['Headline'] != '':
            existing_headlines.append(i["Headline"])
    return existing_headlines


def print_list(hl,exl):
    print_list = []
    for i in hl:
        if i != '':
            if i not in exl:
                print_list.append(i)
    return print_list


def csv_writer(printing):
    database = open('headline_data.csv','a')
    for i in printing:
        database.write('\n')
        database.write(str(today))
        database.write(',')
        database.write(i)



headlines = headline_grabber()
existing = existing_grabber()
printing = print_list(headlines, existing)
print(printing)
csv_writer(printing)
