

class Pile:
    """This class manage a LIFO object"""
    def __init__(self,n):
        """INIT"""
        self.pile = [0 for i in range(n)]
        self.pos = 0
        
    def isFull(self):
        """true if the object is full"""
        return len(self.pile)==self.pos
    
    def isVoid(self):
        """true if the object is empty"""
        return self.pos==0  
         
    def add(self,e):
        """add to the object element e"""
        if not self.isFull():
            self.pile[self.pos]=e
            self.pos+=1

    def rem(self):
        """remove last element added to the object"""
        if not self.isVoid():
            tmp= self.pile[self.pos-1]
            self.pile[self.pos-1]=0
            self.pos-=1
            return tmp
        else : return 0
    
    def top(self):
        """return the last element added to the object"""
        return self.pile[self.pos-1]
        
            
            
            
            
            
            
            
            

                
            
            
            
            
            
            
            
            
            