from bs4 import BeautifulSoup
import requests

## defining website address, from where to scrape data
website_address = "http://quotes.toscrape.com"
result = requests.get(website_address, verify=False)

soup = BeautifulSoup(result.text, "html.parser")

quotes = soup.findAll("div", {"class": "quote"})

quotation_list = []
authors_list = []
quotation_number = []
quotes_dict = {}

i = 1
for quote in quotes:
    quotation = quote.find("span", {"class": "text"}).text

    quotation_list.append(quotation)
    author = quote.find("small", {"class": "author"}).text

    authors_list.append(author)
    quotation_number.append(i)

    i = i+1

## creating dictionary of quotations
quotes_dict['QUOTE_QUOTATION'] = quotation_list
quotes_dict['QUOTE_AUTHOR'] = authors_list
quotes_dict['QUOTE_ID'] = quotation_number

## converting dictionary to dataframe
import pandas as pd
data = pd.DataFrame(data=quotes_dict)

data = data.set_index('QUOTE_ID')
print(data.head())

# print(data)
data.to_csv("Quotation.csv")












