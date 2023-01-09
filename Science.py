import os
os.system('clear')
N=input('What is your name? \n')
print('\nWow! Cool name',N)
S=0
NOQ=0
print('\nWhat delivers oxygen-rich blood from the lungs to the left atrium?')
print('A=Pulmonary Veins')
print('B=Blood Veins')
print('C=Vein Veins')
print('D=None Of The Above')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'A'or e == 'a':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')
print('\nWhat are the four essential parts of the Circulatory System?')
print('A=Capilarries,The heart and Arteries')
print('B=Veins,Capilarries,The heart and Arteries')
print('C=ONLY THE HEART IS ESSENTIAL!')
print('D=Stomach,mouth,intestines and pancreas')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'B'or e == 'b':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')

print('\nHow many chambers are there in a heart?')
print('A=1')
print('B=3')
print('C=4')
print('D=2')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'C'or e == 'c':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')

print('\nWhat are the four valves in the heart called?')
print('A=Trictcuspiid Valve,Pulmonary Valve (or Pulmonic Valve),Mitral Valve and Aortpic Valve')
print('B=valve1,valve2,valve3 and valve4')
print('C=Tricuspidy Valve,Puplmonary Valve (or Pulmonic Valve),Mitral Valve and Aortic Valve')
print('D=Tricuspid Valve,Pulmonary Valve (or Pulmonic Valve),Mitral Valve and Aortic Valve')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'D'or e == 'd':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')

print('\nDo you need both lungs to survive?')
print('A=No, actually - Most people can get by with only one lung instead of two, if needed. Usually, one lung can provide enough oxygen and remove enough carbon dioxide, unless the other lung is damaged.')
print('B=Yes! Imagine living with one lung - IMPOSSIBLE!')
e=input('A or B\n')
NOQ+=1
if e == 'A'or e == 'a':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')
  
print('\nWhich lung is bigger?')
print('A=The one on the left')
print('B=The one on the right')
print('C=They are the same size!')
print('D=The one in the middle')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'B'or e == 'b':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')

print('\nWhat are the names of the chambers of the heart?')
print('A=atriums and veins')
print('B=ventricles and arteries ')
print('C=atriums and ventricles')
print('D=arteries and veins')
e=input('A,B,C or D\n')
NOQ+=1
if e == 'C'or e == 'c':
    S+=1
    print('Correct!')
else:
    print('Incorrect :(')
if S > NOQ//2:
  print('\nWow!',N,'you got',S,'out of',NOQ)
else:
  print('\nTry again',N,':( you got',S,'out of',NOQ)
