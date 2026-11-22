---
tag: 7SSKBQYFW1
kind: statement
role: theorem
name: Sylvester's determinant identity
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
uses: [00KDZRW4C0, 0BT9BYWVRY, 0310REJJY8, 0KA7A4ENVJ]
about: [00KDZRW4C0, 0BT9BYWVRY]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_determinant_identity
same_as:
  wikidata: Q65050391
  wikipedia: Sylvester's determinant identity
---

## Statement

If we fix a square block in the top left corner of a matrix and border it by one more row and one more column in every possible way, the determinants of the bordered blocks form a new matrix whose determinant is a power of the corner determinant times the determinant of the whole matrix.
Let $K$ be a [[commutative ring|0310REJJY8]], let $1 \le k < n$, and let $A = (a_{ij})$ be an $n \times n$ matrix over $K$.
Let $A_0$ be the $k \times k$ submatrix of $A$ formed by its first $k$ rows and its first $k$ columns.
For $k < i, j \le n$, let $b_{ij}$ be the [[minor|0BT9BYWVRY]] of $A$ with rows $1, \dots, k, i$ and columns $1, \dots, k, j$.
Let $B = (b_{ij})_{k < i, j \le n}$, a matrix of size $(n - k) \times (n - k)$.
Then
$$\det B = (\det A_0)^{n-k-1} \det A,$$
where $\det$ is the [[determinant|0C3CFHDN6R]].

## Remarks

### A first computation

Take $n = 3$, $k = 1$ and
$$A = \begin{pmatrix} 2 & 1 & 3 \\ 1 & 4 & 1 \\ 3 & 2 & 5 \end{pmatrix}, \qquad A_0 = (2).$$
Each bordered minor is a $2 \times 2$ determinant that uses the corner entry $a_{11} = 2$:
$$b_{22} = \det \begin{pmatrix} 2 & 1 \\ 1 & 4 \end{pmatrix} = 7, \quad b_{23} = \det \begin{pmatrix} 2 & 3 \\ 1 & 1 \end{pmatrix} = -1, \quad b_{32} = \det \begin{pmatrix} 2 & 1 \\ 3 & 2 \end{pmatrix} = 1, \quad b_{33} = \det \begin{pmatrix} 2 & 3 \\ 3 & 5 \end{pmatrix} = 1.$$
So $B = \begin{pmatrix} 7 & -1 \\ 1 & 1 \end{pmatrix}$ and $\det B = 7 + 1 = 8$.
The identity says $8 = 2^{1} \det A$, so $\det A = 4$.
Check by the [[rule of Sarrus|7H2P40X0MV]]:
$$\det A = 40 + 3 + 6 - 36 - 4 - 5 = 4.$$

### Two identities with one name

Watch out for the name "Sylvester's determinant theorem".
Some books use it for the identity on bordered minors stated here.
Others use it for the [[Weinstein-Aronszajn identity|0G24VQ1088]], $\det(I_m + AB) = \det(I_n + BA)$, which is a different result.
Read the formula, not the name, before you apply a theorem from a source.

### Why each hypothesis is needed

The ring must be commutative, as in every use of the determinant.
The condition $k < n$ makes $B$ a matrix of size at least $1$.
No invertibility of $A_0$ is needed, because the [[proof|XSZEXPCWA6]] works first with a generic matrix and then substitutes values.
But when $\det A_0 = 0$ and $k < n - 1$, the identity only says $\det B = 0$, and it tells us nothing about $\det A$.

### Special cases

For $k = n - 1$, the matrix $B$ is $1 \times 1$ with the single entry $b_{nn} = \det A$, and the identity reads $\det A = \det A$.
For $k = 1$, the entries of $B$ are the $2 \times 2$ minors $a_{11} a_{ij} - a_{i1} a_{1j}$, and the identity reads $\det B = a_{11}^{n-2} \det A$.
This is the step behind Chiò's method of condensation, which reduces the size by one with a single pivot $a_{11}$.
For $k = n - 2$, the matrix $B$ is $2 \times 2$.
After we move the interior rows and columns to the front, it becomes the [[Desnanot-Jacobi identity|KWW7519E58]], and [[Dodgson condensation|RQ44FKS5QM]] applies that case again and again.

### Fraction-free elimination

The [[Bareiss algorithm|ZDBW3AB587]] eliminates an integer matrix without fractions.
After $k$ steps its entries are exactly the bordered minors $b_{ij}$ for the corner of size $k$.
The identity, applied to these minors, shows that each division by the previous pivot is exact.
So all intermediate numbers stay integers, and they stay as small as minors of $A$.

### Generalizations

The identity holds minor by minor.
For sets $I$ and $J$ of $p$ indices in $\{k + 1, \dots, n\}$, the minor of $B$ with rows $I$ and columns $J$ equals $(\det A_0)^{p-1}$ times the minor of $A$ with rows $\{1, \dots, k\} \cup I$ and columns $\{1, \dots, k\} \cup J$.
The proof is the same, with the [[Schur complement|0KA7A4ENVJ]] of $A_0$ in a submatrix of $A$.

## History

The identity is named after James Joseph Sylvester.
Its case $k = 1$ is the basis of the pivotal condensation method of Felice Chiò, and its case $k = n - 2$ carries the names of Desnanot and Jacobi.

## Explanations

### L1 human

Pick the top left number of a square table, say $2$.
Pair it with each other row and each other column, and form the small $2 \times 2$ determinants that contain it.
Put these small determinants into a smaller table.
The determinant of the smaller table equals the determinant of the original table times a power of $2$.
So you can shrink a determinant by one size and only pay with a known factor.

### L2 human

Here is a typical use: compute a $4 \times 4$ determinant with the pivot $a_{11} = 1$, so that the power of $a_{11}$ disappears.
Take
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 3 & 1 & 2 & 0 \\ 0 & 1 & 1 & 2 \\ 2 & 0 & 1 & 1 \end{pmatrix}.$$
With $k = 1$, each entry $b_{ij} = a_{11} a_{ij} - a_{i1} a_{1j}$ for $i, j \ge 2$ is
$$B = \begin{pmatrix} 1 - 6 & 2 - 0 & 0 - 3 \\ 1 - 0 & 1 - 0 & 2 - 0 \\ 0 - 4 & 1 - 0 & 1 - 2 \end{pmatrix} = \begin{pmatrix} -5 & 2 & -3 \\ 1 & 1 & 2 \\ -4 & 1 & -1 \end{pmatrix}.$$
By the rule of Sarrus,
$$\det B = 5 - 16 - 3 - 12 + 10 + 2 = -14.$$
Since $a_{11} = 1$, the identity gives $\det A = \det B = -14$.
The [[Desnanot-Jacobi identity|KWW7519E58]] computes the same matrix by another route and also gets $-14$.
Watch out: the minors $b_{ij}$ always contain the whole corner $A_0$, so for $k > 1$ they are not the $2 \times 2$ minors of $A$.

### L3 human

For fixed $k$, the matrix $B$ is $\det A_0$ times the Schur complement $A / A_0$, and the identity is the Schur complement formula with every entry scaled by $\det A_0$.
This is why the identity holds over every commutative ring, while the Schur complement itself needs $A_0$ to be invertible.
Identities among minors of this kind are a starting point for the study of [[determinantal ideals|SXD7X0WQH1]] in commutative algebra.
