import pandas as pd


pew_data = pd.read_csv("01-A_Working_with_Data/pew.csv")

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

