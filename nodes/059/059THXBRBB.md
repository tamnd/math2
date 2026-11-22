---
tag: 059THXBRBB
kind: statement
role: proposition
name: Isomorphism with the coordinate space
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
about: [04CYQHN6MC]
uses: [0BMVBHTWV2, 0XSJ25Z9M4]
proofs: [C5282SWAEV]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_vector
    locator: The standard representation
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Statement

A choice of ordered basis turns a vector space of dimension $n$ into a faithful copy of $F^n$.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $B = (b_1, \dots, b_n)$ be an ordered basis of $V$.
Then the map
$$\varphi_B \colon V \to F^n, \qquad v \mapsto [v]_B,$$
which sends each vector to its [[coordinate vector|0BMVBHTWV2]], is a [[linear isomorphism|0B8T10CE7N]].
Its inverse sends $(a_1, \dots, a_n)$ to $a_1 b_1 + \dots + a_n b_n$.

## Remarks

### A check with polynomials

Take $V = P_2(\mathbb{R})$ with the basis $B = (1, x - 1, (x - 1)^2)$.
Since $x^2 = 1 + 2(x - 1) + (x - 1)^2$ and $x = 1 + (x - 1)$,
$$[x^2]_B = (1, 2, 1)^{\mathsf{T}}, \qquad [x]_B = (1, 1, 0)^{\mathsf{T}}.$$
Linearity predicts
$$[x^2 + 3x]_B = (1, 2, 1)^{\mathsf{T}} + 3 (1, 1, 0)^{\mathsf{T}} = (4, 5, 1)^{\mathsf{T}}.$$
Check by the inverse map: $4 + 5(x - 1) + (x - 1)^2 = 4 + 5x - 5 + x^2 - 2x + 1 = x^2 + 3x$.

### Why each hypothesis is needed

The family $B$ must be a basis.
For the spanning family $((1, 0), (0, 1), (1, 1))$ of $\mathbb{R}^2$, coordinates are not unique, so $v \mapsto [v]_B$ is not even a well-defined map.
For an independent family that does not span, such as $((1, 0, 0))$ in $\mathbb{R}^3$, coordinates exist only for vectors in the span, so the map is defined only on a subspace.

The basis must be ordered, or the target $F^n$ makes no sense.
Reversing the order of $(b_1, b_2)$ reverses the order of the two coordinates, and so it gives a different isomorphism.

### What it gives you

The isomorphism sends $b_i$ to the standard basis vector $e_i$, and it preserves sums and scalar multiples.
So every question about independence, span or bases in $V$ becomes the same question about columns in $F^n$, where row reduction answers it.
It also shows that any two spaces of the same finite dimension $n$ are isomorphic, since both are isomorphic to $F^n$; this is the [[classification by dimension|0VJBSK15SN]].

Watch out: the isomorphism depends on the basis.
In $\mathbb{R}^2$, the standard basis sends $(3, 1)$ to $(3, 1)^{\mathsf{T}}$, while the basis $((1, 1), (1, -1))$ sends it to $(2, 1)^{\mathsf{T}}$.
No choice is better than another for an abstract space, so $V \cong F^n$ is an isomorphism, not an identification.

### The converse

Every linear isomorphism $\psi \colon V \to F^n$ is the coordinate map of exactly one ordered basis, namely $b_i = \psi^{-1}(e_i)$.
Indeed $\psi$ and $\varphi_B$ are linear and both send $b_i$ to $e_i$, and two linear maps that [[agree on a basis are equal|0R8X9XA83A]].
So the ordered bases of $V$ correspond one to one to the isomorphisms $V \to F^n$.

### Generalizations

For a basis $(b_i)_{i \in I}$ of any vector space, the map $v \mapsto (a_i)_{i \in I}$ is a linear isomorphism from $V$ onto the space $F^{(I)}$ of finitely supported families.
In Mathlib this map is `Module.Basis.repr`, and it is the data from which a basis is built.

## Explanations

### L1 human

Choosing a basis turns every vector into a list of $n$ numbers.
This translation respects addition and stretching: the list for $u + v$ is the sum of the lists for $u$ and $v$.
It also loses no information, because the vector can be rebuilt from its list.
So an $n$-dimensional space is a copy of the lists of $n$ numbers, once a basis is fixed.

### L2 human

Here is a typical use: are $p_1 = 1 + x$, $p_2 = x + x^2$ and $p_3 = 1 + x^2$ independent in $P_2(\mathbb{R})$?
In the monomial basis $(1, x, x^2)$ they have the coordinate vectors $(1, 1, 0)$, $(0, 1, 1)$ and $(1, 0, 1)$.
The coordinate map is an isomorphism, so the polynomials are independent exactly when these columns are.
The matrix with these columns has determinant $1 \cdot (1 - 0) - 0 + 1 \cdot (1 - 0) = 2 \ne 0$, so the columns are independent, and so are $p_1, p_2, p_3$.
Watch out: over the field $\mathbb{F}_2$ the determinant $2$ is $0$, and indeed $p_1 + p_2 + p_3 = 2 + 2x + 2x^2 = 0$ there.

### L3 human

The statement says that $F^n$ with its standard basis is a free vector space on $n$ generators: a basis of $V$ is the same as a linear isomorphism $F^n \to V$.
In the language of categories, the finite-dimensional spaces over $F$ are equivalent to the category whose objects are the numbers $n$ and whose arrows are matrices.
The sub-area on linear maps builds on this to represent every linear map by a matrix, and the sub-area on duality explains what is lost when no basis is chosen.
