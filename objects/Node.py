class Node:
    def __init__(self, state, parent=None, action=None):
        # Etat
        self.state = state
        # Action pour passer du parent au noeud courant
        self.action = action

        # Parents et enfants
        self.parent = parent
        self.children = []

        # Profondeur = cout du chemin
        if self.parent:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0

    def add_child(self, child):
        self.children.append(child)
