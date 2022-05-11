from random import choice,choices

class Player: #Class for creating Players
    def __init__(self,type):
        self.type=type
        self.score=0
    def update(self,points):
        self.score+=points

def cases():#Returns the possible combinations of (x,y,z)
    l=[]
    for i in range(26):
        for j in range(26-i):
            l.append((i,j,25-i-j))
    return l; 

def arrange(p1,p2): #For sorting objects based on type
    if p2.type>p1.type:
        return p1,p2
    return p2,p1

def game_sem(x): #When both players are of same type
    if x=='A':
        return 0
    else:
        return 20

def game(p1,p2): #Updates the scores after a match between the players
    p1,p2=arrange(p1,p2)
    t1=p1.type
    t2=p2.type
    if(t1==t2):
        p=game_sem(t1)
        p1.update(p)
        p2.update(p)
    else:
        if t1=='A' and t2=='B':
            p1.update(30)
            p2.update(-10)
        elif t1=='A' and t2=='C':
            p1.update(3)
            p2.update(-1)
        elif t1=='B' and t2=='C':
            p1.update(20)
            p2.update(20)

def reset(l): #Resets score of all players to 0
    for x in l:
        x.score=0

def typesem(a,b): #This function returns true when 2 ordered lists of players have same type for all its element objects 
    i=0
    while i<25 and a[i].type==b[i].type:
        i+=1
    if i==25:
        return True
    return False

def allsame(l): #Checks if all players are of same type
    a=l[0].type
    b=1
    while b<25 and l[b].type==a:
        b+=1
    if b==25:
        return True
    return False

#_________________Main____________________#

d_wins={}
d_wins_case={}
for case in cases():
    if case[0]==0: 
        typ=choices(["B","C"],weights=case[1:])[0]
    else:
        l_players=[]
        x,y,z=case
        for i in range(x):
            l_players.append(Player('A'))
        for i in range(z):
            l_players.append(Player('C'))
        for i in range(y):
            l_players.append(Player('B'))
        

        while not allsame(l_players):
            #_____Let The Game Begin_____#
            for i in range(25):
                p1=l_players[i]
                for j in range(i+1,25):
                    p2=l_players[j]
                    game(p1,p2)

            l_players.sort(key= lambda x: x.score)
            test=l_players.copy()
            l_players=l_players[5:]
            l_players.extend(l_players[-5:])
            if typesem(test,l_players):
                l_players[0]=choice(l_players)
                break
            reset(l_players)

        typ=l_players[0].type
    if typ not in d_wins:
        d_wins[typ]=1
        d_wins_case[typ]=[]
    else:
        d_wins[typ]+=1
        d_wins_case[typ].append(case)
    #print(case,typ)

print(d_wins)

    


        
