#main script of the project : tower of hanoi
#run the script to see the solution of the game : tower of hanoi

from function import hanoi
from pile import Pile

number = ["0","1","2","3","4","5","6","7","8"]

if __name__=="__main__":
    n = input("Combien d'étages ? (entre 0 et 8)")
    while n not in number:
        n = input("Combien d'étages ? (entre 0 et 8)")
    n = int(n)
    tours1 = Pile(n)
    tours2 = Pile(n)
    tours3 = Pile(n)
    l = [tours1,tours2,tours3]
    for i in range(n,0,-1):
        l[0].add(i)
    hanoi(l,1,-1,n)

