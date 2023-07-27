from tools.OverwatchModule import OverwatchData
data = OverwatchData() # create data, from online (dont need to understand)

'''
👽 Instructions:

    [Before we start]:
    1. Get an Overwatch hero and assign it to a variable
    2. Save its name to a variable (you can access it at hero.name)
    3. Save its role to a variable (you can access it at hero.role)
    
    [The program]:

    1. Show user the hero's name, and ask the user what their role is
        example: "Name: " + name
    2. Get user's input
    3. Show if it's correct
    
- data.getRandomHero()
'''

# STEP 1 - get a hero and save it in a variable
hero1 = data.getRandomHero()
hero2 = data.getRandomHero()

name = hero1.name
role = hero1.role

# STEP 2 - Show user a question
question1_text = ("What is " + name + "'s role? (damage/tank/support)")
print(question1_text)

# STEP 3 - Get user input
user_guess = input ("[Your guess]: ")

# STEP 4 - Show user "RIGHT/WRONG"
if(user_guess == role):
    print("Correct!")
if(user_guess != role):
    print("Incorrect!")

print(f"{name}'s role is {role}!")

ability1 = data.getRandomHeroAbility(hero2)
ability2 = data.getRandomHeroAbility(hero2)

for i in range(12):
    hero = data.getRandomHero()
    print(f"Random hero: {hero.name}")
    for i in range(2):
        ability = data.getRandomHeroAbility(hero)
        print(f"{ability.name}: {ability.description}")

print("\n==FINISHED==")