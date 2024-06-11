inventory = []

def initialize_rooms():
    rooms = {
        'Entrance': {'north': 'Hallway', 'item': None},
        'Hallway': {'south': 'Entrance', 'east': 'Kitchen', 'west': 'Library', 'item': None},
        'Kitchen': {'west': 'Hallway', 'south': 'Treasure Room', 'item': 'Key'},
        'Library': {'east': 'Hallway', 'item': 'Book'},
        'Treasure Room': {'south': 'Kitchen', 'item': 'Treasure'}
    }
    return rooms

def move(current_room, direction, rooms):
    if direction in rooms[current_room]:
        return rooms[current_room][direction]
    else:
        print("There is no possible way!!")
        return current_room

def take_item(current_room, rooms):
    item = rooms[current_room]['item']
    if item is None:
        print("There is no item in the current room")
    else:
        inventory.append(item)
        rooms[current_room]['item'] = None
        print(f"Successfully added the {item} to inventory")

def use_item(item):
    item = item.capitalize()  # Ensure item case matches the items in the inventory
    if item in inventory:
        # Define specific actions for items here
        if item == 'Key':
            print("The key opens a secret door to the Treasure Room!")
            inventory.remove(item)
            print(f"You have used the item {item}")
        elif item == 'Book':
            print("The book contains a map with hints!")
            inventory.remove(item)
            print(f"You have used the item {item}")
        elif item == 'Treasure':
            print("Congratulations! You found the treasure and won the game!")
            return True
    else:
        print("You don't have that item.")
    return False

def game():
    rooms = initialize_rooms()
    current_room = 'Entrance'
    game_over = False
    
    print("Hey Mate, Welcome to the land of Adventure.")
    print(f"You are in the {current_room} room")
    
    while not game_over:
        print()
        choice = input("Enter the operation you want to perform <move/take/use/quit> : ").strip().lower()
        if choice == 'move':
            direction = input("Enter the direction <north/south/east/west> : ").strip().lower()
            current_room = move(current_room, direction, rooms)
            print(f"You are in the {current_room} room")
        elif choice == 'take':
            take_item(current_room, rooms)
        elif choice == 'use':
            item = input("Enter the item you want to use: ").strip().lower()
            game_over = use_item(item)
        elif choice == 'quit':
            print("Thank you, you are quitting...")
            break
        else:
            print("Invalid operation chosen")
    
    if game_over:
        print("Thank you for playing the game!")

if __name__ == "__main__":
    game()
