# #_________          _______                                              
# #\__   __/|\     /|(  ____ \                                             
# #   ) (   | )   ( || (    \/                                             
# #   | |   | (___) || (__                                                 
#    | |   |  ___  ||  __)                                                
#    | |   | (   ) || (                                                   
#    | |   | )   ( || (____/\                                             
#    )_(   |/     \|(_______/                                             
                                                                        
#           _______  _        _        _______           _______  ______  
# |\     /|(  ___  )( \      ( \      (  ___  )|\     /|(  ____ \(  __  \ 
# | )   ( || (   ) || (      | (      | (   ) || )   ( || (    \/| (  \  )
# | (___) || (___) || |      | |      | |   | || | _ | || (__    | |   ) |
# |  ___  ||  ___  || |      | |      | |   | || |( )| ||  __)   | |   | |
# | (   ) || (   ) || |      | |      | |   | || || || || (      | |   ) |
# | )   ( || )   ( || (____/\| (____/\| (___) || () () || (____/\| (__/  )
# |/     \||/     \|(_______/(_______/(_______)(_______)(_______/(______/ 
                                                                        
#  _       _________ _        _______  ______   _______  _______          
# | \    /\\__   __/( (    /|(  ____ \(  __  \ (  ___  )(       )         
# |  \  / /   ) (   |  \  ( || (    \/| (  \  )| (   ) || () () |         
# |  (_/ /    | |   |   \ | || |      | |   ) || |   | || || || |         
# |   _ (     | |   | (\ \) || | ____ | |   | || |   | || |(_)| |         
# |  ( \ \    | |   | | \   || | \_  )| |   ) || |   | || |   | |         
# |  /  \ \___) (___| )  \  || (___) || (__/  )| (___) || )   ( |         
# |_/    \/\_______/|/    )_)(_______)(______/ (_______)|/     \|        
# _______  _______                                              
# (  ___  )(  ____ \                                             
# | (   ) || (    \/                                             
# | |   | || (__                                                 
# | |   | ||  __)                                                
# | |   | || (                                                   
# | (___) || )                                                   
# (_______)|/                                                    
                                                               
#           _______  _        _       _________ _        _______ 
# |\     /|(  ____ \( \      ( \      \__   __/( (    /|(  ____ \
# | )   ( || (    \/| (      | (         ) (   |  \  ( || (    \/
# | (___) || (__    | |      | |         | |   |   \ | || (__    
# |  ___  ||  __)   | |      | |         | |   | (\ \) ||  __)   
# | (   ) || (      | |      | |         | |   | | \   || (      
# | )   ( || (____/\| (____/\| (____/\___) (___| )  \  || (____/\
# |/     \|(_______/(_______/(_______/\_______/|/    )_)(_______/ 


#---------------------------------------------------------------------------------------------------------------------------------
#  _____   ___  ___  ___ _____                            
# |  __ \ / _ \ |  \/  ||  ___|                           
# | |  \// /_\ \| .  . || |__                             
# | | __ |  _  || |\/| ||  __|                            
# | |_\ \| | | || |  | || |___                            
#  \____/\_| |_/\_|  |_/\____/                            
                                                        
                                                        
# ______ _   _ _   _ _____ _____ _____ _____ _   _  _____ 
# |  ___| | | | \ | /  __ \_   _|_   _|  _  | \ | |/  ___|
# | |_  | | | |  \| | /  \/ | |   | | | | | |  \| |\ `--. 
# |  _| | | | | . ` | |     | |   | | | | | | . ` | `--. \
# | |   | |_| | |\  | \__/\ | |  _| |_\ \_/ / |\  |/\__/ /
# \_|    \___/\_| \_/\____/ \_/  \___/ \___/\_| \_/\____/ 
#---------------------------------------------------------------------------------------------------------------------------------
print(" ")




def play_adventure():
    inventory = []
    global player_gold
    player_gold = 0
    
    from random import randint, choice  
    
    
