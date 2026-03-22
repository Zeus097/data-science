import pandas as pd


accidents_data = pd.read_csv("01_Working_with_Data/accidents.csv")

# # PRINTING accidents_data
# print(accidents_data)



# # PRINTING accidents_data COLUMNS
# print(accidents_data.columns)


# # PRINTING accidents_data INDEX VALUES
# print(accidents_data.index)


# # PRINTING accidents_data DIMENSIONS (rows, columns)
# print(accidents_data.shape)


# ----------------------------------------------------------------


green_tripdata = pd.read_excel("01_Working_with_Data/green_tripdata_2015-09.xls")
# print(green_tripdata.shape)


# ----------------------------------------------------------------


library_url = "https://openlibrary.org/api/books?bibkeys=ISBN:9780345354907,ISBN:0881847690,LCCN:2005041555,ISBN:0060957905&format=json"
library_data = pd.read_json(library_url)
library_dimensions = library_data.shape
# print(library_data.index)
# print(library_dimensions)
# print(library_data.head())
# print(library_data.dtypes)


# ----------------------------------------------------------------

pew_data = pd.read_csv("01_Working_with_Data/pew.csv")
less_than_10k = pew_data.pivot_table(index="religion", values="<$10k")
# print(pew_data)
# print(less_than_10k)

# print(less_than_10k.index_col())

# ----------------------------------------------------------------
