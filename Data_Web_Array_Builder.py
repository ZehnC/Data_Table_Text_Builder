import requests
import pandas as pd
from bs4 import BeautifulSoup
import csv

#url's with table
# url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
url = 'https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'
csv = 'C:\\Users\maxzc\Documents\GitHub\Data_Table_Text_Buildermy_data.csv'

#Function to grable the tables from the URL
def read_html_table(url, csv):

    html = requests.get(url).content

    #decode and encod in utf8 for special chars
    unicode_str = html.decode('utf8')
    encoded_str = unicode_str.encode("utf8", 'ignore')

    #parse through html and find tables
    news_soup = BeautifulSoup(encoded_str, "html.parser")
    tables = news_soup.find_all('table')

    #take the dataframe and put it into a csv
    df_list = pd.read_html(str(tables))
    df = df_list[-1]
    # print(df)
    df.to_csv(csv) 

#function to format the csv into a readable sorted array
def format_csv(csv):
    #turn csv into an array
    data = pd.read_csv(csv, sep=',', header=1, index_col=0).values
    params = data.max(axis=0)
    # print(params[0])
    # print(params[1])
    # print(params[2])
    
    #create array of size of the maxim values
    grid = [[' ' for x in range(params[0] + 1)] for y in range(params[2] + 1)]

    #parse through data array and place into the Grid array
    for block in data:
        # print(grid)
        # print(block[2])
        grid[block[2]][block[0]] = block[1]
    # grid[0][0] = 1

    # print(grid)
    return grid

#function to print on the text on the sorted grid
def print_grid(grid):
    max = len(grid) - 1
    
    #print out each line in the grid starting from the top value
    while max > -1:
        for block in grid[max]:
            #printing on the same line
            print(block, end="")
        #creating a new line
        print("")
        max -= 1

#Running all functions together
read_html_table(url, csv)
textblock = format_csv(csv)
print_grid(textblock)

