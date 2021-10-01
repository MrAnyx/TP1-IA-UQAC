class Triplet:
    """
    La classe Triplet permet d'indexer notre graphe :
        - chaque élément contient sa valeur (f ou heuristique) ainsi que sa position dans le tableau (pièce du manoir)
        - l'adresse de son "fils de gauche" (fils à gauche dans le graphe)
        - l'adresse de son premier "frère de droite" (noeud frère directement à droite dans le graphe)
    """

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
