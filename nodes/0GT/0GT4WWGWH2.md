---
tag: 0GT4WWGWH2
kind: concept
name: System of linear equations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
uses: [0Q3ZT8J05R, 04C5ZBG1WT, 0XM8BZD76G]
aliases: [linear-system]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section1-1.xml#L783
    locator: src/section1-1.xml:783
  - book: isbn:9780321982384
    locator: Section 1.1
  - book: isbn:9780135367971
    locator: Chapter 1
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter One, Section I
same_as:
  wikidata: Q11203
  wikipedia: System of linear equations
inventory: [J6QQKN30M4]
---

## Summary

A system of linear equations over a [[field|04C5ZBG1WT]] $F$ is a finite list of $m$ [[linear equations|0Q3ZT8J05R]] in the same $n$ unknowns $x_1, \dots, x_n$:
$$a_{i1} x_1 + a_{i2} x_2 + \cdots + a_{in} x_n = b_i \quad (i = 1, \dots, m).$$
A solution is a tuple in $F^n$ that satisfies all $m$ equations at the same time, and the solution set is the set of all solutions.
The exact definition is in [[the definition node|0JTRMBQ1SA]].
In matrix form the system is $Ax = b$, with the [[coefficient matrix|0HQFZAP3ND]] $A$ and the right-hand side $b \in F^m$.
Over a field, a system has no solution, exactly one solution, or more than one; over an infinite field, "more than one" means infinitely many.
Systems of linear equations matter because almost every computation in linear algebra, from inverses to bases and eigenvectors, reduces to solving one.

## Motivation

Many problems ask for several unknown numbers that satisfy several conditions at once.
A diet with given amounts of protein, fat and carbohydrate, a balanced chemical equation, the currents in an electric network and the forces in a truss all lead to linear conditions.
One linear equation in three unknowns describes a plane, so a system of three equations asks where three planes meet.
Row reduction, which is [[Gaussian elimination|0JVJ2WCXZH]], answers this question for every system in a finite number of steps.
The answer has a fixed shape: the solution set is empty, or it is one particular solution plus all solutions of the [[homogeneous system|04KGXJG1A2]].

## Notation

1. $m$ is the number of equations and $n$ is the number of unknowns; we speak of an $m \times n$ system.
2. $a_{ij}$ is the coefficient of $x_j$ in equation $i$, and $b_i$ is the right-hand side of equation $i$.
3. $A = (a_{ij})$ is the [[coefficient matrix|0HQFZAP3ND]], $[A \mid b]$ is the [[augmented matrix|0T6MWGZSXA]], and $Ax = b$ is the matrix form.
4. We write $R_i$ for equation $i$, or row $i$, when we describe row operations, as in "$R_2 - 2R_1$".

## Remarks

### Examples

1. The system $x + y + z = 6$, $2x - y + z = 3$, $x + 2y - z = 2$ over $\R$ has the unique solution $(1, 2, 3)$, see [[three planes meeting in a point|~382fc66c]].
2. The system $x + y + z = 3$, $x - y + 3z = 1$ has a line of solutions, see [[the line example|~f4f0e07b]].
3. The system $x + y = 2$, $x - y = 0$, $x + 2y = 4$ has no solution, see [[the inconsistent triangle|~464a82a7]].
4. The system $x + 2y + 3z = 1$, $2x + y + z = 4$ over $\mathbb{F}_5$ has exactly $5$ solutions, see [[systems over finite fields|~5cac521a]].
5. The equations of the game Lights Out form a system over $\mathbb{F}_2$, see [[the Lights Out example|~1680847d]].

### Non-examples

1. The system $x + y = 1$, $xy = 0$ is not linear, and it has exactly two solutions, which no linear system over $\R$ can have; see [[the nonlinear system|~c3f6a7d4]].
2. An infinite list of equations $x_1 + x_k = 0$ for all $k \ge 2$ in infinitely many unknowns is not a system in the sense used here, because $m$ and $n$ must be finite.
3. The inequalities $x + y \le 1$, $x \ge 0$, $y \ge 0$ are not equations; they belong to linear programming, which is outside this topic.

### Basic properties

