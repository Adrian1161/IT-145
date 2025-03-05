# Adrian Estrada
rooms = {
    'Mount Olympus': {'South': 'Ares Peak', 'East': 'Athena\'s Room', 'Item': 'None'},
    'Ares Peak': {'South': 'Poseidon\'s Lake', 'East': 'Hera\'s Room', 'West': 'Hestia\'s Room', 'North': 'Mount Olympus','Item': 'Ares Blessing'},
    'Poseidon\'s Lake': {'South': 'Hades Portal', 'East': 'Apollo\'s View', 'North': 'Ares Peak', 'Item': 'Trident'},
    'Hades Portal': {'North': 'Poseidon\'s Lake', 'Item': 'Hades Army'},
    'Apollo\'s View': {'West': 'Poseidon\'s Lake', 'Item': 'Apollos Bow'},
    'Hera\'s Room': {'West': 'Ares Peak', 'Item': 'Scepter', },
    'Hestia\'s Room': {'East': 'Ares Peak', 'Item': 'Sacred Flame'},
    'Athena\'s Room': {'West': 'Mount Olympus', 'North': 'Throne Room', 'Item': 'Shield'},
    'Throne Room': {'Item': 'Zeus'},
}
state = 'Mount Olympus'


def get_new_state(state, direction):
    new_state = state
    for i in rooms:
        if i == state:
            if direction in rooms[i]:
                new_state = rooms[i][direction]
    return new_state


def get_item(state):
    return rooms[state]['Item']


def show_instructions():
    print('Find 7 items to defeat zeus.')
    print('Move commands: go South, go North, go East, go West')
    print("Add to Inventory: get 'item_name'")


show_instructions()
Inventory = []
items = ['Ares Blessing','Trident','Hades Army', 'Apollos View', 'Scepter', 'Scared Flame', 'Shield']
while (1):
    print('You are in ', state)
    print('Inventory:', Inventory)
    item = get_item(state)
    print('You see a ', item)
    print('--------------------')
    if item == 'Zeus':
        print('Zeus flung a bolt of lightning')
        exit(0)
    direction = input('Enter your move: ')
    if direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South':
        direction = direction[3:]
        new_state = get_new_state(state, direction)
        if new_state == state:
            print('There is not path there')
        else:
            state = new_state
    elif direction == str('get ' + item):
        if item in Inventory:
            print('You are carrying this')
        else:
            Inventory.append(item)
    else:
        print('Invalid input or move or item')
    if len(Inventory) == 7:
        print('Zeus I will defeat you right here')
        print('I will show you the might of the gods')
        print('You defeated Zeus and became the new ruler of the Gods')
        exit(0)