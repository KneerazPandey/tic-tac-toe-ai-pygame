import pygame 
import sys 
from constants import *
from game import Game 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe - Niraj Pandey')

clock = pygame.time.Clock()

def run() :
    game = Game(screen) 
    run = True 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key ==pygame.K_r:
                    print('\nGame is restarted sucessfully ............\n')
                    game = Game(screen)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // GRID_SIZE
                col = pos[0] // GRID_SIZE
                
                if game.board.is_mark_available(row, col) and game.running:
                    game.board.mark_board(row, col, game.player)
                    game.draw_player_figure(row, col)
                    game.change_player_turn()
                    pygame.display.update()
                    
                    if game.is_over():
                        game.running = False
                    
        if game.player == game.ai.player and game.running:
            row, col = game.ai.evaluation(game.board)
            game.board.mark_board(row, col, game.player)
            game.draw_player_figure(row, col)
            game.change_player_turn()
            
            if game.is_over():
                game.running = False
            
        pygame.display.update()
        clock.tick(FPS)
    

if __name__ == '__main__':
    run()
            

