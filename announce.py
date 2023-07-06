from time import sleep

fighter_list = {
    1: 'Rock',
    2: 'Paper',
    3: 'Scissors',
    4: 'Spock',
    5: 'Lizard'
}

delay_before_displaying = 0.5


def announce_opponent(opponent):
    """
    This function is used to announce the opponent selected by the computer
    :param opponent: the opponent selected by the computer
    """
    print(f"Your opponent is: {opponent}")


def announce_opponent_made_choice(opponent):
    """
    This function is used to announce that the opponent has made a choice
    :param opponent: the opponent selected by the computer
    """
    sleep(delay_before_displaying)
    print(f'{opponent} made a choice...\n')
    print('________________________________')
    sleep(delay_before_displaying)


def announce_player_input():
    """
    This function is used to announce the player's choice
    """
    print('Choose your fighter (ง •̀_•́)ง')
    for key, value in fighter_list.items():
        print(key, ':', value)


def announce_round_winner(opponent, player_fighter, computer_fighter, winner):
    """
    This function is used to announce the winner of the round
    :param opponent:  the opponent selected by the computer
    :param player_fighter: the fighter chosen by the player.
    :param computer_fighter: the fighter chosen by the computer.
    :param winner: the winner of the round.
    """
    countdown = 3
    print()

    while countdown > 0:
        print(f'({countdown})')
        sleep(delay_before_displaying)
        countdown -= 1

    if winner == 'draw':
        announce = 'Draw'

    elif winner == 'player_win':
        announce = 'Player WON!'

    else:
        announce = f'{opponent} WON!'

    print(f'{opponent} chose:   {computer_fighter}\nThe player chose: {player_fighter} ')
    sleep(delay_before_displaying)
    print(f'\n>>> {announce} <<<')
    print('________________________________')


def announce_game_winner(opponent, player_score, computer_score, max_win):
    """
    This function is used to announce the winner of the game
    :param opponent: the opponent selected by the computer
    :param player_score: how many points the player scored
    :param computer_score: how many points the computer scored
    :param max_win: maximum number of wins
    """
    if player_score == max_win:
        return print(f'\nPlayer won this game with a score: {player_score}:{computer_score}')
    if computer_score == max_win:
        return print(f'\n{opponent} won this game with a score: {computer_score}:{player_score}')
