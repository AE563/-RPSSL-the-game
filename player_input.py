from announce import fighter_list


def player_choose_fighter():
    """
    This function is used to get the player's choice
    """
    while True:
        list_check = [1, 2, 3, 4, 5]
        input_data = int(input('Enter the number:'))
        if input_data in list_check:
            return fighter_list[input_data]
        else:
            print('You entered the wrong number. Try enter 1')
