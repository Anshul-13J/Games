import random
playing= True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    
    def __str__(self):
        return str(self.rank) + ' of '+ str(self.suit)
    
    
    
class Deck:
    '''
    It's a collection of all cards
    '''
    #To collect all cards in a list
    all_cards=[]
    def __init__(self):
        for suit in suits:
            for rank in ranks:
                Deck.all_cards.append(Card(suit,rank))
                
    #It does not return anything,just print the list           
    def __str__(self):
        st=''
        for card in self.all_cards:
            st=  st+ '\n' + str(card) 
        return 'The deck has: ' + st
    
    
    #It returns length of remaining deck
    def __len__(self):
        return len(Deck.all_cards)
            
    
    #It shuffles the deck
    def shuffle(self):
        random.shuffle(Deck.all_cards)
        
    #It pops one card from the deck and return the vaue of popped card
    def deal(self):
        return Deck.all_cards.pop()
        
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank=='Ace':
            self.aces +=1
        
    
    def adjust_for_ace(self):
        while self.value >21 and self.aces !=0:
            self.value -=10
            self.aces -=1
            
            

            
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet        
        
        
def take_bet(chips):
    while True:
        try:
            print('Available Balance: {}'.format(chips.total))
            chips.bet=int(input('Enter how many chips you want to bet: '))

        except TypeError:
            print('Try entering an integer value')

        else:
            if(chips.bet > chips.total):
                print('Amount exceeds total chips, try again!')
            else:
                break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck,hand):
  #  global playing  # to control an upcoming while loop
    
    while True:
        choice=input('You want to hit or stand? (h or s): ')
        if choice[0].lower()=='h':
            hit(deck,hand)
        elif choice[0].lower()=='s':
            print('Player stands, dealer is playing')
            playing=False
            
        else:
            print('Please try again')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
    
def player_busts(player,dealer,chips):
    print('PLAYER BUST')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print('PLAYER WINS')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER BUST')
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print('PLAYER BUST')
    chips.win._bet()
    
def push():
    print("Dealer and Player tie! it's a push")
        
