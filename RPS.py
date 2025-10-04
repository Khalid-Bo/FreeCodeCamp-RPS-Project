# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# Initialize global variables
my_history = []
prev_play = 'S'
opponent_list = [False] * 4
ideal_response = {'P': 'R', 'R': 'S', 'S': 'P'}
opponent_quincy_counter = -1
play_order = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}


def player(prev_opponent_play, opponent_history=[]):
    global my_history, prev_play, opponent_list, ideal_response, opponent_quincy_counter, play_order

    # Update histories
    opponent_history.append(prev_opponent_play)
    my_history.append(prev_play)

    # Check for Quincy strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['R', 'P', 'P', 'S', 'R']:
        opponent_list[0] = True

    # Reset opponent_list and opponent_history after 1000 plays
    if opponent_list[0]:
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()

        # Quincy's strategy moves
        opponent_quincy_list = ['P', 'S', 'S', 'R', 'P']
        opponent_quincy_counter = (opponent_quincy_counter + 1) % 5
        return opponent_quincy_list[opponent_quincy_counter]

    # Check for Abbey strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['P', 'P', 'R', 'R', 'R']:
        opponent_list[1] = True

    # Update play_order
    if opponent_list[1]:
        last_two = ''.join(my_history[-2:])
        if len(last_two) == 2:
            play_order[last_two] += 1

        # Determine the most frequent move in the last two plays
        potential_plays = [prev_play + 'R', prev_play + 'P', prev_play + 'S']
        sub_order = {k: play_order[k] for k in potential_plays if k in play_order}
        prediction = max(sub_order, key=sub_order.get)[-1:]

        # Reset opponent_list, opponent_history, and play_order after 1000 plays
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()
            play_order = {"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0}

        prev_play = ideal_response[prediction]
        return prev_play

    # Check for Kris strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['P', 'R', 'R', 'R', 'R']:
        opponent_list[2] = True

    if opponent_list[2]:
        # Reset opponent_list and opponent_history after 1000 plays
        if len(opponent_history) % 1000 == 0:
            opponent_list = [False] * 4
            opponent_history.clear()

        prev_play = ideal_response[prev_play]
        return prev_play

    # Check for Mrugesh strategy
    if len(set(opponent_list)) == 1 and opponent_history[-5:] == ['R', 'R', 'R', 'R', 'R']:
        opponent_list[3] = True

    if opponent_list[3]:
        # Reset opponent_list and opponent_history after 1000 plays
        if len(opponent_history) == 1000:
            opponent_list = [False] * 4
            opponent_history.clear()

        # Determine the most frequent move in the last ten plays
        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        prev_play = ideal_response[most_frequent]
        return prev_play

    prev_play = 'S'
    return prev_play
