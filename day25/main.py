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

print(data["temp"])