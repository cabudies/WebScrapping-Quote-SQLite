# WebScrapping-Quote-SQLite
Webscrapping using beautiful soup4 and storing the data and retrieving the data from sqlite.

## Steps followed -
```
1. Scrape the data from website - quotes.toscrape.com
2. Store the data into dictionary 'Quotation.csv'.
3. Open tkinter gui.
4. Click on 'Load' button, to load the data into SQLite table.
5. Click on 'Show' button, to show the data into TreeView.
```

## Files in order - 
```
1. Web scrapping - intro-scrapping.py 
Work done - scrapping data from quotes.toscrape.com
Output - Quotation.csv containing 10 quotations.

2. Creating Tkinter gui having 2 buttons Load and Save data.
Load Button - 
Work done - Load button will be used to convert csv file to sql data.
Output - Quotes_Data.db database file containing all the quotations from csv file.

Save Button - 
Work done - Load data from sql data into cursor 
Output - Tree view containing all the quotations from the sqlite database.
