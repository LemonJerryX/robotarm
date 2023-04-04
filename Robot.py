# !/usr/bin/python


class Robot:
    "l'exprime de Robot"

    def __init__(self):
        self.bras_vide = True  # le bras du robot est vide
        self.tenir_X = None

    def update_robot(self, bras_vide):
        self.bras_vide = bras_vide

    def display_robot(self):
        if self.bras_vide:
            print("         le bras de robot est vide")
        else:
            print("         le robot teni cube", self.tenir_X.nom)

    def tenir(self, X, etat):
        """tenir le cube qui est sur table"""
        if self.bras_vide:
            if X.libre:

                for j in etat.cube_list:
                    if j.nom == X.sur_cube:
                        j.libre = True

                X.libre = False
                X.tenue = True
                X.sur_cube = None
                X.sur_table = False
                self.bras_vide = False
                self.tenir_X = X


            else:
                print(X.nom, " non libre")
        else:
            print("le bras robot non vide")

    def poser_sur_table(self, X):
        """poser le cube X sur table """
        if not self.bras_vide:
            X.libre = True
            X.tenue = False
            X.sur_cube = None
            X.sur_table = True
            self.tenir_X = None
            self.bras_vide = True
        else:
            print("le bras de robot est vide")

    def poser_sur_cube(self, X, sur_cube):
        """poser le cube X sur table """
        if not self.bras_vide:
            X.libre = True
            X.tenue = False
            X.sur_cube = sur_cube
            X.sur_table = False
            self.tenir_X = None
            self.bras_vide = True


