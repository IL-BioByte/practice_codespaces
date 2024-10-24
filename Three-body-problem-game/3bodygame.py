import random

#dictionary of all the game rooms and list the derection as well as interactions
rooms = {
    'simulation_control_room': {
        'description': 'You are in the Simulation Control Room. Here, you can adjust the parameters of the Trisolaran world simulation.',
        'north': 'climate_observation_deck',
        'east': 'star_calibration_chamber',
        'south': 'resource_management_center',
        'west': 'three_body_simulation_room',
        'interact': 'You see screens displaying real-time data of the Trisolaran climate and sun positions.',
    },
    'climate_observation_deck': {
        'description': 'You are on the Climate Observation Deck. The view is spectacular, with three suns illuminating the chaotic landscapes.',
        'south': 'simulation_control_room',
        'interact': 'You can observe the effects of changing sun positions on the Trisolaran landscape.',
    },
    'star_calibration_chamber': {
        'description': 'In the Star Calibration Chamber, you can manipulate the paths of the three suns to observe different climate scenarios.',
        'west': 'simulation_control_room',
        'interact': 'You can adjust the orbits of the suns. What would you like to change?',
    },
    'resource_management_center': {
        'description': 'You are in the Resource Management Center. Here, you can manage resources based on the climate predictions.',
        'north': 'simulation_control_room',
        'interact': 'You can allocate resources to different Trisolaran regions based on the current simulations.',
    },
    'three_body_simulation_room': {
        'description': 'You enter the Three-Body Simulation Room. Here, you can interact with the Trisolaran world and observe its unpredictable climate patterns.',
        'south': 'simulation_control_room',
        'interact': 'You see a simulation of three suns dancing around each other, causing chaos in the Trisolaran environment.',
    }
}


def display_room(room):
    print("=" * 120) #make the terminal output easier to read
    print(room['description'])
    print("Available directions: ", ', '.join(room.keys() - {'description', 'interact'}))
    print("=" * 120)

# Function to move to another room
def move_to_room(current_room, direction):
    if direction in current_room:
        return rooms[current_room[direction]]
    else:
        print("You can't go that way!")
        return current_room

# Function for room interaction with random outcome
def interact_with_room(current_room):
    if 'interact' in current_room:
        print(current_room['interact'])
    else:
        print("There's nothing to interact with here.")

# Function for room interaction with options for adjusting sun orbits
def interact_with_room(current_room):
    if 'interact' in current_room:
        if current_room == rooms['star_calibration_chamber']:
            print("You can adjust the orbits of the suns. What would you like to change?")
            print("1. Increase the orbit speed of Sun 1.")
            print("2. Decrease the orbit speed of Sun 2.")
            print("3. Change the distance of Sun 3.")
            choice = input("Enter the number of your choice: ").strip()
            if choice == '1':
                print("You increased the orbit speed of Sun 1. The simulations show a dramatic temperature rise!")
            elif choice == '2':
                print("You decreased the orbit speed of Sun 2. The environment stabilizes for now.")
            elif choice == '3':
                print("You changed the distance of Sun 3. It creates unpredictable gravitational effects!")
            else:
                print("Invalid choice. The suns remain as they are.")
            return  # Exit the function after handling this room's specific interaction
        else:
            outcomes = [
                "You observe an unexpected surge in solar activity!",
                "The simulation displays a catastrophic climate event!",
                "You notice a calm day in the Trisolaran world.",
                "A rare phenomenon occurs: the suns align perfectly!",
                "You receive a warning about a potential ice age!",
            ]
            outcome = random.choice(outcomes)
            print(outcome)
    else:
        print("There's nothing to interact with here.")


# game setup
current_room = rooms['simulation_control_room']  # Initialize current_room

# Main game loop
while True:
    display_room(current_room)
    command = input("Enter a command (or 'interact' to engage with the room): ").strip().lower()

    if command in ['north', 'south', 'east', 'west']:
        current_room = move_to_room(current_room, command)
    elif command == 'interact':
        interact_with_room(current_room)
    elif command == 'quit':
        print("Thanks for playing!")
        break
    else:
        print("Invalid command!")