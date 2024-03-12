print('Welcome to my quiz game')

playing= input('Do you want to play the game ')

if playing.lower() != 'yes':
    quit()

print('Welcome to my quiz game')
score=0

answer=input('what cpu stands for? ')

if answer.lower() == 'central processing unit':
    print('You are correct')
    score=score+1
else:
    print('You are wrong')


answer=input('what is 1+1 equal to? ')

if answer.lower() == '2':
    print('You are correct')
    score=score+1
else:
    print('You are wrong')

answer=input('what gpu stands for? ')

if answer.lower() == 'graphical processing unit':
    print('You are correct')
    score=score+1
else:
    print('You are wrong')

answer=input('which is the third month of the year? ')

if answer.lower() == 'march':
    print('You are correct')
    score=score+1
else:
    print('You are wrong')

print('you got '+ str(score)+ ' correct answers')
print('you got '+ str((score/4)*100)+ ' %')
