---
tag: C5QA672NPH
kind: example
name: Standard basis
aliases: []
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_basis
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2B
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Example

Let $F$ be a field and let $n \ge 1$.
For $i = 1, \dots, n$, let $e_i \in F^n$ have entry $1$ in position $i$ and $0$ in the other positions.
The family $(e_1, \dots, e_n)$ is a [[basis|0VTQTPQGAV]] of $F^n$, the *standard basis*.

1. Spanning: for $x = (x_1, \dots, x_n)$, the combination $x_1 e_1 + \cdots + x_n e_n$ has entry $x_i$ in position $i$, so it equals $x$.
2. Independence: if $a_1 e_1 + \cdots + a_n e_n = 0$, then $(a_1, \dots, a_n) = (0, \dots, 0)$, by step 1 with $x_i = a_i$.
3. So the coordinates of $x$ in the standard basis are its entries.

For $n = 3$ over $\R$: $(2, -1, 5) = 2 e_1 - e_2 + 5 e_3$.

The same pattern gives standard bases of other spaces.

4. The monomials $1, x, \dots, x^n$ form a basis of $P_n(F)$; see the [[space of polynomials|0JGZCDT5DN]].
5. The matrix units $E_{ij}$, with $1$ in position $(i, j)$ and $0$ elsewhere, form a basis of $M_{m \times n}(F)$; see the [[space of matrices|0RE6X3BGPN]].
6. The functions $\delta_s$ form a basis of the finitely supported functions $F^{(S)}$; see [[spaces of functions|0GZB2SN0PH]].

Other bases of $F^n$ are the columns of invertible matrices; see [[this statement|WFM1CX5PZT]].
For example, the columns $(1, 1)$ and $(1, -1)$ of $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, with determinant $-2 \ne 0$, form a basis of $\R^2$.

## Remarks

The column $j$ of an $m \times n$ matrix $A$ is $A e_j$.
In $\R^3$, the standard basis vectors are often written $\mathbf{i}, \mathbf{j}, \mathbf{k}$.
The standard basis of $\R^n$ is an [[orthonormal basis|0S9GGTR0EX]] for the dot product.
In an abstract space there is no standard basis; a basis is a choice.
In Mathlib, the standard basis of `ι → R` is `Pi.basisFun R ι`.
The older object node [[standard basis|0V7ZD6P7RK]] records the same family as an object.

## Explanations

### L1 human

The standard basis vectors point along the coordinate axes, with length one.
Every vector is the sum of its entries times these basis vectors.

### L2 human

Over a field of characteristic $2$, the standard basis is still a basis: the argument uses only the entries $0$ and $1$.
A common slip is to think that $(1, 1, \dots, 1)$ must be in every basis; it is in none of the standard ones.
