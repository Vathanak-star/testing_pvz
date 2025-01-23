import pygame
import random

# Initialize Pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plants vs Zombies")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define classes for Plant, Zombie, and Bullet
class Plant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = GREEN

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def shoot(self):
        return Bullet(self.x + self.width, self.y + self.height // 2)

class Zombie:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = RED
        self.speed = 1

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.color = (255, 255, 0)
        self.speed = 5

    def move(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Main game loop
def main():
    plants = []
    zombies = []
    bullets = []
    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Add a new plant where the mouse clicked
                x, y = pygame.mouse.get_pos()
                plants.append(Plant(x, y))

        # Update game logic
        for plant in plants:
            plant.draw(screen)

        # Create and move zombies
        if random.randint(0, 50) == 0:  # Random chance of spawning zombies
            zombies.append(Zombie(WIDTH, random.randint(50, HEIGHT - 50)))
        
        for zombie in zombies:
            zombie.move()
            zombie.draw(screen)

        # Create and move bullets
        for plant in plants:
            bullets.append(plant.shoot())

        for bullet in bullets:
            bullet.move()
            bullet.draw(screen)

        # Collision detection
        for zombie in zombies:
            for bullet in bullets:
                if zombie.x < bullet.x < zombie.x + zombie.width and zombie.y < bullet.y < zombie.y + zombie.height:
                    zombies.remove(zombie)  # Zombie is destroyed
                    bullets.remove(bullet)  # Bullet is destroyed
                    break

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
