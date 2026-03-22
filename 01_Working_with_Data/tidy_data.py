import pandas as pd


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

