---
tag: 7SSKBQYFW1
kind: statement
role: theorem
name: Sylvester's determinant identity
msc: [15A15]
uses: [00KDZRW4C0, 0BT9BYWVRY, 0310REJJY8, 0KA7A4ENVJ]
about: [00KDZRW4C0, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_determinant_identity
same_as:
  wikidata: Q65050391
  wikipedia: Sylvester's determinant identity
---

## Statement

Let $K$ be a [[commutative ring|0310REJJY8]], let $1 \le k < n$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$.
Let $A_0$ be the $k \times k$ submatrix of $A$ formed by its first $k$ rows and its first $k$ columns.
For $k < i, j \le n$, let $b_{ij}$ be the [[minor|0BT9BYWVRY]] of $A$ with rows $1, \dots, k, i$ and columns $1, \dots, k, j$.
Let $B$ be the $(n-k) \times (n-k)$ matrix $(b_{ij})_{k < i, j \le n}$.
Then
$$\det B = (\det A_0)^{n-k-1} \det A,$$
where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

First assume that $A_0$ is invertible, and write $A$ in blocks with $A_0$ in the top left corner.
By the [[Schur complement formula|0KA7A4ENVJ]], $\det A = \det A_0 \cdot \det S$, where $S = (s_{ij})$ is the Schur complement of $A_0$ in $A$.
The same formula on each bordered submatrix gives $b_{ij} = \det A_0 \cdot s_{ij}$, so $B = (\det A_0) S$ and the identity follows.
Both sides are polynomials in the entries of $A$ with integer coefficients, so the identity holds over every commutative ring.

For $k = n - 1$, the matrix $B$ is $1 \times 1$ with entry $\det A$, and the identity is trivial.
For $k = n - 2$, it is a form of the Desnanot–Jacobi identity, which is the basis of [[Dodgson condensation|RQ44FKS5QM]].
It should not be confused with [[Sylvester's determinant theorem|0G24VQ1088]], which says $\det(I_m + AB) = \det(I_n + BA)$.

## Explanations

### L1 human

Fix the top left corner block of a square matrix.
Build a smaller matrix whose entries are determinants of this corner block bordered by one more row and one more column.
The determinant of the new matrix equals the determinant of the original matrix times a power of the determinant of the corner block.
For a $3 \times 3$ matrix and $k = 1$, the four entries of $B$ are $2 \times 2$ minors that all contain the entry $a_{11}$, and $\det B = a_{11} \det A$.

### L2 human

The identity explains why fraction-free Gaussian elimination works over the integers.
The intermediate entries of the Bareiss algorithm are such bordered minors, and the division by the previous pivot is exact.
It sits next to the [[determinant via the Schur complement|0KA7A4ENVJ]] and to the [[determinant of a block triangular matrix|0J9TVTNB4K]].
