who_beats_whom = {
    'Rock': [
        'Scissors',
        'Lizard'
    ],
    'Paper': [
        'Rock',
        'Spock'
    ],
    'Scissors': [
        'Paper',
        'Lizard'
    ],
    'Spock': [
        'Scissors',
        'Rock'
    ],
    'Lizard': [
        'Paper',
        'Spock'
    ]
}


def get_winner(player_fighter, computer_fighter):
    """
    Returns the winner of the round.
    :param player_fighter: The fighter chosen by the player.
    :param computer_fighter: The fighter chosen by the computer.
    """
    if player_fighter == computer_fighter:
        return 'draw'

    elif computer_fighter in who_beats_whom.get(player_fighter):
        return 'player_win'

    return 'computer_win'
