---
tag: 04CYQHN6MC
kind: concept
name: Coordinate vector
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0KCQ9Y3QKA, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3C
  - book: isbn:9780134860244
    locator: Section 2.2
same_as:
  wikidata: Q1057996
  wikipedia: Coordinate vector
---

## Summary

The coordinate vector of $v$ is the list of numbers that says how much of each basis vector you need to build $v$.
It turns an abstract vector, such as a polynomial or a matrix, into a column of numbers that we can compute with.
Let $B = (b_1, \dots, b_n)$ be an ordered [[basis|0KCQ9Y3QKA]] of a vector space $V$ over a field $F$.
Each $v \in V$ is $v = a_1 b_1 + \dots + a_n b_n$ for [[exactly one list of scalars|E2ZRZGXSNX]], and the *coordinate vector* of $v$ is the column
$$[v]_B = \begin{pmatrix} a_1 \\ \vdots \\ a_n \end{pmatrix} \in F^n,$$
as the [[definition|0BMVBHTWV2]] states.
The map $v \mapsto [v]_B$ is a [[linear isomorphism from V to F^n|059THXBRBB]].

## Motivation

Row reduction works on columns of numbers, not on polynomials or matrices.
Is $x^2 + 1$ a combination of $x^2 - x$ and $x + 1$?
After we choose a basis, the question becomes one about columns in $F^3$, and an ordinary linear system answers it.
In the basis $(1, x, x^2)$ the three polynomials have coordinates $(1, 0, 1)$, $(0, -1, 1)$ and $(1, 1, 0)$, and the first column is the sum of the other two.
So $x^2 + 1 = (x^2 - x) + (x + 1)$.
The translation respects sums and scalar multiples, so the answer translates back to the polynomials.

This is how linear algebra is done in practice: choose a basis, pass to coordinates, compute with matrices, and translate back.
The sub-area on linear maps uses coordinates to give every linear map a matrix, and the [[change of basis matrix|0MKRHZB3WS]] describes how coordinates change when the basis changes.

## Notation

We write $[v]_B$, usually as a column.
Some books write $\varphi_B(v)$, $\operatorname{coord}_B(v)$ or $v_B$.
The notation must show the basis, because the same vector has different coordinates in different bases.
In Mathlib, `b.repr v` gives the coordinates of `v` in the basis `b`, as a finitely supported function on the index type.

## Remarks

### First computations

In $F^n$ with the [[standard basis|C5QA672NPH]] $E$, the coordinates of a vector are its entries, so $[x]_E = x$.
Other bases give other numbers.
In $\mathbb{R}^2$ with $B = ((1, 1), (1, -1))$, the vector $(3, 1)$ satisfies
$$(3, 1) = 2 (1, 1) + 1 (1, -1), \qquad \text{so} \qquad [(3, 1)]_B = \begin{pmatrix} 2 \\ 1 \end{pmatrix}.$$
In the [[space of polynomials|0JGZCDT5DN]] $P_2(\mathbb{R})$ with $B = (1, x - 1, (x - 1)^2)$, we have $x^2 = 1 + 2(x - 1) + (x - 1)^2$, so $[x^2]_B = (1, 2, 1)^{\mathsf{T}}$.
In the [[space of matrices|0RE6X3BGPN]] $M_2(F)$ with the ordered basis $(E_{11}, E_{12}, E_{21}, E_{22})$, the coordinates of $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$ are $(a, b, c, d)^{\mathsf{T}}$.

### Why a basis, and why an order

Coordinates need both halves of a basis.
In the spanning family $S = ((1, 0), (0, 1), (1, 1))$ of $\mathbb{R}^2$, the vector $(1, 1)$ has the two coefficient lists $(1, 1, 0)$ and $(0, 0, 1)$, so "$[v]_S$" has no single value.
In the independent family $((1, 0, 0))$ of $\mathbb{R}^3$, the vector $(0, 1, 0)$ has no coefficient list at all.

Coordinates also need an order.
For the set $\{(1, 1), (1, -1)\}$, the list for $(3, 1)$ could be $(2, 1)$ or $(1, 2)$, depending on which vector we call first.
That is why the definition asks for an ordered basis.