1. Two systems with the same solution set are called equivalent; [[elementary row operations|04XWH28452]] turn a system into an equivalent one, see [[the theorem on row operations|~6410ee51]].
2. Every system is equivalent to a system in [[reduced row echelon form|0WF5AQYTW6]], and the solutions can be read from it, see [[the lemma on systems in RREF|~e45eea91]].
3. A system is consistent if and only if no echelon form of $[A \mid b]$ has a pivot in its last column, see [[the existence and uniqueness theorem|BKA191KD1S]].
4. The solution set is empty or of the form $p + N$, where $N$ is the [[null space|0PHDYNR24D]] of $A$, see [[the structure theorem|~a01a76ca]].
5. A system is consistent if and only if $\rank A = \rank [A \mid b]$, which is the [[Rouché-Capelli theorem|0HV1SKWPMS]].
6. A homogeneous system with more unknowns than equations has a nontrivial solution, see [[the theorem on homogeneous systems|~37f18967]].

### History

Chapter 8 of the Chinese text *The Nine Chapters on the Mathematical Art*, called "Fangcheng" (rectangular arrays), solves systems by elimination on a counting board.
Liu Hui wrote a commentary on it in the 3rd century.
Leibniz in 1693 and Cramer in 1750 gave determinant formulas for square systems.
Gauss used systematic elimination for the normal equations of least squares, and in 1810 he gave a notation for it.
The theory of rank and consistency was completed in the second half of the 19th century, with the [[Rouché-Capelli theorem|0HV1SKWPMS]].

### Common errors

1. Thinking that a system with as many equations as unknowns always has exactly one solution. The system $x + y = 1$, $2x + 2y = 3$ has none.
2. Thinking that a system with more equations than unknowns has no solution. The system $x = 1$, $2x = 2$, $3x = 3$ has one.
3. Thinking that a linear system can have exactly two solutions. If $s \ne t$ are solutions, then $s + c(t - s)$ is a solution for every $c \in F$.
4. Changing the order of the unknowns in one equation but not in the others when writing the matrix.

## Explanations

### L1 human

A system of linear equations is a set of linear equations that must all be true at the same time.
For example, $x + y = 3$ and $x - y = 1$ have the single common solution $x = 2$, $y = 1$.
With two unknowns, each equation draws a line, and a solution is a point where all the lines meet.
Two lines can meet in one point, be parallel and never meet, or be the same line.
So a system has one solution, no solution, or infinitely many solutions.

### L2 human

We solve $x + y + z = 6$, $2x - y + z = 3$, $x + 2y - z = 2$ by elimination.

1. Replace $R_2$ by $R_2 - 2R_1$: $-3y - z = -9$.
2. Replace $R_3$ by $R_3 - R_1$: $y - 2z = -4$.
3. Swap the new $R_2$ and $R_3$, so the equation $y - 2z = -4$ comes second.
4. Replace $R_3$ by $R_3 + 3R_2$: $-7z = -21$, so $z = 3$.
5. Back substitution: $y = -4 + 2z = 2$ and $x = 6 - y - z = 1$.
6. Check in all three equations: $1 + 2 + 3 = 6$, $2 - 2 + 3 = 3$, $1 + 4 - 3 = 2$.

The typical use is to find the point where lines or planes meet, or to find unknown amounts that satisfy several balance conditions.
A trap: always check the answer in all the original equations, not only in the reduced ones, because one wrong row operation changes the solution set.

### L3 human

The system $Ax = b$ asks whether $b$ is in the image of the linear map $x \mapsto Ax$ from $F^n$ to $F^m$, and for the full preimage of $b$.
So the solution set is a fibre of a [[linear map|0NRYHJPQG2]]: empty, or a translate of the kernel, see [[the structure theorem|~a01a76ca]].
The rank of $A$ governs everything: the [[Rouché-Capelli theorem|0HV1SKWPMS]] decides consistency, and the dimension of the solution set is $n - \rank A$.
For large systems over $\R$, numerical linear algebra replaces exact elimination by pivoting strategies and iterative methods; these are outside this topic.
Over $\mathbb{Z}$ or another ring, solvability needs more than ranks, for example the Smith normal form.
Systems that have no solution are still useful: [[least squares|0BYTQ4X1HC]] finds the $x$ that makes $Ax$ closest to $b$.
