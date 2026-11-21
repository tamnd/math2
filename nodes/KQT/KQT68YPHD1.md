---
tag: KQT68YPHD1
kind: concept
name: Parametric form of the solution set
aliases: [parametric-vector-form, general-solution-of-a-linear-system]
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
uses: [0GT4WWGWH2, 0J0BBCMJ5W, 0WF5AQYTW6, P3HMRQN5KT, 0V8F3E48E6]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Describing the solution
---

## Summary

An infinite solution set can be written down with finitely many vectors: one starting point and one direction for each free choice.
The parametric form of the solution set of a consistent [[linear system|0GT4WWGWH2]] $Ax = b$ over a field $F$ writes every solution as
$$x = p + t_1 v_1 + \dots + t_k v_k, \qquad t_1, \dots, t_k \in F,$$
where $k$ is the number of [[free variables|0J0BBCMJ5W]].
We find it from the [[reduced row echelon form|0WF5AQYTW6]] of $[A \mid b]$: each free variable becomes a parameter $t_l$, and each row gives one basic variable in terms of the parameters.
The vector $p$ is the solution with all parameters $0$, and $v_l$ is the coefficient vector of $t_l$.
Every choice of $(t_1, \dots, t_k)$ gives exactly one solution, and every solution comes from exactly one choice, by [[the lemma on systems in RREF|P3HMRQN5KT]].

## Motivation

The single equation $x + y = 2$ over $\mathbb{R}$ has infinitely many solutions, so we cannot list them.
Choose $y = t$; then $x = 2 - t$, and the solutions are $(2, 0) + t(-1, 1)$.
This lists a starting point and one direction instead of all the points.
In $\mathbb{R}^n$ the form also shows the shape: the solution set is a point, a line, a plane, or a flat of higher dimension.

## Notation

The scalar form gives each variable separately, for example $x_1 = 3 - 2t$, $x_2 = 1 + t$, $x_3 = t$.
The vector form groups the same data as $x = (3, 1, 0) + t(-2, 1, 1)$, and Lay calls it the parametric vector form.
Some books call the parametric form the general solution of the system.

## Remarks

### A worked case

We solve $x_1 + 2x_2 - x_3 = 1$, $x_3 = 2$ over $\mathbb{R}$.
The augmented matrix $\left[\begin{array}{rrr|r} 1 & 2 & -1 & 1 \\ 0 & 0 & 1 & 2 \end{array}\right]$ is in echelon form, and $R_1 \leftarrow R_1 + R_2$ gives the RREF row $(1, 2, 0 \mid 3)$.
The pivots are in columns 1 and 3, so $x_2$ is free, and we put $x_2 = t$.
The rows give $x_1 = 3 - 2t$ and $x_3 = 2$, so $x = (3, 0, 2) + t(-2, 1, 0)$, a line in $\mathbb{R}^3$.
Check: $(3 - 2t) + 2t - 2 = 1$ and $x_3 = 2$, for every $t$.

### More examples

In [[two planes meeting in a line|PRB44DTZ1P]] the solution set is $(2, 1, 0) + t(-2, 1, 1)$, a line in $\mathbb{R}^3$.
In [[a linear equation whose solutions form a plane|MT2XRG51GF]] one equation in three unknowns gives two parameters, a plane.
In [[a homogeneous system with two free variables|3GN7PFNRV2]] we get $p = 0$ and two direction vectors.
In [[a system solved by Gauss-Jordan elimination|F91EH08466]] the solution set is a line in $\mathbb{R}^4$.
A system with a unique solution has $k = 0$, and its parametric form is the single point $p$.

### What is not a parametric form

[[Redundant parameters for a line|PMQPQBZVH3]] describes the right set with two parameters, but different parameter values give the same point.
An inconsistent system, such as $x + y = 1$, $x + y = 2$, has no parametric form, since there is no point $p$.
The description $\{(x, y) : x + y = 1\}$ is an implicit form by an equation, not a parametric form.

### What the pieces are

The vector $p$ is one particular solution of $Ax = b$, and each $v_l$ is a solution of the homogeneous system $Ax = 0$.
The vectors $v_1, \dots, v_k$ are linearly independent: if $f_l$ is the column of the $l$-th free variable, entry $f_l$ of $v_l$ is $1$, and entry $f_l$ of every other $v_j$ is $0$.
So $v_1, \dots, v_k$ form a basis of the null space of $A$, and $k = n - \operatorname{rank} A$, by [[the structure of the solution set|PDH3HKXWAZ]].
Over a field with $q$ elements the solution set has $q^k$ elements, by [[the theorem on finite fields|8QM2Y41P69]].

### Watch out

The parameters must be the free variables; if a basic variable is made a parameter, some choices can give no solution.
Read the form from the reduced echelon form, or do back substitution first.
Each $v_l$ has the entry $1$ in the place of its own free variable, and it is easy to forget.

### Try it

Write the solutions of $x_1 - x_2 + 2x_3 = 4$ over $\mathbb{R}$ in parametric form.
With $x_2 = s$ and $x_3 = t$, we get $x = (4, 0, 0) + s(1, 1, 0) + t(-2, 0, 1)$, a plane.

## Explanations

### L1 human

When a system has many solutions, we describe them all with a formula.
We choose the free unknowns as we like, and we give each one a letter such as $t$.
The other unknowns are then fixed by the equations.
For example, for $x + y = 2$ the solutions are $x = 2 - t$, $y = t$, that is, $(2, 0) + t(-1, 1)$.

### L2 human

The typical use is to describe the general solution of a system with free variables.
Reduce to RREF, name the free variables, solve each row for its pivot variable, and collect the coefficients of each parameter into a vector.
Watch out: the parametric form is not unique, since another particular solution, or another basis of the null space, gives the same set.

### L3 human

The parametric form is a bijection $F^k \to S$, $t \mapsto p + Vt$, where $V$ is the $n \times k$ matrix with columns $v_l$.
It is an affine isomorphism of $F^k$ onto the affine subspace $S$, see [[affine subspace|0PYW26VNT6]].
In geometry this is the [[vector equation of a line|0399QFDFS8]] for $k = 1$, and the parametric equation of a [[plane|07SDJ5DNE4]] for $k = 2$.
