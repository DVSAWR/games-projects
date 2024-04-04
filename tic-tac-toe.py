import random

tile_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1, player2, score1, score2 = None, None, 0, 0
turn_count = 0
round_count = 1


def refresh_field():
    global tile_field
    global turn_count
    tile_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    turn_count = 0


def game_field():
    print('\n')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(tile_field[0], tile_field[1], tile_field[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(tile_field[3], tile_field[4], tile_field[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(tile_field[6], tile_field[7], tile_field[8]))
    print('\t     |     |')
    print("\n")


def player_turn(player):
    while True:
        print(f'ROUND: {round_count}')
        cur_choice = input(f"<{player}>, IT'S YOUR TURN. CHOOSE EMPTY TILE: ")
        if not cur_choice.isdigit():
            print('\t*Invalid input. You need choose 1 - 9 tile*')
            continue

        cur_choice = int(cur_choice)

        if cur_choice not in range(1, 10):
            print('\t*Invalid input. You need choose 1 - 9 tile*')
            continue

        if tile_field[cur_choice - 1] == 'x' or tile_field[cur_choice - 1] == 'o':
            print('\t*Invalid input. You need choose empty tile*')
            continue

        cur_choice -= 1
        return cur_choice


def comp_choice():
    while True:
        comp_ch = str(random.choice(tile_field))
        if comp_ch.isdigit():
            return comp_ch


def win_check():
    winfield = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in winfield:
        if tile_field[i[0]] == tile_field[i[1]] == tile_field[i[2]]:
            return tile_field[i[0]]

    return False


def next_round():
    while True:
        next_r = input('DO YOU WANT THE NEXT ROUND OF CURRENT GAME? [y/n]: ')
        if next_r == 'y':
            refresh_field()
            game_field()
            return True
        if next_r == 'n':
            refresh_all()
            return False
        else:
            print('\t*Invalid input.*')


def score_board():
    global player1
    global player2
    global score1
    global score2
    print('\t--------------------------------------\n'
          '\t            SCORE BOARD\n'
          '\t          <CROSSES ZEROES>\n'
          f'\t\t\n  <x> PLAYER <{player1}> SCORE: {score1}'
          f'\t\t\n  <o> PLAYER <{player2}> SCORE: {score2}\n'
          '\t--------------------------------------')


def refresh_all():
    global player1
    global player2
    global score1
    global score2
    global tile_field
    global turn_count
    global round_count
    player1, player2, score1, score2, turn_count, round_count = None, None, 0, 0, 0, 1
    tile_field = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def start_2players_game():
    global player1
    global player2
    global score1
    global score2
    global turn_count
    global round_count

    player1 = input('\nENTER <x> PLAYER NAME: ')
    player2 = input('ENTER <o> PLAYER NAME: ')

    game_field()

    while True:
        if turn_count % 2 == 0:
            cur_player_sign = 'x'
            cur_player = player1
        else:
            cur_player_sign = 'o'
            cur_player = player2
        turn_count += 1

        tile_field[player_turn(cur_player)] = cur_player_sign

        game_field()

        if win_check() == 'x':
            print(f'* AND THE WINNER IS <{cur_player}>! *')
            score1 += 1
            score_board()
            if next_round():
                round_count += 1
                continue
            break
        if win_check() == 'o':
            print(f'* AND THE WINNER IS <{cur_player}>! *')
            score2 += 1
            score_board()
            if next_round():
                round_count += 1
                continue
            break
        if turn_count == 9:
            print(f"* DRAW *")
            score_board()
            if next_round():
                round_count += 1
                continue
            break
        else:
            continue


def start_single_game():
    global player1
    global player2
    global score1
    global score2
    global turn_count
    global round_count

    player1 = input('\nENTER <x> PLAYER NAME: ')
    player2 = 'COMPLUCTER'

    game_field()

    while True:
        if turn_count % 2 == 0:
            cur_player_sign = 'x'
            cur_player = player1
            tile_field[player_turn(cur_player)] = cur_player_sign
        else:
            cur_player_sign = 'o'
            cur_player = player2
            x = int(comp_choice()) - 1
            tile_field[x] = cur_player_sign
            print(f'<{player2}> CHOSE TILE NUMBER {x + 1}')
        turn_count += 1

        game_field()

        if win_check() == 'x':
            print(f'* AND THE WINNER IS <{cur_player}>! *')
            score1 += 1
            score_board()
            if next_round():
                round_count += 1
                continue
            break

        if win_check() == 'o':
            print(f'* AND THE WINNER IS <{cur_player}>! *')
            score2 += 1
            print(f'<{cur_player}>: hehe')
            score_board()
            print('')
            if next_round():
                round_count += 1
                continue
            break

        if turn_count == 9:
            print(f"* DRAW *")
            score_board()
            if next_round():
                round_count += 1
                continue
            break

        else:
            continue


def game_mode_choice():
    refresh_all()

    while True:
        print('\n'
              '\t--------------------------------------------------\n'
              '\t                   WELLCOME TO\n'
              '\t                <CROSSES ZEROES>\n\n'
              '\t(tic tak toe cosmic adventure distraction edition)\n'
              '\t--------------------------------------------------')
        print('1 RULES OF THE GAME\n'
              '2 FOR SINGLE GAME WITH <COMPLUCTER>\n'
              '3 FOR PLAY 2 PLAYERS MODE\n'
              '4 FOR QUIT')

        game_mode = input('CHOOSE GAME MODE: ')

        if not game_mode.isdigit():
            print('\t*Invalid input.*')
            continue

        game_mode = int(game_mode)

        if game_mode not in range(1, 5):
            print('\t*Invalid input.*')
            continue

        if game_mode == 1:
            print("\n<CROSSES ZEROES> RULES"
                  "\n1. The game is played on a grid that's 3 tiles by 3 tiles."
                  "\n2. You are <x>, your friend is <o>, or vice versa. Players take turns putting their marks in empty tiles."
                  "\n3. The first player to get 3 of marks in a row (up, down, across, or diagonally) is the winner."
                  "\n4. When all 9 tiles are full, the game is over. If no player has 3 marks in a row, the game ends in a draw.")
            pause = input('\nPRESS ENTER TO BACK IN MAIN MENU: ')
            if pause == 'hehe':
                print(f'<COMPLUCTER>: hehe')
            continue

        if game_mode == 2:
            start_single_game()
        if game_mode == 3:
            start_2players_game()
        if game_mode == 4:
            print('\n')
            break


game_mode_choice()
