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
For $i = 1, \dots, n$, let $e_i \in F^n$ be the vector with entry $1$ in position $i$ and entry $0$ in every other position.
The family $(e_1, \dots, e_n)$ is a [[basis|0VTQTPQGAV]] of the [[coordinate space|713F6AM1X1]] $F^n$, called the *standard basis*.
For $n = 3$ the three vectors are
$$e_1 = (1, 0, 0), \qquad e_2 = (0, 1, 0), \qquad e_3 = (0, 0, 1).$$
We check the two conditions of a basis.

1. Spanning. Let $x = (x_1, \dots, x_n)$ be any vector. In the combination $x_1 e_1 + \dots + x_n e_n$, position $i$ receives $x_i$ from the term $x_i e_i$ and $0$ from every other term. So the combination has entry $x_i$ in position $i$, and it equals $x$.
2. Independence. Suppose that $a_1 e_1 + \dots + a_n e_n = 0$. By step 1 with $x_i = a_i$, the left side is the vector $(a_1, \dots, a_n)$. So $(a_1, \dots, a_n) = (0, \dots, 0)$, and every $a_i$ is $0$.

Both conditions hold, so $(e_1, \dots, e_n)$ is a basis.
Step 1 also shows that the [[coordinates|04CYQHN6MC]] of $x$ in the standard basis are just its entries.
For example, in $\mathbb{R}^3$,
$$(2, -1, 5) = 2 e_1 - e_2 + 5 e_3.$$

## Remarks

### The same pattern in other spaces

Each of the basic examples of vector spaces has a basis that plays the same role.
In the [[space of polynomials|0JGZCDT5DN]] $P_n(F)$ of degree at most $n$, the monomials $1, x, x^2, \dots, x^n$ form a basis, so $\dim P_n(F) = n + 1$.
In the [[space of matrices|0RE6X3BGPN]] $M_{m \times n}(F)$, the matrix units $E_{ij}$, with $1$ in position $(i, j)$ and $0$ elsewhere, form a basis of $mn$ elements.
For example,
$$\begin{pmatrix} 3 & 0 \\ -1 & 4 \end{pmatrix} = 3 E_{11} - E_{21} + 4 E_{22}.$$
In the space $F^{(S)}$ of finitely supported functions on a set $S$, the functions $\delta_s$, equal to $1$ at $s$ and $0$ elsewhere, form a basis; see the [[spaces of functions|0GZB2SN0PH]].
In each case the coordinates of a vector are the numbers that already describe it: coefficients, entries or values.

### Other bases of the same space

The standard basis is one basis among many.
By the [[column criterion|WFM1CX5PZT]], the ordered bases of $F^n$ are exactly the column lists of the invertible $n \times n$ matrices, and the standard basis belongs to the identity matrix.
For instance, the matrix $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ has determinant $1 \cdot (-1) - 1 \cdot 1 = -2 \ne 0$, so its columns $(1, 1)$ and $(1, -1)$ form another basis of $\mathbb{R}^2$.
An abstract vector space, such as a plane through the origin in $\mathbb{R}^3$, has no standard basis at all; any basis there is a choice.

### Small facts that come up often

For an $m \times n$ matrix $A$, the product $A e_j$ is column $j$ of $A$, since the only nonzero entry of $e_j$ picks out that column.
The standard basis of $\mathbb{R}^n$ is an [[orthonormal basis|0S9GGTR0EX]] for the dot product, because $e_i \cdot e_j$ is $1$ for $i = j$ and $0$ otherwise.
The checks above use only the elements $0$ and $1$ of $F$, so the standard basis is a basis over every field, including $\mathbb{F}_2$.

### Notation

In $\mathbb{R}^3$, physics books write $\mathbf{i}, \mathbf{j}, \mathbf{k}$ for $e_1, e_2, e_3$.
In Mathlib, the standard basis of `ι → R` is `Pi.basisFun R ι`.
The object node on the [[standard basis|0V7ZD6P7RK]] records the same family.

## Explanations

### L1 human

The standard basis vectors are steps of length one along the coordinate axes.
In the plane they are $(1, 0)$, one step right, and $(0, 1)$, one step up.
To reach the point $(4, 7)$, take four steps right and seven steps up.
So the numbers that name a point are already its recipe in the standard basis.

### L2 human

Here is a typical use: the standard basis makes it easy to find the matrix of a linear map.
Suppose $T \colon \mathbb{R}^2 \to \mathbb{R}^2$ is linear with $T(e_1) = (2, 1)$ and $T(e_2) = (-1, 3)$.
For $x = (x_1, x_2) = x_1 e_1 + x_2 e_2$, linearity gives
$$T(x) = x_1 (2, 1) + x_2 (-1, 3) = \begin{pmatrix} 2 & -1 \\ 1 & 3 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}.$$
So the columns of the matrix of $T$ are the images of the standard basis vectors.
Check with $x = (1, 1)$: $T(1, 1) = (2, 1) + (-1, 3) = (1, 4)$, and the matrix gives $(2 - 1, 1 + 3) = (1, 4)$.
Watch out: in a different basis the same map has a different matrix, so always say which basis you use.
