from flask import Flask, request, render_template

app = Flask(__name__)

# Game begins
current_room = 'bedroom'
inventory = []
game_over = False




required_items = {
    'gold pouch': False,
    'travel cloak': False,
    'stable key': False,
    'sturdy horse': False,
    'map of the estate': False
}

#added the images to the dictionaru
rooms = {
    'bedroom': {
        'description': "You are in your opulent bedroom, though it has felt more like a gilded cage for weeks. Moonlight streams through the tall, barred window, glinting off the silk sheets and velvet furniture that feel cold and mocking. The air is still and suffocating. A heavy, dark travel cloak hangs in an otherwise empty armoire, a stark contrast to the finery—a promise of a different life. The only exit is south, back into the heart of the house.",
        'exits': {'south': 'hallway'},
        'items': ['travel cloak'],
        'image': "https://i.pinimg.com/1200x/78/d7/1f/78d71f7471ed0c39784c033bf7f5a3cb.jpg"
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
        'items': [],
        'image': "https://i.pinimg.com/1200x/76/2e/f7/762ef7febeaf6cd6277b0605a0fdad8d.jpg"
    },
    'study': {
        'description': "You've slipped into the old study, a room thick with the scent of dust and aging paper. Leather-bound books sag on forgotten shelves, and a thin layer of grime covers every surface. A single candle flickers on the cluttered desk, casting long, dancing shadows. Partially hidden beneath a heavy tome, you see a rolled-up map of the estate. The only way out is west into the hallway.",
        'exits': {'west': 'hallway'},
        'items': ['map of the estate'],
        'image': "https://i.pinimg.com/736x/14/5d/a7/145da7bb3c468617adb8f4313040b86b.jpg"
    },
    'stables': {
        'description':  "The earthy smell of hay and leather fills the air, a welcome relief from the stuffiness of the manor. Moonlight filters through the wooden slats of the walls, illuminating the gentle, shifting forms of the horses in their stalls. Your favorite, a sturdy horse known for his stamina, is here, but his stall is securely locked. By the door, hanging on a rusty nail, is a simple iron stable key, an arrogant oversight by your captors. To take the sturdy horse, you must take the key The path east leads back to the hallway.",
        'exits': {'east': 'hallway'},
        'items': ['stable key', 'sturdy horse'],
        'image': "https://i.pinimg.com/1200x/47/9b/a5/479ba5da13667d4fd603cd1bdfd642ae.jpg"
    },
    'hidden_shed': {
        'description': "You're inside a small, dilapidated shed at the edge of the gardens, a place you haven't visited since childhood. The air smells of damp earth and rotting wood, and spiderwebs cling to old gardening tools. You notice one of the floorboards near the back wall is slightly loose, just as you remember. A quick pry reveals a hidden recess beneath it, containing a small but heavy gold pouch. The only way out is north to the hallway.",
        'exits': {'north': 'hallway'},
        'items': ['gold pouch'],
        'image': "https://i.pinimg.com/736x/4b/f3/94/4bf394dc66d02dbb7916116c29645b99.jpg"
    },
    'escape_point': {
        'description':  "You've reached the edge of the estate, a rusted iron gate almost completely swallowed by overgrown ivy. This is the forgotten entrance from the map. The air is cool and smells of the wild forest and freedom that lies just beyond the creaking bars. This is your chance. You're at the estate edge. Do you have everything you need to leave this life behind? You can go back into the hallway if you're not ready.",
        'exits': {'back': 'hallway'},
        'items': [],
        'image': "https://i.pinimg.com/1200x/87/60/93/8760937d131318b3fb6163484e255bdc.jpg"
    }
}

@app.route("/", methods=["GET", "POST"])
def game():
    #using global 
    global current_room, inventory, game_over

    message = ""
    if request.method == "POST":
        command = request.form.get("command", "").strip().lower()
        room = rooms[current_room]

        if game_over:
            message = "Game over. Refresh to play again."
        elif command.startswith('go '):
            direction = command[3:]
            if direction in room['exits']:
                current_room = room['exits'][direction]
            else:
                message = "Can't go that way."
                #new funtion type startswith
        elif command.startswith('take '):
            item = command[5:]
            if item in room['items']:
                if item == 'sturdy horse' and 'stable key' not in inventory:
                    message = "The horse stall is locked. You need the key."
                else:
                    inventory.append(item)
                    room['items'].remove(item)
                    if item in required_items:
                        required_items[item] = True
                    message = f"You took the {item}."
            else:
                message = "No such item here."
        elif command == 'look':
            pass  
        elif command in ['inventory', 'i']:
            message = f"Inventory: {', '.join(inventory) if inventory else 'empty'}"
        elif command == 'escape':
            if current_room == 'escape_point':
                if all(required_items.values()):
                    game_over = True
                    message = "You escaped! Congratulations!"
                else:
                    missing = [item for item, found in required_items.items() if not found]
                    message = "You're missing: " + ", ".join(missing)
            else:
                message = "You can't escape from here."
        else:
            message = "Unknown command."

    room = rooms[current_room]
    visible_items = [i for i in room['items'] if not (i == 'sturdy horse' and 'stable key' not in inventory)]
  #Gemnini assisted 
    return render_template('index.html',
         room_name=current_room.replace("_", " ").title(),
        description=room['description'],
        items=visible_items,
        exits=room['exits'].keys(),  # the key function retrieves all the keys
        inventory=inventory,
        image_url=room['image'],
        message=message
                           

    )


if __name__ == "__main__":
    app.run(debug=True)

