# !/usr/bin/python

"""
    les operations de algorithme A*
"""


class Node:
    """class node a un etat, valeur de fonction heuristique et de fonction gout  """

    def __init__(self, id_node, etat_couvrant, node_parent, h, g):
        self.id_node = id_node
        self.etat = etat_couvrant
        self.node_parent = node_parent
        self.h = h
        self.g = g

    def display_Node(self):
        print("Node ", self.id_node)

        if self.node_parent is None:
            print("         node parent : has no node parent")
        else:
            print("         node parent : ", self.node_parent.id_node)

        print("         h = ", self.h, ",    g = ", self.g)
        self.etat.display_etat()

    def est_dans_list(self, _list):
        if _list is None:
            return False

        for i in _list:
            if self.etat.etat_meme(i.etat):
                return True
        return False


def h1(etat_couvrant, etat_fin):
    """fonction pour calcule fonction heuristique h1"""
    h = 0

    if etat_couvrant is None:
        return 0

    for i in range(0, len(etat_couvrant.cube_list)):
        if etat_couvrant.cube_list[i].libre != etat_fin.cube_list[i].libre:
            h = h + 1
        if etat_couvrant.cube_list[i].tenue != etat_fin.cube_list[i].tenue:
            h = h + 1
        if etat_couvrant.cube_list[i].sur_cube != etat_fin.cube_list[i].sur_cube:
            h = h + 1
        if etat_couvrant.cube_list[i].sur_table != etat_fin.cube_list[i].sur_table:
            h = h + 1
    return h


def h2(etat_couvrant, etat_fin):
    h = 0
    if etat_couvrant is None:
        return 0

    if etat_couvrant.cube_list[0].sur_cube != "B":
        h += 1
    if etat_couvrant.cube_list[1].sur_cube != "C":
        h += 1
    if not etat_couvrant.cube_list[2].sur_table:
        h += 1

    return h


def g1(node_parent):
    if node_parent is None:
        return 0
    else:
        return node_parent.g + 1


def ajouter_node(ouvert, fermet, etat_new, etat_fin, node_couvrant, func_h, func_g, compt):
    node = Node(compt[0], etat_new, node_couvrant, func_h(etat_new, etat_fin),
                func_g(node_couvrant))

    if not node.est_dans_list(ouvert):
        if not node.est_dans_list(fermet):
            ouvert.append(node)
            compt[0] += 1
        else:
            for i in fermet:
                if node.etat.etat_meme(i.etat) and node.h <= i.h:
                    fermet.remove(i)
                    ouvert.append(node)

    else:
        for i in range(0, len(ouvert)):
            if etat_new.etat_meme(ouvert[i].etat):
                if node.h <= ouvert[i].h:
                    ouvert[i] = node


def A_etoile(etat_couvrant, etat_fin, func_h, func_g):
    node_0 = Node(0, etat_couvrant, None, func_h(etat_couvrant, etat_fin), func_g(None))

    ouvert = [node_0]
    fermet = []

    compt = 1
    compt1 = 0
    while ouvert is not None and ouvert[0].h != 0:
        print("/////////////////////////////////////////////////////////////////////////////////")
        node_couvrant = ouvert[0]
        print("node couvrant : ")
        node_couvrant.display_Node()
        print("         --------------------")
        node_couvrant.etat.display_etat_attribute()
        del ouvert[0]
        fermet.append(node_couvrant)

        etat_couvrant = node_couvrant.etat
        print("---")
        if etat_couvrant.robot.bras_vide:
            """le robot bras est vide, il dois tenir un cube qui est libre """
            for i in etat_couvrant.cube_list:
                if i.libre:
                    print("tenir cube ", i.nom)
                    etat_new = node_couvrant.etat.upadate_etat(1, i.nom)
                    node_new = Node(compt, etat_new, node_couvrant, func_h(etat_new, etat_fin),
                                    func_g(node_couvrant))

                    if not node_new.est_dans_list(ouvert):
                        if not node_new.est_dans_list(fermet):
                            ouvert.append(node_new)
                            compt += 1
                        else:
                            print("node ", node_new.id_node, "deja dans fermet")
                    else:
                        print("node ", node_new.id_node, "deja dans ouvert")

        else:
            """poser le cube qui est tenue par robot sur table"""
            etat_new = etat_couvrant.upadate_etat(2, etat_couvrant.robot.tenir_X.nom)
            node_new = Node(compt, etat_new, node_couvrant, func_h(etat_new, etat_fin),
                            func_g(node_couvrant))

            if not node_new.est_dans_list(ouvert):
                if not node_new.est_dans_list(fermet):
                    ouvert.append(node_new)
                    compt += 1
                else:
                    print("node ", node_new.id_node, "deja dans fermet")
            else:
                print("node ", node_new.id_node, "deja dans ouvert")

            """poser le cube qui est tenue par robot sur cube"""
            for i in node_couvrant.etat.cube_list:
                if i.libre:
                    etat_new = etat_couvrant.upadate_etat(3, etat_couvrant.robot.tenir_X.nom, i.nom)
                    node_new = Node(compt, etat_new, node_couvrant, func_h(etat_new, etat_fin),
                                    func_g(node_couvrant))

                    if not node_new.est_dans_list(ouvert):
                        if not node_new.est_dans_list(fermet):
                            ouvert.append(node_new)
                            compt += 1
                        else:
                            print("node ", node_new.id_node, "deja dans fermet")
                    else:
                        print("node ", node_new.id_node, "deja dans ouvert")

        print("---")

        ouvert.sort(key=lambda x: x.h)
        print("************")
        print("ouvert : ")
        for k in ouvert:
            k.display_Node()
            print("         --------------------")
            k.etat.display_etat_attribute()
        print("************")
        print("fermet : ")
        for j in fermet:
            j.display_Node()
            print("         --------------------")
            j.etat.display_etat_attribute()
        print("************")

        compt1 += 1

    print("/////////////////////////////////////////////////////////////////////////////////")
    print("Success !!!")
    print("l'etat de but est : ")
    etat_fin.display_etat()
    print("         --------------------")
    etat_fin.display_etat_attribute()
    print(" ")
    print("**************************************************")
    print(" ")
    print("le node de success est : ", ouvert[0].id_node)
    ouvert[0].display_Node()
    print("         --------------------")
    ouvert[0].etat.display_etat_attribute()
