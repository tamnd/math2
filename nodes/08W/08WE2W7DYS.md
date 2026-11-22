---
tag: 08WE2W7DYS
kind: statement
role: theorem
name: Cauchy-Binet formula
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug2
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Binet_formula
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
same_as:
  wikidata: Q45286
  wikipedia: Cauchy–Binet formula
---

## Statement

The Cauchy-Binet formula computes the determinant of a product of two rectangular matrices as a sum of products of matching maximal minors, and it contains the product rule for square matrices as its simplest case.
Let $K$ be a commutative ring, let $m, n \ge 1$, let $A$ be an $m \times n$ matrix and let $B$ be an $n \times m$ matrix over $K$.
For a subset $S \subseteq \{1, \dots, n\}$ with $m$ elements, let $A_S$ be the $m \times m$ matrix of the columns of $A$ with index in $S$, in increasing order.
Let $B^S$ be the $m \times m$ matrix of the rows of $B$ with index in $S$, in the same order.

1. If $m \le n$, then
$$\det(AB) = \sum_{S} \det(A_S) \det(B^S),$$
where the sum runs over the $\binom{n}{m}$ subsets $S$ of $\{1, \dots, n\}$ with $m$ elements, and $\det$ is the [[determinant|0C3CFHDN6R]].
2. If $m > n$, then $\det(AB) = 0$.

## Remarks

### A first computation

Take
$$A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 1 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad AB = \begin{pmatrix} 3 & 1 \\ 1 & 1 \end{pmatrix}.$$
Directly, $\det(AB) = 3 - 1 = 2$.
Now there are three subsets $S$ of $\{1, 2, 3\}$ with two elements.
For each one, take those columns of $A$ and those rows of $B$:
$$S = \{1, 2\}: \ \det \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \det \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = 1 \cdot 1 = 1,$$
$$S = \{1, 3\}: \ \det \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \det \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} = 1 \cdot (-1) = -1,$$
$$S = \{2, 3\}: \ \det \begin{pmatrix} 0 & 2 \\ 1 & 1 \end{pmatrix} \det \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = (-2) \cdot (-1) = 2.$$
The sum is $1 - 1 + 2 = 2$, as it should be.
The determinants $\det(A_S)$ and $\det(B^S)$ are [[minors|0SD528P0EK]] of order $m$ of the two factors.

### How the formula fits with the product rule

For $m = n$ there is only one subset, $S = \{1, \dots, n\}$, and the formula is the [[multiplicativity of the determinant|04CPJ6AF00]], $\det(AB) = \det A \det B$.
For $m = 1$ the subsets are single indices, and the formula is the product of a row and a column, $\sum_k a_{1k} b_{k1}$.
For $m > n$ there are no subsets with $m$ elements, the sum is empty, and part 2 says that its value $0$ is correct.
The reason for part 2 is rank: $AB$ is an $m \times m$ matrix of rank at most $n < m$.

### The Gram determinant and Lagrange's identity

Over $\mathbb{R}$, take $B = A^{\mathsf{T}}$.
Then $B^S = (A_S)^{\mathsf{T}}$, so each term is a square:
$$\det(A A^{\mathsf{T}}) = \sum_{S} \det(A_S)^2 \ge 0.$$
The matrix $A A^{\mathsf{T}}$ is the [[Gram matrix|00SPJSDT3Z]] of the rows of $A$.
Its determinant is $0$ exactly when all maximal minors of $A$ vanish, that is, when the rows of $A$ are linearly dependent, by the theorem on [[rank by minors|HVHQ50TJB1]].

For two rows $a$ and $b$ in $\mathbb{R}^n$, this is Lagrange's identity:
$$\Bigl(\sum_i a_i^2\Bigr)\Bigl(\sum_i b_i^2\Bigr) - \Bigl(\sum_i a_i b_i\Bigr)^2 = \sum_{i<j} (a_i b_j - a_j b_i)^2.$$
The right side is at least $0$, so Lagrange's identity proves the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in $\mathbb{R}^n$, with equality exactly when $a$ and $b$ are dependent.
For $a = (1, 2, 3)$ and $b = (4, 5, 6)$ both sides are $14 \cdot 77 - 32^2 = 54$ and $(-3)^2 + (-6)^2 + (-3)^2 = 54$.

