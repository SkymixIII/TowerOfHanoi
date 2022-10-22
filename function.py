def displayH(l,r):
    """this function display the game : tower of hanoi"""

    for o in range(r):
        t = ""
        if l[0].pile[r-1-o] == 0:
            for i in range(r):
                t+=" "
        else:
            for y in range(l[0].pile[r-1-o]):
                t += "x"
            for i in range(r-l[0].pile[r-1-o]):
                t += " "
        
        t += " | "
        
        if l[1].pile[r-1-o] == 0:
            for i in range(r):
                t+=" "
        else:
            for y in range(l[1].pile[r-1-o]):
                t += "x"
            for i in range(r-l[1].pile[r-1-o]):
                t += " "
            
        t += " | "
        
        if l[2].pile[r-1-o] == 0:
            for i in range(r):
                t+=" "
        else:
            for y in range(l[2].pile[r-1-o]):
                t += "x"
            for i in range(r-l[2].pile[r-1-o]):
                t += " "
        
        print(t)
    
    
    
    

def hanoi(l,n,c,r):
    """This function run the game : tower of hanoi"""

    input("\n'Enter' pour l'étape suivante")
    print("E : "+str(c+1)+"")
    displayH(l,r)
    fin = False
    
    if l[0].isVoid():
        if l[2].isFull() or l[1].isFull():
            print("\nGG !")
            fin = True
        
    if not fin:
        if c == -1:
            l[2].add(l[0].rem())
            return hanoi(l,3,c+1,r)
        elif c == 0:
            l[1].add(l[0].rem())
            return hanoi(l,3,c+1,r)
        
        elif n == 1:
            if l[2].top()==0:
                l[2].add(l[0].rem())
            elif l[0].top()==0:
                l[0].add(l[2].rem())
            else:
                if l[0].top()> l[2].top():
                    l[0].add(l[2].rem())
                else:
                    l[2].add(l[0].rem())
            return hanoi(l,2,c+1,r)
        
        elif n == 2:
            if l[1].top()==0:
                l[1].add(l[0].rem())
            elif l[0].top()==0:
                l[0].add(l[1].rem())
            else:
                if l[0].top()> l[1].top():
                    l[0].add(l[1].rem())
                else:
                    l[1].add(l[0].rem())
            return hanoi(l,3,c+1,r)
                
        elif n == 3:
            if l[2].top()==0:
                l[2].add(l[1].rem())
            elif l[1].top()==0:
                l[1].add(l[2].rem())
            else:
                if l[2].top()> l[1].top():
                    l[2].add(l[1].rem())
                else:
                    l[1].add(l[2].rem())
            return hanoi(l,1,c+1,r)
            
