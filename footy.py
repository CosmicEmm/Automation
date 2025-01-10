import pandas as pd
import lxml # not used directly, but pandas uses lxml internally for parsing


scraper = pd.read_html('https://en.wikipedia.org/wiki/Jude_Bellingham')

for index, table in enumerate(scraper): # Iterates over the DataFrames
    print('********************************************')
    print(index)
    print(table)

print(scraper[2]) # Prints the 3rd table (index 2) from the list of DataFrames