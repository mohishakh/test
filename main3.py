import random
a=['almas','banana','appel']
def spin():
    return[random.choice(a) for i in range(3)]
def jackpat(spin_r):
    return spin_r[0]==spin_r[1]==spin_r[2]
while 1:
    re=spin()
    print(''.join(re))
    if jackpat(re):
        print('win') 
    game=input('bazam mikhei bazi koni (yes/no)')
    if game=='no':
        break
