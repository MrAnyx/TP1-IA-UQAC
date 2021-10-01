# Auteur : Robin Bidanchon


class Graph:
    """
    Cette classe permet de symboliser le graph entre les pièces
    Le graph à proprement parlé est un dictionnaire python contenant en clé, l'indice de la pièce actuelle et en valeur, l'ensemble de ses voisins

    {
        "0" : [1, 5],
        "1" : [0, 6, 2],
        ...
    }

    L'indice de la pièce actuelle est calculé en faisant : x + (y * 5)
    Par exemple, dans l'exemple suivant :
        - la pièce [0, 0] aura l'indice 0
        - la pièce [0, 1] aura l'indice 1
        - la pièce [1, 0] aura l'indice 5
        - ...

    Ce qui correspond au pattern suivant :
    [
        [0 , 1 , 2 , 3 , 4 ],
        [5 , 6 , 7 , 8 , 9 ],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24]
    ]
    """

    def __init__(self, nodes={}):
        self.nodes = nodes

    # Cette fonction permet de retourner l'ensemble des voisins d'une pièce donnée selon son indice
    def get_node_neighbors(self, key):
        # Si la pièce n'existe pas
        if key not in self.nodes:

            # On retourne None
            return None

        # Sinon, on retourne l'ensemble de ses voisins, c'est à dire, la valeur ayant comme clé l'indice de la pièce voulue
        return self.nodes[key]
