import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroid_field = AsteroidField()
	Shot.containers = (shots, updatable, drawable)
	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		updatable.update(dt)	
		
		screen.fill("black")
		
		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game over!")
				sys.exit()

		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					shot.kill()
					asteroid.split()

		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
	
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
