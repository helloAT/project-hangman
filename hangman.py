import random
import replit
wordlist = ["Awkward", "Bagpipes", "Banjo", "Crypt", "Dwarves", "Fishhook", "Haiku", "Haphazard", "Hyphen", "Ivory", "Jazzy", "Jinx", "Jukebox", "Kayak", "Kiosk", "Oxygen", "Pajama", "Pixel", "Rhythmic", "Rogue", "Sphinx"]
guesses = 0
hidden_word = []
guessed_letters = []
hangman = (

"""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """,

"""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    """,

"""
   _________                 
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    """,


"""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    """,


"""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    """,



"""
   _________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    """,


"""
   _________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    """)

print("Welcome to hangman")
choice = input("Would you like to choose your word").lower()
replit.clear()
if "yes" in choice:
  answer = input("What will the word be?")
  replit.clear()
else:
  answer = random.choice(wordlist).lower()
  print("I have chosen my word")

answerlen = len(answer)
print(hangman[0])

for x in range(answerlen):
  hidden_word.append("_")

def win():
  print("You won")
  
def change():
  print(' '.join(hidden_word))
  print(','.join(guessed_letters))
  print("\n\n")

def wrong():
  global guesses
  guesses += 1
  guessed_letters.append(guess)
  print("Your guess was incorrect :(")
  print(hangman[guesses])

change()

while True:
  guess = input("Guess a letter or the word\n\n").lower()
  guesslen = len(guess)
  replit.clear()

  if guesslen == 1:
    if guess in answer:
      for i in range(0, answerlen):
        if guess == answer[i]:
          hidden_word[i] = guess
      print("Your guess was correct")
      print(hangman[guesses])
      change()
      if not "_" in hidden_word:
        win()
        break
    else:
      wrong()
      change()
  else:
    if guess == answer:
      win()
      break
    else:
      wrong()
  if guesses == 6:
    print("You lost")
    break

