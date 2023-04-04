#!/usr/bin/python
import A_etoile

from Cube import Cube
from Etat import Etat
from Robot import Robot

# A/C, B
# A = Cube("A", True, False, "C", False)
# B = Cube("B", True, False, None, True)
# C = Cube("C", False, False, None, True )

# B/A, C
# A = Cube("A", False, False, None, True)
# B = Cube("B", True, False, "A", False)
# C = Cube("C", True, False, None, True)


# C/A, B
A = Cube("A", False, False, None, True)
B = Cube("B", True, False, None, True)
C = Cube("C", True, False, "A", False)

R = Robot()
print("------------------------------------------------")
print("Etat initial")
etat_initial = Etat(A, B, C, R)
etat_initial.display_etat()

print("------------------------------------------------")
print("Etat fin")
C1 = Cube("C", False, False, None, True)
B1 = Cube("B", False, False, "C", False)
A1 = Cube("A", True, False, "B", False)
R1 = Robot()
etat_fin = Etat(A1, B1, C1, R1)
etat_fin.display_etat_attribute()
etat_fin.display_etat()

print("------------------------------------------------")

A_etoile.A_etoile(etat_initial, etat_fin, A_etoile.h2, A_etoile.g1)
