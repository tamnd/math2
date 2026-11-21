---
tag: 04KGXJG1A2
kind: concept
name: Homogeneous system of linear equations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
specializes: [0GT4WWGWH2]
uses: [0GT4WWGWH2, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Homogeneous systems
  - book: isbn:9780321982384
    locator: Section 1.5
  - book: isbn:9780135367971
    locator: Chapter 1
---

## Summary

A homogeneous system is a system of linear equations whose right sides are all zero.
It always has the solution $x = 0$, and the real question is whether it has others.
In matrix form a homogeneous system is
$$Ax = 0,$$
a [[system of linear equations|0GT4WWGWH2]] in which every constant term is zero, as the [[formal definition|06JT7KDHXM]] states.
Its solution set is a [[linear subspace|00YC1D652K]] of $F^n$, the [[null space|0PHDYNR24D]] of $A$.
It has a solution other than $0$ exactly when some column of $A$ has no pivot, and this always happens when there are [[more unknowns than equations|JPW6KVS70A]].

## Motivation

The question "does $Ax = 0$ have a nonzero solution?" turns up all over linear algebra.
Vectors $v_1, \dots, v_n$ are linearly independent when $c_1 v_1 + \cdots + c_n v_n = 0$ forces all $c_j = 0$, and in coordinates this is a homogeneous system in the unknowns $c_j$.
Eigenvectors are the nonzero solutions of $(A - \lambda I)x = 0$.
Balancing a chemical equation, or finding the steady state of a network, also leads to $Ax = 0$.

Homogeneous systems also explain every other system.
The solutions of a consistent system $Ax = b$ are one particular solution plus the solutions of $Ax = 0$, by the [[structure theorem|PDH3HKXWAZ]].
So once you understand the homogeneous system, you understand the shape of every solution set with the same coefficient matrix.

## Notation

For a system $Ax = b$, the system $Ax = 0$ is called its associated homogeneous system.
The solution set of $Ax = 0$ is written $N(A)$, $\operatorname{Nul} A$ or $\ker A$, depending on the book.
The solution $x = 0$ is the trivial solution, and every other solution is nontrivial.

## Remarks

### Solutions can be added and scaled

Take $x + 2y - z = 0$ and $2x + 5y + z = 0$ over $\mathbb{R}$.
Reduce the coefficient matrix with $R_2 - 2R_1$ and then $R_1 - 2R_2$:
$$\begin{pmatrix} 1 & 2 & -1 \\ 2 & 5 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 2 & -1 \\ 0 & 1 & 3 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & -7 \\ 0 & 1 & 3 \end{pmatrix}.$$
So $x = 7z$ and $y = -3z$, and with $z = t$ the solutions are $t(7, -3, 1)$, a line through the origin.
Check: $7 - 6 - 1 = 0$ and $14 - 15 + 1 = 0$.

This line passes through the origin, and that is no accident.
If $u$ and $v$ are solutions and $c$ is a scalar, then
$$A(u + v) = Au + Av = 0 + 0 = 0, \qquad A(cu) = c\,Au = c \cdot 0 = 0.$$
So the solutions form a subspace of $F^n$.
For a larger case, the $2 \times 4$ system in [[a homogeneous system with two free variables|3GN7PFNRV2]] has a plane of solutions.

### When only the trivial solution exists

The coefficient matrix of [[three planes meeting in one point|YM0PB9F9HG]] has a pivot in every column.
So the system $Ax = 0$ with that matrix has no free variable, and $x = 0$ is its only solution, as [[a homogeneous system with only the trivial solution|8QMWDVE4RE]] shows.
In general, a nontrivial solution exists exactly when the echelon form of $A$ has a column without a pivot.
The number of free variables is $n - r$, where $r$ is the number of pivots, and this is the dimension of the solution set by the [[parametric form|KQT68YPHD1]].

### More unknowns than equations

If $n > m$, there are at most $m$ pivots, one in each row, so at least $n - m$ columns have no pivot.
So a homogeneous system with more unknowns than equations always has a nontrivial solution, which is the [[theorem on homogeneous systems|JPW6KVS70A]].
For example, the vectors $(1, 2)$, $(3, 1)$ and $(0, 5)$ in $\mathbb{R}^2$ must be dependent, because $c_1(1, 2) + c_2(3, 1) + c_3(0, 5) = 0$ is a system of $2$ equations in $3$ unknowns.

### What is not homogeneous

The system $x + y = 1$, $x - y = 0$ has a nonzero right side.
Its solution set $\set{(\tfrac12, \tfrac12)}$ does not contain $0$, so it is not a subspace, as [[a non-homogeneous system|J291MKHE97]] explains.
The equation $x^2 + y^2 = 0$ has a zero right side, but it is not linear, so it is not a homogeneous linear system.

### Watch out

When elimination gives only $x = 0$, the system does not "have no solution".
It has exactly one solution, the trivial one.
Do not assume that a square homogeneous system has only the trivial solution either: $x + y = 0$, $2x + 2y = 0$ has the solution $(1, -1)$.
You may augment $A$ with a zero column, but row operations keep that column zero, so you can leave it out.

### History

Homogeneous systems appear in the elimination problems of the *Nine Chapters* and in all later work on linear systems.
Many textbooks use the theorem on more unknowns than equations to prove that the dimension of a vector space is well defined.

### Try it

First, find all solutions of $x - y = 0$, $y - z = 0$ over $\mathbb{R}$.
The equations give $x = y = z$, so the solutions are $t(1, 1, 1)$ for $t \in \mathbb{R}$.

Second, must $4$ vectors in $\mathbb{R}^3$ be linearly dependent?
Yes: a dependence relation is a solution of a homogeneous system of $3$ equations in $4$ unknowns, and such a system has a nontrivial solution.

## Explanations

### L1 human

A homogeneous system has zero on the right side of every equation.
Setting every unknown to zero always works, so these systems always have at least one solution.
The interesting question is whether there are other solutions.
If you have fewer equations than unknowns, there always are.
Adding two solutions, or multiplying a solution by a number, gives another solution.

### L2 human

Here is a typical use: are $(1, 2)$ and $(2, 4)$ linearly independent?
We look for numbers $c_1, c_2$ with $c_1(1, 2) + c_2(2, 4) = (0, 0)$, which is the system
$$c_1 + 2c_2 = 0, \qquad 2c_1 + 4c_2 = 0.$$
The operation $R_2 - 2R_1$ turns the second equation into $0 = 0$, so $c_2$ is free and $c_1 = -2c_2$.
With $c_2 = -1$ we get the nontrivial solution $(2, -1)$, and indeed $2(1, 2) - (2, 4) = (0, 0)$.
So the vectors are dependent.
Watch out: in the reduced matrix the zero right side is not written, but it is still there, so a zero row means $0 = 0$ and never a contradiction.

### L3 human

The solution set of $Ax = 0$ is the kernel of the [[linear map|0NRYHJPQG2]] $x \mapsto Ax$.
By [[rank-nullity|0W4FSW1TVB]], its dimension is $n - \rank A$.
For linear differential equations the same pattern holds: the [[superposition principle|0F2VBPXNP9]] says that the solutions of a homogeneous equation form a vector space.
The [[general solution of an inhomogeneous equation|0GHWEH6H15]] is then a particular solution plus the homogeneous solutions, just as for algebraic systems.
