from player_input import player_choose_fighter
from computer_options import get_computer_fighter, get_computer_opponent
from determine_winner import get_winner
from announce import *


def run_game(max_win=3):
    """
    This function is used to run the game
    :param max_win: the number of wins required to win the game
    """
    # Initialize variables
    player_score = 0
    computer_score = 0
    round_counter = 1

    opponent = get_computer_opponent()
    announce_opponent(opponent)
    announce_opponent_made_choice(opponent)

    # Run the game
    while player_score != max_win and computer_score != max_win:
        if round_counter >= 2:
            print(f'~ ROUND {round_counter} ~\n Player score: {player_score}\n {opponent} score: {computer_score}')

        announce_player_input()
        player_fighter = player_choose_fighter()
        computer_fighter = get_computer_fighter(opponent, player_fighter)

        winner = get_winner(player_fighter, computer_fighter)
        if winner == 'player_win':
            player_score += 1
        elif winner == 'computer_win':
            computer_score += 1

        announce_round_winner(opponent, player_fighter, computer_fighter, winner)
        round_counter += 1

    announce_game_winner(opponent, player_score, computer_score, max_win)


run_game()
