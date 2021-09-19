import random
import tkinter as tk
from tkinter import ttk

class Item:
    """Item. (name, value)."""

    def __init__(self, name, value):
        self.name = name
        self.value = value

class Weapon (Item):
    """Weapon. (name (iht), value(iht), attack)"""

    def __init__(self, name, value, attack):
        super().__init__(name, value)
        self.attack = attack

class Armour (Item):
    """Armour. (name (iht), value(iht), hp)"""

    def __init__(self, name, value, hp):
        super().__init__(name, value)
        self.hp = hp

class Location:
    """Locations. No Functions."""
    
    undiscovered_locations = 0 #required to monitor general progress. DONT CHANGE.
    
    def __init__(self, name, riddle, answer, description, image = "", discovered = False):
        self.name = name
        self.image = image
        self.riddle = riddle
        self.answer = answer
        self.description = description
        self.discovered = discovered
        Location.undiscovered_locations += 1

class Character:
    """Character. Functions include check_stats and improve"""

    foes_remaining = -1 #negative required to account for player character
    wins = 0
    losses = 0

    def __init__(self, name = "XXXXX", attack = 10, hp = 10, speed = 10, money = 15, armour = "", weapon = "", inventory=[], badge_count = 0):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.money = money
        self.armour = armour
        self.weapon = weapon
        self.inventory = inventory
        self.badge_count = badge_count
        Character.foes_remaining += 1
    
    def improve(self, stat):
        if self.money >= 10:
            self.money -= 10
            if stat == "attack":
                self.attack += 5
            if stat == "health":
                self.hp += 5           
            if stat == "speed":
                self.speed += 5
        save("n")
        train()


#GUI ROOT OBJECTS
root = tk.Tk()
root.title("Bad-Guy Brawl")
root.geometry("1920x1080")
menubar = tk.Menu(root)
options = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Game Options", menu = options)
options.add_command(label = "Save", command = lambda:save("y"))
options.add_command(label = "Help", command = lambda:help())
options.add_command(label = "Quit", command = root.destroy)
root.config(menu = menubar)


#GUI IMAGE OBJECTS
try:
    drink_image = tk.PhotoImage(file="drink.png")
    drink_image = drink_image.subsample(3, 3)
    dodge_image = tk.PhotoImage(file="dodge.png")
    dodge_image = dodge_image.subsample(3, 3)
    strike_image = tk.PhotoImage(file="strike.png")
    strike_image = strike_image.subsample(3, 3)
    jungle_image = tk.PhotoImage(file="jungle.png")
    desert_image = tk.PhotoImage(file="desert.png")
    swamp_image = tk.PhotoImage(file="swamp.png")
    abandoned_city_image = tk.PhotoImage(file="abandoned_city.png")
    bull_ring_image = tk.PhotoImage(file="bull_ring.png")
    great_plain_image = tk.PhotoImage(file="great_plain.png")
    mountain_image = tk.PhotoImage(file="mountain.png")
    volcano_image = tk.PhotoImage(file="volcano.png")
except:
    print(" \n \n PLEASE ENSURE THAT ALL .PNG FILES ARE IN THE SAME FOLDER AS THE WORKSPACE\n \n ")

