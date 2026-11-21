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

A system of linear equations is a list of [[linear equations|0Q3ZT8J05R]] that must all hold at the same time.
Solving one is the basic computation of linear algebra: inverses, bases, eigenvectors and least squares fits all come down to it.
Over a [[field|04C5ZBG1WT]] $F$, a system of $m$ equations in the $n$ unknowns $x_1, \dots, x_n$ reads
$$a_{i1} x_1 + a_{i2} x_2 + \cdots + a_{in} x_n = b_i \qquad (i = 1, \dots, m).$$
A solution is a tuple in $F^n$ that satisfies all $m$ equations, and the solution set is the intersection of the solution sets of the single equations.
In matrix form the system is $Ax = b$, with the [[coefficient matrix|0HQFZAP3ND]] $A$ and the right side $b \in F^m$.
The [[formal definition|0JTRMBQ1SA]] gives every condition.

## Motivation

Many problems ask for several unknown numbers that satisfy several conditions at once.
A diet with given amounts of protein, fat and carbohydrate, a balanced chemical equation, the currents in an electric network and the forces in a bridge all lead to linear conditions.
One linear equation in three unknowns describes a plane, so a system of three such equations asks where three planes meet.

The rest of the sub-area answers that question for every system.
Row reduction, also called [[Gaussian elimination|0JVJ2WCXZH]], finds all solutions in a finite number of steps.
The answer always has the same shape: the solution set is empty, or it is one particular solution plus all solutions of the [[homogeneous system|04KGXJG1A2]].
Later sub-areas read the same system as a question about a linear map, and the rank of the matrix becomes the main number.

## Notation

We call a system of $m$ equations in $n$ unknowns an $m \times n$ system.
The coefficient of $x_j$ in equation $i$ is $a_{ij}$, so the first index names the equation and the second names the unknown.
The matrix $A = (a_{ij})$ is the coefficient matrix, and $[A \mid b]$ is the [[augmented matrix|0T6MWGZSXA]].
When we describe row operations we write $R_i$ for equation $i$, as in "$R_2 - 2R_1$".
Many books say "linear system" for short.

## Remarks

### Three pictures of one system

Take the $3 \times 3$ system over $\mathbb{R}$
$$x + y + z = 6, \qquad 2x - y + z = 3, \qquad x + 2y - z = 2.$$
In the row picture, each equation is a plane in space, and a solution is a point on all three planes.
These three planes meet in the single point $(1, 2, 3)$, as [[three planes meeting in one point|YM0PB9F9HG]] shows step by step.

In the column picture, we read the system as one equation between vectors in $\mathbb{R}^3$:
$$x \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} + y \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} + z \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix}.$$
Now the question is how to combine the three columns to get the right side.
Check: $1 \cdot (1, 2, 1) + 2 \cdot (1, -1, 2) + 3 \cdot (1, 1, -1) = (6, 3, 2)$.
The theorem on [[linear systems as vector equations|E7SAHXQEVC]] makes this view exact.

The matrix form packs both pictures into $Ax = b$, where row $i$ of $A$ holds the coefficients of equation $i$ and column $j$ holds the coefficients of $x_j$.

### None, one or infinitely many

Not every system meets in one point.
The two planes $x + y + z = 3$ and $x - y + 3z = 1$ meet in a line, worked out in [[two planes meeting in a line|PRB44DTZ1P]].
The three lines $x + y = 2$, $x - y = 0$ and $x + 2y = 4$ have no common point, as [[three lines without a common point|XJX2NN45ED]] shows.

Why can a system not have exactly two solutions?
If $s$ and $t$ are different solutions, then for every scalar $c$ the point $s + c(t - s)$ is a solution, because
$$A\big(s + c(t - s)\big) = As + c(At - As) = b + c(b - b) = b.$$
Over $\mathbb{R}$ this gives infinitely many solutions.
Over a finite field with $q$ elements the count is $0$ or a power of $q$.
For example, $x + 2y + 3z = 1$, $2x + y + z = 4$ over $\mathbb{F}_5$ has exactly $5$ solutions, see [[linear systems over finite fields|J6A58MEM8R]].
The puzzle Lights Out is also a system, over $\mathbb{F}_2$, and [[the Lights Out example|JD8FEPHM6T]] solves a small board.

### What is not a linear system

The system $x + y = 1$, $xy = 0$ has exactly the two solutions $(1, 0)$ and $(0, 1)$.
That is impossible for a linear system over $\mathbb{R}$, and the reason is the product $xy$; see [[a nonlinear system with exactly two solutions|FB6HBKEGPR]].
An infinite list of equations, such as $x_1 + x_k = 0$ for all $k \ge 2$, is not a system in our sense, because $m$ and $n$ must be finite.
Inequalities such as $x + y \le 1$ are not equations at all, and they belong to linear programming.

