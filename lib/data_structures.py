spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = [n["name"] for n in spicy_foods]
    return name_list
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_list = [n for n in spicy_foods if n["heat_level"] >= 5]
    return spiciest_list
    pass

def print_spicy_foods(spicy_foods):
    printed_spice = [print(f'{n["name"]} ({n["cuisine"]}) | ' + 'Heat Level: ' + '🌶'*n["heat_level"]) for n in spicy_foods]
    return printed_spice
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    get_cuisine = [n for n in spicy_foods if n["cuisine"] == cuisine]
    return get_cuisine[0]
    pass

def print_spiciest_foods(spicy_foods):
    printed_spiciest = [print(f'{n["name"]} ({n["cuisine"]}) | ' + 'Heat Level: ' + '🌶'*n["heat_level"]) for n in spicy_foods if n["heat_level"] >= 5]
    return printed_spiciest
    pass

def get_average_heat_level(spicy_foods):
    heat_levels = [n["heat_level"] for n in spicy_foods]
    return sum(heat_levels) / len(heat_levels)
    pass

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    pass
