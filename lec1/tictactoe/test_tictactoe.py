from tictactoe import player, actions, result, winner, terminal, utility

X = "X"
O = "O"
EMPTY = None

board1 = [[EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

board2 = [[EMPTY, X, EMPTY],
          [O, X, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

board3 = [[EMPTY, X, EMPTY],
          [O, X, EMPTY],
          [O, X, EMPTY]]

board4 = [[X, O, X],
          [X, O, O],
          [O, X, X]]

def test_player():
    assert player(board1) == X
    assert player(board2) == O

def test_actions():
    assert actions(board2) == {(0,0), (0,2), (1,2), (2,0), (2,1), (2,2)}

def test_result():
    assert result(board2, (0,0)) == [[O, X, EMPTY],
                                     [O, X, EMPTY],
                                     [EMPTY, EMPTY, EMPTY]]
    
def test_winner():
    assert winner(board2) == None
    assert winner(board3) == X
    assert winner(board4) == None

def test_terminal():
    assert terminal(board2) == False
    assert terminal(board3) == True
    assert terminal(board4) == True

def test_utility():
    assert utility(board3) == 1
    assert utility(board4) == 0