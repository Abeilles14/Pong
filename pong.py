import pygame

# game settings
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

COLOR_BLACK = 0, 0, 0
COLOR_GREEN = 166, 206, 57

TEXT_PADDING = 25
PADDLE_SPEED = 5
PADDLE_OFFSET = 10
BALL_SPEED = 3
SPIN_PERCENT = 0.5

# classes
class Vector2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return Vector2(self.x + other, self.y + other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)

    def set_zero(self):
        self.x = 0
        self.y = 0

class Actor:
    def __init__(self, texture):
        self.position = Vector2()
        self.velocity = Vector2()
        self.texture = texture

    def get_bounds(self):
        return pygame.Rect(round(self.position.x),
                           round(self.position.y),
                           self.texture.get_rect(). width,
                           self.texture.get_rect().height)

    def move(self, amount):
        self.position += amount

    def center_y(self):
        self.position.y = SCREEN_HEIGHT / 2 - self.texture.get_rect().height / 2

    def center_xy(self):
        self.position = Vector2(SCREEN_WIDTH / 2 - self.texture.get_rect().width / 2,
                                SCREEN_HEIGHT / 2 - self.texture.get_rect(). height / 2)

# functions
def update(elapsedTime):
    timeFactor = elapsedTime * 0.05
    ball.move(ball.velocity * timeFactor)

def draw():
    screen.fill(COLOR_BLACK)
    screen.blit(ball.texture, ball.get_bounds())
    pygame.display.flip()

# initialization
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# textures
ballTexture = pygame.image.load("chibi_willem.png")
playerTexture = pygame.image.load("chibi_isabelle.png")

# game objects
ball = Actor(ballTexture)
ball.velocity = Vector2(1, 2)

# loop control and timing
gameover = False

lastTick = pygame.time.get_ticks()
elapsedTime = 0

# gameloop
while not gameover:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            gameover = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            gameover = True

    # measure time since last event check
    elapsedTime = pygame.time.get_ticks() - lastTick
    lastTick = pygame.time.get_ticks()

    # alert how much drawings should be moved
    update(elapsedTime)
    draw()