### The rules you can use

The coordinate map is linear: $[v + w]_B = [v]_B + [w]_B$ and $[cv]_B = c [v]_B$, because adding two expressions in the basis adds their coefficients.
Each basis vector has coordinates $[b_i]_B = e_i$.
The map $v \mapsto [v]_B$ is a bijection onto $F^n$, so it is an isomorphism, by the [[isomorphism theorem for coordinates|059THXBRBB]].
As a result, a list of vectors of $V$ is independent, spans $V$ or is a basis exactly when the list of their coordinate vectors has the same property in $F^n$.
For two bases $B$ and $C$, the [[change of basis matrix|0MKRHZB3WS]] $P$ satisfies $[v]_C = P [v]_B$ for every $v$.

### Watch out

The coordinate vector depends on the basis and on its order, not only on $v$.
In $F^n$, the coordinates of $x$ in a basis $B$ are not its entries, unless $B$ is the standard basis.

The most common slip is to multiply when you should solve.
To find $[v]_B$ in $F^n$, let $A$ be the matrix with the vectors of $B$ as columns, and solve $Ac = v$.
With $B = ((1, 2), (3, 4))$ and $v = (5, 6)$, the answer is $c = (-1, 2)$, as the L2 explanation shows.
The product $Av = (23, 34)$ is a different vector, and it answers a different question.

### History

Descartes and Fermat introduced coordinates in the plane in the seventeenth century, to turn geometric curves into equations.
Coordinates with respect to an arbitrary basis came with the abstract theory of vector spaces.

### Try it

First, find the coordinates of $(4, 0)$ in the basis $B = ((1, 1), (1, -1))$ of $\mathbb{R}^2$.
Solve $c + d = 4$ and $c - d = 0$, so $c = d = 2$ and $[(4, 0)]_B = (2, 2)^{\mathsf{T}}$.

Second, find $[3 + 2x]_B$ in the basis $B = (1, x - 1)$ of $P_1(\mathbb{R})$.
Since $3 + 2x = 5 \cdot 1 + 2 (x - 1)$, the answer is $(5, 2)^{\mathsf{T}}$.

## Explanations

### L1 human

The coordinates of a vector tell you how much of each basis vector you need to build it.
Think of a recipe: with "east" and "north" as the basic steps, the point $(3, 2)$ is "3 east, 2 north", and its coordinates are $3$ and $2$.
With "north-east" and "east" as the basic steps, the same point is "2 north-east, 1 east", so its coordinates are $2$ and $1$.
The point did not move; only the recipe changed.
Once a basis is fixed, every vector is just a list of numbers.

### L2 human

Here is the typical computation in $F^n$: put the basis vectors as the columns of a matrix $A$ and solve $Ac = v$.
Take $B = ((1, 2), (3, 4))$ and $v = (5, 6)$.
The system is
$$c_1 + 3 c_2 = 5, \qquad 2 c_1 + 4 c_2 = 6.$$
Subtract twice the first equation from the second: $-2 c_2 = -4$, so $c_2 = 2$, and then $c_1 = 5 - 6 = -1$.
Check: $-1 \cdot (1, 2) + 2 \cdot (3, 4) = (-1 + 6, -2 + 8) = (5, 6)$, so $[v]_B = (-1, 2)^{\mathsf{T}}$.
For an abstract space, first pass to coordinates in a known basis, such as the monomials, and then solve the same kind of system.

### L3 human

The coordinate map $V \to F^n$ is the inverse of the isomorphism $F^n \to V$, $a \mapsto \sum_i a_i b_i$, that the basis defines.
So choosing an ordered basis is the same as choosing an isomorphism $V \cong F^n$, and the coordinate functions $v \mapsto a_i$ are the [[dual basis|0ZD2CF6ZS0]] of the sub-area on duality.
For an infinite basis $(b_i)_{i \in I}$, coordinates are finitely supported families, and the coordinate map is an isomorphism $V \to F^{(I)}$.
The fact that no isomorphism $V \cong F^n$ is preferred is the reason that coordinate-free definitions matter in later sub-areas.
