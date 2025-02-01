# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random


def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)


#####################################

def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer = []
    other = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    length = len(deck)
    for i in range(length):
        if i % 2 == 0:
            dealer.append(deck[i]) #bot's
        else:
            other.append(deck[i]) #Mine
    
    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs = []

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    l.sort() #sorting
    l_length = len(l)
    i = 0 # counter
    while i < l_length - 1: # while loop
        if l[i][:-1] == l[i+1][:-1]:
            i += 2 # press two
        else:
            no_pairs.append(l[i])
            i += 1 # put it into and next one

    #last one if exist
    if i == l_length -1:
        no_pairs.append(l[i])

    # MY CODE ENDS HERE
    
    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    print(" ".join(deck))
    # MY CODE ENDS HERE


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    valid_input = False
    while not valid_input:
        choice = input(f"Give me an integer between 1 and {n}: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= n:
                valid_input = True
            else:
                print(f"Invalid number. Please enter an integer between 1 and {n}.")
    # MY CODE ENDS HERE
    return choice

def play_game():
    '''()->None
    This function plays the game'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE
    turn = 0 # 0 -> player, 1 -> bot
    while len(dealer) > 0 and len(human) > 0:
        if turn == 0: # my turn
            print("Your Ture.")
            print("Your current deck of cards is:")
            print_deck(human)
            print(f"I have {len(dealer)} cards. If 1 stands for my first card and {len(dealer)} for my last card, which of my cards would you like?")
            choice = get_valid_input(len(dealer)) - 1
            chosen_card = dealer.pop(choice) # remove the chosen card from dealer
            human.append(chosen_card) # plug it into my card
            print(f"You asked for my {choice + 1}{'st' if (choice + 1) == 1 else 'nd' if (choice + 1) == 2 else 'rd' if (choice + 1) == 3 else 'th'} card. Here it is. It is {chosen_card}")
            human = remove_pairs(human)

        else: # bot turn
            print("My Turn.")
            chosen_card_bot = random.randint(0, len(human) - 1)  # pick a card randomly
            chosen_card = human.pop(chosen_card_bot) # remove that card from human
            dealer.append(chosen_card)  # plug it into dealer's
            print(f"I took your {chosen_card_bot + 1}{'st' if (chosen_card_bot + 1) == 1 else 'nd' if (chosen_card_bot + 1) == 2 else 'rd' if (chosen_card_bot + 1) == 3 else 'th'} card.")
            dealer = remove_pairs(dealer)

        wait_for_player() # WAITTING
        turn = 1 - turn # switch

    if len(human) == 0:
        print("Ups. You do not have any more cards \n Congratulations! You, Human, win")
    else:
        print("Ups. I do not have any more cards \n You lost! I, Robot, win")
    # MY CODE ENDS HERE
# main
play_game()
