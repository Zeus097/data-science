import pandas as pd




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

# less_than_10k = pew_data.pivot_table(index="religion", values="<$10k")


# print(pew_data)
# print(less_than_10k)

# print(less_than_10k.index_col())

pew_tidy = pew_data.melt(
    id_vars=["religion"], # Identifier variables (all others are "unpivoted")
    var_name="income", # Variable
    value_name="frequency" # Value
)

# print(pew_tidy)


# ----------------------------------------------------------------
# TASK:
#     Tidying process
#         ▪ First, melt all columns (they are values and should not be)
#         ▪ Next, split the column names and extract the gender and age information
#         ▪ Add the new info to the dataset
#         ▪ Remove all missing values


tb_data = pd.read_csv("01_Working_with_Data/tb.csv")

def process_age_group(age_group):
    ages = {
        "04": "0-4",
        "65": "65+",
        "u": "unknown"
    }
    if age_group in ages:
        return ages[age_group]
    else:
        return f"{age_group[:-2]}-{age_group[-2:]}"
    

tb = tb_data.melt(
    id_vars = ["iso2", "year"],
    var_name = "sex_and_age",
    value_name = "cases"
)

tb["sex"] = tb.sex_and_age.str.get(0)
tb["age_group"] = tb.sex_and_age.str.slice(1)
tb = tb.drop(columns="sex_and_age")

tb.age_group = tb.age_group.apply(process_age_group)

# Tidy up the column and row order
tb = tb[["iso2", "year", "sex", "age_group", "cases"]]
tb = tb.sort_values(["iso2", "year"])

# print(tb.head())
# ----------------------------------------------------------------
