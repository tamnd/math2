---
tag: 0JTRMBQ1SA
kind: definition
name: System of linear equations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
defines: 0GT4WWGWH2
uses: [0DNNT7DBFM]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-1.xml#L821
    locator: src/section1-1.xml:821
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-1.xml#L849
    locator: src/section1-1.xml:849
  - book: isbn:9780321982384
    locator: Section 1.1
inventory: [J6QQKN30M4]
---

## Definition

A system of linear equations is a finite list of linear equations in the same unknowns, and a solution must satisfy all of them.
Let $F$ be a [[field|04C5ZBG1WT]] and let $m, n \ge 1$ be integers.
A *system of linear equations* over $F$, with $m$ equations in the unknowns $x_1, \dots, x_n$, is a list of [[linear equations|0Q3ZT8J05R]]
$$\begin{aligned} a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1, \\ &\ \ \vdots \\ a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m, \end{aligned}$$
where all $a_{ij}$ and $b_i$ are elements of $F$.
A *solution* of the system is a tuple $(s_1, \dots, s_n) \in F^n$ that is a solution of each of the $m$ equations.
The *solution set* of the system is the set of all its solutions.
Two systems in the same unknowns are *equivalent* if they have the same solution set.

## Remarks

All the equations use the same unknowns, so a solution is a single tuple that we can test in every equation.
The numbers $m$ and $n$ are finite, and this is what makes elimination stop after finitely many steps.
The coefficients lie in one field $F$, so we can divide by any nonzero coefficient during elimination.

With the [[coefficient matrix|0HQFZAP3ND]] $A = (a_{ij})$, the column $b = (b_1, \dots, b_m)^{\mathsf{T}}$ and $x = (x_1, \dots, x_n)^{\mathsf{T}}$, the whole system is the single equation $Ax = b$.
For example, $(2, 1)$ solves the system $x + y = 3$, $x - y = 1$, because $3 = 3$ and $1 = 1$.
The pair $(1, 2)$ solves the first equation but not the second, since $1 - 2 = -1$, so it is not a solution of the system.

Over a field, a system has no solution, exactly one solution, or more than one, and over an infinite field "more than one" means infinitely many.
When $F$ has $q$ elements, the number of solutions is $0$ or a power of $q$, by the [[count of solutions over a finite field|8QM2Y41P69]].
The concept page on the [[system of linear equations|0GT4WWGWH2]] shows the row picture and the column picture.

## Explanations

### L1 human

A system of linear equations asks for values of the unknowns that make several linear equations true together.
For example, $x + y = 3$ and $x - y = 1$ together have the single solution $x = 2$, $y = 1$.
In the plane, each equation is a line, and a solution is a point on all the lines.

### L2 human

Does $(2, 1)$ solve $x + y = 3$, $x - y = 1$, $3x - 2y = 4$, and does $(1, 2)$?
For $(2, 1)$ the three left sides are
$$2 + 1 = 3, \qquad 2 - 1 = 1, \qquad 6 - 2 = 4,$$
so all three equations hold.
For $(1, 2)$ the first equation holds, but $1 - 2 = -1 \ne 1$, so $(1, 2)$ is not a solution.
Watch out: a solution must satisfy every equation, and satisfying most of them is not enough.
