"""
Mini-max Tic-Tac-Toe Player
"""
import sys
import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
# import codeskulptor
# codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

INF = sys.maxint

def non_neg_score(actual_score, player):
    """
    Turns a score for a player into a 1 if it's a winning move
    (useful for comparison)
    """
    return SCORES[player] * actual_score

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    best_score = -INF
    best_move = (-1, -1)
    for row, col in board.get_empty_squares():
        score = -INF
        board_copy = board.clone()
        board_copy.move(row, col, player)
        if board_copy.check_win() is None:
            score, _ = mm_move(board_copy, provided.switch_player(player))
        else:
            score = SCORES[board_copy.check_win()]

        if score == SCORES[player]:
            # we have a board where player can win, so move their
            return score, (row, col)

        if non_neg_score(score, player) > best_score:
            best_score = non_neg_score(score, player)
            best_move = (row, col)

    # convert score back before returning
    return SCORES[player] * best_score, best_move 

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
