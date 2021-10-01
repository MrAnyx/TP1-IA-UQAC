class Node:
    """
    Représente un noeud de notre graphe ou arbre d'exploration.
    Possède un état, la dernière action qui dirige vers ce noeud,
    un noeud parent et des noeuds enfants.
    Possède également une profondeur qui représente également notre
    coût de chemin.
    """

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
