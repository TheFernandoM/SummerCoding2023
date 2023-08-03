from tools.HeroModule import Hero, Hitpoints, Ability
class OverwatchData:
    heroes = {}
    def getHeroesList(self):
        return list(self.heroes)
    
    def getRandomHeroName(self):
        import random
        return random.choice(list(self.heroes))
    def getRandomHeroAbility(self, hero : Hero) -> Ability:
        import random
        return random.choice(list(hero.abilities))
    def getRandomHero(self) -> Hero:
        '''
        Made by Fernando. Gets a random Overwatch hero.
        '''
        random_hero_name = self.getRandomHeroName()
        return self.heroes[random_hero_name]
    
    def _getOverwatchHeroesDataJson(self):
        import urllib.request # this lets us make a REQUEST to a website
        import urllib.response # this lets us get a RESPONSE from a website (after a request)
        import urllib.parse # (this helps to make the text for the request )
        import ssl # this lets us use HTTPS
        import json # this lets us read the response in a text format called JSON
        import time # this lets us wait x seconds

        # STEP 0 - (setting up everything first to be able to get online)
        ctx = ssl.create_default_context() # (this block of code was copy pasted from Stackoverflow "/27208131/urllib-cannot-read-https")
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        base_url = "https://overfast-api.tekrop.fr"
        heroes_url = "/heroes"                         # url to get names of heroes
        hero_data_url = "/heroes/{name}"               # url to get data of a specific hero (if you know their name)

        # STEP 1 - get list of Overwatch hero names
        url = base_url + heroes_url # create the url
        heroes_response = urllib.request.urlopen(url, context=ctx) # make the request
        heroes_json = json.loads(heroes_response.read()) # read the request in JSON format

        hero_names = [ ]

        for hero_json in heroes_json:
            name_short = hero_json['key'] # get short version of hero name
            name_full = hero_json['name'] # get full version of hero name
            hero_names.append({ 'name_short' : name_short, 'name_full' : name_full })
        
        # STEP 2 - get data about each hero
        heroes = { }  # create a dictionary of heroes (empty at the moment)

        print("Loading data for...")
        for hero_name_object in hero_names:
            hero_name = hero_name_object['name_full']
            hero_name_short = hero_name_object['name_short']
            hero_url = hero_data_url.replace('name','0').format(hero_name_short)
            url = base_url + hero_url # create the url for the hero
            try:
                hero_data_response = urllib.request.urlopen(url, context=ctx) # make the request
            except:
                print("(ERROR:", hero_name, "). ", end='')
                continue
            print(hero_name + "...", end='')
            hero_data_json = json.loads(hero_data_response.read()) # read the request in JSON format
            hero_abilities = hero_data_json['abilities']
            hero_description = hero_data_json['description']
            hero_hitpoints = hero_data_json['hitpoints']
            hero_location = hero_data_json['location']
            hero_story = hero_data_json['story']['chapters'][0]['content']
            hero_role = hero_data_json['role']
            heroes[hero_name] = { 'name': hero_name, 'name_short': hero_name_short, 'abilities' : hero_abilities, 'description' : hero_description, 'hitpoints' : hero_hitpoints, 'location' : hero_location,
                                'role' : hero_role, 'story' : hero_story }
            #time.sleep(0.01) # wait 0.01 second, to not spam the website too much
        print("Loaded", len(heroes), "heroes.")
        return heroes # after everything is done, return the heroes data
    
    def _convertJsonToHero(self, hero_json):
        hero = Hero()

        hero.name = hero_json['name']
        hero.name_short = hero_json['name_short']
        hero.description = hero_json['description']
        hero.location = hero_json['location']
        hero.role = hero_json['role']
        abilities_json = hero_json['abilities']
        hero.abilities = self._convertAbilitiesJsonToObject(abilities_json)

        hitpoints_json = hero_json['hitpoints']
        hero.hitpoints = self._convertHitpointsJsonToObject(hitpoints_json)

        return hero
    
    def _convertJsonsToHeroes(self, heroes_json):
        heroes = {}
        for hero_name in heroes_json:
            hero_json = heroes_json[hero_name]
            hero = self._convertJsonToHero(hero_json)
            heroes[hero.name] = hero
        return heroes

    def _convertAbilityJsonToObject(self, ability_json):
        ability = Ability() # create ability
        ability.name = ability_json['name']
        ability.description = ability_json['description']

        return ability

    def _convertAbilitiesJsonToObject(self, abilities_json):
        abilities_array = [] # empty array
        for ability_json in abilities_json:
            abilities_array.append(self._convertAbilityJsonToObject(ability_json))

        return abilities_array
    
    def _convertHitpointsJsonToObject(self, hitpoints_json):
        hitpoints = Hitpoints()
        hitpoints.armor = hitpoints_json['armor']
        hitpoints.health = hitpoints_json['health']
        hitpoints.shields = hitpoints_json['shields']

        return hitpoints

    def __init__(self):
        heroesJson = self._getOverwatchHeroesDataJson()
        self.heroes = self._convertJsonsToHeroes(heroesJson)
        print("="*12,end='')
        print("\nOverwatch heroes data has been loaded and is ready to be used.")
        print("="*12 + "\n")