### The tools of the sub-area

Two systems with the same solution set are called equivalent.
[[Elementary row operations|04XWH28452]] turn a system into an equivalent one, by the theorem that [[row operations keep the solution set|K41GT10YM6]].
Every system is equivalent to one in [[reduced row echelon form|0WF5AQYTW6]], and from that form you can [[read off the solutions|P3HMRQN5KT]].
A system is consistent exactly when an echelon form of $[A \mid b]$ has no pivot in its last column, by the theorem on [[existence and uniqueness of solutions|BKA191KD1S]].
In the language of rank, the same test is the [[Rouché-Capelli theorem|0HV1SKWPMS]]: $\rank A = \rank\, [A \mid b]$.
When a solution exists, the full solution set is that solution plus the [[null space|0PHDYNR24D]] of $A$, by the [[structure theorem|PDH3HKXWAZ]].

### Watch out

Counting equations does not decide the answer.
A square system can have no solution: $x + y = 1$ and $2x + 2y = 3$ describe parallel lines.
A system with more equations than unknowns can have a solution: $x = 1$, $2x = 2$, $3x = 3$ has the solution $x = 1$.
Also keep the unknowns in the same order in every equation before you write the matrix, or the columns will mix different unknowns.

### History

Chapter 8 of the Chinese book *The Nine Chapters on the Mathematical Art*, called "Fangcheng" (rectangular arrays), solves systems by elimination on a counting board.
Liu Hui wrote a commentary on the book in the 3rd century.
Leibniz in 1693 and Cramer in 1750 gave determinant formulas for square systems.
Gauss used systematic elimination for the normal equations of least squares, and in 1810 he introduced a notation for it.
The theory of rank and consistency took its final form in the late 19th century, with the [[Rouché-Capelli theorem|0HV1SKWPMS]].

### Try it

First, does $(2, 1)$ solve the system $x + y = 3$, $x - y = 1$, $3x - 2y = 4$?
Yes: $2 + 1 = 3$, $2 - 1 = 1$ and $6 - 2 = 4$.

Second, write the system $2x - z = 1$, $y + 4z = 0$ as $Ax = b$.
With the unknowns in the order $x, y, z$, the matrix is $A = \begin{pmatrix} 2 & 0 & -1 \\ 0 & 1 & 4 \end{pmatrix}$ and $b = (1, 0)^{\mathsf{T}}$.

## Explanations

### L1 human

A system of linear equations is a set of linear equations that must all be true at the same time.
For example, $x + y = 3$ and $x - y = 1$ have the single common solution $x = 2$, $y = 1$.
With two unknowns, each equation draws a line, and a solution is a point where all the lines meet.
Two lines can cross in one point, be parallel and never meet, or be the same line.
So a system has one solution, no solution, or infinitely many solutions.

### L2 human

Here is the standard way to solve $x + y + z = 6$, $2x - y + z = 3$, $x + 2y - z = 2$.
First remove $x$ from the second and third equations with $R_2 - 2R_1$ and $R_3 - R_1$:
$$-3y - z = -9, \qquad y - 2z = -4.$$
Swap these two so that $y - 2z = -4$ comes second, and then remove $y$ from the last equation with $R_3 + 3R_2$:
$$-7z = -21, \qquad \text{so } z = 3.$$
Back substitution gives $y = -4 + 2z = 2$ and then $x = 6 - y - z = 1$.
Check in all three original equations: $1 + 2 + 3 = 6$, $2 - 2 + 3 = 3$ and $1 + 4 - 3 = 2$.
The final check matters, because one wrong row operation changes the solution set without any warning.

### L3 human

The system $Ax = b$ asks whether $b$ is in the image of the [[linear map|0NRYHJPQG2]] $x \mapsto Ax$ from $F^n$ to $F^m$, and for the full preimage of $b$.
So the solution set is a fiber of a linear map: empty, or a translate of the kernel, by the [[structure theorem|PDH3HKXWAZ]].
The rank of $A$ governs everything: the [[Rouché-Capelli theorem|0HV1SKWPMS]] decides consistency, and the solution set has dimension $n - \rank A$.
For large systems over $\mathbb{R}$, numerical linear algebra adds pivoting strategies and iterative methods to exact elimination.
Over $\mathbb{Z}$ or another ring, solvability needs more than ranks, for example the Smith normal form.
Systems without a solution are still useful: [[least squares|0BYTQ4X1HC]] finds the $x$ that makes $Ax$ closest to $b$.
