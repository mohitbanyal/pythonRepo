capitals= {
    "France": "Paris",
    "Germany": "Berlin", 
}

print(capitals)

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C","D"]]

print(nested_list[2][1])

travel_log = {
    "France": {
        "total_visits" : 10,
        "cities_visited":["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "total_visits" : 2,
        "cities_visited":["Hamburg", "Stuttgart", "Berlin"],
    },
}

print(travel_log["Germany"]["cities_visited"][0])