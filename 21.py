# Blackjack - 21
# Author - Coder: github.com/koray-killi
# Created for examine and study.
# Date : 25.01.2025 - 27.01.2025

# built-in functions #
import random as rd
def c_print(text,color): # For more readabi
    colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
    "reset": "\033[0m"
}
    return print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}")
def import_balance():
    try:
        with open("balan.ce","r") as balance_file:
            balance = int(balance_file.read())
        return balance
    except Exception:
        c_print("ERROR: No balan.ce found, giving default credit (1000).","red")
        return 1000

# Game classes which has class-groupped essential functions
class Deck:
    def randdeck(): # random index generator
        return rd.randint(1,52)-1
    def create_deck(): # it returns a list of whole deck
        deck = list()
        symbols = ["Spades","Clubs","Hearts","Diamonds"]
        values = ["A"] + list(range(2,11)) +["King","Queen","Jester"]
        deck = []
        for i in symbols:
            for j in values:
                deck.append([i,j])
        return deck
class Menu:
    def logout(): # exit function
        with open("balan.ce","w") as balance_file:
            balance_file.write(str(Vars.balance))
        return exit()
    def ui(): # main menu
        c_print("*"*50,"yellow")
        print("Your Balance: ",end="")
        c_print(Vars.balance,"blue")
        def reset():
            Vars.double = False
            Vars.bet = 0
            Vars.hand_value = 0
            Vars.dealer_value = 0
            Vars.hand = [Vars.deck[Deck.randdeck()],Vars.deck[Deck.randdeck()]]
            Vars.dealers_deck = [Vars.deck[Deck.randdeck()],Vars.deck[Deck.randdeck()]]
            return
        reset()
        print("1. Start Game\n2. Exit")
        dec = input("\033[97mSelection: \033[0m")
        if dec == "1":
            return main()
        elif dec == "2":
            return Menu.logout()
        else:
            return Menu.ui()
class Game:
    def won(bet_rate): # game won module
        if Vars.double == True:
            c_print(f"You got {Vars.hand_value}, You won {int(Vars.bet*bet_rate*2)} credits!","green")
            Vars.balance+=int(Vars.bet*bet_rate*2)
            return Menu.ui() 
        c_print(f"You got {Vars.hand_value}, You won {int(Vars.bet*bet_rate)} credits!","green")
        Vars.balance+=int(Vars.bet*bet_rate)
        return Menu.ui()
    def value_get(card,player): # It defines the behavior of dealer's cards values and returns any cards value
        if type(card) == int:
            return card
        elif card == "King" or card == "Queen" or card == "Jester":
            return 10
        else:
            if player == "dealer":
                if Vars.dealer_value+11>21:
                    return 1
                else:
                    return 11
            action = input("Please select the value of your A (1/11): ")
            while action != "1" and action != "11":
                c_print("ERROR: Wrong action, please try again.","red")
                action = input("Please select the value of your A (1/11): ")
            return int(action)

    def dealer_phase():
        c_print("*"*50,"red")
        if 21<Vars.hand_value:
            c_print(f"You Bust! You lose {Vars.bet} credits.","red")
            return Menu.ui()
        elif 21 == Vars.hand_value:
            Game.won(2)
        elif Vars.hand_value<21:
            c_print(f"Dealers hidden card is: '{Vars.dealers_deck[1][1]} of {Vars.dealers_deck[1][0]}'","cyan")
            if Vars.dealer_value<17:
                c_print("Value of dealer's cards is smaller than 17 so dealer draws a card.","magenta")
                new_card = Deck.randdeck()
                Vars.dealers_deck.append(Vars.deck[new_card])
                Vars.dealer_value+=Game.value_get(Vars.deck[new_card][1],"dealer")
                c_print(f"Dealer draws.\nDealers' new card is {Vars.deck[new_card][1]} of {Vars.deck[new_card][0]}[{Vars.dealer_value}]","cyan")
                return Game.hand_phase()
            else:
                if 21-Vars.hand_value>21-Vars.dealer_value:
                    c_print("Dealer is closer than you to 21! You bust!","red")
                    return(Menu.ui())
                elif 21-Vars.hand_value==21-Vars.dealer_value:
                    c_print("Dealer and you have same range to 21! It draws!","yellow")
                    Vars.balance+= Vars.bet
                    return Menu.ui()
                else:
                    Game.won(2)
                    return Menu.ui()
    def hand_phase():
        c_print("*"*50,"blue")
        if Vars.dealer_value > 21 and Vars.first_round>0:
            c_print("Dealer Bust!","green")
            Game.won(2)
        if Vars.hand_value > 21:
            c_print(f"You Bust! You lose {Vars.bet} credits.","red")
            return Menu.ui()       
        Vars.first_round+=1
        print("1. Draw another card.\n2. Double (Draw one card and stand)\n3. Stand")
        action = input("Choose your action: ")
        while action != "1" and action !="2" and action != "3":
            c_print("ERROR: Wrong action, please select an valid action.",'red')
            action = input("Choose your action: ")
        if action == "1":
            def hit():
                new_card = Deck.randdeck()
                Vars.hand.append(Vars.deck[new_card])
                Vars.hand_value+=Game.value_get(Vars.deck[new_card][1],"hand")
                c_print(f"\nYour new card is {Vars.deck[new_card][1]} of {Vars.deck[new_card][0]}[{Vars.hand_value}]","cyan")
                if Vars.hand_value == 21:
                    return 
                return Game.hand_phase()
            hit()
        elif action == "2":
            def double():
                Vars.double = True
                new_card = Deck.randdeck()
                Vars.hand.append(Vars.deck[new_card])
                print(f"Your new card is {Vars.deck[new_card][1]} of {Vars.deck[new_card][0]}")
                Vars.hand_value+=Game.value_get(Vars.deck[new_card][1],"hand")
                c_print("You stand after drawing one card!","yellow")
                return Game.dealer_phase()
            double()
        else:
            def stand():
                c_print("You stand with your own deck...","yellow")
                return Game.dealer_phase()
        return stand()