#LOCATION OBJECTS
#name, location_no, description
jungle = Location("Jungle", "What is always in front of you but cannot be seen?", "future","A gloomy but serene oasis of green, with plants and trees at every turn which block\nthe sunlight and where the thick, humid air is saturated with a cacophony of birdsong.", jungle_image)
desert = Location("Desert", "What must be broken before it can be used?", "egg",  "Waves of desolate sand stretching in every direction as far as\nthe eye can see, where the hot sun fiercely pierces the ground.", desert_image)
swamp = Location("Swamp", "What is full of holes but still holds water?", "sponge", "A dismal, flat and featureless marshland, where the air is\nstagnant, and the ground is damp and sticky underfoot.", swamp_image)
abandoned_city = Location("Abandoned City", "The more you take the more you leave behind", "footstep", "Eerily quiet streets, houses and shop fronts, once bustling with life that\nhas been extinguished, leaving behind a raided corpse of the city before.", abandoned_city_image)
bull_ring = Location("Bull Ring", "What has many keys but can't open a door?", "piano", "A gigantic arena with staring and un-forgiving faces in every direction, where the\nair is shattered with screaming and chanting voices and where the dusty ground is covered with bloodspots of previous slaughters.", bull_ring_image)
great_plain = Location("Great Plains", "What runs without feet and has a mouth but can't talk?", "river","A vast and undulating prairie exposed to the hot and sticky sun,\nwhere no life is safe from the predators that roam the grasslands.", great_plain_image)
mountain = Location("Mountains", "What gets wet while drying?", "towel", "A peaceful but breath-taking giant which towers above\nthe land, where the jagged snow covered-tip seems a world away.", mountain_image)
volcano = Location("Volcano", "Where does 'today' come before 'yesterday'?", "dictionary", "A place where no life can survive, where the earth is shattered\nin places and luminescent liquid fire oozes and bubbles from its core.", volcano_image)

location_list = [jungle, desert, swamp, abandoned_city, bull_ring, great_plain, mountain, volcano]


#ITEM OBJECTS
#name, value, attack/hp
clothes = Armour("Clothes",0, 5)
gloves = Weapon("Gloves", 0, 5)
potion_hp = Item("Health Potion", 50)
ring_of_power = Armour("Ring of Power", 20, 15)
oddjob = Weapon("Odd-Job", 40, 30)
sith_armour = Armour("Sith Armour", 50, 35)
lightsaber = Weapon("Lightsaber", 60, 40)
infinity_gauntlet = Armour("Infinity Gauntlet",70,55)
stasis_rifle = Weapon("Stasis Rifle",50,35)
helmet = Armour("Metal Helmet",50,50 )
magnet = Weapon("Magnetic Powers", 85, 65)
batsuit = Armour("Batsuit", 70, 55)
batmobile = Weapon("Batmobile", 100, 80)
kevlar_armour = Armour("Kevlar Armour", 60, 60)
assault_rifle = Weapon("Assault Rifle", 60, 60)
cloak = Armour("Invisibility Cloak", 60, 70)
elder_wand = Weapon("Elder Wand", 80, 100)

item_list = [clothes, gloves, potion_hp, ring_of_power, oddjob, sith_armour, lightsaber, stasis_rifle, infinity_gauntlet,helmet, magnet, batsuit, batmobile, kevlar_armour, assault_rifle, cloak, elder_wand]
weapon_list = [gloves, oddjob, lightsaber, stasis_rifle, magnet, batmobile, assault_rifle, elder_wand]
armour_list = [clothes, ring_of_power, sith_armour, infinity_gauntlet, helmet, batsuit, kevlar_armour, cloak]


#CHARACTER OBJECTS
#name, attack, hp, speed, money, armour=clothes, weapon=gloves, inventory=[]
foe_1 = Character("Gollum", 5, 5, 25, 15, ring_of_power, gloves)
foe_2 = Character("Goldfinger", 10, 15, 15, 20, clothes, oddjob)
foe_3 = Character("Darth Vader", 25, 20, 20, 50,sith_armour,lightsaber)
foe_4 = Character("Magneto", 20, 30, 25, 70, helmet, magnet)
foe_5 = Character("Bane", 40, 40, 30, 90, kevlar_armour, assault_rifle)
foe_6 = Character("Batman", 40, 40, 35,120,batsuit,batmobile)
foe_7 = Character("Voldemort", 40, 50, 40, 100, cloak, elder_wand)
foe_8 = Character("Thanos", 80, 80, 45,1000,infinity_gauntlet,stasis_rifle)
my_character = Character(armour = clothes, weapon = gloves, inventory=[potion_hp])

foe_list = [foe_1, foe_2, foe_3, foe_4, foe_5, foe_6, foe_7, foe_8]

#GUI OBJECTS
canvas_left = tk.Canvas(root)
canvas_left.grid(row=0,column=1)
canvas_right = tk.Canvas(root)
canvas_right.grid(row=0,column=2)

