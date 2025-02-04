import random as rd

def print_stats(player_deck, computer_deck, final):
    if final == False:
        print(f"Your cards: {player_deck}, current score: {calc_score(player_deck)}")
        print(f"Computer's first card: {computer_deck[0]}")
    else:
        print(f"Your final hand: {player_deck}, final score: {calc_score(player_deck)}")
        print(f"Computers final hand: {computer_deck}, final score: {calc_score(computer_deck)}")

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rd.choice(cards)

def calc_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    if (11 in deck) and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
    return sum(deck)    

def compare(player_score, computer_score):
    if computer_score == 0:
        return "Lose, opponent has blackjack."
    elif player_score == 0:
        return "You win with a black jack!"
    elif computer_score > 21:
        return "You win. Computer went over."
    elif player_score > 21:
        return "You went over, you lose."
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose."
        
def playgame():        
    computer_deck = []
    player_deck = []

    for i in range(2):
        computer_deck.append(deal_cards())
        player_deck.append(deal_cards())

    print_stats(player_deck, computer_deck, False)

    player_score = calc_score(player_deck)
    computer_score = calc_score(computer_deck)

    if player_score == 0 and computer_score == 0:
        print(compare(player_score, computer_score))

    players_choice = True

    while players_choice:
        
        hit = input("Type 'y' to get another card, type 'n' to pass: ")

        if hit == 'y':
            player_deck.append(deal_cards())
            player_score = calc_score(player_deck)
            print_stats(player_deck, computer_deck, False)
            if player_score > 21:
                players_choice = False

        else:
            players_choice = False

    while calc_score(computer_deck) < 17 and calc_score(computer_deck) != 0:
        computer_deck.append(deal_cards())
        computer_score = calc_score(computer_deck)

    print_stats(player_deck, computer_deck, True)
    print(compare(player_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    print("\n"*40)
    playgame()