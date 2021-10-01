from numpy import sqrt, zeros, array
import random

"""
    La classe triplet permet 
"""
class triplet:
    def __init__(self, f, position, indFils, indBro):
        self.val = f
        self.pos = position
        self.lChild = indFils
        self.rBro = indBro

    def setLChild(self, indFils):
        self.lChild = indFils
    
    def setRBro(self, indBro):
        self.rBro = indBro

    def isPresent(self, position):
        if self.pos == position:
            return True
        return False

    def wherePos(self, position):
        for i in range(len(self)):
            if self[i].pos == position:
                return i
        return -1

def genTableau():
    tab = zeros((5,5), int)

    print("Indices poussières :")
    for i in range(0, 2):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        tab[x,y] = 33
        print(x, ", ", y)

    return tab

def closeDirt(tab, pos):
    dist = 6
    goal = [-1, -1]
    for i in range (0, 5):
        for j in range(0,5):
            if tab[i][j] == 33:
                a = sqrt((pos[0] - i)**2 + (pos[1] - j)**2)
                if a < dist:
                    goal = [i,j]

    return goal

def getVoisins(pos):
    indVoisins = []
    if pos[0]>0:
        indVoisins.append([pos[0]-1, pos[1]])
    if pos[0]<4:
        indVoisins.append([pos[0]+1, pos[1]])
    if pos[1]>0:
        indVoisins.append([pos[0], pos[1]-1])
    if pos[1]<4:
        indVoisins.append([pos[0], pos[1]+1])
    return indVoisins

def heuristique(pos, goal):
    return sqrt((pos[0] - goal[0])**2 + sqrt((pos[1] - goal[1])**2))
    

def distStart(pos, start):
    print(abs(pos[0] - start[0]) + abs(pos[1] - start[1]))
    return abs(pos[0] - start[0]) + abs(pos[1] - start[1])

def fin(pos, goal):
    if (pos[0] == goal[0]) and (pos[1] == goal[1]):
        return False
    return True

def aspire(tab, pos):
    tab[pos[0],pos[1]] = 0
    return tab

def cheminOpti(tab):
    a = random.randint(0, 4)
    b = random.randint(0, 4)
    position = [a,b]
    print("Position de départ : ", position)

    #On détermine le prochain élément à aller ramasser
    goal = closeDirt(tab, position)
    path = []

    while(goal != [-1, -1]):

        openIndex = []
        closeIndex = []
        arbre = []
        indice = 0
        index = 0
        arbre.append(triplet(heuristique(position, goal), position, -1, -1))
        
        while(fin(position, goal)):
            
            # Indexation des fils directs du noeud
            indice += 1
            openIndex.append(indice)
            arbre[index].setLChild(indice)
            posVois = getVoisins(position)
            nbVois = len(posVois)
            for i in range(0, nbVois - 1):
                keep = True
                for j in closeIndex:
                    if arbre[j].isPresent(posVois[i]):
                        keep = False
                        break
                if keep:
                    indice += 1
                    openIndex.append(indice)
                    arbre.append(triplet(heuristique(posVois[i], goal), posVois[i], -1, indice))
            arbre.append(triplet(heuristique(posVois[-1], goal), posVois[-1], -1, -1))

            # Changement du noeud vers celui avec le meilleur f
            f = 26
            for i in openIndex:
                tempf = arbre[i].val
                if tempf < f:
                    position[0] = arbre[i].pos[0]
                    position[1] = arbre[i].pos[1]
                    f = tempf
                    index = i
            path.append([position[0],position[1]])
            closeIndex.append(index)
            openIndex.remove(index)

            # Incrémentation du chemin jusqu'à la position actuelle
            if f > 25:
                break
        
        path.append("action")
        tab = aspire(tab, position)
        goal = closeDirt(tab, position)

    return path

def greedSearch():
    tab = genTableau()
    path = cheminOpti(tab)
    print(path)

greedSearch()