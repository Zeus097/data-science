import pandas as pd

# Tidying process
#   ▪ Melt all days
#   ▪ Create days based on date, month and year
#   ▪ Pivot the tmin and tmax columns


weather_data = pd.read_csv("01-A_Working_with_Data/weather.csv")
# print(weather_data.head()) # get first 5 rows of the data

weather_data = weather_data.melt(
    id_vars=[
        "id", "year", "month", "element"
    ],
    var_name="day"
)
weather_data.day = weather_data.day.str.slice(1).astype(int)
# print(weather_data.head())



# Remove missing 
#   / invalid days (e.g., 31st April) 
#       and dates with no records

weather_data = weather_data.dropna()
weather_data["date"] = pd.to_datetime(
    weather_data[
        ["year", "month", "day"]
    ]
)
weather_data = weather_data.drop(
    columns = ["year", "month", "day"]
)
# print(weather_data.head())



# Pivot the elements back to their own columns

weather_data = weather_data.pivot_table(
    index=["id", "date"],
    columns="element",
    values="value"
)
# print(weather_data.head())



# Pivoting returns a multi-indexed element, 
#   go back to a flat DataFrame

weather_data = weather_data.reset_index()
weather_data.columns.name = ""
weather_data = weather_data[
    ["id", "date", "tmin", "tmax"]
]
# print(weather_data.head())

