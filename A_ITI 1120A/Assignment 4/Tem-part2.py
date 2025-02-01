import random


# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and
# the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two
# are the rank and the 3rd is a suit.

def wait_for_player():
    '''() -> None
    Pauses the program until the user presses enter
    '''
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''() -> list of str
       Returns a list of strings representing the playing deck,
       with one queen missing.
    '''
    deck = []
    suits = ['♠', '♡', '♢', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    deck.remove('Q♣')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str) -> None
       Shuffles the given list of strings representing the playing deck
    '''
    random.shuffle(deck)


# 这个函数从给定的牌堆中为两个玩家（庄家和玩家）发牌
def deal_cards(deck):
    '''(list of str) -> tuple of (list of str, list of str)

    返回两个列表，分别表示从给定的牌堆中发给两个玩家的牌。
    第一个列表代表庄家（即计算机）的牌，
    第二个列表代表另一个玩家（即用户）的牌。
    '''
    dealer = []
    other = []

    # 交替为庄家和玩家发牌
    for i in range(len(deck)):
        if i % 2 == 0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])

    print(f"[DEBUG] Dealer's initial deck: {dealer}")
    print(f"[DEBUG] Other player's initial deck: {other}")
    return (dealer, other)


# 这个函数移除给定牌堆中的所有对并返回一个不包含对的洗牌后的列表
def remove_pairs(l):
    '''
    (list of str) -> list of str

    返回列表 l 的副本，其中所有的对子都被移除，
    并且新列表中的元素被打乱顺序。

    前置条件：l 的元素是表示牌的字符串，如上所述
    '''
    no_pairs = []
    l.sort()  # 将列表排序以方便找到对子
    i = 0

    # 遍历列表并移除对子
    while i < len(l) - 1:
        if l[i][:-1] == l[i + 1][:-1]:  # 检查两个牌的等级是否相同（不考虑花色）
            print(f"[DEBUG] Removing pair: {l[i]}, {l[i + 1]}")
            i += 2  # 跳过下一个牌，因为它与当前牌组成对子
        else:
            no_pairs.append(l[i])
            i += 1

    # 如果最后还有一张未配对的牌，将它添加到列表中
    if i == len(l) - 1:
        no_pairs.append(l[i])

    random.shuffle(no_pairs)  # 移除对子后打乱列表顺序
    print(f"[DEBUG] Deck after removing pairs and shuffling: {no_pairs}")
    return no_pairs


# 这个函数以可读的格式打印牌堆
def print_deck(deck):
    '''
    (list) -> None
    打印给定的牌堆列表中的元素，以空格分隔
    '''
    print(" ".join(deck))  # 打印牌堆中的所有牌，以空格分隔


# 这个函数从用户获取有效的输入，输入值必须在给定的范围内
def get_valid_input(n):
    '''
    (int) -> int

    返回用户给定的一个在 1 到 n 之间的整数。
    如果用户输入的整数不在范围 [1, n] 内，则继续询问直到得到有效输入。

    前置条件：n >= 1
    '''
    while True:
        try:
            choice = int(input(f"Give me an integer between 1 and {n}: "))
            if 1 <= choice <= n:
                return choice
            else:
                print(f"Invalid number. Please enter an integer between 1 and {n}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# 这个函数实现了游戏的主要逻辑
def play_game():
    '''() -> None
    这个函数用于玩游戏'''

    deck = make_deck()  # 创建一副新的牌堆
    print(f"[DEBUG] Initial deck: {deck}")
    shuffle_deck(deck)  # 洗牌
    print(f"[DEBUG] Shuffled deck: {deck}")
    tmp = deal_cards(deck)  # 为庄家和玩家发牌

    dealer = tmp[0]
    human = tmp[1]

    # 初始游戏指令和玩家的牌堆展示
    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print_deck(human)
    print("Do not worry. I cannot see the order of your cards")

    # 庄家和玩家都先移除初始的对子
    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # 在庄家和玩家之间轮流进行游戏，直到其中一个的牌堆为空
    turn = 0  # 0 代表玩家，1 代表庄家
    while len(dealer) > 0 and len(human) > 0:
        if turn == 0:
            print("Your turn.")
            print("Your current deck of cards is:")
            print_deck(human)
            print(f"I have {len(dealer)} cards. If 1 stands for my first card and {len(dealer)} for my last card, which of my cards would you like?")
            choice = get_valid_input(len(dealer)) - 1  # 获取用户的有效输入
            chosen_card = dealer.pop(choice)  # 玩家从庄家那里抽一张牌
            human.append(chosen_card)  # 将抽到的牌加入玩家的牌堆
            print(f"You asked for my {choice + 1} card. Here it is. It is {chosen_card}")
            print(f"[DEBUG] Dealer's deck after player's turn: {dealer}")
            print(f"[DEBUG] Player's deck after adding card: {human}")
            human = remove_pairs(human)  # 将新加入的牌后的对子移除
            print(f"[DEBUG] Player's deck after removing pairs: {human}")
        else:
            print("My turn.")
            chosen_card_index = random.randint(0, len(human) - 1)  # 庄家随机从玩家那里抽一张牌
            chosen_card = human.pop(chosen_card_index)
            dealer.append(chosen_card)  # 将抽到的牌加入庄家的牌堆
            print(f"I took your {chosen_card_index + 1} card.")
            print(f"[DEBUG] Player's deck after dealer's turn: {human}")
            print(f"[DEBUG] Dealer's deck after adding card: {dealer}")
            dealer = remove_pairs(dealer)  # 将新加入的牌后的对子移除
            print(f"[DEBUG] Dealer's deck after removing pairs: {dealer}")

        wait_for_player()  # 等待用户按下回车键
        turn = 1 - turn  # 切换回合

    # 根据剩下的牌堆来确定赢家
    if len(human) == 0:
        print("Ups. You do not have any more cards. Congratulations! You, Human, win!")
    else:
        print("Ups. I do not have any more cards. You lost! I, Robot, win!")


# main
play_game()

# 每个函数的说明：
# 1. deal_cards(deck): 这个函数交替为庄家和玩家分发牌。它返回两个列表，一个用于庄家，一个用于玩家。
# 2. remove_pairs(l): 这个函数接受一个牌列表，移除所有对子，并返回一个移除对子后洗牌的新列表。
# 3. print_deck(deck): 这个函数以可读的格式打印牌堆，每张牌之间以空格分隔。
# 4. get_valid_input(n): 这个函数确保用户输入的值是 1 到 n 之间的整数。如果输入无效，函数会不断提示直到得到有效输入。
# 5. play_game(): 这个函数包含游戏的主要逻辑。它处理轮流抽牌、移除对子和确定赢家的过程。
