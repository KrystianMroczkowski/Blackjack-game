import random
import sys


def play():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    for card in range(0, 2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards[0]}, {user_cards[1]}")
    print(f"Computers cards: {computer_cards[0]}, ?")
    total_user = sum(user_cards)
    total_comp = sum(computer_cards)
    choose = input("What do you want to do? Hit 'h' or Stand 's': ")
    is_blackjack(total_comp, total_user)
    if choose == "s":
        if total_comp > 16:
            check(total_comp, total_user)
        else:
            while total_comp < 16:
                next_card = random.choice(cards)
                if next_card == 11 and total_comp + next_card > 21:
                    next_card = 1
                computer_cards.append(next_card)
                total_comp = sum(computer_cards)
            check(total_comp, total_user)
    elif choose == "h":
        while choose != "s":
            next_card = random.choice(cards)
            user_cards.append(next_card)
            total_user = sum(user_cards)
            if total_user > 21:
                print(f"You lose! Your final score: {total_user}, Computer final score: {total_comp}")
                play_again()
            else:
                choose = input(f"Your score: {total_user}, do you want to 'h' hit or 's' stand? ")
        if total_comp < 16:
            while total_comp < 16:
                next_card = random.choice(cards)
                if next_card == 11 and total_comp + next_card > 21:
                    next_card = 1
                computer_cards.append(next_card)
                total_comp = sum(computer_cards)
                print(f"Total comp: {total_comp}")

        check(total_comp, total_user)


def play_again():
    again = input("Do you want to play again? 'y' or 'n': ")
    if again == "y":
        play()
    elif again == "n":
        sys.exit("Thank you for playing, bye!")


def check(total_comp, total_user):
    if total_comp > total_user:
        print(f"You lose! Your final score: {total_user}, Computer final score: {total_comp}")
        play_again()
    elif total_comp == total_user:
        print(f"Draw! Your final score: {total_user}, Computer final score: {total_comp}")
        play_again()
    else:
        print(f"You win! Your final score: {total_user}, Computer final score: {total_comp}")
        play_again()


def is_blackjack(total_comp, total_user):
    if total_comp >= 21:
        print("You lose! Computer's got a blackjack!")
        play_again()
    elif total_user >= 21 and total_comp != 21:
        print("You win! You've got a blackjack")
        play_again()


play()