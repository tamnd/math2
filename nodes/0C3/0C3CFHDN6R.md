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

Let $K$ be a commutative ring and let $n \ge 1$.
View an $n \times n$ [[square matrix|0CP7YY6NAG]] over $K$ as the family of its $n$ rows in $K^n$.
The *determinant* is the unique map $\det \colon M_n(K) \to K$ with these properties:

1. $\det A$ is a multilinear function of the $n$ rows of $A$.
2. $\det A = 0$ when two rows of $A$ are equal.
3. $\det I_n = 1$, for the [[identity matrix|06DW9BAWB1]] $I_n$.

Such a map exists and is unique by the [[existence and uniqueness theorem|1C8RRWHD45]], and it is given by the Leibniz sum
$$\det A = \sum_{\sigma \in S_n} \sgn(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)}.$$

## Notation

We write $\det A$, $\det(A)$ or $\abs{A}$, and $\det(r_1, \dots, r_n)$ when the rows $r_1, \dots, r_n$ are given.
For $n = 0$ one sets $\det$ of the empty matrix equal to $1$; this convention makes formulas with empty minors work.

## Remarks

Properties 1 and 2 say that $\det$ is an [[alternating multilinear map|0MSWYWHYF5]] of the rows.
The same three properties with columns in place of rows define the same function, by the [[equivalence theorem|W3JN0WPZ10]].
Mathlib defines `Matrix.det` by the Leibniz sum and proves that it is alternating and multilinear in the rows.
The definition uses no division, so it makes sense over $\mathbb{Z}$, over polynomial rings and over $\mathbb{Z}/m\mathbb{Z}$.

## Explanations

### L1 human

The determinant gives one number for each square matrix.
Three rules fix it: it is linear in each row, it is zero when two rows agree, and it is $1$ for the identity matrix.
Over the real numbers, its absolute value is the factor by which the matrix scales volume.

### L2 human

The rules alone compute small determinants.
For rows $(a, b) = a e_1 + b e_2$ and $(c, d) = c e_1 + d e_2$, linearity gives four terms, the two terms with equal rows vanish, and the swap $\det(e_2, e_1) = -1$.
So $\det = ad - bc$.
A trap: the rules are about rows one at a time, so $\det(A + B)$ is not $\det A + \det B$.

### L3 human

The definition identifies $\det$ with a basis of the rank one module of alternating $n$-linear forms on $K^n$.
Because it uses only ring operations, $\det$ commutes with every ring homomorphism $K \to K'$ applied to the entries.
This is the basis of the generic matrix arguments, which prove identities for matrices of indeterminates and then specialize.
