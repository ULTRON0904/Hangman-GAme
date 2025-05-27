
###############HANGMAN GAME########################

import random

word=('shinchain','doremon','hagemaru','hathori','perman')

art={0: ("   ",
          "   ",
          "   "),
       1:(" o ",
          "   ",
          "   "),
      2: (" o ",
          " | ",
          "   "),
      3: (" o ",
          "/| ",
          "   "),
      4: (" o ",
          "/|\\",
          "   "),
      5: (" o ",
          "/|\\",
          "/  "),
      6: (" o ",
          "/|\\",
          "/ \\")}

def display_man(wrong_guess):
     print('######################')
     for line in art[wrong_guess]:
         print(line)
     print('######################')

def display_hint(hint):
    print(' '.join(hint))

def display_ans(answer):
    print(' '.join(answer))

def main():
    answer=random.choice(word)
    hint=["_"]*len(answer)
    wrong_guess=0
    guessed_letter=set( )
    is_running=True

    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess=input("Enter a letter:").lower()

        if len(guess)!=1 or not guess.isalpha():
            print('^^^^^Invalid input^^^^^^')
            continue

        if guess in guessed_letter:
            print(f'^^^^^^  {guess} already guessed^^^^^'.upper())
            continue
        guessed_letter.add(guess)

        if guess in answer:
            for a in range(len(answer)):
                if answer[a]==guess: 
                    hint[a]=guess
        else:
            wrong_guess+=1

        if "_" not in hint:
            display_man(wrong_guess)
            display_ans(answer)
            print('!you win!')
            is_running=False

        elif wrong_guess>=len(art)-1:
            display_man(wrong_guess)
            display_ans(answer)
            print('you lose')
            is_running=False

if __name__=="__main__":
    main()