import pygame


class InputHandler():

    def __init__(self, game, player1, player2):

        self.game = game
        self.player1 = player1
        self.player2 = player2

    def interpret(self, actions):  # pygame.event.get()
        for action in actions:

            # ____ Quit ________________________

            if event.type == pygame.QUIT:
                self.game.on = False

            # ____ Moves ________________________

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player1.moves.append("right")
                if event.key == pygame.K_UP:
                    player1.moves.append("up")
                if event.key == pygame.K_LEFT:
                    player1.moves.append("left")
                if event.key == pygame.K_DOWN:
                    player1.moves.append("down")
                # -------------------------
                if event.key == pygame.K_d:
                    player2.moves.append("right")
                if event.key == pygame.K_w:
                    player2.moves.append("up")
                if event.key == pygame.K_a:
                    player2.moves.append("left")
                if event.key == pygame.K_s:
                    player2.moves.append("down")

            # -------------------------

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player1.moves.remove("right")
                if event.key == pygame.K_UP:
                    player1.moves.remove("up")
                if event.key == pygame.K_LEFT:
                    player1.moves.remove("left")
                if event.key == pygame.K_DOWN:
                    player1.moves.remove("down")
                    # -------------------------
                if event.key == pygame.K_d:
                    player2.moves.remove("right")
                if event.key == pygame.K_w:
                    player2.moves.remove("up")
                if event.key == pygame.K_a:
                    player2.moves.remove("left")
                if event.key == pygame.K_s:
                    player2.moves.remove("down")