btn_0 = tk.Button(canvas_right, text = "NEW GAME", command = lambda:newgame(), width = 35, font = "bold", anchor = "n")
btn_1 = tk.Button(canvas_right, text = "LOAD GAME", command = lambda:load(conf = "y"), width = 35, font = "bold", anchor = "n")
btn_2 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_3 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_4 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_5 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_6 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_7 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_8 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")
btn_9 = tk.Button(canvas_right, width = 35, font = "bold", anchor = "n")

pop_up = tk.Label(canvas_left, anchor = "n", width = 90, font = ("bold",13))
pop_up.pack()

label = tk.Label(canvas_left, anchor = "n", width = 90, font = ("bold",13))
label.pack()

combobox = ttk.Combobox(canvas_right, width = 33, font = "bold")

entry = tk.Entry(canvas_right, width = 35, font = "bold")

btn_list = [btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8, btn_9]
btn_0.pack()
btn_1.pack()

def help():
    help_text = "The aim of the game is to adventure and battle your way to becoming the Bad Guy Brawl Champion.\n\nGet started by starting a new game and selecting which character you would like to play as.\nThis will bring you to the main menu of the game where you can choose to adventure, battle, shop or train.\n\nTraining will help to improve stats if you have the gold available.\n\nAdventuring will challenge you to solve puzzles and reward you with badges which can be used to battle.\n\nThe shop will allow you to buy potions or sell items within your inventory.\n\nBattling will allow you to fight the next foe if you have enough badges available."
    help_root = tk.Tk()
    help_label = tk.Label(help_root, text = help_text)
    help_label.pack()

def btn_reset(btns_required):
    for btn in btn_list:
        btn.pack()
        btn["image"] = ""
        btn["width"] = 35

    if btns_required == 0:
        for btn in btn_list:
            btn.pack_forget()

    if btns_required == 1:
        btn_list[1].pack_forget()
        btn_list[2].pack_forget()
        btn_list[3].pack_forget()
        btn_list[4].pack_forget()
        btn_list[5].pack_forget()
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 2:
        btn_list[2].pack_forget()
        btn_list[3].pack_forget()
        btn_list[4].pack_forget()
        btn_list[5].pack_forget()
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 3:
        btn_list[3].pack_forget()
        btn_list[4].pack_forget()
        btn_list[5].pack_forget()
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 4:
        btn_list[4].pack_forget()
        btn_list[5].pack_forget()
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 5:
        btn_list[5].pack_forget()
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 6:
        btn_list[6].pack_forget()
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 7:
        btn_list[7].pack_forget()
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 8:
        btn_list[8].pack_forget()
        btn_list[9].pack_forget()

    elif btns_required == 9:
        btn_list[9].pack_forget()

def changename():
    player_name = entry.get()
    if len(player_name) < 10 and len(player_name) != 0:
        my_character.name = player_name
        pop_up["text"]= f"You have chosen to play as {my_character.name}"
        entry.delete(0, 'end')
        entry.pack_forget()
        save("n")
        load()
    elif len(player_name) >= 10:
        label["text"] = "\nPlease use less than 10 characters and more than 1 in your name."
    elif len(player_name) == 0:
        label["text"] = "\nPlease enter a name."

def save(conf = "n"):
    if my_character.name != "XXXXX":
        with open("save_game.txt", "w") as file_object:
            for character in foe_list:
                file_object.write(f"{character.name},{character.hp}\n")
            file_object.write(f"my_character_name,{my_character.name}\n")
            file_object.write(f"my_character_attack,{my_character.attack}\n")
            file_object.write(f"my_character_hp,{my_character.hp}\n")
            file_object.write(f"my_character_speed,{my_character.speed}\n")
            file_object.write(f"my_character_money,{my_character.money}\n")
            for item in my_character.inventory:
                file_object.write(f"inventory_item,{item.name}\n")
            file_object.write(f"my_character_badge_count,{my_character.badge_count}\n")
            file_object.write(f"weapon_item,{my_character.weapon.name}\n")
            file_object.write(f"armour_item,{my_character.armour.name}\n")
            for location in location_list:
                file_object.write(f"{location.name},{location.discovered}\n")
            file_object.write(f"undiscovered_locations,{Location.undiscovered_locations}\n")
            file_object.write(f"foes_remaining,{Character.foes_remaining}\n")
            file_object.write(f"wins,{Character.wins}\n")
            file_object.write(f"losses,{Character.losses}\n")
            if conf == "y":
                pop_up["text"] = "\nGame saved.\n "
    else:
        pop_up["text"] = "You can't save before starting!"

