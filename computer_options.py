import random
from determine_winner import who_beats_whom


# The following dictionaries are used to determine the computer's chance choice of fighter and opponent
chance_pick_opponent_hashmap = {
    'Norman Reedus': 40,
    'Chris Rock': 30,
    'Leonard Nimoy': 20,
    'Loki Odinson': 10
}

drop_chance_hashmap = {
    'Norman Reedus': {
        'Rock': 20,
        'Paper': 20,
        'Scissors': 20,
        'Spock': 20,
        'Lizard': 20
    },
    'Chris Rock': {
        'Rock': 55,
        'Paper': 30,
        'Scissors': 5,
        'Spock': 5,
        'Lizard': 5
    },
    'Leonard Nimoy': {
        'Rock': 10,
        'Paper': 25,
        'Scissors': 10,
        'Spock': 30,
        'Lizard': 25
    }
}


def get_computer_opponent():
    """
    This function is used to get the computer's choice of opponent
    """
    # Calculate the chances of picking the opponent
    chance_pick_norman = 100 - chance_pick_opponent_hashmap.get('Norman Reedus')
    chance_pick_chris = chance_pick_norman - chance_pick_opponent_hashmap.get('Chris Rock')
    chance_pick_leonard = chance_pick_chris - chance_pick_opponent_hashmap.get('Leonard Nimoy')

    # Roll the dice to get the opponent
    roll_dice = random.randint(1, 100)
    if roll_dice >= chance_pick_norman:
        return 'Norman Reedus'
    elif roll_dice >= chance_pick_chris:
        return 'Chris Rock'
    elif roll_dice >= chance_pick_leonard:
        return 'Leonard Nimoy'
    else:
        return 'Loki Odinson'


def get_computer_fighter(opponent, player_fighter):
    """
    This function is used to get the computer's opponent choice of fighter
    :param opponent: the opponent selected by the computer
    :param player_fighter: the fighter chosen by the player.
    """

    # If opponent is Loki Odinson, then he will always win
    if opponent == 'Loki Odinson':
        loki_choice = ['Rock', 'Paper', 'Scissors', 'Spock', 'Lizard']
        loki_choice.remove(player_fighter)
        loki_choice.remove(who_beats_whom[player_fighter][0])
        loki_choice.remove(who_beats_whom[player_fighter][1])
        return loki_choice[random.randint(0, 1)]

    # Calculate the chances of picking the fighter
    drop_chance_opponent = drop_chance_hashmap.get(opponent)
    drop_chance_rock = 100 - drop_chance_opponent.get('Rock')
    drop_chance_paper = drop_chance_rock - drop_chance_opponent.get('Paper')
    drop_chance_scissors = drop_chance_paper - drop_chance_opponent.get('Scissors')
    drop_chance_spock = drop_chance_scissors - drop_chance_opponent.get('Spock')

    # Roll the dice to get the fighter
    roll_dice = random.randint(1, 100)
    if roll_dice >= drop_chance_rock:
        return 'Rock'
    elif roll_dice >= drop_chance_paper:
        return 'Paper'
    elif roll_dice >= drop_chance_scissors:
        return 'Scissors'
    elif roll_dice >= drop_chance_spock:
        return 'Spock'
    else:
        return 'Lizard'
