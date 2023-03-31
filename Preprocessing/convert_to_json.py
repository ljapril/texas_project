# Marc Garcia
# libriaries
import pandas as pd
import json

# read data
df = pd.read_csv('Station_list.csv')

# create an empty dictionary to store the data
data = {}

# iterate over each row in the DataFrame
for _, row in df.iterrows():

    # create a dictionary for each station
    station_data = {
        "latitude": row["lat"],
        "longitude": row["lon"],
        "elevation(m)": row["elv(m)"],
        "unit": row["unit"],
        "component": row["componet"].split(","),
        "response": [float(x) for x in row["response"].split(",")]
    }

    # add the station data to the main dictionary
    data[row["station"]] = station_data

# write the data to a JSON file
with open('Station_list.json', 'w') as f:
    json.dump(data, f, indent=2)