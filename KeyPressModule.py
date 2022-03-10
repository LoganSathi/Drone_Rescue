import pygame


def init():
    pygame.init()  # Initialize pygame
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False  # Default ans is false when  key is not pressed
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()  # Get pressed key
    myKey = getattr(pygame, 'K_{}'.format(keyName))  # Set format for key name
    print('K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()  # Update pygame screen
    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key Pressed")


if __name__ == '__main__':
    init()
    while True:
        main()
