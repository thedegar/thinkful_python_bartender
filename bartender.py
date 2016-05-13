# Tyler Hedegard 5/13/2016
# Thinkful.com Python Introduction Lesson 3
# Pirate Bartender 

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

names = {
    "adjective": ["Fluffy","Gallant","Rebellious","Sassy","Malicious"],
    "noun": ["Sea-Dog","Batman","Knight","Nail","Doormat"],
}

def ask(questions):
    """Asks all questions in a dictionary and returns the answers in a dictionary"""
    answers = {}
    for question in questions:
        reply = input(questions[question])
        if reply.lower() == "yes" or reply.lower() == "y":
            answers[question] = True
        else:
            answers[question] = False
    return answers

def makeDrink(ingredients, preferences):
    """Takes preferences and ingredients, picks random ingredient from each preference and returns a drink (name and ingredients)"""
    import random
    drinkName = random.choice(names["adjective"]) + " " + random.choice(names["noun"])
    drink = {
        "name": drinkName,
        "ingredients": [],
    }
    
    for preference in preferences:
        if preferences[preference] == True:
            drink["ingredients"].append(random.choice(ingredients[preference]))
    
    return drink
    
if __name__ == '__main__':
    drink = makeDrink(ingredients,ask(questions))
    print("Here is your {} with {}.".format(drink["name"],drink["ingredients"]))