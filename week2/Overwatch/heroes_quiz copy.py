from tools.OverwatchModule import OverwatchData
data = OverwatchData() # create data, from online (dont need to understand)

heroes = data.heroes

# STEP 1 - get a hero and save it in a variable
hero1 = data.getRandomHero()
hero1.abilities