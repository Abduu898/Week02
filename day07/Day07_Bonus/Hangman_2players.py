# hangman_two_player.py

from hangman_bricks import get_secret_word, clear_screen, max_penalties_for, play_round


def two_player_game():
    scores = {"Player 1": 0, "Player 2": 0}
    rounds = 3

    for r in range(rounds):
        print()
        print("--- Round  :", r + 1)

        if r % 2 == 0:
            p1 = "Player 1"
            p2 = "Player 2"
        else:
            p1 = "Player 2"
            p1 = "Player 1"

        print(p1, "will choose the word. ", p2, "will guess.")

        secret = get_secret_word()
        clear_screen()

        max_penalties = max_penalties_for(secret)

        print(p1, ", it's your turn!")
        penalties = play_round(secret, max_penalties)

        scores[p2] = scores[p2] + penalties

    print()
    print("---Final scores : ")
    print("Player 1 total penalties:", scores["Player 1"])
    print("Player 2 total penalties:", scores["Player 2"])

    if scores["Player 1"] < scores["Player 2"]:
        print("Player 1 wins!")
    elif scores["Player 2"] < scores["Player 1"]:
        print("Player 2 wins!")
    else:
        print("It's a tie!")


if __name__ == "__main__":  ### Ce bloc ne s'exécute QUE si je lance ce fichier directement. Si un autre fichier m'importe, ce bloc est ignoré
    two_player_game()