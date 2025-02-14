import random
import pygame
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = pygame.font.Font(None, 48)
SMALL_FONT = pygame.font.Font(None, 36)

LEVELS = {
    'easy': ['cat', 'dog', 'fish', 'bird', 'tree'],
    'medium': ['python', 'hangman', 'coding', 'developer', 'puzzle'],
    'hard': ['challenge', 'algorithm', 'framework', 'application', 'complexity']
}

def choose_word(level):
    return random.choice(LEVELS[level])

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def draw_screen(screen, word, guessed_letters, attempts, message, hangman_stage):
    screen.fill(WHITE)
    text = FONT.render(display_word(word, guessed_letters), True, BLACK)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 3))
    attempts_text = SMALL_FONT.render(f'Attempts left: {attempts}', True, RED)
    screen.blit(attempts_text, (WIDTH // 2 - attempts_text.get_width() // 2, HEIGHT // 3 + 50))
    message_text = SMALL_FONT.render(message, True, BLACK)
    screen.blit(message_text, (WIDTH // 2 - message_text.get_width() // 2, HEIGHT // 3 + 100))
    draw_hangman(screen, hangman_stage)
    pygame.display.flip()

def draw_hangman(screen, stage):
    base_x, base_y = WIDTH // 4, HEIGHT // 2
    parts = [
        lambda: pygame.draw.line(screen, BLACK, (base_x, base_y), (base_x + 100, base_y), 5),
        lambda: pygame.draw.line(screen, BLACK, (base_x + 50, base_y), (base_x + 50, base_y - 150), 5),
        lambda: pygame.draw.line(screen, BLACK, (base_x + 50, base_y - 150), (base_x + 100, base_y - 150), 5),
        lambda: pygame.draw.circle(screen, BLACK, (base_x + 100, base_y - 130), 20, 5),
        lambda: pygame.draw.line(screen, BLACK, (base_x + 100, base_y - 110), (base_x + 100, base_y - 70), 5),
        lambda: pygame.draw.line(screen, BLACK, (base_x + 100, base_y - 100), (base_x + 80, base_y - 80), 5),
        lambda: pygame.draw.line(screen, BLACK, (base_x + 100, base_y - 100), (base_x + 120, base_y - 80), 5)
    ]
    for i in range(stage):
        parts[i]()

def hangman():
    level = ''
    while level not in LEVELS:
        level = input("Choose difficulty (easy, medium, hard): ").lower()
    
    word = choose_word(level)
    guessed_letters = set()
    attempts = 6 if level == 'easy' else 5 if level == 'medium' else 4
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Advanced Hangman Game")
    running = True
    message = "Guess a letter"
    hangman_stage = 0
    start_time = time.time()
    
    while running and attempts > 0:
        elapsed_time = int(time.time() - start_time)
        if elapsed_time > 60:
            message = "Time is up! Game Over!"
            draw_screen(screen, word, guessed_letters, attempts, message, hangman_stage)
            pygame.time.delay(2000)
            break
        draw_screen(screen, word, guessed_letters, attempts, message, hangman_stage)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    guess = event.unicode.lower()
                    if guess in guessed_letters:
                        message = "You already guessed that letter!"
                        continue
                    guessed_letters.add(guess)
                    if guess not in word:
                        attempts -= 1
                        hangman_stage += 1
                        message = f'Wrong guess! {attempts} attempts left'
                    else:
                        message = "Good guess!"
        
        if all(letter in guessed_letters for letter in word):
            message = f"Congratulations! You guessed the word: {word}"
            draw_screen(screen, word, guessed_letters, attempts, message, hangman_stage)
            pygame.time.delay(2000)
            break
    else:
        message = f"Game over! The word was: {word}"
        draw_screen(screen, word, guessed_letters, attempts, message, hangman_stage)
        pygame.time.delay(2000)
    
    pygame.quit()

if __name__ == "__main__":
    hangman()
