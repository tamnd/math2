---
tag: 0C3CFHDN6R
kind: definition
name: Determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
defines: 00KDZRW4C0
uses: [0MSWYWHYF5, 0CP7YY6NAG, 06DW9BAWB1, 1C8RRWHD45]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.det
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Over a commutative ring
---

## Definition

The determinant is the one function on square matrices that is linear in each row, vanishes on two equal rows, and gives $1$ on the identity.
Let $K$ be a commutative ring and let $n \ge 1$.
View an $n \times n$ [[square matrix|0CP7YY6NAG]] $A$ over $K$ as the family of its rows $r_1, \dots, r_n \in K^n$.
The *determinant* is the unique map $\det \colon M_n(K) \to K$ with these three properties.

1. For each $i$, the map $r_i \mapsto \det A$ is $K$-linear when the other rows are fixed.
2. $\det A = 0$ when two rows of $A$ are equal.
3. $\det I_n = 1$, for the [[identity matrix|06DW9BAWB1]] $I_n$.

Such a map exists and is unique by the [[existence and uniqueness theorem|1C8RRWHD45]], and it is given by the Leibniz sum
$$\det A = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)}.$$

## Notation

We write $\det A$, $\det(A)$ or $\lvert A \rvert$, and $\det(r_1, \dots, r_n)$ when the rows are given.
For $n = 0$ the determinant of the empty matrix is set equal to $1$, so that formulas with empty minors stay true.

## Remarks

Properties 1 and 2 together say that $\det$ is an [[alternating multilinear map|0MSWYWHYF5]] of the rows.
Property 1 lets us split a row into a sum and pull out a factor.
Property 2 is what makes the function sensitive to dependence, and it forces a swap of two rows to change the sign.
Property 3 fixes the scale, since without it every multiple $c \det$ would also satisfy 1 and 2.

A small example: for rows $(1, 2)$ and $(3, 4)$, write $(3, 4) = 3(1, 2) + (0, -2)$.
Property 1 splits off $3 \det((1, 2), (1, 2))$, which is $0$ by property 2, and leaves $\det((1, 2), (0, -2)) = -2$, the product of the diagonal entries of this triangular matrix.
A function that fails a condition is the permanent $ad + bc$, which satisfies 1 and 3 but gives $2$ on $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, as the [[permanent non-example|K9T8BNTZ2G]] shows.

The same three properties with columns in place of rows give the same function, by the [[equivalence theorem|W3JN0WPZ10]].
The definition uses no division, so it works over $\mathbb{Z}$, over polynomial rings and over $\mathbb{Z}/m\mathbb{Z}$.
Mathlib defines `Matrix.det` by the Leibniz sum and proves that it has the three properties.
The concept page on the [[determinant|00KDZRW4C0]] gives its meaning and its uses.

## Explanations

### L1 human

Three rules fix the determinant.
It grows in proportion when one row grows, it is zero when two rows agree, and it is $1$ for the identity matrix.
Over the real numbers, its absolute value is the factor by which the matrix scales volume.

### L2 human

The rules alone compute a $2 \times 2$ determinant.
Write the rows as $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$.
Linearity in each row gives four terms, and the two terms with a repeated $e_j$ vanish.
The swap $\det(e_2, e_1)$ equals $-1$, so the result is $ad - bc$.
Watch out: the rules speak about one row at a time, so $\det(A + B)$ is not $\det A + \det B$.

### L3 human

The definition says that $\det$ is the basis of the free module of rank $1$ of alternating $n$-linear forms on $K^n$ that takes the value $1$ on the standard basis.
Because it uses only ring operations, $\det$ commutes with every ring homomorphism $K \to K'$ applied to the entries.
This is the base of the generic matrix method, which proves an identity for a matrix of indeterminates over $\mathbb{Z}$ and then specializes it to any commutative ring.
