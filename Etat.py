# !/usr/bin/python
import copy


class Etat:

    def __init__(self, A, B, C, robot):
        self.cube_list = [A, B, C]
        self.robot = robot

    def etat_meme(self, etat1):
        for i in range(0, len(self.cube_list)):
            if not self.cube_list[i].cube_meme(etat1.cube_list[i]):
                return False

        return True

    def upadate_etat(self, operation, X, sur_cube=None):
        """update l'etat a partir de fonction 'func' pour cube X
              et retourner le noveaux etat
              operation : 1 : tenir le cube X
                          2 : poser le cube sur table
                          3 : poser le cube sur cube A
              """
        new_etat = copy.deepcopy(self)
        if operation == 1:
            for i in new_etat.cube_list:
                if i.nom == X:
                    new_etat.robot.tenir(i, new_etat)
                    break

        if operation == 2:
            for i in new_etat.cube_list:
                if i.nom == X:
                    new_etat.robot.poser_sur_table(i)
                    break

        if operation == 3:
            for i in new_etat.cube_list:
                if i.nom == X:
                    for j in new_etat.cube_list:
                        if j.nom == sur_cube:
                            new_etat.robot.poser_sur_cube(i, sur_cube)
                            j.libre = False
                            break
        return new_etat

    def display_etat(self):
        self.cube_list[0].display_cube()
        self.cube_list[1].display_cube()
        self.cube_list[2].display_cube()
        self.robot.display_robot()

    def display_etat_attribute(self):
        print("         nom,    libre,  tenue,  sur_cube,   sur_table")
        self.cube_list[0].display_cube_attribut()
        self.cube_list[1].display_cube_attribut()
        self.cube_list[2].display_cube_attribut()
