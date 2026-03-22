import pandas as pd


library_url = "https://openlibrary.org/api/books?bibkeys=ISBN:9780345354907,ISBN:0881847690,LCCN:2005041555,ISBN:0060957905&format=json"
library_data = pd.read_json(library_url)
library_dimensions = library_data.shape
# print(library_data.index)
# print(library_dimensions)
# print(library_data.head())
# print(library_data.dtypes)

