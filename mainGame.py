import pygame
import sys
import random

# Initialize Pygame
pygame.init()

def start_game():
    # Set up the screen
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Typing Game')

    # Read words from file generated by C++ program
    with open('C:\\Users\\dylan\\Desktop\\C++\\MyPyGame\\words.txt', 'r') as file:
        words = file.read().splitlines()

    # Dinosaur setup
    dino_height = 40
    dino_width = 20
    dino_x = 50
    dino_y = screen_height - dino_height
    dino = pygame.Rect(dino_x, dino_y, dino_width, dino_height)

    # Other game setup (fonts, speed, etc.)
    moving_words = []
    word_speed = 0.5
    font = pygame.font.SysFont(None, 36)
    score = 0
    score_font = pygame.font.SysFont(None, 48)

    def add_new_word():
        word = random.choice(words)
        word_x = random.randint(0, screen_width - 50)
        moving_words.append({'word': word, 'pos': [word_x, 0]})

    # Initial word
    add_new_word()

    # Game loop
    running = True
    current_typed = ""
    game_over = False
    words_to_remove = []
    
    while running:
        pygame.time.delay(15)  # Delay for slowing down the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:  # Restart the game
                        return
                else:
                    if event.key == pygame.K_BACKSPACE and len(current_typed) > 0:
                        current_typed = current_typed[:-1]
                    elif event.key == pygame.K_RETURN:
                        for mw in moving_words:
                            if current_typed.lower() == mw['word']:
                                words_to_remove.append(mw)
                                score += 1
                        current_typed = ""
                    elif event.unicode.isalpha():
                        current_typed += event.unicode

        if not game_over:
            # Only update game elements if the game is not over
            for word in words_to_remove:
                if word in moving_words:
                    moving_words.remove(word)
            words_to_remove.clear()

            for mw in moving_words:
                mw['pos'][1] += word_speed
                if mw['pos'][1] > dino_y and mw['pos'][0] < dino_x + dino_width:
                    game_over = True

            if random.randint(1, 100) > 98:
                add_new_word()

            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (0, 0, 0), dino)
            for mw in moving_words:
                word_surf = font.render(mw['word'], True, (0, 0, 0))
                screen.blit(word_surf, mw['pos'])

            score_surf = score_font.render(f'Score: {score}', True, (0, 0, 0))
            screen.blit(score_surf, (10, 10))

            typed_word_surf = font.render(current_typed, True, (0, 0, 0))
            screen.blit(typed_word_surf, (10, 50))

        # Check for game over and draw the game over screen
        if game_over:
            game_over_surf = score_font.render('Game Over! Press R to Restart', True, (255, 0, 0))
            screen.blit(game_over_surf, (screen_width // 4, screen_height // 2))

        pygame.display.flip()

# Start the game
while True:
    start_game()
