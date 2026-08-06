capitlas = {"France": "Paris", "Germany": "Berlin,"}
# nesting the List in dictionary
travel_log = {"France": ["Paris", "Lille", "Dijon"], "Germany": ["stuttgart", "Berlin"]}

# print(lille)
print(travel_log["France"])
print(travel_log["France"][0])
print(travel_log["France"][1])
print(travel_log["France"][2])
print(travel_log["Germany"])
print(travel_log["Germany"][0])
print(travel_log["Germany"][1])

# nesting List inside another List
nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])
print(nested_list[2][0])
print(nested_list[2])
print(nested_list[0])
print(nested_list[1])

# Nesting Dictionary inside Dictionary and List inside Dictionary
print("\n")
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["stuttgart", "Berlin"],
        "total_visits": 5,
    },
}
print(travel_log["France"])
print(travel_log["France"]["cities_visited"])
print(travel_log["France"]["cities_visited"][0])
print(travel_log["France"]["cities_visited"][1])
print(travel_log["France"]["cities_visited"][2])
print(travel_log["France"]["total_visits"])

print(travel_log["Germany"])
print(travel_log["Germany"]["cities_visited"])
print(travel_log["Germany"]["cities_visited"][0])
print(travel_log["Germany"]["cities_visited"][1])
print(travel_log["Germany"]["total_visits"])
