---
tag: PRQAA1FA3Z
kind: example
name: Dimension classifies finite-dimensional vector spaces
msc: ["00A35", "15A03"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [9HQ3TADPA8]
uses: [9HQ3TADPA8, 0ZHWKQMVX5, 03GSZ8RTZJ, 0B8T10CE7N, 0VJBSK15SN, 0WK0Y8RH1M, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
---

## Example

Fix a field $F$.
Let $X$ be the class of [[finite-dimensional vector spaces|0ZHWKQMVX5]] over $F$, and let $\sim$ be the relation "is isomorphic to", where an isomorphism is a [[linear isomorphism|0B8T10CE7N]].
We show that the [[dimension|03GSZ8RTZJ]] $\dim V$ classifies $X$ up to $\sim$.

1. The dimension is well defined, because any two [[bases|0KCQ9Y3QKA]] of $V$ have the same number of elements, by the [[dimension theorem|0WK0Y8RH1M]].
2. The dimension is an invariant, because a linear isomorphism sends a basis to a basis, so isomorphic spaces have bases of the same size.
3. The dimension is complete.
   If $\dim V = \dim W = n$, choose bases $v_1, \ldots, v_n$ of $V$ and $w_1, \ldots, w_n$ of $W$.
   The linear map with $v_i \mapsto w_i$ for each $i$ is an isomorphism, since it sends a basis to a basis.
4. Steps 2 and 3 together are the theorem that [[finite-dimensional spaces are isomorphic exactly when their dimensions are equal|0VJBSK15SN]].
5. Every value $n \ge 0$ occurs.
   The space $F^n$ of columns with $n$ entries has the standard basis $e_1, \ldots, e_n$, so $\dim F^n = n$, and for $n = 0$ the space is $\{0\}$ with the empty basis.
6. So the list $F^0, F^1, F^2, \ldots$ contains exactly one space from each isomorphism class.

We test the classification on the space $P_2$ of real polynomials of degree at most $2$.
It has the basis $1, x, x^2$, so $\dim P_2 = 3 = \dim \mathbb{R}^3$, and the classification says $P_2 \cong \mathbb{R}^3$.
One isomorphism sends the coefficients to a column:
$$a + bx + cx^2 \longmapsto \begin{pmatrix} a \\ b \\ c \end{pmatrix}.$$
Check: the sum of $1 + 2x$ and $3x - x^2$ is $1 + 5x - x^2$, and the columns $(1, 2, 0)$ and $(0, 3, -1)$ add to $(1, 5, -1)$.

## Remarks

This is the simplest classification theorem of linear algebra: one natural number describes each space completely.
It also shows why classification is useful.
Every statement about a finite-dimensional space that isomorphisms preserve can be checked on $F^n$, where we compute with columns.

What changes when the setting changes?
If we drop the condition "finite-dimensional", the dimension becomes a cardinal number, and it is still a complete invariant.
If we replace the field $F$ by the ring $\mathbb{Z}$, the analogous objects are the finitely generated abelian groups, and one number is no longer enough: by the [[structure theorem|0RY0B72XAS]], the classification needs the rank and the torsion part.
If we classify pairs $(V, T)$ of a space and a linear map $T \colon V \to V$ up to change of basis, the dimension is far from complete, and over $\mathbb{C}$ the classification is the [[Jordan normal form|085HQ5G5TE]].

## Explanations

### L1 human

A vector space is a collection of arrows or lists of numbers that we can add and stretch.
The dimension counts how many independent directions it has.
A line has one direction, a plane has two, and space has three.
Two vector spaces with the same number of directions behave in exactly the same way, even if their elements look different.
For example, the polynomials $a + bx + cx^2$ behave like lists $(a, b, c)$ of three numbers.

### L2 human

Here is a typical use: is the space $M$ of real $2 \times 2$ matrices isomorphic to $\mathbb{R}^4$ or to $\mathbb{R}^3$?
The four matrices with one entry $1$ and the other entries $0$ form a basis of $M$, because
$$\begin{pmatrix} p & q \\ r & s \end{pmatrix} = p E_{11} + q E_{12} + r E_{21} + s E_{22}$$
in exactly one way.
So $\dim M = 4$, and the classification gives $M \cong \mathbb{R}^4$ and $M \not\cong \mathbb{R}^3$, since $4 \ne 3$.
The classification lets us move a problem from an unfamiliar space to $F^n$.
Watch out: the field must be fixed before the dimension classifies anything.
The complex numbers have dimension $1$ over $\mathbb{C}$ and dimension $2$ over $\mathbb{R}$.
