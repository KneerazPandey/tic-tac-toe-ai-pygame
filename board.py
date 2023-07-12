from constants import * 
import numpy as np
import pygame


class Board:
    def __init__(self):
        self.board = np.zeros((ROWS, COLS))
        self.marked_count = 0
        self.empty_board = self.board
        
    def mark_board(self, row, col, player):
        self.board[row][col] = player
        self.marked_count += 1
    
    def is_mark_available(self, row, col):
        return self.board[row][col] == 0 
    
    def is_board_full(self):
        return self.marked_count == 9
    
    def is_board_fully_empty(self):
        return self.marked_count == 0
    
    def get_empty_board(self):
        empty_board = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_mark_available(row, col):
                    empty_board.append((row, col))
        return empty_board
    
    def final_state(self, show=False, window=None):
        """_summary_
        return 0 if there is no win yet
        return 1 if player 1 wins
        return 2 if player 2 wins
        Returns:
            int: It can return three differnt value
        """
        # For vertical winss
        for col in range(COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != 0:
                if show:
                    color = PLAYER_X_COLOR if self.board[0][col] == 1 else PLAYER_O_COLOR
                    x_pos = (col * GRID_SIZE + GRID_SIZE // 2, 20)
                    y_pos = (col * GRID_SIZE + GRID_SIZE // 2, WIDTH - 20)
                    pygame.draw.line(window, color, x_pos, y_pos, LINE_WIDTH)
                return self.board[0][col]
        
        # For horizontal wins
        for row in range(ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != 0:
                if show:
                    color = PLAYER_X_COLOR if self.board[0][col] == 1 else PLAYER_O_COLOR
                    x_pos = (20, row * GRID_SIZE + GRID_SIZE // 2)
                    y_pos = (WIDTH - 20, row * GRID_SIZE + GRID_SIZE // 2)
                    pygame.draw.line(window, color, x_pos, y_pos, LINE_WIDTH)
                return self.board[row][0]
            
        # For diagonal wins
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            if show:
                color = PLAYER_X_COLOR if self.board[0][col] == 1 else PLAYER_O_COLOR
                x_pos = (20, 20)
                y_pos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(window, color, x_pos, y_pos, LINE_WIDTH)
            return self.board[0][0]
        
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != 0:
            if show:
                color = PLAYER_X_COLOR if self.board[0][col] == 1 else PLAYER_O_COLOR
                x_pos = (WIDTH - 20, 20)
                y_pos = (20, HEIGHT - 20)
                pygame.draw.line(window, color, x_pos, y_pos, LINE_WIDTH)
            return self.board[2][0]
        
        return 0