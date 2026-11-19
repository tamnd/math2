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

A homogeneous system of linear equations is a [[system of linear equations|0GT4WWGWH2]] in which every constant term is zero, so in matrix form it is $Ax = 0$.
The exact definition is in [[the definition node|06JT7KDHXM]].
Such a system always has the trivial solution $x = 0$, and its solution set is a [[linear subspace|00YC1D652K]] of $F^n$, the [[null space|0PHDYNR24D]] of $A$.
It has a nontrivial solution exactly when some column of $A$ has no pivot, and this always happens when there are more unknowns than equations, see [[the theorem|JPW6KVS70A]].
Homogeneous systems matter because the solutions of every consistent system $Ax = b$ are one particular solution plus the solutions of $Ax = 0$, see [[the structure theorem|PDH3HKXWAZ]].

## Motivation

Linear independence asks whether $c_1 v_1 + \cdots + c_n v_n = 0$ forces all $c_j = 0$.
In coordinates this is a homogeneous system in the unknowns $c_j$.
Eigenvectors are the nonzero solutions of $(A - \lambda I)x = 0$, again a homogeneous system.
Balancing a chemical equation, or finding the steady state of a network, also leads to $Ax = 0$.
So the question "does $Ax = 0$ have a nonzero solution?" appears everywhere in linear algebra.

## Notation

1. The homogeneous system $Ax = 0$ is called the homogeneous system associated with $Ax = b$.
2. Its solution set is written $N(A)$, $\operatorname{Nul} A$ or $\ker A$.
3. The solution $x = 0$ is the trivial solution; any other solution is nontrivial.

## Remarks

### Examples

1. The system $x_1 + 2x_2 - x_3 + x_4 = 0$, $2x_1 + 4x_2 + x_3 + 5x_4 = 0$ has a two-parameter family of solutions, see [[the 2 by 4 example|3GN7PFNRV2]].
2. The system with the coefficient matrix of [[the three planes example|YM0PB9F9HG]] has only the trivial solution, see [[the trivial-solution example|8QMWDVE4RE]].
3. The single equation $x + y + z = 0$ over $\R$ has a plane through the origin as its solution set.
4. The conditions $c_1 (1, 2) + c_2 (2, 4) = 0$ give the homogeneous system $c_1 + 2c_2 = 0$, $2c_1 + 4c_2 = 0$, with the nontrivial solution $(2, -1)$.

### Non-examples

1. The system $x + y = 1$, $x - y = 0$ is not homogeneous, and its solution set $\set{(\tfrac12, \tfrac12)}$ is not a subspace, see [[the non-homogeneous example|J291MKHE97]].
2. The equation $x^2 + y^2 = 0$ has zero right side, but it is not linear, so it is not a homogeneous linear system.

### Basic properties

1. $x = 0$ is a solution, so a homogeneous system is always consistent.
2. If $u$ and $v$ are solutions and $c \in F$, then $u + v$ and $cu$ are solutions, because $A(u + v) = Au + Av = 0$ and $A(cu) = cAu = 0$.
3. So the solution set is a subspace of $F^n$, the null space of $A$.
4. A nontrivial solution exists if and only if the reduced row echelon form of $A$ has a free column.
5. If $n > m$, a nontrivial solution exists, see [[the theorem on homogeneous systems|JPW6KVS70A]].
6. The dimension of the solution set is $n - r$, where $r$ is the number of pivots, see [[the parametric form|KQT68YPHD1]].

### History

Homogeneous systems appear in the elimination problems of the *Nine Chapters* and in all later work on linear systems.
Many textbooks, for example Hoffman and Kunze, use the fact that more unknowns than equations give a nonzero solution to prove that dimension is well defined.

### Common errors

1. Saying that a homogeneous system "has no solution" when elimination gives only $x = 0$. It has exactly one solution, the trivial one.
2. Augmenting a homogeneous system with a zero column and then reducing it; this is correct but wastes work, since the zero column stays zero.
3. Assuming that a square homogeneous system has only the trivial solution. The system $x + y = 0$, $2x + 2y = 0$ has the nontrivial solution $(1, -1)$.

## Explanations

### L1 human

A homogeneous system has zero on the right side of every equation.
Setting every unknown to zero always works, so these systems always have at least one solution.
The interesting question is whether there are other solutions.
If you have fewer equations than unknowns, there always are.
Adding two solutions, or multiplying a solution by a number, gives a new solution.

### L2 human

We solve $x + 2y - z = 0$, $2x + 5y + z = 0$.

1. $R_2 \leftarrow R_2 - 2R_1$ gives $(0, 1, 3)$.
2. $R_1 \leftarrow R_1 - 2R_2$ gives $(1, 0, -7)$.
3. So $x = 7z$ and $y = -3z$, with $z = t$ free.
4. The solutions are $t(7, -3, 1)$, a line through the origin.
5. Check $t = 1$: $7 - 6 - 1 = 0$ and $14 - 15 + 1 = 0$.

The typical use is to test linear independence or to find a basis of a null space.
A trap: the zero right-hand side is not written in the reduced matrix, but it is still there; do not read a zero row as $0 = 0$ of a different system.

### L3 human

The solution set of $Ax = 0$ is the kernel of the [[linear map|0NRYHJPQG2]] $x \mapsto Ax$.
By [[rank-nullity|0W4FSW1TVB]], its dimension is $n - \rank A$.
For linear differential equations the same pattern holds: the [[superposition principle|0F2VBPXNP9]] says that solutions of the homogeneous equation form a vector space.
The [[general solution of an inhomogeneous equation|0GHWEH6H15]] is a particular solution plus the homogeneous solutions, just as for algebraic systems.
