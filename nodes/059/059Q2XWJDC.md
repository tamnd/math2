---
tag: 059Q2XWJDC
kind: statement
role: proposition
name: Scalar triple product as a determinant
aliases: [mixed-product, box-product]
msc: ["15A72", "15A15"]
topics: [VKVAJ94SKZ]
audience: school
about: [34VJYG6GVD]
uses: [0N5N15HWZ7, 0S52TNNTH9, 34VJYG6GVD, 00KDZRW4C0]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
---

## Statement

Let $a = (a_1, a_2, a_3)$, $b = (b_1, b_2, b_3)$ and $c = (c_1, c_2, c_3)$ be vectors in $\mathbb{R}^3$.
Let $\times$ be the [[cross product|0N5N15HWZ7]] and let $\cdot$ be the [[dot product|0S52TNNTH9]].
Then the [[scalar triple product|34VJYG6GVD]] is the [[determinant|00KDZRW4C0]] of the matrix with the rows $a$, $b$ and $c$:
$$a \cdot (b \times c) = \det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b, c \in \mathbb{R}^3$, with no further hypothesis.
The space must be $\mathbb{R}^3$, because the cross product and the $3 \times 3$ determinant need three coordinates.

### Consequences

- Cyclic symmetry: $a \cdot (b \times c) = b \cdot (c \times a) = c \cdot (a \times b)$, since a cyclic shift of the rows is two row swaps.
- A swap of two of the vectors changes the sign, since a row swap changes the sign of a determinant.
- $a \cdot (b \times c) = (a \times b) \cdot c$, by cyclic symmetry and the symmetry of the dot product.
- The value is $0$ if two of the vectors are equal, since the determinant then has two equal rows.
- The [[volume and coplanarity test|7RMCRQ9ERC]] can be read off from the determinant: $\det = 0$ if and only if the rows are linearly dependent.

### Converse

The formula determines $b \times c$: the vector $w = b \times c$ is the only vector with $a \cdot w = \det(a, b, c)$ for all $a$.
Put $a = \mathbf{i}, \mathbf{j}, \mathbf{k}$ to get the three components of $w$ as $2 \times 2$ minors.

### Generalizations

In $\mathbb{R}^n$, the determinant of $n$ vectors is the signed volume of the parallelotope that they span; the [[signed volume|04X3PR72VJ]] node treats this.
The map $(a_2, \ldots, a_n) \mapsto$ the vector $w$ with $a_1 \cdot w = \det(a_1, \ldots, a_n)$ is a cross product of $n - 1$ vectors in $\mathbb{R}^n$.

## Explanations

### L1 human

The scalar triple product of three arrows is the volume of the slanted box they make, with a sign.
This statement gives a way to compute it: write the three vectors as the rows of a $3 \times 3$ table, and take its determinant.
For the unit arrows $(1, 0, 0)$, $(0, 1, 0)$ and $(0, 0, 1)$ the table is the identity, and both sides are $1$.

### L2 human

Worked check with $a = (1, 2, 3)$, $b = (0, 1, 4)$, $c = (5, 6, 0)$.

1. Cross product: $b \times c = (-24, 20, -5)$, so $a \cdot (b \times c) = -24 + 40 - 15 = 1$.
2. Laplace expansion along row $1$: $1 \cdot (0 - 24) - 2 \cdot (0 - 20) + 3 \cdot (0 - 5) = -24 + 40 - 15 = 1$.

The two computations are the same nine products in the same order, as the proof shows.
A trap: the minus sign on the middle term of the Laplace expansion is the same sign as in the middle component of the cross product.

### L3 human

Both sides are trilinear and alternating in $(a, b, c)$, and both are $1$ at $(\mathbf{i}, \mathbf{j}, \mathbf{k})$.
The space of alternating trilinear forms on $\mathbb{R}^3$ has dimension $1$, so the two sides agree; the sub-area on [[determinants|DTBK11SR77]] proves this uniqueness.
