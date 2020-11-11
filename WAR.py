from random import shuffle

class Cards:
    suits=["spades","hearts","diamonds","clubs"]
    values=[None, None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    
    def __init__(self,v,s):
        self.suit= self.suits[s]
        self.value= self.values[v]
        
        
        
        
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
        
    def __repr__(self):
        return self.value + " of " + self.suit
       
    
class Deck:
    
    def __init__(self):
        self.cards=[]
        for i in range(4):
            for j in range (2,15):
                self.cards.append(Cards(j,i))
             
                
        shuffle(self.cards)
        # for card in self.cards:
        #    print(card)
        #print(len(self.cards))
        
        
    def rem_card(self):
        
        if len(self.cards)==0:
            return False
        
      #  shuffle(self.cards)
        return self.cards.pop()
    
    
class Player:
    
    def __init__(self,name):
        
        self.wins=0
        self.card= False
        self.name= name
        
        
        
class Game:
    
    def __init__(self):
        play1 = input("Enter 1st Player's name: ").capitalize()
        play2 = input("Enter 2nd Player's name: ").capitalize()
        self.p1 = Player(play1)
        self.p2 = Player(play2)
        self.deck = Deck()
        
        
        

        
        
        
    def win(self,winner):
        print(f"{winner} wins this round")
        
        
        
    def draw(self,p1n,p1c,p2n,p2c):
        print(f"\n{p1n} drew {p1c}")
        print(f"{p2n} drew {p2c}\n")
        
        
        
    def winner(self,p1,p2):
        
        print("\nSUMMARY:")
        print(p1.name + f" won {p1.wins} rounds")
        print(p2.name + f" won {p2.wins} rounds")
        if p1.wins > p2.wins:
            print(p1.name + " wins!")
            
        elif p2.wins > p1.wins:
            print(p2.name + " wins!")
        
        else:
            print("It's a draw!")
        
        
    def play_game(self):
        print("!!Begining the WAR!!\n\n")
        cards= self.deck.cards
    
        
        while len(cards)>=2:
            
            ch= input("\nTo draw 1 card each, press any key, q to exit: ")
            if ch=='q':
                break
            else:
            
                p1c = self.deck.rem_card()
                p2c = self.deck.rem_card()
                p1n = self.p1.name
                p2n = self.p2.name
                self.draw(p1n,p1c,p2n,p2c)
                
                if p1c>p2c:
                    self.p1.wins +=1
                    self.win(self.p1.name)
                    
                else:
                    self.p2.wins +=1
                    self.win(self.p2.name)
            
        self.winner(self.p1,self.p2)
        print("\n\nThe war is over")
            
            
            
            
game= Game()
game.play_game()
        
