---
tag: W3JN0WPZ10
kind: statement
role: theorem
name: Equivalence of the three definitions of the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 016PE4VZ8Q, 0C08BQ3M05, 0ZZQ2E1MTE, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Laplace_expansion
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Statement

Books define the determinant in three ways, and this theorem says that all of them give the same number, whether we work with rows or with columns.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A = (a_{ij}) \in M_n(K)$.
Consider these four functions of $A$.

1. The axiomatic [[determinant|0C3CFHDN6R]] $\det A$, the unique function that is multilinear and alternating in the rows, with value $1$ on $I_n$.
2. The Leibniz sum
$$L(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma)\, a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)}.$$
3. The Laplace recursion, given by $D_1(a) = a$ and, for $n \ge 2$,
$$D_n(A) = \sum_{j=1}^n (-1)^{1+j} a_{1j}\, D_{n-1}(A_{1j}),$$
where $A_{1j}$ is the $(n-1) \times (n-1)$ matrix that remains after we delete row $1$ and column $j$, so that $D_{n-1}(A_{1j})$ is a [[minor|0SD528P0EK]] of $A$.
4. The column version $\det'(A)$, the unique function that is multilinear and alternating in the columns, with value $1$ on $I_n$.

Then the function $\det'$ exists, and $\det A = L(A) = D_n(A) = \det'(A)$ for every $n \ge 1$ and every $A \in M_n(K)$.

## Remarks

### A check on a 2 by 2 matrix

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.
The Leibniz sum has two terms, one for the identity and one for the swap:
$$L(A) = 1 \cdot 4 - 2 \cdot 3 = -2.$$
The recursion expands along row $1$ into $1 \times 1$ determinants:
$$D_2(A) = 1 \cdot D_1(4) - 2 \cdot D_1(3) = 4 - 6 = -2.$$
The rules give the same value.
Write row $2$ as $(3, 4) = 3(1, 2) + (0, -2)$, split by linearity, and drop the part with two equal rows; what is left is $\det \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix} = -2$ by the [[triangular rule|0K1KKMFHYH]].

### Why the ring must be commutative

The theorem needs $K$ to be commutative.
Over a noncommutative ring the order of the factors in each Leibniz term matters, and the row and column versions part ways.
For example, over the quaternions, take the matrix with two equal rows $(i, j)$ and $(i, j)$.
The Leibniz sum with the factors in row order is
$$a_{11} a_{22} - a_{12} a_{21} = ij - ji = k - (-k) = 2k \ne 0,$$
so it is not alternating, and the three definitions no longer describe one function.

### What it gives you

You may start from whichever definition is most convenient, and all the theorems about determinants hold for the others.
The rules suit structural results such as [[multiplicativity|04CPJ6AF00]].
The Leibniz sum suits the [[transpose rule|0ZZQ2E1MTE]] and shows that $\det A$ is a polynomial in the entries with integer coefficients, homogeneous of degree $n$.
The recursion suits proofs by induction on $n$.
Since rows and columns give the same function, every statement about rows has a twin about columns.

### Generalizations

The recursion can expand along any row or any column, by the [[Laplace expansion|0C08BQ3M05]].
A fourth description uses the top exterior power: an endomorphism acts on $\Lambda^n K^n$ as multiplication by its determinant.
It agrees with the others by the [[existence and uniqueness theorem|1C8RRWHD45]], which says that the alternating $n$-linear forms on $K^n$ form a free module of rank $1$.

## History

The recursion carries the name of Laplace, and the sum over permutations carries the name of Leibniz.
Most modern algebra textbooks start from the rules, while Mathlib takes the Leibniz sum as its definition of `Matrix.det` and proves the rules as theorems.

## Explanations

### L1 human

There are three common recipes for the determinant.
The first adds signed products over all ways to choose one entry from each row and each column.
The second breaks the table along its first row into smaller tables.
The third describes the determinant by three rules that it must obey.
The theorem says that the three recipes always give the same number.

### L2 human

Here is how the theorem is used in practice: a proof picks the recipe that makes it short.
To show $\det A^{\mathsf{T}} = \det A$, use the Leibniz sum, since transposing turns each permutation $\sigma$ into $\sigma^{-1}$, which has the same sign.
To show $\det(AB) = \det A \det B$, use the rules, since $X \mapsto \det(XB)$ obeys the first two rules.
To show that the determinant of an integer matrix is an integer, any recipe works, because each uses only sums and products.
Watch out: if you drop the signs $(-1)^{1+j}$ from the recursion, you get the permanent, which is a different function.

### L3 human

The three descriptions are three views of one object.
The rules describe a basis vector of the rank one module $\operatorname{Alt}^n(K^n)$, the Leibniz sum writes it in the basis of monomials in the entries, and the recursion records how it behaves under the splitting $K^n = K \oplus K^{n-1}$.
The agreement of rows and columns says that a map and its dual map have the same determinant on the top exterior power.
