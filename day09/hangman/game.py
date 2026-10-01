import pygame
import os
import sys
import random
from hangman import load_words
from hangman_bricks import max_penalties_for
pygame.init()

def count_unique_letters(word):
    unique = []
    for letter in word:
        if letter not in unique:
            unique.append(letter)
    return len(unique)

base_dir = os.path.dirname(os.path.abspath(__file__))#### _file_ is the current file patpath.abspath gets the absolute path
image_path = os.path.join(base_dir, "assets", "bg.jpg")
## screen setup
screen = pygame.display.set_mode((700, 600))
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (700, 600))

font = pygame.font.SysFont("Comic Sans MS", 40)
## random word and penalties setup
if len(sys.argv) < 2:
    print("Error: missing argument", file=sys.stderr)
    sys.exit(1)

words = load_words(sys.argv[1])
secret = random.choice(words)
max_penalties = max_penalties_for(secret)
guessed = []
penalties = 0
game_over = False
won = False
total_unique = count_unique_letters(secret)

def get_display_word(secret, guessed):
    display = ""
    for letter in secret:
        if letter in guessed:
            display = display + letter.upper() + " "
        else:
            display = display + "_ "
    return display.strip()

def draw_hangman(screen, penalties):
    black = (0, 0, 0)
    # Potence (toujours)
    pygame.draw.line(screen, black, (500, 500), (500, 100), 5)
    pygame.draw.line(screen, black, (500, 100), (400, 100), 5)
    pygame.draw.line(screen, black, (400, 100), (400, 150), 5)

    # 1. Tête
    if penalties >= 1:
        pygame.draw.circle(screen, black, (400, 180), 30, 5)
    # 2. Corps
    if penalties >= 2:
        pygame.draw.line(screen, black, (400, 210), (400, 320), 5)
    # 3. Bras gauche
    if penalties >= 3:
        pygame.draw.line(screen, black, (400, 240), (350, 290), 5)
    # 4. Bras droit
    if penalties >= 4:
        pygame.draw.line(screen, black, (400, 240), (450, 290), 5)
    # 5. Jambe gauche
    if penalties >= 5:
        pygame.draw.line(screen, black, (400, 320), (360, 400), 5)
    # 6. Jambe droite
    if penalties >= 6:
        pygame.draw.line(screen, black, (400, 320), (440, 400), 5)

    # 7. Œil gauche
    if penalties >= 7:
        pygame.draw.circle(screen, black, (390, 175), 3, 0)
    # 8. Œil droit
    if penalties >= 8:
        pygame.draw.circle(screen, black, (410, 175), 3, 0)
    # 9. Bouche
    if penalties >= 9:
        pygame.draw.line(screen, black, (390, 195), (410, 195), 3)
    # 10. Cheveux
    if penalties >= 10:
        pygame.draw.line(screen, black, (380, 155), (420, 155), 3)
    # 11. Corde (plus longue)
    if penalties >= 11:
        pygame.draw.line(screen, black, (400, 100), (400, 130), 5)
    # 12. Ombre au sol
    if penalties >= 12:
        pygame.draw.ellipse(screen, (100, 100, 100), (370, 500, 60, 10))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False
            if not game_over and pygame.K_a <= event.key <= pygame.K_z: ## to accept  keys from a to z
                letter = chr(event.key)
                if letter not in guessed:
                    guessed.append(letter)
                    if letter not in secret:
                        penalties = penalties + 1
            if game_over and event.key == pygame.K_r:
                secret = random.choice(words)
                max_penalties = max_penalties_for(secret)
                guessed = []
                penalties = 0
                game_over = False
                won = False
                total_unique = count_unique_letters(secret)

    if not game_over:
        all_found = True
        for letter in secret:
            if letter not in guessed:
                all_found = False
                break
        if all_found:
            game_over = True
            won = True
        elif penalties >= max_penalties:
            game_over = True
            won = False

    screen.blit(background, (0, 0))
    draw_hangman(screen, penalties)

    # Couleur du mot selon l'état
    if game_over:
        if won:
            word_color = (100, 255, 100) 
        else:
            word_color = (255, 100, 100)
    else:
        word_color = (255, 255, 255)

    # Affichage du mot 
    if game_over and not won:
        display = secret.upper()
    else:
        display = get_display_word(secret, guessed)

    word_text = font.render(display, True, word_color)
    word_rect = word_text.get_rect(center=(350, 470))
    screen.blit(word_text, word_rect)

    pen_text = font.render("Penalties: " + str(penalties) + "/" + str(max_penalties), True, (255, 255, 255))
    screen.blit(pen_text, (50, 50))

    # Compteur de lettres trouvées
    found = 0
    for letter in guessed:
        if letter in secret:
            found = found + 1
    counter_text = font.render("Found: " + str(found) + "/" + str(total_unique), True, (255, 255, 255))
    screen.blit(counter_text, (400, 50))

    if game_over:
        if won:
            msg = "You win! Press R."
        else:
            msg = "You lose! Press R."
        end_text = font.render(msg, True, (255, 100, 100))
        end_rect = end_text.get_rect(center=(350, 540))
        screen.blit(end_text, end_rect)
    
    
    pygame.display.update()

pygame.quit()