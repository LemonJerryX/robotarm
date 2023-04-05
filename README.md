# Introduction

我们有三个立方体A、B和C，一张桌子（无限空间）和一个可编程机械臂。
目标是从初始状态（a）转移到最终状态（b）（如下图所示）。

![](https://s2.loli.net/2023/04/05/glYaRPOFWxD7AGe.png)



系统的所有状态都可以用以下谓词来描述：

- LIBRE（X）：表示立方体X是自由的，因此它上面没有其他立方体，也没有被机械臂抓住等（¬LIBRE（X）表示LIBRE（X）的相反）。
- TENU（X）：表示机械臂抓住了立方体X（X在机械臂上）。
- SUR（X，Y）：表示立方体X在立方体Y上（例如SUR（C，A））。
- SURTABLE（X）：表示立方体X在桌子上。
- BRASVIDE：表示机械臂是空闲的（¬BRASVIDE表示BRASVIDE的相反）。
以下是这4个生产规则R1、R2、R3和R4的非正式描述（伪语言）。

- R1：如果机械臂是空闲的（空的）并且立方体X是自由的，并且X位于桌子上，则机械臂会抓住立方体X并更新系统状态以执行此操作。
- R2：如果机械臂是空闲的，并且立方体X在立方体Y上并且立方体X是自由的，则机械臂会抓住立方体X并更新系统状态以执行此操作。
- R3：如果机械臂抓住立方体X，则将X放在桌子上并更新系统状态以表达将立方体X放在桌子上的行动以及对系统状态的影响。
- R4：如果机械臂抓住立方体X并且立方体Y是自由的，则将立方体X放在立方体Y上并更新系统状态以表达立方体X放在立方体Y上的行动以及对系统状态的影响。

----

On dispose de trois cubes (A, B et C), d'une table (espace infini) et d'un bras robotisé programmable. Le but est de passer de l'état initial (a) à l'état final (b) tel que représenté dans la figure ci-dessus.

![](https://s2.loli.net/2023/04/05/glYaRPOFWxD7AGe.png)

Tous les états du système peuvent être décrits avec les prédicats suivants :

LIBRE(X) : Exprime le fait que le cube X est libre, c'est-à-dire qu'il n'y a pas d'autre cube au-dessus, ni qu'il est saisi par le bras robotisé, etc. (¬LIBRE(X) exprime le contraire de LIBRE(X)).
TENU(X) : Exprime le fait que le bras robotisé saisit le cube X (X dans le bras robotisé).
SUR(X,Y) : Exprime le fait que le cube X est sur le cube Y (exemple SUR(C,A)).
SURTABLE(X) : Exprime le fait que le cube X est sur la table.
BRASVIDE : Exprime le fait que le bras robotisé est libre (¬BRASVIDE exprime le contraire de BRASVIDE).
Voici une description informelle (pseudo-langage) de ces 4 règles de production R1, R2, R3 et R4 :

R1 : Si le bras robotisé est libre (vide) et que le cube X est libre et sur la table, alors le robot va saisir le cube X et mettre à jour l'état du système à la suite de cette action.
R2 : Si le bras robotisé est libre et qu'un cube X est sur un cube Y et que le cube X est libre, alors le robot va saisir le cube X et mettre à jour l'état du système à la suite de cette action.
R3 : Si le robot tient le cube X, alors poser X sur la table et mettre à jour l'état du système pour exprimer l'action de poser le cube X sur la table et les conséquences sur l'état du système.
R4 : Si le robot tient le cube X et que le cube Y est libre, alors poser le cube X sur le cube Y et mettre à jour l'état du système pour exprimer que le cube X est sur le cube Y et les conséquences sur l'état du système.