def load(conf = "n"):
    try:
        combobox.pack_forget()
        label["image"] = ""
        btn_reset(4)
        my_character.inventory=[]
        with open("save_game.txt", "r") as file_object:
            lines = file_object.readlines()
            lines = list(lines)
            for line in lines:
                line = line.strip()
                for foe in foe_list:
                    if foe.name in line:
                        res_int = int(line.replace(f"{foe.name},", ""))
                        foe.hp = res_int
                for location in location_list:
                    if location.name in line:
                        res_bool = (line.replace(f"{location.name},", ""))
                        location.discovered = eval(res_bool)
                if "my_character_name" in line:
                    my_character.name = str(line.replace("my_character_name,", ""))
                elif "my_character_attack" in line:
                    my_character.attack = int(line.replace("my_character_attack,", ""))
                elif "my_character_hp" in line:
                    my_character.hp = int(line.replace("my_character_hp,", ""))
                elif "my_character_speed" in line:
                    my_character.speed = int(line.replace("my_character_speed,", ""))
                elif "my_character_money" in line:
                    my_character.money = int(line.replace("my_character_money,", ""))
                elif "inventory_item" in line:
                    item_name = str(line.replace("inventory_item,", ""))
                    for item in item_list:
                        if item.name == item_name:
                            my_character.inventory.append(item)
                elif "my_character_badge_count" in line:
                    my_character.badge_count = int(line.replace("my_character_badge_count,", ""))
                elif "armour_item" in line:
                    armour_name = str(line.replace("armour_item,", ""))
                    for item in item_list:
                        if item.name == armour_name:
                            my_character.armour = item
                elif "weapon_item" in line:
                    weapon_name = str(line.replace("weapon_item,", ""))
                    for item in item_list:
                        if item.name == weapon_name:
                            my_character.weapon = item
                elif "undiscovered_locations" in line:
                    Location.undiscovered_locations = int(line.replace("undiscovered_locations,",""))
                elif "foes_remaining" in line:
                    Character.foes_remaining = int(line.replace("foes_remaining,", ""))
                elif "wins" in line:
                    Character.wins = int(line.replace("wins,", ""))
                elif "losses" in line:
                    Character.losses = int(line.replace("losses,", ""))
            if conf == "y":
                pop_up["text"] = "\nGame Loaded.\n "
            elif conf == "n":
                pop_up["text"] = ""
            label["text"] = f"{my_character.name}, what would you like to do from The Battle Hub?\n"
            btn_list[0].pack()
            btn_list[0]["text"] = "Battle"
            btn_list[0]["command"] = lambda:battle()
            btn_list[1].pack() 
            btn_list[1]["text"] = "Train"
            btn_list[1]["command"] = lambda:train()
            btn_list[2].pack()
            btn_list[2]["text"] = "Shop"
            btn_list[2]["command"] = lambda:shop()
            btn_list[3].pack()
            btn_list[3]["text"] = "Adventure"
            btn_list[3]["command"] = lambda:adventure()
    except FileNotFoundError:
        label["text"] = "No save game found. Please start a new game\n "
        btn_reset(2)

def newgame():
    output_text="\
    \nWelcome to the Bad-Guy Brawl universe, where Bad Guys from every\
    \nfranchise can fight it out to discover... Who is the Bad-Guy Brawl Champion?!\
    \n\
    \nThroughout the next hour of your life, you must adventure, train and battle\
    \nyour way to your calling... becoming The Bad-Guy Brawl Champion.\
    \n\
    \nYou will be based at the Battle Hub, where you are free to battle your way up the Bad-Guy ladder.\
    \nHowever, no warrior has the skills necessary (or luck) to become the Bad-Guy Brawl Champion without\
    \nsome training to boost your abilities and adventure to gain the necessary badges.\
    \n\
    Who would you like to play as?\
    \n"
    btn_reset(1)
    pop_up["text"] = "You have started a new game."
    label["text"] = output_text
    entry.pack()
    btn_list[0]["text"] = "Choose Name"
    btn_list[0]["command"] = lambda:changename()

