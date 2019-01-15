#tic_tac_toe_ttt
import random
import poc_ttt_gui
import poc_ttt_provided as provided

NTRIALS = 15
SCORE_CURRENT = 1
SCORE_OTHER = 1


def mc_trial(board, player):
      while board.check_win() is None:
        all_empty_squares = board.get_empty_squares()
        random_squares = random.choice(all_empty_squares)
        board.move(random_squares[0], random_squares[1], player)
        player = provided.switch_player(player)




def mc_update_scores(scores, board, player):
    current_player = player
    another_player = provided.switch_player(player)
    winner_player = board.check_win()
    board_dimension = board.get_dim()

    for row in range(board_dimension):
        for col in range(board_dimension):
            if ((winner_player == current_player) and (current_player == board.square(row, col))):
                scores[row][col] = scores[row][col] + SCORE_CURRENT

            elif ((winner_player == current_player) and (another_player == board.square(row, col))):
                scores[row][col] = scores[row][col] - SCORE_OTHER

            elif ((winner_player == another_player) and (current_player == board.square(row, col))):
                scores[row][col] = scores[row][col] - SCORE_CURRENT

            elif ((winner_player == another_player) and (another_player == board.square(row, col))):
                scores[row][col] = scores[row][col] + SCORE_OTHER




def get_best_move(board, scores):

    board_dimension = board.get_dim()
    empty_square = provided.EMPTY

    best_possible_move = NTRIALS * (-NTRIALS)
    array_of_good_moves = []

    for row in range(board_dimension):
        for col in range(board_dimension):
            if ((scores[row][col] > best_possible_move) and (board.square(row, col) == empty_square)):
                best_possible_move = scores[row][col]
                array_of_good_moves = [(row, col)]

            elif ((scores[row][col] == best_possible_move) and (board.square(row, col) == empty_square)):
                array_of_good_moves.append((row, col))

    return random.choice(array_of_good_moves)




def mc_move(board, player, trials):

    board_dimension = board.get_dim()
    scores = [[0 for _ in range(board_dimension)]
              for _ in range(board_dimension)]

    for _ in range(trials):
        cloned_board = board.clone()
        mc_trial(cloned_board, player)
        mc_update_scores(scores, cloned_board, player)

    return get_best_move(board, scores)
provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