class Vars:
    double = False
    balance = import_balance()
    bet = int()
    first_round = 0
    hand_value = 0
    dealer_value = 0
    deck = Deck.create_deck()
    hand = [deck[Deck.randdeck()],deck[Deck.randdeck()]]
    dealers_deck = [deck[Deck.randdeck()],deck[Deck.randdeck()]]

# Main function -- for beginning of the game #
def main():
    bet_count = input("Please enter your bet count: ")
    try:
        bet_count = int(bet_count)
    except Exception:
        print("Unvalid bet.")
        return main()
    while bet_count > Vars.balance:
        print("Unvalid bet.")
        return main()
    Vars.bet = bet_count
    Vars.balance=Vars.balance-Vars.bet
    c_print(f"You bet {Vars.bet}.","blue")
    c_print("*"*50,"green")
    c_print("\t\tGame begins...", "magenta")
    c_print("*"*50,"green")
    c_print(f"Dealer draws '{Vars.dealers_deck[0][1]} of {Vars.dealers_deck[0][0]}' and 'one hidden card!'","cyan")
    c_print(f"You draws '{Vars.hand[0][1]} of {Vars.hand[0][0]}' and '{Vars.hand[1][1]} of {Vars.hand[1][0]}.'","cyan")
    # to get first phase value #
    for i in Vars.hand:
        valuable = i[1]
        if valuable == "King" or valuable == "Queen" or valuable == "Jester":
            Vars.hand_value+=10
        elif valuable == "A":
            action = input("What is the value of your A (1/11): ")
            while action != "1" and action !="11":
                c_print("ERROR: Wrong value. Please enter an valid value.")
                action = input("What is the value of your A (1/11): ")
            if action == "11":
                Vars.hand_value+=11
            else:
                Vars.hand_value +=1
        else:
            Vars.hand_value+=valuable
    for i in Vars.dealers_deck:
        valuable = i[1]
        if valuable == "King" or valuable == "Queen" or valuable == "Jester":
            Vars.dealer_value+=10
        elif valuable == "A":
            Vars.dealer_value+=11
        else:
            Vars.dealer_value+=valuable
    # to get first phase value ends #
    
    if Vars.hand_value == 21:
        Game.won(2.5)
    return Game.hand_phase()

# Start trigger
c_print(str("*"*50+"\nWelcome to Blackjack Python V1.0"),'yellow')
Menu.ui()