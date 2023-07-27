from tools.OverwatchModule import OverwatchData
data = OverwatchData() # import data (dont need to understand)

'''
👽 Instructions:

- data.getRandomHero()
'''
hero1 = data.getRandomHero()

name = hero1.name
role = hero1.role

print(name, "'s role is", role)

questionText = ("What is " + name + "'s role?")

user_guess = input ("[Your guess]: ")

if(user_guess == role):
    print("Correct!")
if(user_guess != role):
    print("Incorrect!")