# Character options
    male = ("Eadwin The Human", "Banain The Dwarf", "Lathore The Elf", "Brian the Halfling")
    female = ("Cyna The Human", "Khimah The Dwarf", "Laserie The Elf", "Jane The Halfling")
    classes = ("Warrior", "Mage", "Rogue")
    pre_game_selection = (
        "Yes",
        "Absolutely",
        "Erm... maybe, but what's in it for me?",
        "What will you pay me for this task?"
    )
    Level5_Selection = ("Yes", "No")

    # Main adventure function


    print("Welcome to Character Creation!")

    def get_user_choice(options):
        #Display the numbered list of options
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        # Prompt until a valid input is received
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    # function for purchasing items from merchant
    def purchase(price, item_name):
        global player_gold
        
        if price > player_gold:
            print("You don't have enough gold for this item")
        else:
            player_gold -= price
            inventory.append(item_name)
            print(f"You purchased {item_name} for {price} gold! You now have {player_gold} remaining")


    # function for bartering the price of an item with a merchant
    def barter(minimum, item_name):
        global player_gold
        
        while True:
            try:
                offer = int(input("What's your best offer?"))
                if offer < minimum:
                    print("Pfft, you're wasting my time. Get out of my sight!")
                    return
                elif offer >=minimum and offer <= player_gold:
                    print(f"{offer}? Fine, I guess. You have a deal.")
                    player_gold -= offer
                    inventory.append(item_name)
                    return
                elif player_gold < offer:
                    print("You don't have enough gold! Stop wasting my time!")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")

    def mimic_fight(pre_choice): # Alice
        print("It's time to fight!")
        combat_roll = randint(1, 20)
        print(f"Combat Roll: {combat_roll}")
    
        success_threshold = 7 if pre_choice in (1, 2) else 13

        if combat_roll >= success_threshold:
            print("You defeat the enemy and loot a Potion!")
            inventory.append("Potion")
        else:
            if "Potion" in inventory:
                inventory.remove("Potion")
                print("You barely survive using a Potion.")
            else:
                print("You are defeated.")
                result = "restart"
        return "continue"

    def chest_items(pre_choice=None): #Alice
        rolld4 = randint(1, 4)
        if rolld4 in (1, 2):
            print("There is a Potion of Healing inside the chest! You pick it up.")
            inventory.append("Potion")
            return "continue"
        elif rolld4 == 3:
            print("There is an excellent hat inside the chest! You pick it up.")
            inventory.append("Rare Hat")
            return "continue"
        else:
            print("You reach forward to open the chest, but it opens by itself. The wood warps to reveal jagged teeth, and a long slimy purple tongue springs out and wraps around your arm - it's a Mimic!")
            input("\033[1mClick to continue...\033[0m\n")
            result = mimic_fight(pre_choice if pre_choice is not None else 1)
            return result

    def check_for_traps():
    
        return randint(1, 4) == 4
    
    

        
            
   
    
    
  



    #  _______  _______  _        _______  _______ _________
    # (  ____ \(  ____ \( \      (  ____ \(  ____ \\__   __/
    # | (    \/| (    \/| (      | (    \/| (    \/   ) (   
    # | (_____ | (__    | |      | (__    | |         | |   
    # (_____  )|  __)   | |      |  __)   | |         | |   
    #       ) || (      | |      | (      | |         | |   
    # /\____) || (____/\| (____/\| (____/\| (____/\   | |   
    # \_______)(_______/(_______/(_______/(_______/   )_(   
                                                        
    #  _______  _        _______           _______  _______ 
    # (  ____ )( \      (  ___  )|\     /|(  ____ \(  ____ )
    # | (    )|| (      | (   ) |( \   / )| (    \/| (    )|
    # | (____)|| |      | (___) | \ (_) / | (__    | (____)|
    # |  _____)| |      |  ___  |  \   /  |  __)   |     __)
    # | (      | |      | (   ) |   ) (   | (      | (\ (   
    # | )      | (____/\| )   ( |   | |   | (____/\| ) \ \__
    # |/       (_______/|/     \|   \_/   (_______/|/   \__/


    while True:
        gender_input = input("Choose your gender (Male/Female): ").strip().lower()
        if gender_input in ("m", "male"):
            options = male
            break
        elif gender_input in ("f", "female"):
            options = female
            break
        else:
            print("Invalid input. Please type 'M' or 'F'.")

    print("\nChoose your character:")
    for i, name in enumerate(options, 1):
        print(f"{i}. {name}")
    while True:
        try:
            char_choice = int(input("Enter the number of your choice: "))
            if 1 <= char_choice <= len(options):
                selected_character = options[char_choice - 1]
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nChoose your class:")
    for i, class_name in enumerate(classes, 1):
        print(f"{i}. {class_name}")
    while True:
        try:
            class_choice = int(input("Enter the number of your class: "))
            if 1 <= class_choice <= len(classes):
                selected_class = classes[class_choice - 1]
                break
            else:
                print("Please enter a valid class number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            
            
            
            

            
            
            
            
            
            
            
            

    #  _______  _______  _______  _        _______  _______           _______ 
    # (  ____ )(  ____ )(  ___  )( \      (  ___  )(  ____ \|\     /|(  ____ \
    # | (    )|| (    )|| (   ) || (      | (   ) || (    \/| )   ( || (    \/
    # | (____)|| (____)|| |   | || |      | |   | || |      | |   | || (__    
    # |  _____)|     __)| |   | || |      | |   | || | ____ | |   | ||  __)   
    # | (      | (\ (   | |   | || |      | |   | || | \_  )| |   | || (      
    # | )      | ) \ \__| (___) || (____/\| (___) || (___) || (___) || (____/\
    # |/       |/   \__/(_______)(_______/(_______)(_______)(_______)(_______/

    print("--- Character Created ---\n")
    print(f"You have selected {selected_character} and chosen the {selected_class} class.")
    input("\033[1mClick to continue...\033[0m\n")

    print("We wish you good luck on your adventure through the world of Helline!")
    input("\033[1mClick to continue...\033[0m\n")

    print("Our Story begins in the local blacksmith, in the harbour town of Antbluff on the South coast of Helline where Helline meets the Maelstrom Sea.")
    input("\033[1mClick to continue...\033[0m\n")

    print("This blacksmiths is where you will start your adventure.")
    input("\033[1mClick to continue...\033[0m\n")
    print(f"Over the music from the local bards, 'Working for the Weekend,' you hear a booming voice!")
    input("\033[1mClick to continue...\033[0m\n")
    print(f"Welcome to Buns and Ovens, {selected_character.split()[0]} — it is I, Wulfa.")
    input("\033[1mClick to continue...\033[0m\n")

    print("I have a task for you, but be warned, it is dangerous. I need an enchanted book, a grimoire, to create some enchanted armour. The book lies in the hoard of Nabaru, an evil creature that lurks far away in Ordathorp. It will be a treacherous journey, but your reward will be worth it, I'm sure...")
    input("\033[1mClick to continue...\033[0m\n")

    print("Will you help Wulfa?")
    for i, option in enumerate(pre_game_selection, 1):
        print(f"{i}. {option}")
    while True:
        try:
            pre_choice = int(input("Enter the number of your choice: "))
            if 1 <= pre_choice <= len(pre_game_selection):
                selected_pre_game_option = pre_game_selection[pre_choice - 1]
                print(f"You selected: {selected_pre_game_option}")
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if pre_choice == 1:
        print("You receive a standard weapon.")
        if selected_class == "Warrior":
            inventory.append("Sword")
        elif selected_class == "Mage":
            inventory.append("Magic Staff")
        elif selected_class == "Rogue":
            inventory.append("Twin Daggers")
    elif pre_choice == 2:
        print("You receive powerful gear!")
        if selected_class == "Warrior":
            inventory.extend(["Golden Sword", "Shield of Vapaz"])
        elif selected_class == "Mage":
            inventory.extend(["Vale of Song Staff", "Cloak"])
        elif selected_class == "Rogue":
            inventory.extend(["Daggers of the Fallen", "Smoke Bomb"])
    elif pre_choice == 3:
        print("You begin your journey with empty hands.")
    elif pre_choice == 4:
        inventory.append("Potion")
        print("You receive a Healing Potion.")

    # Show inventory
    input("\033[1mClick to continue...\033[0m\n")
    print("\n--- Inventory ---")
    print(f"You have {len(inventory)} item(s): {', '.join(inventory) if inventory else 'nothing'}")
    input("\033[1mClick to continue...\033[0m\n")    

    #  _        _______           _______  _           __   
    # ( \      (  ____ \|\     /|(  ____ \( \         /  \  
    # | (      | (    \/| )   ( || (    \/| (         \/) ) 
    # | |      | (__    | |   | || (__    | |           | | 
    # | |      |  __)   ( (   ) )|  __)   | |           | | 
    # | |      | (       \ \_/ / | (      | |           | | 
    # | (____/\| (____/\  \   /  | (____/\| (____/\   __) (_
    # (_______/(_______/   \_/   (_______/(_______/   \____/

    print("As you travel down the Pandy River you reach a fork in the road:")
    input("\033[1mClick to continue...\033[0m\n")

    print("You look down the left path and you see a treacherous cliff edge path.")
    input("\033[1mClick to continue...\033[0m\n")

    print("On the right you see the higher path taking you further down the river.")
    input("\033[1mClick to continue...\033[0m\n")

    while True:
        direction_input = input("Choose your path (Left or Right): ").strip().lower()
        if direction_input in ("left", "l"):
            fall_risk = randint(1, 20)
            print(f"Fall Risk Roll: {fall_risk}")
            if fall_risk >= 13:
                survival_roll = randint(1, 20)
                print(f"Survival Roll: {survival_roll}")
                if survival_roll <= 5:
                    if "Potion" in inventory:
                        print("You use your potion and survive the fall!")
                        inventory.remove("Potion")
                    else:
                        print("You die from the fall.")
                        return "restart"
                else:
                    print("You survive the fall with injuries.")
            else:
                print("You navigate the cliff safely.")

            # Loot at end of path
            if pre_choice in (1, 2):
                inventory.append("Potion")
            elif pre_choice == 3:
                loot_options = {
                    "Warrior": ["Potion", "Sword"],
                    "Mage": ["Potion", "Magic Staff"],
                    "Rogue": ["Potion", "Twin Daggers"]
                }
                found_item = choice(loot_options.get(selected_class, ["Potion"]))
                inventory.append(found_item)
            elif pre_choice == 4:
                if selected_class == "Warrior":
                    inventory.append("Steel Sword")
                elif selected_class == "Mage":
                    inventory.append("Magical Staff")
                elif selected_class == "Rogue":
                    inventory.append("Poisoned Dagger")
            break

        elif direction_input in ("right", "r"):
            enemy = choice(["Goblin", "Troll", "Bandit"])
            print(f"A wild {enemy} appears!")
            combat_roll = randint(1, 20)
            print(f"Combat Roll: {combat_roll}")
            success_threshold = 7 if pre_choice in (1, 2) else 13
            if combat_roll >= success_threshold:
                
                print("You defeat the enemy and loot a potion and some gold!")
                inventory.append("Potion")
                player_gold += 200
            else:
                if pre_choice == 4 and "Potion" in inventory:
                    print("You barely survive using a Potion.")
                    inventory.remove("Potion")
                else:
                    print("You are defeated.")
                    return "restart"
            break
   
    # Show updated inventory
    input("\033[1mClick to continue...\033[0m\n")
    print("\n--- Inventory & Gold ---")    
    print(f"You have {len(inventory)} item(s): {', '.join(inventory) if inventory else 'nothing'}")
    print(f"You have {(player_gold)} gold")
    input("\033[1mClick to continue...\033[0m\n")

    #  _        _______           _______  _          _______ 
    # ( \      (  ____ \|\     /|(  ____ \( \        / ___   )
    # | (      | (    \/| )   ( || (    \/| (        \/   )  |
    # | |      | (__    | |   | || (__    | |            /   )
    # | |      |  __)   ( (   ) )|  __)   | |          _/   / 
    # | |      | (       \ \_/ / | (      | |         /   _/  
    # | (____/\| (____/\  \   /  | (____/\| (____/\  (   (__/\
    # (_______/(_______/   \_/   (_______/(_______/  \_______/

    print("You have now moved on from The Pandy River, and now have the task of traversing the Rusting Hills:")
    input("\033[1mClick to continue...\033[0m\n")

    print("As you progress through the tiring terrain, you notice a figure in the distance approaching down your path...")
    input("\033[1mClick to continue...\033[0m\n")

    print("As you get closer, it becomes clear the figure is a traveling merchant!")
    input("\033[1mClick to continue...\033[0m\n")

    print("The merchant stops you in your tracks and introduces himself as Sornast Vresta, how would you like to continue?")
    input("\033[1mClick to continue...\033[0m\n")
    
    while True:
        traveler_options = ["1. Buy Item", "2. Attack", "3. Ignore"]
        merchants_items = ["Magic Potion", "Smoke Bomb", "Continue Quest"]
        choice = get_user_choice(traveler_options)

    #Player chooses to buy an item
        if choice == traveler_options[0]:
            while True:

                shop_choice = get_user_choice(merchants_items)

                #Player chooses to go back to initial interaction
                if shop_choice == merchants_items[2]:
                    break

                #Player chooses Magic potion
                elif shop_choice == merchants_items[0]:
                    while True:
                        print("Magic Potion? Sure, best I can do is 150 gold. Hows that?")
                        sale_options = ["Agreed", "Barter", "Go Back"]
                        sale_choice = get_user_choice(sale_options)

                        #Player chooses to go back to shop menu
                        if sale_choice == sale_options[2]:
                            break
                        #Player agrees to purchase at current price
                        elif sale_choice == sale_options[0]:
                            purchase(150, merchants_items[0])
                            break
                        #Player chooses to barter the price
                        elif sale_choice == sale_options[1]:
                            barter(100, merchants_items[0])
                            break
                        break
                #Player chooses smoke bomb
                elif shop_choice == merchants_items[1]:
                    while True:
                        print("Smoke Bomb? Sure, best I can do is 200. Hows that?")
                        sale_options = ["Agreed", "Barter", "Go Back"]
                        sale_choice = get_user_choice(sale_options)
                        
                        #Player chooses to go back to shop menu
                        if sale_choice == sale_options[2]:
                            break
                        #Player agrees to purchase at current price
                        if sale_choice == sale_options[0]:
                            purchase(150, merchants_items[1])
                            break
                        #Player chooses to barter the price
                        elif sale_choice == sale_options[1]:
                            barter(100, merchants_items[1])
                            break
                        break
        #Player chooses to attack the merchant
        elif choice == traveler_options[1]:
            print("Sornast Vresta has a shocked look on his face, as you draw your weapon...")
            input("\033[1mClick to continue...\033[0m\n")

            print("You swing at Sornast Vresta with your weapon to their surprise, taking one chance you have...")
            input("\033[1mClick to continue...\033[0m\n")
            diceroll_player = randint(1, 20)
            diceroll_enemy = randint(1, 20)

            print(f"You roll a {diceroll_player}!")
            input("\033[1mClick to continue...\033[0m\n")
            if diceroll_player > diceroll_enemy:
                print("You successfully kill Sornast Vresta in a single swift swing, and take his goods with you!")

                inventory.append(merchants_items[0])
                inventory.append(merchants_items[1])
            else:
                print("Sornast Vresta was too resiliant to your attack, and flees the confrontation swiftly!")

        #Player chooses to ignore the merchant
        elif choice == traveler_options[2]:
            print("Sornast Vresta stands and stares in disbelief as you completely ignore him and continue your journey through the hills.")
            input("\033[1mClick to continue...\033[0m\n")
            break


        print("You continue on your way after the strange encounter with Sornast Vresta.")
        input("\033[1mClick to continue...\033[0m\n")
        break









    #  _        _______           _______  _          ______  
    # ( \      (  ____ \|\     /|(  ____ \( \        / ___  \ 
    # | (      | (    \/| )   ( || (    \/| (        \/   \  \
    # | |      | (__    | |   | || (__    | |           ___) /
    # | |      |  __)   ( (   ) )|  __)   | |          (___ ( 
    # | |      | (       \ \_/ / | (      | |              ) \
    # | (____/\| (____/\  \   /  | (____/\| (____/\  /\___/  /
    # (_______/(_______/   \_/   (_______/(_______/  \______/ 
                                        
    print("You make it to the other side of the Rusting Hills:")
    input("\033[1mClick to continue...\033[0m\n")
    print("On route to The Temple Of The Fallen, you meet a stranger on the road.")
    input("\033[1mClick to continue...\033[0m\n")
    print()
    print("The stranger offers you the chance to meet The Great Orc of Heggifell to have a strength contest. He is undefeated so far!")
    while True:
        while True:
            try:
                choice_side_quest = input("Choose your answer (yes/no): ").strip().lower()
                if choice_side_quest in ("y", "yes"):
                    print("Good choice, brave adventurer, follow me and let's go and see The Great Orc of Heggifell to see how strong you are!")
                    combat_roll = randint(1, 20)
                    print(f"dice roll: {combat_roll}")
                    input("\033[1mClick to continue...\033[0m\n")
                    if combat_roll < 8:
                        print("Congratulations! You defeated The Great Orc of Heggifell in a strength test! He'll never live this down!")
                        break
                    else:
                        print("Unlucky! You are not as strong as The Great Orc of Heggifell.")
                    break
                elif choice_side_quest in ("n", "no"):
                    print("Not feeling so brave are we! Continue on to The Temple of The Fallen.")
                    input("\033[1mClick to continue...\033[0m\n")
                    break
            except ValueError:
                print("invalid input, please type 'y' or 'n'")
        
                                       
                                        
                                        
        #  _        _______           _______  _             ___   
        # ( \      (  ____ \|\     /|(  ____ \( \           /   )  
        # | (      | (    \/| )   ( || (    \/| (          / /) |  
        # | |      | (__    | |   | || (__    | |         / (_) (_ 
        # | |      |  __)   ( (   ) )|  __)   | |        (____   _)
        # | |      | (       \ \_/ / | (      | |             ) (  
        # | (____/\| (____/\  \   /  | (____/\| (____/\       | |  
        # (_______/(_______/   \_/   (_______/(_______/       (_)  
                                            
    # Begin scene
        
        print("You have reached the fabled Temple of The Fallen.")
        print("It has long since been abandoned, but in searching through the rubble... you find a treasure chest!")
        input("\033[1mClick to continue...\033[0m\n")

        while True:
                print("\nDo you open the chest?")
                chest_choice = ["Yes", "No", "Check it for traps"] #Alice
                for i, option in enumerate(chest_choice, 1):
                    print(f"{i}. {option}")

                try:
                    pre_choice = int(input("Enter the number of your choice: "))
                    if pre_choice == 1:
                        print("You decide to open the chest.")
                        chest_items(pre_choice)
                        break
                    elif pre_choice == 2:
                        print("This place gives you the creeps... you decide not to take any unnecessary risks and you continue on your journey.")
                        break
                    elif pre_choice == 3:
                        print("It's better to be safe than sorry. You carefully inspect the chest for traps...")
                        input("\033[1mClick to continue...\033[0m\n")
                        if check_for_traps():
                            print("Uh oh... you've heard stories about Mimics in these parts. They are monsters that disguise themselves as chests to trick adventurers. This chest definitely looks suspicious... but is it worth the risk?")
                        
                            while True:
                                decision = input("Do you still want to open it? (Yes/No): ").strip().lower()
                                if decision == "yes":
                                    print("You open the suspicious chest...")
                                    chest_items(4)
                                    break
                                elif decision == "no":
                                    print("This place gives you the creeps... you decide not to take any unnecessary risks and you continue on your journey.")
                                    break
                                else:
                                    print("Please type Yes or No.")
                                    
                        else:
                            print("It seems safe enough...")
                            input("\033[1mClick to continue...\033[0m\n")
                            continue
                        break
                    else:
                        print("Please enter a number between 1 and 3.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                    
            # Show inventory
                print("\n--- Inventory ---")
                print("You have:", ", ".join(inventory) if inventory else "nothing.")                                        
                                            
                                                
                                                
                                            
                                                
            #  _        _______           _______  _          _______ 
            # ( \      (  ____ \|\     /|(  ____ \( \        (  ____ \
            # | (      | (    \/| )   ( || (    \/| (        | (    \/
            # | |      | (__    | |   | || (__    | |        | (____  
            # | |      |  __)   ( (   ) )|  __)   | |        (_____ \ 
            # | |      | (       \ \_/ / | (      | |              ) )
            # | (____/\| (____/\  \   /  | (____/\| (____/\  /\____) )
            # (_______/(_______/   \_/   (_______/(_______/  \______/      

        print("You approach the Tower of Forno near the city of Ordathorp:")
        input("\033[1mClick to continue...\033[0m\n")
        print("Your Journey is nearly over. You arrive at the gate of The Tower Of Forno which overlooks the city of Ordathorp.")
        input("\033[1mClick to continue...\033[0m\n")
        print()
        print("There, standing in front of you, guarding the gate, is one of the Guards of Ordathorp. These are the legendary warriors who have always protected Ordathorp from danger.") 
        input("\033[1mClick to continue...\033[0m\n")
        print()
        print("Hello there, traveller. The city is locked and under siege from the Ancient Dragon Nabaru.")
        input("\033[1mClick to continue...\033[0m\n")
        print()
        print("I advise you to return from whence you came.")
        input("\033[1mClick to continue...\033[0m\n")

        print("\nDo you heed the guard's warning?")
        for i, option in enumerate(Level5_Selection, 1):
            print(f"{i}. {option}")

        while True:
                try:
                    user_choice = int(input("Enter your choice (1 or 2): "))
                    if user_choice == 1:  
                        print("\nYou choose to turn back. Perhaps another day, another time, you will brave the path again.")
                        input("\033[1mClick to continue...\033[0m\n")
                        print("As you head back, you hear a voice say 'We can't all be heroes.'")
                        input("\033[1mClick to continue...\033[0m\n")
                        return "restart"

                    elif user_choice == 2:  
                        print("\nYou steel your resolve and press forward towards Ordathorp.")
                        input("\033[1mClick to continue...\033[0m\n")
                        print("As you leave the gate towards Ordathorp, the guard shouts: 'You are a brave one. May the elder gods be with you…'")
                        input("\033[1mClick to continue...\033[0m\n")
                        break
                    else:
                        print("Please enter 1 or 2.")
                except ValueError:
                    print("Invalid input. Please enter a number.")



            #  _        _______           _______  _           ______ 
            # ( \      (  ____ \|\     /|(  ____ \( \         / ____ \
            # | (      | (    \/| )   ( || (    \/| (        ( (    \/
            # | |      | (__    | |   | || (__    | |        | (____  
            # | |      |  __)   ( (   ) )|  __)   | |        |  ___ \ 
            # | |      | (       \ \_/ / | (      | |        | (   ) )
            # | (____/\| (____/\  \   /  | (____/\| (____/\  ( (___) )
            # (_______/(_______/   \_/   (_______/(_______/   \_____/ 
            
            
        potential_bosses = ["Wyvern", "Wyrm", "Drakon", "Cockatrice", "Hydra"]

        Dragon_type = potential_bosses[randint(0, 4)]    


        print("You reach Ordathorp, a winding dunegon labyrinth with a hoard of magical items at the end of it,")
        input("\033[1mClick to continue...\033[0m\n")
        print()
        print("protected by the dastardly Nabaru.")
        input("\033[1mClick to continue...\033[0m\n")
        print()
        
        
        print(f"You enter Ordathorp, sneak down the spiralling dungeon maze, and reach the Dragon's hoard, where you are face to face with Mighty {Dragon_type} known as Nabaru.")
        input("\033[1mClick to continue...\033[0m\n")
        print("You see the grimoire, nestled between the claws of the beast, and you know what you have to do.")
        input("\033[1mClick to continue...\033[0m\n")
        print("The scary stories they told to you as a child were true. This will be your final stand.")
        input("\033[1mClick to continue...\033[0m\n")
        print()

        while True:
            dragon_fight = randint(1, 20)
            print(f"Dragon fight dice roll: {dragon_fight}")
            input("\033[1mClick to continue...\033[0m\n")
            print()        
            if dragon_fight <= 12:
                        
                if "Potion" in inventory:
                        print("You use your potion and Retry your fight with Nabaru!")
                        input("\033[1mClick to continue...\033[0m\n")
                        print()
                        inventory.remove("Potion")
                        
                else:
                        print("This was some other hero's destiny. You struggle and fight, but it's no use. You are eaten by Nabaru.")
                        input("\033[1mClick to continue...\033[0m\n")
                        print()
                        return "restart"
                
            else:
                print("You’ve done the impossible! You dodge and deflect the monster's attacks, and eventually manage to drive your weapon into the mighty Dragon's heart!")
                input("\033[1mClick to continue...\033[0m\n")
                print("Your quest is complete. You journey back to Wulfa with the grimoire!")
                print()
                break
                # return "restart"



    # _______  _______ _________ _        _______  _______           _______ 
    # (  ____ \(  ____ )\__   __/( \      (  ___  )(  ____ \|\     /|(  ____ \
    # | (    \/| (    )|   ) (   | (      | (   ) || (    \/| )   ( || (    \/
    # | (__    | (____)|   | |   | |      | |   | || |      | |   | || (__    
    # |  __)   |  _____)   | |   | |      | |   | || | ____ | |   | ||  __)   
    # | (      | (         | |   | |      | |   | || | \_  )| |   | || (      
    # | (____/\| )      ___) (___| (____/\| (___) || (___) || (___) || (____/\
    # (_______/|/       \_______/(_______/(_______)(_______)(_______)(_______/


        print()
        print("--- EPILOGUE ---")
        print()

        print ("You return to Antbluff in all your glory, Grimoire in hand.")
        print ("The townsfolk celebrate you as a hero, and Wulfa congradulates you on your bravery.")
        input("\033[1mClick to continue...\033[0m\n")

        print ("The people of the village used to tell stories about the lives lost to Nabaru. Now, they'll tell stories of your victory instead.")
        input("\033[1mClick to continue...\033[0m\n")

        print ("Wulfa has a reward for you! As well as being the owner of the bakery, 'Buns & Ovens,' he is the most famous blacksmith in the area, specifically for crafting his magical weapons and armour...")
        input("\033[1mClick to continue...\033[0m\n")

        print ("Wulfa hands over your reward:")
        print ("It's a bun, fresh from the oven!")
        print()
        input("\033[1mClick to continue...\033[0m\n")
        print("---------------")
        print("--- THE END ---")
        print("---------------")
        print()
        print ("Thanks for playing! :)")
        print()
        return "restart"
            



while True:
    result = play_adventure()
    if result == "restart":
        print("\nRestarting your adventure...\n")
        continue
    else:
        while True:
            restart = input("Would you like to restart your adventure? (yes/no): ").strip().lower()
            if restart in ("yes", "y"):
                print("\nRestarting your adventure...\n")
                break
            elif restart in ("no", "n"):
                print("Farewell, brave adventurer!")
                exit()
            else:
                print("Please enter 'yes' or 'no'.")


    play_adventure()
    player_gold = 0
    is_developer=False