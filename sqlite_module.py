

import sqlite3

database: sqlite3.Connection

QUOTE_ID = "QUOTE_ID"
QUOTE_QUOTATION = "QUOTE_QUOTATION"
QUOTE_AUTHOR = "QUOTE_AUTHOR"
TABLE_NAME = "QUOTATION"

## establishing connection between database and python
def database_connection():
    global database
    database = sqlite3.connect("Quotes_Data.db")
    print("Database created/opened successfully.")
    create_table()
    return database

## creating table
def create_table():
    CREATE_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + QUOTE_ID + \
                         " INTEGER PRIMARY KEY AUTOINCREMENT, " + QUOTE_QUOTATION + \
                         " TEXT, " + QUOTE_AUTHOR + " TEXT );"

    database.execute(CREATE_TABLE_QUERY)
    print("Table Created successfully.")

## saving details to table
def save_data(quotation, author):

    SAVE_QUOTE = "INSERT INTO " + TABLE_NAME + " ( " + QUOTE_QUOTATION + ", " \
                 + QUOTE_AUTHOR + " ) VALUES ( '" + quotation + "', '" + author + "' );"

    try:
        database.execute(SAVE_QUOTE)
        database.commit()
    except sqlite3.OperationalError:
        print("Cannot save this quotation", quotation)

## reading data from sqlite table
def read_data():

    RETREIVE_QUOTES = "SELECT * FROM " + TABLE_NAME + " ;"

    try:
        cursor = database.execute(RETREIVE_QUOTES)
        return cursor
    except sqlite3.OperationalError:
        print("Cannot save this quotation")
        return ("No record found")