import sys, pygame


class Window:
    def __init__(self, size):
        self.ball = self.ball_init("intro_ball.gif", (30, 30))
        self.size = self.width, self.height = size
        self.screen = pygame.display.set_mode(size)
        self.ball_speed = [-2, -2]
        self.loop = True

    def ball_init(self, path, ball_size):
        self.ball = pygame.image.load(path)
        self.ball = pygame.transform.scale(self.ball, ball_size)
        self.ballrect = self.ball.get_rect()
        self.ballrect = self.ballrect.move((500, 400))
        return self.ball
