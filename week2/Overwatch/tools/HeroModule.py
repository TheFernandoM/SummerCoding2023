class Hitpoints:
    health = 0
    armor = 0
    shields = 0

class Ability:
    name = "Default ability name"
    description = "Default ability description."

class Hero:
    name = "Default Hero Name"
    name_short = "default-short-name"                 
    abilities = [ ] # empty array
    description = "Default Hero Description"
    hitpoints : Hitpoints # default hitpoints object
    location = "Default Hero Location"
    story = "Epic story goes here."
    role : str