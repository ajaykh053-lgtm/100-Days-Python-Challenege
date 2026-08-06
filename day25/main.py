# with open("C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/weather_data.csv") as weather_data_file:
#     data=weather_data_file.readlines()
#     for items in data:
#         print(f"{items}")
# import csv
# with open("C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/weather_data.csv") as weather_data_file:
#     data = csv.reader(weather_data_file)
#     days=[]
#     temperatures=[]
#     condition=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import csv
# import pandas

# # fromtting the csv file using pandas libary
# data = pandas.read_csv(
#     "C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/weather_data.csv"
# )
# # print(data)
# # print(data["temp"])

# # converting exsisting dta in csv file to python dictionary
# data_dict = data.to_dict()
# print(data_dict)

# # converting exsisting data in csv file to list in python
# temp_list = data["temp"].to_list()
# print(temp_list)

# # finding the average temprature of whole week
# # print(sum(temp_list)/len(temp_list))
# print(data["temp"].mean())
# print(data["temp"].max())


# # Get columns
# print(data["condition"])
# # or
# print(data.condition)
# # Get row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])


# monday = data[data.day == "Monday"]
# print(monday.condition)
# frenhit = (monday.temp * 9 / 5) + 32
# print(f"Temp in frenheit {frenhit}")


# # Create a data frame from sratch
# data_dictionary = {"Students": ["Any", "James", "Angela"], "scores": [76, 56, 65]}
# data1 = pandas.DataFrame(data_dictionary)
# print(data1)

# data1.to_csv("new_data.csv")

import pandas

data = pandas.read_csv(
    "C:/Users/ajayk/OneDrive/ドキュメント/Python/day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)
num_of_Gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
num_of_Cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
num_of_Black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
print(num_of_Gray_squirrel)
print(num_of_Cinnamon_squirrel)
print(num_of_Black_squirrel)

analized_data={
   " Fur color" : ["Gray","Red","Black"],
   "Count" :[num_of_Gray_squirrel,num_of_Cinnamon_squirrel,num_of_Black_squirrel]
}
df=pandas.DataFrame(analized_data)
df.to_csv("new_squirrel_data.csv")
