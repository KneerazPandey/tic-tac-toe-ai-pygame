import pygame
from constants import *
from board import Board
from ai import AI


class Game:
    def __init__(self, window):
        self.window = window
        self.board = Board()
        self.player = 1
        self.running = True 
        self.ai = AI()
        self.draw_grids()
        self.show_menus()
        
    def show_menus(self):
        print('please enter r to restart the game')
    
    def draw_grids(self):
        # Setting the background color of the game
        self.window.fill(BACKGROUND_COLOR)
        
        for index in range(1, COLS):
            # drawing horizontal line
            pygame.draw.line(self.window, LINE_COLOR, (0, index * 200), (WIDTH, index * 200) ,LINE_WIDTH)

            # drawing vertical line
            pygame.draw.line(self.window, LINE_COLOR, (index * 200, 0), (index * 200, HEIGHT) ,LINE_WIDTH)
            
    def change_player_turn(self):
        self.player = 2 if self.player == 1 else 1
        
    def draw_player_figure(self, row, col):
        if self.player == 1:
            # drawing X for player 1
            start_first = (col * GRID_SIZE + OFFSET, row * GRID_SIZE + OFFSET)
            end_first = (col * GRID_SIZE + GRID_SIZE - OFFSET, row * GRID_SIZE + GRID_SIZE - OFFSET)
            pygame.draw.line(self.window, PLAYER_X_COLOR, start_first, end_first, X_WIDTH) 
            
            start_second = (col * GRID_SIZE + GRID_SIZE - OFFSET , row * GRID_SIZE + OFFSET)
            end_second = (col * GRID_SIZE + OFFSET, row * GRID_SIZE + GRID_SIZE - OFFSET)
            pygame.draw.line(self.window, PLAYER_X_COLOR, start_second, end_second, X_WIDTH) 
              
        elif self.player == 2:
            # drawing O for player 2
            center = (col * GRID_SIZE + GRID_SIZE // 2, row * GRID_SIZE + GRID_SIZE // 2)
            pygame.draw.circle(self.window, PLAYER_O_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)  
            
    def is_over(self):
        return self.board.final_state(show=True, window=self.window) != 0 or self.board.is_board_full()
    