def strike(foe, heal_limit, heal_limit_foe):
    strike_success = random.randint(1,2) # 1=successful attack. 2=unsuccessfulattack.
    if strike_success == 1:
        damage = int((my_character.attack + my_character.weapon.attack)/random.randint(2,5))
        foe.hp = foe.hp - damage
        if (foe.hp + foe.armour.hp) > 0:
            pop_up["text"] = f"{my_character.name.title()} inflictcted {damage} damage with their strike.\n{foe.name.title()} has {foe.hp + foe.armour.hp} hp remaining.\n{my_character.name.title()} has {my_character.hp + my_character.armour.hp} hp remaining.\n "
        elif (foe.hp + foe.armour.hp) <= 0:
            pop_up["text"] = f"Congratulations on your victory!\nThe medics on site will return your health to normal.\nBefore you leave you loot {foe.name}'s {foe.armour.name}, {foe.weapon.name} and {foe.money} gold."
            my_character.inventory.append(foe.armour)
            my_character.inventory.append(foe.weapon)
            my_character.money += foe.money
            my_character.hp = heal_limit
            Character.wins += 1
            Character.foes_remaining -= 1
            save()
            load(conf = "x")

    elif strike_success == 2:
        damage = random.randint(1,10)
        my_character.hp -= damage
        if (my_character.hp + my_character.armour.hp) > 0:
            pop_up["text"] = f"The strike by {my_character.name.title()} failed and {foe.name.title()} inflicted {damage} damage.\n{foe.name.title()} has {foe.hp + foe.armour.hp} hp remaining.\n{my_character.name.title()} has {my_character.hp + my_character.armour.hp} hp remaining.\n "
        elif (my_character.hp + my_character.armour.hp) <= 0:
            pop_up["text"] = "You have been defeated and will be taken to the Battle-Hub Hospital for treatment to restore your health.\n "
            my_character.hp = heal_limit
            Character.losses += 1
            foe.hp = heal_limit_foe
            save()
            load(conf = "x")

def dodge(foe, heal_limit, heal_limit_foe):
    counter_success = random.randint(1,2) # 1=successful counter attack. 2=unsuccessful counter attack.
    if counter_success == 1:
        damage = int((my_character.attack + my_character.weapon.attack)/random.randint(2,5))
        foe.hp = foe.hp - damage
        if (foe.hp + foe.armour.hp) > 0:
            pop_up["text"] = f"{my_character.name} successfully dodged an attack from {foe.name}.\n{my_character.name.title()} inflictcted {damage} damage with a counter attack.\n{foe.name.title()} has {foe.hp + foe.armour.hp} hp remaining.\n "
        elif (foe.hp + foe.armour.hp) <= 0:
            pop_up["text"] = f"Congratulations on your victory!\nThe medics on site will return your health to normal.\nBefore you leave you loot {foe.name}'s {foe.armour.name}, {foe.weapon.name} and {foe.money} gold."
            my_character.inventory.append(foe.armour)
            my_character.inventory.append(foe.weapon)
            my_character.money += foe.money
            my_character.hp = heal_limit
            Character.wins += 1
            Character.foes_remaining -= 1
            save()
            load(conf = "x")

    elif counter_success == 2:
        damage = random.randint(1,10)
        my_character.hp -= damage
        if (my_character.hp + my_character.armour.hp) > 0:
            pop_up["text"] = f"The dodge by {my_character.name.title()} failed and {foe.name.title()} inflicted {damage} damage.\n{foe.name.title()} has {foe.hp + foe.armour.hp} hp remaining.\n{my_character.name.title()} has {my_character.hp + my_character.armour.hp} hp remaining.\n "
        elif (my_character.hp + my_character.armour.hp) <= 0:
            pop_up["text"] = "You have been defeated and will be taken to the Battle-Hub Hospital for treatment to restore your health.\n "
            my_character.hp = heal_limit
            Character.losses += 1
            foe.hp = heal_limit_foe
            save()
            load("x")

