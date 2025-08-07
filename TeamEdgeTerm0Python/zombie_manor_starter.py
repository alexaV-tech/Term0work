# The Villainess's Escape

# Game state variables
current_room = 'bedroom'
inventory = []
game_over = False

# Required items for escape
required_items = {
    'gold pouch': False,
    'travel cloak': False,
    'stable key': False,
    'sturdy horse': False,
    'map of the estate': False
}

# Game rooms and their properties 
rooms = {
    'bedroom': {
        'description': "You are in your opulent bedroom, though it has felt more like a gilded cage for weeks. Moonlight streams through the tall, barred window, glinting off the silk sheets and velvet furniture that feel cold and mocking. The air is still and suffocating. A heavy, dark travel cloak hangs in an otherwise empty armoire, a stark contrast to the finery—a promise of a different life. The only exit is south, back into the heart of the house.",
        'exits': {'south': 'hallway'},
        'items': ['travel cloak'] 
    },
    'hallway': {
        'description': "You stand in the grand, cavernous hallway. Your footsteps echo silently on the cold marble floor. Stern-faced portraits of your ancestors line the walls, their painted eyes seeming to follow your every move. This is the nexus of the estate, a dangerous, open space. The path north leads to your bedroom, the east door opens to the study, and the west passage goes to the stables. To the south, a door leads to the old gardens and a hidden shed. The main exit of the estate is also here, heavily guarded and impossible to use.",
        'exits': {
            'north': 'bedroom',
            'east': 'study',
            'west': 'stables',
            'south': 'hidden_shed',
            'exit': 'escape_point'
        },
        'items': []
    },
    'study': {
        'description': "You've slipped into the old study, a room thick with the scent of dust and aging paper. Leather-bound books sag on forgotten shelves, and a thin layer of grime covers every surface. A single candle flickers on the cluttered desk, casting long, dancing shadows. Partially hidden beneath a heavy tome, you see a rolled-up map of the estate. The only way out is west into the hallway.",
        'exits': {'west': 'hallway'},
        'items': ['map of the estate']
    },
    'stables': {
        'description': "The earthy smell of hay and leather fills the air, a welcome relief from the stuffiness of the manor. Moonlight filters through the wooden slats of the walls, illuminating the gentle, shifting forms of the horses in their stalls. Your favorite, a sturdy horse known for his stamina, is here, but his stall is securely locked. By the door, hanging on a rusty nail, is a simple iron stable key, an arrogant oversight by your captors. To take the sturdy horse, you must take the key The path east leads back to the hallway.",
        'exits': {'east': 'hallway'},
        'items': ['stable key', 'sturdy horse']
    },
    'hidden_shed': {
        'description': "You're inside a small, dilapidated shed at the edge of the gardens, a place you haven't visited since childhood. The air smells of damp earth and rotting wood, and spiderwebs cling to old gardening tools. You notice one of the floorboards near the back wall is slightly loose, just as you remember. A quick pry reveals a hidden recess beneath it, containing a small but heavy gold pouch. The only way out is north to the hallway.",
        'exits': {'north': 'hallway'},
        'items': ['gold pouch']
    },
    'escape_point': {
        'description': "You've reached the edge of the estate, a rusted iron gate almost completely swallowed by overgrown ivy. This is the forgotten entrance from the map. The air is cool and smells of the wild forest and freedom that lies just beyond the creaking bars. This is your chance. You're at the estate edge. Do you have everything you need to leave this life behind? You can go back into the hallway if you're not ready.",
        'exits': {'back': 'hallway'},
        'items': []
    }
}


def display_room():
    #A display
    room = rooms[current_room]
    print(f"\n--- {current_room.replace('_', ' ').upper()} ---") # make it pretty by replacing underscore with spaces
    print(room['description'])

    display_items = []
    for item in room['items']:
        if item == 'sturdy horse' and 'stable key' not in inventory:
            pass
        else:
            display_items.append(item)

    if display_items:
        print(f"You see: {', '.join(display_items)}.")

    exits = list(room['exits'].keys())
    if exits:
        print(f"Exits: {', '.join(exits)}.")
    print(f"Inventory: {', '.join(inventory) if inventory else 'None'}")

def handle_command(command):
    global current_room, game_over
    #make it visable thorugh the entire program
    if game_over:
        print("Game over. Restart to play.")
        return

    room = rooms[current_room]
    lower_command = command.lower().strip() #strip does the white space removeal and needed lower to account for many responses

    if lower_command.startswith('go '):
        direction = lower_command[3:]
        if direction in room['exits']:
            current_room = room['exits'][direction] #this is what allows the intervhanging between rooms
            display_room()
        else:
            print("Can't go there.")
    elif lower_command.startswith('take '):
        item_to_take = lower_command[5:]
        if item_to_take in room['items']:
            if item_to_take == 'sturdy horse':
                if 'stable key' in inventory:
                    inventory.append(item_to_take)
                    room['items'].remove(item_to_take)
                    required_items[item_to_take] = True
                    print(f"You take the {item_to_take}.")
                else:
                    print("Stable is locked. Need key.")
            else:
                inventory.append(item_to_take)
                room['items'].remove(item_to_take)
                if item_to_take in required_items:
                    required_items[item_to_take] = True
                print(f"You take the {item_to_take}.")
        else:
            print("No such item here.")
    elif lower_command == 'look':
        display_room()
    
    elif lower_command in ['inventory', 'i']:
        print(f"Your inventory: {', '.join(inventory) if inventory else 'empty'}.")
    elif lower_command == 'escape':
        if current_room == 'escape_point':
            check_escape_condition()
        else:
            print("Can only escape from escape point.")
    else:
        print("Unknown command. Try 'go [direction]', 'take [item]', 'look', 'inventory', 'escape'.")

def check_escape_condition():
    #Checks if all items are collected.
    global game_over
    if all(required_items.values()):
        print("\nYou escaped! Freedom!")
        game_over = True
        print("\nCongratulations! You escaped!")
    else:
        print("\nMissing items for escape:")
        for item, collected in required_items.items():
            if not collected:
                print(f"- {item}")
        print("Go back and find them.")

def main():
    #the geral looping and the starting point
    print("Welcome to The Villainess's Escape!")
    print("Escape this cage. Good luck.")
    display_room()

    while not game_over:
        command = input("\nWhat do you do? ").strip()
        handle_command(command)

if __name__ == "__main__":
    main()
