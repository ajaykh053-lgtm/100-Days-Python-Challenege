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

analized_data = {
    " Fur color": ["Gray", "Red", "Black"],
    "Count": [num_of_Gray_squirrel, num_of_Cinnamon_squirrel, num_of_Black_squirrel],
}
df = pandas.DataFrame(analized_data)
df.to_csv("new_squirrel_data.csv")
