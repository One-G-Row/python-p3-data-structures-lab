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

""" print_spicy_foods(spicy_foods)  """

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        food_cuisine = food['cuisine']
        name = food['name']

        if food_cuisine == cuisine:
           print(food)

get_spicy_food_by_cuisine(spicy_foods, "American")


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food['heat_level']
        if heat_level > 5:
            print(f"{food['name']} ({food['cuisine']})| Heat Level:" + '🌶' * heat_level)
            

print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    """  heat_level_list = []
     total_list = []
     
     total = 0
     for food in spicy_foods:
        heat_level = food['heat_level']
        heat_level_list.append(heat_level)
        total += heat_level
        print(total)
        total_list.append(total)
        print(total_list)
        last_list = total_list[-1]
        last_element = last_list[-1]
        print(last_element) 
        print(total)  """
        
         
        
get_average_heat_level(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
       food_list = []
       
       food_list.append(spicy_food) 
       spicy_foods.extend(food_list)
       print(spicy_foods)
       
create_spicy_food(spicy_foods,     {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })