#___________________________Q1.A Creating a List to keep track of the position of the organism__________________________________#

#_______________________________________________________________________________________________________________________________#
#                                                                                                                               #
#  This Program Creates a Random 2D Matrix with values in accordance with the given constrains and creates the reqd Simulation  #
#_______________________________________________________________________________________________________________________________#


from math import *
from random import *

#______Definitions_______#
class cell:
    def __init__(self,pos):
        self.pos=pos
        self.x=pos[0]
        self.y=pos[1]
        self.stat=0
		
class blob:
 	
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.inpursuit=False
 		
    def rpfcell(self): #Returns a food cell in proximity
        min= 2*n-2
        temp=[]
        for z in fcells:
            d=md(z.pos,(self.x,self.y))
            if d<=r and d>0:
                if min>d:
                    min=d
                temp.append((z,d))
        if temp:
            temp2=[]
            for t in temp:
                if t[1]==min:
                    temp2.append(t[0])
                    return choice(temp2)
        return []
 			 
    def legmov(self): #Checks if the blob in within the environment
        if self.x>-1 and self.y>-1 and self.x<n and self.y<n:
            return True
        else:
            return False
            
    def left(self):
        self.x-=1
        if not self.legmov():
            self.x+=2
            
    def right(self):
        self.x+=1
        if not self.legmov():
            self.x-=2
    
    def up(self):
        self.y+=1
        if not self.legmov():
            self.y-=2
    
    def down(self):
        self.y-=1
        if not self.legmov():
            self.y+=2
            
    def rmove(self): #Returns a random direction for the blob to move
        eval(choice(["self.left()","self.right()","self.up()","self.down()"]))

            
    def towards(self,fcell): #Returns a direction towards the nearest food cell
        d1=fcell.x-self.x
        d2=fcell.y-self.y
        lpos=[]
        if d1>0:
            lpos.append("self.right()")
        elif d1<0:
            lpos.append("self.left()")
        if d2>0:
            lpos.append("self.up()")
        elif d2<0:
            lpos.append("self.down()")
        if lpos:
            eval(choice(lpos))
 			

def md(x,y): #Returns the Manhattan Distance between 2 pos vectors
    return sum([fabs(e1-e2) for e1,e2 in zip(x,y)])


def display(): #Displays the status of each iteration (This function is not called in the main code)
    for i in range(n):
        for j in range(n):
            print(cells[i][j].stat,end=" ")
        print()
    print()
    
    
#_____Creating The Environment(Random n*n Matrix)____#

mov=10000 #The Number of Iterations
n=7    #The Number of Rows/Columns of the 2D Matrix
k=5    #The Number of Food Particles
r=3    #Manhattan Distance Vision

#____Lists for Storing various objects_____#
cells=[]
cells2=[]
fcells=[]
poslog=[]

#Making cells
for i in range(n):
    cells.append([])
    for j in range(n):
        obj=cell((i,j))
        cells[i].append(obj)
        cells2.append(obj)

#Creating our Hero
m=floor(n/2)
bob=blob(m,m)
cells[m][m].stat=1
		
#Randomizing food cells
l=list(range(n*n))
l.remove(m*(n+1))
l=sample(l,k)
for x in l:
	cells2[x].stat=2
	fcells.append(cells2[x])

#Actual Simulation	
for x in range(mov):
    poslog.append([bob.x,bob.y])
    prev=cells[bob.x][bob.y]
    if not bob.inpursuit:
        t1=bob.rpfcell()
    #display()
    if t1:
        bob.towards(t1)
        bob.inpursuit=True
    else:
        bob.inpursuit=False
        bob.rmove()
    prev.stat=0
    curr=cells[bob.x][bob.y]
    if curr in fcells:
        fcells.remove(curr)
        t1=bob.rpfcell()
    curr.stat=1
    

print(poslog)
#poslog is our reqd list

#_______________________________________End_______________________________________#



		
	
	
	