### The terms can cancel

The formula is an identity, so it has no converse in the usual sense.
But the sum can vanish when its terms do not.
For $A = (1, 1)$ and $B = (1, -1)^{\mathsf{T}}$, the two terms are $1 \cdot 1$ and $1 \cdot (-1)$, and $\det(AB) = 0$.
So $\det(AB) = 0$ does not force any minor of $A$ or of $B$ to be $0$.

### Watch out

The same set $S$ chooses the columns of $A$ and the rows of $B$.
The sum is not over pairs of sets chosen independently, so it has $\binom{n}{m}$ terms, not $\binom{n}{m}^2$.
For example, a sum over pairs in the first computation would include $S = \{1, 2\}$ for $A$ with $\{1, 3\}$ for $B$.
Its total would be $(1 + 1 - 2)(1 - 1 - 1) = 0$, not $2$.

### Generalizations

The same argument computes every minor of a product: for row indices $I$ and column indices $J$ with $k$ elements,
$$\det (AB)_{I, J} = \sum_{S} \det A_{I, S} \det B_{S, J},$$
where $S$ runs over the subsets of $\{1, \dots, n\}$ with $k$ elements.
In the language of multilinear algebra, this says that the $k$-th exterior power of a product is the product of the $k$-th exterior powers.
The formula is also behind the matrix-tree theorem, which counts the spanning trees of a graph by a determinant.

## History

The formula is named after Jacques Binet and Augustin-Louis Cauchy, who both gave it in 1812.

## Explanations

### L1 human

For square matrices, the determinant of a product is the product of the determinants.
When the two matrices are rectangular, say $2 \times 3$ and $3 \times 2$, their product is still square, but they have no determinants of their own.
The Cauchy-Binet formula fixes this.
Choose two of the three middle indices, take the $2 \times 2$ piece of each factor that uses them, and multiply the two small determinants.
Add these products over all three choices, and you get the determinant of the product.

### L2 human

Here is a typical use: the area of the parallelogram spanned by $a = (1, 2, 3)$ and $b = (4, 5, 6)$ in $\mathbb{R}^3$.
Let $A$ be the $2 \times 3$ matrix with rows $a$ and $b$.
Its Gram matrix and determinant are
$$A A^{\mathsf{T}} = \begin{pmatrix} 14 & 32 \\ 32 & 77 \end{pmatrix}, \qquad \det(A A^{\mathsf{T}}) = 1078 - 1024 = 54.$$
The three $2 \times 2$ minors of $A$ are
$$\det \begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = -3, \qquad \det \begin{pmatrix} 1 & 3 \\ 4 & 6 \end{pmatrix} = -6, \qquad \det \begin{pmatrix} 2 & 3 \\ 5 & 6 \end{pmatrix} = -3.$$
Check: $9 + 36 + 9 = 54$.
Each minor is the signed area of the shadow of the parallelogram on one coordinate plane, and the formula says that the squared area is the sum of the squared shadow areas.
So the area is $\sqrt{54} = 3\sqrt{6}$.
In the other order, $A^{\mathsf{T}} A$ is $3 \times 3$ and $3 > 2$, so part 2 gives $\det(A^{\mathsf{T}} A) = 0$.

### L3 human

The Cauchy-Binet formula is the functoriality of exterior powers written in coordinates.
The matrix $A$, as a linear map $K^n \to K^m$, induces a map $\Lambda^m A$ from $\Lambda^m K^n$, with the basis of wedges $e_S$ indexed by $m$-subsets $S$, to the line $\Lambda^m K^m$.
The coefficients of $\Lambda^m A$ are the maximal minors $\det A_S$, and $\Lambda^m(AB) = \Lambda^m A \circ \Lambda^m B$ is the formula.
The Gram determinant form gives the $m$-dimensional volume of a parallelotope in $\mathbb{R}^n$, which extends the [[determinant as volume scaling factor|RC5BTSG8T2]] to non-square matrices.
In combinatorics the same formula drives the matrix-tree theorem and counting results for families of paths in graphs.