def drink(heal_limit):
    if potion_hp in my_character.inventory:
        drink_test = my_character.hp + 30
        if drink_test <= heal_limit:
            my_character.hp += 30
            pop_up["text"] = f"You now have {my_character.hp + my_character.armour.hp} hp"
            my_character.inventory.remove(potion_hp)
        elif (my_character.hp + 30) > heal_limit:
            my_character.hp = heal_limit
            pop_up["text"] = f"You now have {my_character.hp + my_character.armour.hp} hp"
            my_character.inventory.remove(potion_hp)
    else:
        pop_up["text"] = "You have no potions to drink!"
        pop_up.pack()

def fight(foe): #contains strike and counter functions
    btn_reset(3)
    heal_limit = int(my_character.hp)
    heal_limit_foe = int(foe.hp)
    pop_up["text"] = f"{my_character.name} v {foe.name}\nAttack:\n{my_character.attack + my_character.weapon.attack} v {foe.attack + foe.weapon.attack}\nHealth:\n{my_character.hp + my_character.armour.hp} v {foe.hp + foe.armour.hp}\nSpeed:\n{my_character.speed} v {foe.speed}\n "
    btn_reset(3)
    label["text"] = "Would you like to strike, dodge or drink a potion to replenish up to 30hp?\n "
    btn_list[0]["image"] = strike_image
    btn_list[0]["width"] = 120
    btn_list[0]["compound"] = "left"
    btn_list[0]["text"] = "  Strike"
    btn_list[0]["command"] = lambda:strike(foe, heal_limit, heal_limit_foe)
    btn_list[1]["image"] = dodge_image
    btn_list[1]["width"] = 120
    btn_list[1]["compound"] = "left"
    btn_list[1]["text"] = "  Dodge"
    btn_list[1]["command"] = lambda:dodge(foe, heal_limit, heal_limit_foe)
    btn_list[2]["image"] = drink_image
    btn_list[2]["width"] = 120
    btn_list[2]["compound"] = "left"
    btn_list[2]["text"] = "  Drink"
    btn_list[2]["command"] = lambda:drink(heal_limit)

def battle():
    battle_access = my_character.badge_count + Character.foes_remaining
    btn_reset(0)
    if Character.foes_remaining == 0:
        pop_up["text"] = "There is no one left to fight!! You are the Bad-Guy Brawl CHAMPION!!!."
        load(conf = "x")
    elif Character.foes_remaining != 0:
        if battle_access > 8:
            for foe in foe_list:
                if foe.hp > 0:
                    fight(foe)
                    break
        elif battle_access <= 8:
            pop_up["text"] = "You must collect more badges through adventuring to reach your next foe."
            load(conf = "x")

def shop():
    combobox.pack_forget()
    pop_up["text"] = ""
    btn_reset(4)
    label["text"] = "Welcome to the shop. Would you like to buy, sell or go back to The Battle Hub?\n "
    btn_list[0]["text"] = "Buy"
    btn_list[0]["command"] = lambda:buy()
    btn_list[1]["text"] = "Sell"
    btn_list[1]["command"] = lambda:sell()
    btn_list[2]["text"] = "Check Stats"
    btn_list[2]["command"] = lambda:check_stats()    
    btn_list[3]["text"] = "Back"
    btn_list[3]["command"] = lambda:load()

def check_stats():
    output = f"Name: {my_character.name}\nAttack: {my_character.attack + my_character.weapon.attack}\nHealth: {my_character.hp + my_character.armour.hp}\nSpeed: {my_character.speed}\nMoney: {my_character.money}\nBadges: {my_character.badge_count}\nWins: {Character.wins}\nLosses: {Character.losses}\nFoes Remaining: {Character.foes_remaining}\n"
    pop_up["text"] = output
    label["text"] = ""
    btn_reset(2)
    btn_list[0]["text"] = "Change Loadout"
    btn_list[0]["command"] = lambda:change_loadout()
    btn_list[1]["text"] = "Back to Shop"
    btn_list[1]["command"] = lambda:shop()

