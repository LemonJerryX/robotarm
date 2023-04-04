# !/usr/bin/python

class Cube:
    "l'exprime de cube"

    def __init__(self, nom, libre, tenue, sur_X, surtable):
        self.nom = nom
        self.libre = libre  # le cube X est libre
        self.tenue = tenue  # X dans le bras du Robot
        self.sur_cube = sur_X  # le cube est sur le cube X
        self.sur_table = surtable  # le cube X est sur la table

    def cube_meme(self, cube1):
        if self.libre != cube1.libre:
            return False
        if self.tenue != cube1.tenue:
            return False
        if self.sur_cube != cube1.sur_cube:
            return False
        if self.sur_table != cube1.sur_table:
            return False
        return True

    def display_cube(self):

        if not self.sur_table and not self.tenue:
            print("         cube", self.nom, "est sur cube ", self.sur_cube)
        elif self.tenue:
            print("         cube", self.nom, " est tenue par robot")
        else:
            print("         cube", self.nom, " est sur table")

    def display_cube_attribut(self):
        if self.sur_cube is None:
            print("         ", self.nom, "   ", self.libre, "    ", self.tenue, "    None", "     ",
                  self.sur_table)
        else:
            print("         ", self.nom, "   ", self.libre, "    ", self.tenue, "    ", self.sur_cube, "     ",
                  self.sur_table)
