import random


def hangman(word):
    wrong=0
    remaining_words=list(word.upper())
    board= ["_"] *len(word)
    hangman=["___________",
             "    |    ||",
             "    |    ||",
             "    O    ||",
             "   /|\   ||",
             "   / \   ||",
             "         ||",
             "===========",
             ]
    print("Welcome to hangman\n")
    print("Your hangman looks like:")
    for line in hangman:
        print(line)
        
    print("\n\n")
    
    while wrong< len(hangman):
        ch=input("Guess a alphabet/word: ")
        if ch.upper()==word.upper():
            print("\n\nYou won!")
            return None
            
        
        try:
            ch = ch[0].upper()
        except:
            print("Enter an aplhabet")
            continue
        if ch in remaining_words: 
            while ch in remaining_words:
            
                chi= remaining_words.index(ch)
                remaining_words[chi]="#"
                board[chi]= ch
                print("You guessed right")
        else:
            print("Wrong guess")
            wrong+=1
            
        if "".join(board)== word.upper():
            print("You won!")
            return None
        
        

            
        print("\nCurrent Hangman looks like:\n")
        for i in range(0,wrong):
            print(hangman[i])

        print("\nBoard is: "+ " ".join(board) + '\n')
        
        
        
    print("You lose!")
    
    
words= ["Apple","Lemon","Banana","Grapes","Guava"]
word = words[random.randint(0,len(words))]
hangman(word)
print("\n\nTHE WORD WAS "+word.upper())