def buy():
    if my_character.money >= 50:
        pop_up["text"] = ""
        label["text"] = "This shop only sells health potions. Would you like to buy one for 50 gold?\n "
        btn_reset(2)
        btn_list[0]["text"] = "Yes"
        btn_list[0]["command"] = lambda:buy_conf()
        btn_list[1]["text"] = "No"
        btn_list[1]["command"] = lambda:shop()
    else:
        label["text"] = "Unfortunately you don't have enough gold to buy one.\n "
        pop_up["text"] = "This shop only sells health potions. Would you like to buy one for 50 gold?\n "
        btn_reset(1)
        btn_list[0]["text"] = "Back"
        btn_list[0]["command"] = lambda:shop()

def buy_conf():
    my_character.inventory.append(potion_hp)
    my_character.money -= 50
    pop_up["text"] = "A health potion has been added to your inventory."
    save()
    shop()

def sell():
    if len(my_character.inventory) > 0:
        label["text"] = "Which inventory item would you like to sell?\n "
        item_name_list = []
        for item in my_character.inventory:
            item_name_list.append(item.name)
        combobox.pack()
        combobox["values"] = item_name_list
        combobox.current(0)
        btn_reset(3)
        btn_list[0]["text"] = "Sell"
        btn_list[0]["command"] = lambda:sell_conf()
        btn_list[1]["text"] = "Sort"
        btn_list[1]["command"] = lambda:alphabetise(item_name_list)
        btn_list[2]["text"] = "Back"
        btn_list[2]["command"] = lambda:shop()
    if len(my_character.inventory) == 0:
        label["text"] = "You have no items to sell.\n "
        combobox.pack_forget()
        btn_reset(1)
        btn_list[0]["text"] = "Back"
        btn_list[0]["command"] = lambda:shop()

def sell_conf():
    item_name = combobox.get()
    for item in my_character.inventory:
        if item.name == item_name:
            my_character.money += item.value
            my_character.inventory.remove(item)
            break
        combobox.pack_forget()
    save()
    sell()

def train():
    btn_reset(4)
    pop_up["text"] = f"Training will cost 10 gold and improve a skill by 5.\nYou currently have {my_character.money} gold."
    label["text"] = f"What would you like to train?\nAttack: {my_character.attack}\nHealth: {my_character.hp}\nSpeed: {my_character.speed}"
    btn_list[0]["text"] = "Attack"
    btn_list[0]["command"] = lambda:my_character.improve("attack")
    btn_list[1]["text"] = "Health"
    btn_list[1]["command"] = lambda:my_character.improve("health")
    btn_list[2]["text"] = "Speed"
    btn_list[2]["command"] = lambda:my_character.improve("speed")
    btn_list[3]["text"] = "Return to Battle Hub"
    btn_list[3]["command"] = lambda:load()

def adventure():
    if my_character.money >= 5:
        pop_up["text"] = f"There are {Location.undiscovered_locations} undiscovered locations remaining.\n "
        label["text"] = "Exploring will cost 5 gold per turn to pay for supplies.\nWhere would you like to explore?\n "
        btn_reset(9)
        btn_list[0]["text"] = "The Jungle"
        btn_list[0]["command"] = lambda:search(location_list[0])
        btn_list[1]["text"] = "The Desert"
        btn_list[1]["command"] = lambda:search(location_list[1])
        btn_list[2]["text"] = "The Swamp"
        btn_list[2]["command"] = lambda:search(location_list[2])
        btn_list[3]["text"] = "The Abandoned City"
        btn_list[3]["command"] = lambda:search(location_list[3])
        btn_list[4]["text"] = "The Bull Ring"
        btn_list[4]["command"] = lambda:search(location_list[4])
        btn_list[5]["text"] = "The Great Plains"
        btn_list[5]["command"] = lambda:search(location_list[5])
        btn_list[6]["text"] = "The Mountain"
        btn_list[6]["command"] = lambda:search(location_list[6])
        btn_list[7]["text"] = "The Volcano"
        btn_list[7]["command"] = lambda:search(location_list[7]) 
        btn_list[8]["text"] = "Return to Battle Hub"
        btn_list[8]["command"] = lambda:load()
    if my_character.money < 5:
        pop_up["text"] = f"There are {Location.undiscovered_locations} undiscovered locations remaining.\n "
        label["text"] = "You don't have enough gold to adventure. \n "
        btn_reset(1)
        btn_list[0]["text"] = "Return to Battle Hub"
        btn_list[0]["command"] = lambda:load()

