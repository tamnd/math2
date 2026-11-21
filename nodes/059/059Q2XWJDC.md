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

The volume of a slanted box can be read off from a single determinant.
Let $a = (a_1, a_2, a_3)$, $b = (b_1, b_2, b_3)$ and $c = (c_1, c_2, c_3)$ be vectors in $\mathbb{R}^3$.
Let $\times$ be the [[cross product|0N5N15HWZ7]] and $\cdot$ the [[dot product|0S52TNNTH9]].
Then the [[scalar triple product|34VJYG6GVD]] is the [[determinant|00KDZRW4C0]] of the matrix with rows $a$, $b$ and $c$:
$$a \cdot (b \times c) = \det \begin{pmatrix} a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \\ c_1 & c_2 & c_3 \end{pmatrix}.$$

## Remarks

### Why each hypothesis is needed

The identity holds for all $a, b, c \in \mathbb{R}^3$, with no further hypothesis.
The space must be $\mathbb{R}^3$, because the cross product and the $3 \times 3$ determinant both need exactly three coordinates.

### What it gives you

The rules for determinants turn into rules for the triple product.
A cyclic shift of the rows is two row swaps, so the value does not change:
$$a \cdot (b \times c) = b \cdot (c \times a) = c \cdot (a \times b).$$
A single swap of two vectors is one row swap, so it changes the sign.
Combining the cyclic symmetry with the symmetry of the dot product gives $a \cdot (b \times c) = (a \times b) \cdot c$, so dot and cross may be exchanged.

A determinant with two equal rows is $0$, so the triple product vanishes whenever two of the vectors are equal.
More generally the determinant is $0$ exactly when the rows are linearly dependent, which gives the [[volume and coplanarity test|7RMCRQ9ERC]] a second proof.

### The converse

The formula determines $b \times c$.
The vector $w = b \times c$ is the only vector with $a \cdot w = \det(a, b, c)$ for all $a$.
Putting $a = \mathbf{i}, \mathbf{j}, \mathbf{k}$ in turn reads off the three components of $w$ as signed $2 \times 2$ minors.

### Beyond three dimensions

In $\mathbb{R}^n$ the determinant of $n$ vectors is the signed volume of the parallelotope they span, as the page on [[signed volume|04X3PR72VJ]] explains.
The same trick defines a cross product of $n - 1$ vectors $a_2, \ldots, a_n$ in $\mathbb{R}^n$: it is the vector $w$ with $a_1 \cdot w = \det(a_1, \ldots, a_n)$ for all $a_1$.

## Explanations

### L1 human

The scalar triple product of three arrows is the volume of the slanted box they make, with a sign.
This statement gives a way to compute it: write the three vectors as the rows of a $3 \times 3$ table, and take its determinant.
For the unit arrows $(1, 0, 0)$, $(0, 1, 0)$ and $(0, 0, 1)$ the table is the identity, and both sides are $1$.

### L2 human

Here is a check with $a = (1, 2, 3)$, $b = (0, 1, 4)$ and $c = (5, 6, 0)$.
Through the cross product, $b \times c = (-24, 20, -5)$, so $a \cdot (b \times c) = -24 + 40 - 15 = 1$.
Through the Laplace expansion along the first row,
$$1 \cdot (0 - 24) - 2 \cdot (0 - 20) + 3 \cdot (0 - 5) = -24 + 40 - 15 = 1.$$
The two computations use the same nine products in the same order, as the proof shows.
Watch out: the minus sign on the middle term of the Laplace expansion is the same sign as in the middle component of the cross product, and forgetting it in one place but not the other breaks the agreement.

### L3 human

Both sides are trilinear and alternating in $(a, b, c)$, and both equal $1$ at $(\mathbf{i}, \mathbf{j}, \mathbf{k})$.
The space of alternating trilinear forms on $\mathbb{R}^3$ has dimension $1$, so the two sides agree, and the sub-area on [[determinants|DTBK11SR77]] proves this uniqueness.
