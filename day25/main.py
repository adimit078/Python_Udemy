# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# tempList = data["temp"].to_list()
# print(data["temp"].max())

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241013.csv")
grayCount = len(data[data["Primary Fur Color"] == "Gray"])
blackCount = len(data[data["Primary Fur Color"] == "Black"])
cinnamonCount = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Colors": ["Gray", "Black", "Cinnamon"],
    "Total": [grayCount, blackCount, cinnamonCount]
}

newData = pandas.DataFrame(data_dict)
newData.to_csv("./squirrelColors.csv")



