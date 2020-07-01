import random
def get_word():
    words=['elephant','apple','pizza','burger','cat']
    return random.choice(words)
def play_game():
    word=get_word()
    letters_guessed=[]
    tries=10
    letters='abcdefghijklmnopqrstuvxyz'
    guessed=False
    print('word contains ',len(word),' letters')
    
    while guessed==False and tries>0:
        print('You have '+str(tries)+' tries')
        guess=input('Please enter a letter or a full word').lower()
        if len(guess)==1:
            if guess not in letters:
                print('Please enter a letter')
            elif guess in letters_guessed:
                print('Already guessed the letter')
            elif guess not in word:
                print('Wrong guess. Please try again')
                letters_guessed.append(guess)
                tries=tries-1
            elif guess in word:
                print('Well done guessed the correct word')
                letters_guessed.append(guess)
        elif len(word)==len(guess):
            if word==guess:
                print('Congratualtions you have guessed the word')
                guessed=True
            else:
                print('Wrong guess. Please try again')
                tries=tries-1
        else:
            print('The length you have entered is not same as the length of the word')
        status=''
        if guessed==False:
            
            for letter in word:
                if letter in letters_guessed:
                    status+=letter
                else:
                    status+='*'
        print(status)
        if status==word:
            print('Congratulations you have guessed the word')
            guessed=True
        elif tries==0:
            printf('Sorry but you are out of tries')
            
