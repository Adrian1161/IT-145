rooms = {
    'Mount Olympus': {'South': 'Ares Peak', 'East': 'Athena\'s Room'},
    'Ares Peak': {'South': 'Poseidon\'s Lake', 'East': 'Hera\'s Room', 'West': 'Hestia\'s Room',
                  'North': 'Mount Olympus', 'item': 'Ares Blessing'},
    'Poseidon\'s Lake': {'South': 'Hades Portal', 'East': 'Apollo\'s View', 'North': 'Ares Peak', 'item': 'Trident'},
    'Hades Portal': {'North': 'Poseidon\'s Lake', 'item': 'Hades Army'},
    'Apollo\'s View': {'West': 'Poseidon\'s Lake', ' item': 'Apollos Bow'},
    'Hera\'s Room': {'West': 'Ares Peak', 'item': 'Scepter'},
    'Hestia\'s Room': {'East': 'Ares Peak', 'item': 'Scared Flame'},
    'Athena\'s Room': {'West': 'Mount Olympus', 'North': 'Throne Room', 'item': 'Shield'},
    'Throne Room': {'South': 'Athena\'s Room'}
}
texts = {
    'Mount Olympus': 'There is nothing for you here',
    'Ares Peak': 'You see Ares Blessing',
    'Poseidon\'s Lake': 'You see a Trident in the water',
    'Hades Portal': 'You see hades Army ready for a war',
    'Apollo\'s' 'View': 'You see Apollos Bow on the rock wall', 
    'Hera\'s Room': 'You see a Scepter inside of a chest',
    'Hestia\'s Room': 'You see a Sacred Flame chain hung up on a stand',
    'Athena\'s Room': 'You see Athena\'s Shield'

}


# if inventory = 7 lead to  a def to say you beat the boss
# make a pick up option



items = 'Ares Blessing', 'Trident', 'Hades Army', 'Sacred Flame', 'Apollos Bow', 'Scepter', 'Shield'

room = 'Mount Olympus'
text_item = 'Mount Olympus'
text = 'Mount Olympus'
inventory = []

print(
    'To beat zeus you must find Ares Blessing, a trident, Hades Army, Apollos Bow, a scepter, sacred flame, and a shield')

while True:
    print('you are in the', room)
    player_direction = input('Choose North, South, East, or West').capitalize()
    item_pickup = input()
    location = rooms[room]
    sent = texts[text]
    if room == 'Throne Room':
        if len(inventory) == 7:
            print('you are done')
            break
    elif player_direction in location:
        print('You are in the', location[player_direction])
        room = location[player_direction]

        print(inventory)
    elif player_direction == 'Exit':
        print('You gave up on your journey')
        break
    elif player_direction == 'I':
        print(inventory)
    elif player_direction == 'Get':
        if items in inventory:
            print('You have this already')
        else:
            print('You picked it up')
            inventory.append(items)

    else:
        print('There is no path')
