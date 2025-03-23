# # with open("weather_data.csv") as weather_data:
# #     data = weather_data.readlines()
# #     print(data)
#
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
# from statistics import mean
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # result = data["temp"].max()
# # print(result)
#
# # print(data[data.temp == data["temp"].max() ])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp)
#
# #create a data frame
# data_dict = {
#     "students" : ["Amy", "GayBoy"],
#     "scores" : [21,32]
#
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas
data = pandas. read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count,black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrels.csv")