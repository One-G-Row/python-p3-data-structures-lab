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
    food_names = []
    for food in spicy_foods:
        food_name = food['name']
        food_names.append(food_name)
    return food_names

def get_spiciest_foods(spicy_foods):
   food_heat_level = []
   for food in spicy_foods:
       food_heat = food['heat_level']
   if food_heat > 5:
       food_heat_level.append(food)

   print(food_heat_level)  
   return(food_heat_level)   
   
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food['heat_level'] 
        result = (f"{food['name']}({food['cuisine']})| Heat Level: " + '🌶' * heat_level)
        print(result) 

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
       if food['cuisine'] == cuisine:
           return food

get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    new_spicy_food_list = [food for food in spicy_foods if food['heat_level'] > 5]
    print_spicy_foods(new_spicy_food_list)
    spiciest_food = []
    for food in spicy_foods:
        heat_level = food['heat_level']
        pepper_heat = '🌶' * heat_level
        if heat_level > 5:
            result =f"{food['name']} ({food['cuisine']})| Heat Level: {pepper_heat}" 
            spiciest_food.append(result)
    print(spiciest_food)

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    heat_level = 0
    for food in spicy_foods:
        heat_level = food['heat_level']
        if heat_level > 5:
            heat_level += heat_level
            average_heat_level = heat_level / len(spicy_foods)    
        return average_heat_level
    else:
        return 0
    
   
print(get_average_heat_level(spicy_foods))

def create_spicy_food(my_spicy_foods, new_spicy_food):
       food_list = []
       
       my_spicy_foods.append(new_spicy_food) 
       spicy_foods.extend(food_list)
       print(spicy_foods)
       
create_spicy_food(my_spicy_foods =spicy_foods,    
                  new_spicy_food={
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })