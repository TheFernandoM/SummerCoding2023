from tools.OverwatchModule import OverwatchData
# ⬆ Importing stuff we need, first
data = OverwatchData() # create OverwatchData object

# STEP 1 - get a hero and save it in a variable
hero1 = data.getRandomHero()

name = hero1.name
role = hero1.role

# STEP 2 - Show user a question
questionText = ("What is " + name + "'s role?")
print(questionText)

# STEP 3 - Get user input
user_guess = input ("[Your guess]: ")

# STEP 4 - Show user "RIGHT/WRONG"
if(user_guess == role):
    print("Correct!")
if(user_guess != role):
    print("Incorrect!")

print(f"{name}'s role is {role}!")
print("\n\n==FINISHED==")