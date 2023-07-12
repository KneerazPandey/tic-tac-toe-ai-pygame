import random
import copy


class AI:
    def __init__(self, level=1, player=2):
        self.level = level
        self.player = player 

    def mark_random(self, board):
        empty_board = board.get_empty_board()
        index = random.randrange(0, len(empty_board))
        return empty_board[index]
    
    def minimax(self, board, maximizing):
        # base case 
        case = board.final_state()
        
        # player 1 wins
        if case == 1:
            return 1, None
        
        # player 2 wins
        if case == 2:
            return -1, None
        
        # game is draw
        elif board.is_board_full():
            return 0, None
        
        # start of actual minimax algorithm
        if maximizing:
            max_eval = -100
            best_move = None 
            empty_board = board.get_empty_board()
            
            for (row, col) in empty_board:
                temp_board = copy.deepcopy(board)
                temp_board.mark_board(row, col, 1)
                eval = self.minimax(temp_board, False)[0]
                
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)
            return max_eval, best_move 
        
        if not maximizing:
            min_eval = 100
            best_move = None 
            empty_board = board.get_empty_board()
            
            for (row, col) in empty_board:
                temp_board = copy.deepcopy(board)
                temp_board.mark_board(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = (row, col)
            return min_eval, best_move 
    
    def evaluation(self, main_board):
        if self.level == 0:
            # random choice 
            move = self.mark_random(main_board)
            print(f'AI have choosen the random choice at position {move}')
            return move 
        else:
            # minimax algorithm
            eval, move = self.minimax(main_board, False)
            print(f'AI has choosen to mark the square in pos {move} with an eval of: {eval}')
            return move
     
        
        