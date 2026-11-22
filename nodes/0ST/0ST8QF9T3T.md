---
tag: 0ST8QF9T3T
kind: definition
name: Adjoint of a linear map
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
defines: 0R9NMSM1ZP
uses: [01EK923SKP, 0RJF668P1T, 0NRYHJPQG2, E0KFAXMTC2]
formal:
  - system: lean4
    library: mathlib
    decl: LinearMap.adjoint
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780135367971
    locator: Section 8.3
---

## Definition

The adjoint of a linear map is the map that moves it from the first slot of the inner product to the second slot.
Let $V$ and $W$ be finite-dimensional [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *adjoint* of $T$ is the map $T^* \colon W \to V$ such that
$$\ip{Tv}{w} = \ip{v}{T^* w} \qquad \text{for all } v \in V \text{ and } w \in W.$$
By the [[existence theorem|E0KFAXMTC2]], exactly one map $T^*$ has this property, and $T^*$ is linear.

## Notation

The inner product is linear in the first slot and conjugate linear in the second slot.
When $V = W$, the adjoint is again an operator on $V$, so we can compare $T$ with $T^*$, add them and multiply them.
For a matrix $A$, the symbol $A^*$ is the [[conjugate transpose|0EX045E2BP]] $\overline{A}^{\mathsf{T}}$, and over $\mathbb{R}$ it is the transpose $A^{\mathsf{T}}$.
Physics books often write $T^\dagger$ for $T^*$.

## Remarks

Each part of the definition has a job.
The two inner products are part of the data: the identity compares a number computed in $W$ with a number computed in $V$.
So the same map has different adjoints for different inner products, as the [[weighted example|CPQB5HABC6]] shows.
Finite dimension makes the definition safe, because the [[Riesz representation theorem|04GYPXDXNH]] then gives, for each $w$, the vector $u$ with $\ip{Tv}{w} = \ip{v}{u}$ for all $v$, and $T^* w$ is that $u$.
The identity must hold for every pair $v$, $w$, and this is what makes the map unique.

Here is a small example.
On $\mathbb{R}^2$ with the dot product, let $T(x_1, x_2) = (x_2, 0)$.
Then $\ip{Tx}{y} = x_2 y_1$, and the map $S(y_1, y_2) = (0, y_1)$ gives $\ip{x}{Sy} = x_2 y_1$ as well, so $T^* = S$.
Now replace the dot product by $\ip{x}{y} = 2 x_1 y_1 + x_2 y_2$.
The same $S$ gives $\ip{x}{Sy} = x_2 y_1$, but now $\ip{Tx}{y} = 2 x_2 y_1$, so the identity fails at $x = (0, 1)$, $y = (1, 0)$, and $S$ is no longer the adjoint.

Conjugate symmetry gives the mirror form $\ip{T^* w}{v} = \ip{w}{Tv}$, so the adjoint can also move from the left slot to the right slot.
The concept page on the [[adjoint of a linear map|0R9NMSM1ZP]] works more examples.
The rules for sums, scalar multiples, products and inverses are the [[algebraic properties|TPP76FP659]], and in orthonormal bases the matrix of $T^*$ is the conjugate transpose, by the [[matrix of the adjoint|0DBTE6HVBD]].

## Explanations

### L1 human

An inner product combines two vectors into one number.
A linear map $T$ can act on the first vector before we combine them.
The adjoint is the map that gives the same number when it acts on the second vector instead.
For a real matrix and the dot product, the adjoint is the transpose.
For example, with rows $(0, 1)$ and $(0, 0)$, the vectors $(0, 1)$ and $(1, 0)$ give the number $1$ both ways.

### L2 human

Here we compute an adjoint from the definition alone, without a matrix.
Let $V = \mathbb{C}^2$ with $\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2}$, and let $T(x_1, x_2) = (i x_2, 0)$.
For $w = (w_1, w_2)$ we get $\ip{Tx}{w} = i x_2 \overline{w_1}$.
We need a vector $u$ with
$$x_1 \overline{u_1} + x_2 \overline{u_2} = i x_2 \overline{w_1} \qquad \text{for all } x.$$
Compare the coefficients of $x_1$ and $x_2$: $\overline{u_1} = 0$ and $\overline{u_2} = i \overline{w_1}$, so $u_2 = -i w_1$.
Hence $T^*(w_1, w_2) = (0, -i w_1)$.
Check: the matrix of $T$ is $\begin{pmatrix} 0 & i \\ 0 & 0 \end{pmatrix}$, and its conjugate transpose $\begin{pmatrix} 0 & 0 \\ -i & 0 \end{pmatrix}$ is the matrix of the map we found.
Watch out: the answer has $-i$ and not $i$, because the second slot is conjugate linear.

### L3 human

The definition is the finite-dimensional case of the [[adjoint of a bounded operator|6HSJBJ8TTQ]] on a Hilbert space, where the [[Riesz theorem for Hilbert spaces|TTC40N49M6]] gives existence.
For unbounded operators the defining identity holds only on a domain, and the adjoint can fail to be densely defined.
On the operators of one space, $T \mapsto T^*$ is an involution, and this involution is the model for $C^*$-algebras.
