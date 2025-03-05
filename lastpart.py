rooms = {
    'Mount Olympus': {'name': 'Mount Olympus',
                      'South': 'Ares Peak', 'East': 'Athena\'s Room',
                      'text': 'You see many paths open up to you.'},
    'Ares Peak': {'name': 'Ares Peak',
                  'South': 'Poseidon\'s Lake', 'East': 'Hera\'s Room', 'West': 'Hestia\'s Room',
                  'North': 'Mount Olympus',
                  'text': 'You see Ares blessing.', },
    'Poseidon\'s Lake': {'South': 'Hades Portal', 'East': 'Apollo\'s View', 'North': 'Ares Peak'},
    'Hades Portal': {'North': 'Poseidon\'s Lake'},
    'Apollo\'s View': {'West': 'Poseidon\'s Lake'},
    'Hera\'s Room': {'West': 'Ares Peak'},
    'Hestia\'s Room': {'East': 'Ares Peak'},
    'Athena\'s Room': {'West': 'Mount Olympus', 'North': 'Throne Room'},
    'Throne Room': {},
}
items = {
    'Ares Peak': 'Ares Blessing',
    'Poseidon\'s lake': 'Trident',
    'Hades portal': 'Hades Army',
    'Apollo\'s View': 'Apollos View',
    'Hera\'s Room': 'Scepter',
    'Hestia\'s Room': 'Scared Flame',
    'Athena\'s Room': 'Shield',

}
directions = ['north', 'south', 'east', 'west']
inventory = []


def get_new_room (room,direction )
# if inventory = 7 lead to  a def to say you beat the boss

# make a pick up option


room = rooms['Mount Olympus']
text = rooms['Mount Olympus']['text']

inventory = []

while True:
    print('You have entered the', room)
    if room == 'Throne Room'
        print('Zeus I have come to defeat you')
        print('zeus: You will try')
