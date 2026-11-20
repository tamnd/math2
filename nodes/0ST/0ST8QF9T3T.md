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

Let $V$ and $W$ be finite-dimensional [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *adjoint* of $T$ is the map $T^* \colon W \to V$ such that
$$\ip{Tv}{w} = \ip{v}{T^* w} \qquad \text{for all } v \in V \text{ and } w \in W.$$
By [[the existence theorem|E0KFAXMTC2]], exactly one map $T^*$ has this property, and $T^*$ is linear.

## Notation

- The inner product is linear in the first slot and conjugate linear in the second slot.
- When $V = W$, the adjoint $T^*$ is again a map from $V$ to $V$, and we can compare $T$ with $T^*$.
- For a matrix $A$, the symbol $A^*$ is the [[conjugate transpose|0EX045E2BP]]. Over $\mathbb{R}$ it is the transpose $A^T$.

## Remarks

- The adjoint depends on the inner products on $V$ and on $W$. The same map has different adjoints for different inner products, as [[the weighted example|CPQB5HABC6]] shows.
- To compute $T^*(w)$ for a given $w$, find the vector $u \in V$ with $\ip{Tv}{w} = \ip{v}{u}$ for all $v$. The [[Riesz representation theorem|04GYPXDXNH]] gives this $u$.
- The equivalent identity $\ip{T^* w}{v} = \ip{w}{Tv}$ follows from the definition by conjugate symmetry. So the adjoint can also move from the left slot to the right slot.
- The rules for sums, scalar multiples, products and inverses are in [[the algebraic properties|TPP76FP659]].
- In orthonormal bases, the matrix of $T^*$ is the conjugate transpose of the matrix of $T$, by [[the matrix of the adjoint|0DBTE6HVBD]].

## Explanations

### L1 human

An inner product combines two vectors into one number.
A linear map $T$ can act on the first vector before we combine.
The adjoint is the map that gives the same number when it acts on the second vector instead.
For a real matrix and the dot product, the adjoint is the transpose: $(Ax) \cdot y = x \cdot (A^T y)$.
For example, with $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $x = (0, 1)$ and $y = (1, 0)$, both sides equal $1$.

### L2 human

Worked example: we compute an adjoint from the definition, without a matrix.

1. Let $V = \mathbb{C}^2$ with $\ip{x}{y} = x_1 \overline{y_1} + x_2 \overline{y_2}$, and let $T(x_1, x_2) = (i x_2, 0)$.
2. For $w = (w_1, w_2)$, we compute $\ip{Tx}{w} = i x_2 \overline{w_1}$.
3. We need $u$ with $\ip{x}{u} = x_1 \overline{u_1} + x_2 \overline{u_2} = i x_2 \overline{w_1}$ for all $x$.
4. Comparing coefficients gives $\overline{u_1} = 0$ and $\overline{u_2} = i \overline{w_1}$, so $u_2 = -i w_1$.
5. Hence $T^*(w_1, w_2) = (0, -i w_1)$.
6. The matrix of $T$ is $\begin{pmatrix} 0 & i \\ 0 & 0 \end{pmatrix}$, and its conjugate transpose $\begin{pmatrix} 0 & 0 \\ -i & 0 \end{pmatrix}$ is the matrix of $T^*$, as expected.

The typical use of the adjoint is to move a map from one slot to the other inside a computation.
A trap: over $\mathbb{C}$, the answer has $-i$ and not $i$, because the second slot is conjugate linear.

### L3 human

The definition is the finite-dimensional case of the [[adjoint of a bounded operator|6HSJBJ8TTQ]] on a Hilbert space, where the [[Riesz theorem for Hilbert spaces|TTC40N49M6]] gives existence.
For unbounded operators the defining identity holds only on a domain, and the adjoint can fail to be densely defined.
Algebraically, $T \mapsto T^*$ is an involution on the algebra of operators on $V$, and this involution is the model for $C^*$-algebras.
