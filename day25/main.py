# import csv
#
# data = []
#
# with open("weather_data.csv") as data_file:
#     # for line in csv:
#     #     newline = line.rstrip("\n")
#     #     data.append(newline)
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperature = row[1]
#         if 'temp' not in temperature:
#             temperatures.append(int(temperature))
#
#     print(temperatures)
# # print(data)

import pandas

data = pandas.read_csv("weather_data.csv")
#
# # print(data["temp"])
#
# data_dict = data.to_dict()
# temp_list = data["temp"].to_list()

# sum = sum(temp_list)
# temp_list_len = len(temp_list)

# print(round(sum/temp_list_len))
# print(data["temp"].mean())
# print(data["temp"].max())

#Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp_c = monday.temp
temp_f = monday.temp * 1.8 + 32
print(temp_f)

#Create dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
#
# data.to_csv("student_scores.csv")

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
cinnamon = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
black = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "count": [grey, cinnamon, black]
}

dataf = pandas.DataFrame(data_dict)
dataf.to_csv("squirrel_color.csv")