def search(location):
    if location.discovered == False:
        my_character.money -= 5
        label["image"] = ""
        entry.pack()
        pop_up["text"] = f"You have decided to explore The {location.name} in search of another badge.\n{location.description}\n "
        label["text"] = f"You walk into a dark room and a door slams behind you.\nTo revel the badge and escape you must solve this puzzle:\n\n{location.riddle}\n "
        Location.undiscovered_locations -= 1
        btn_reset(1)
        btn_list[0]["text"] = "Submit"
        btn_list[0]["command"] = lambda:get_entry(entry, location.answer, location)
    elif location.discovered == True:
        pop_up["text"] = f"You have already discovered The {location.name}.\nPlease choose another area to explore\n "
        label["image"] = location.image

def get_entry(entry, answer, location):
    player_guess = entry.get()
    player_guess = player_guess.lower()
    if answer in player_guess:
        entry.delete(0, 'end')
        entry.pack_forget()
        pop_up["text"] = "CORRECT! The badge reveals itself and you have been rewarded 5 speed, 5 attack and 5 health.\nA portal teleports you back to The Battle Hub"
        my_character.attack += 5
        my_character.hp += 5
        my_character.speed += 5
        location.discovered = True
        my_character.badge_count += 1
        save()
        load(conf = "x")
    else:
        pop_up["text"] = "INCORRECT"

def change_loadout(conf = "n"):
    if conf == "n":
        pop_up["text"] = ""
    item_name_list = []
    for item in my_character.inventory:
        if item in armour_list:
            item_name_list.append(item.name)
        elif item in weapon_list:
            item_name_list.append(item.name)
    if len(item_name_list) == 0:
        label["text"] = "You have no items in your inventory to equip\n "
        btn_reset(1)
        btn_list[0]["text"] = "Return to Battle Hub"
        btn_list[0]["command"] = lambda:load()
    elif len(item_name_list) > 0:
        label["text"] = "Which item would you like to equip?"
        btn_reset(3)
        combobox.pack()
        combobox["values"] = item_name_list
        combobox.current(0)
        btn_list[0]["text"] = "Return to Battle Hub"
        btn_list[0]["command"] = lambda:load()
        btn_list[1]["text"] = "Sort Alphabetically"
        btn_list[1]["command"] = lambda:alphabetise(item_name_list)
        btn_list[2]["text"] = "Equip Item"
        btn_list[2]["command"] = lambda:change_conf()

def change_conf():
    item_name = combobox.get()
    equipped_name = item_name
    for item in my_character.inventory:
        if item.name == item_name:
            if item in weapon_list:
                my_character.inventory.append(my_character.weapon)
                unequipped_name = my_character.weapon.name
                unequipped_stat = my_character.weapon.attack
                equipped_stat = item.attack
                my_character.inventory.remove(item)
                my_character.weapon = item
                test = True
            elif item in armour_list:
                my_character.inventory.append(my_character.armour)
                unequipped_name = my_character.armour.name
                unequipped_stat = my_character.armour.hp
                equipped_stat = item.hp
                my_character.inventory.remove(item)
                my_character.armour = item
                test = False
            break
        combobox.pack_forget()
    stat_change = equipped_stat - unequipped_stat
    if test == True:
        pop_up["text"] = f"Equipped : {equipped_name}\nUnequipped : {unequipped_name}\nAttack Change: {stat_change}\n " 
    elif test == False:
        pop_up["text"] = f"Equipped : {equipped_name}\nUnequipped : {unequipped_name}\nHealth Change: {stat_change}\n " 
    save()
    change_loadout("y")

def alphabetise(listt):
    listt.sort()
    combobox["values"] = listt
    combobox.current(0)

tk.mainloop()
