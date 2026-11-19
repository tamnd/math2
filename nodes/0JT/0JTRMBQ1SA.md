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

Let $F$ be a [[field|04C5ZBG1WT]] and let $m, n \ge 1$ be integers.
A *system of linear equations* over $F$, with $m$ equations in the unknowns $x_1, \dots, x_n$, is a list of [[linear equations|0Q3ZT8J05R]]
$$\begin{aligned} a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1, \\ &\ \ \vdots \\ a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m, \end{aligned}$$
where all $a_{ij}$ and $b_i$ are elements of $F$.
A *solution* of the system is a tuple $(s_1, \dots, s_n) \in F^n$ that is a solution of each of the $m$ equations.
The *solution set* of the system is the set of all its solutions.
Two systems in the same unknowns are *equivalent* if they have the same solution set.

## Remarks

With the [[coefficient matrix|0HQFZAP3ND]] $A = (a_{ij})$, the vector $b = (b_1, \dots, b_m)^T$ and $x = (x_1, \dots, x_n)^T$, the system is the single equation $Ax = b$.
Over a field, a system has no solution, exactly one solution, or more than one solution.
When $F$ is infinite, "more than one" means infinitely many.
When $F$ is finite with $q$ elements, the number of solutions is $0$ or a power of $q$, see [[the theorem on finite fields|8QM2Y41P69]].

## Explanations

### L1 human

A system of linear equations asks for values of the unknowns that make several linear equations true together.
For example, $x + y = 3$ and $x - y = 1$ together have the single solution $x = 2$, $y = 1$.
In the plane, each equation is a line, and a solution is a point on all the lines.

### L2 human

We check that $(2, 1)$ solves $x + y = 3$, $x - y = 1$, $3x - 2y = 4$, and that $(1, 2)$ does not.

1. For $(2, 1)$: $2 + 1 = 3$, $2 - 1 = 1$ and $6 - 2 = 4$, so all three equations hold.
2. For $(1, 2)$: $1 + 2 = 3$ holds, but $1 - 2 = -1 \ne 1$.
3. So $(1, 2)$ solves the first equation only, and it is not a solution of the system.

A trap: a solution must satisfy every equation; satisfying most of them is not enough.
