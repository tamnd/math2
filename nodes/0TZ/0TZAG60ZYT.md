---
tag: 0TZAG60ZYT
kind: statement
role: theorem
name: Row rank equals column rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY, 069MCGX635, 03AJKXH1AV]
uses: [0EWQEYRVA8, 0EP73HK4C4, 0W809K6AW0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.rank_transpose
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proofs that column rank = row rank
  - book: isbn:9780134860244
    locator: Section 3.2
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L3738
    locator: ap-linear-algebra.tex:3738
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4825
    locator: ap-linear-algebra.tex:4825
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L1144
    locator: src/section6-2.xml:1144
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L1628
    locator: src/section7-4.xml:1628
---

## Statement

A matrix has exactly as many independent rows as independent columns.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Then the dimension of the [[row space|069MCGX635]] $\operatorname{Row}(A) \subseteq F^n$ equals the dimension of the [[column space|03AJKXH1AV]] $\operatorname{Col}(A) \subseteq F^m$.
Equivalently,
$$\rank A^{\mathsf{T}} = \rank A,$$
where $A^{\mathsf{T}}$ is the [[transpose|09DXWYRD43]] of $A$.

## Remarks

### A first check

Take
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \end{pmatrix}.$$
The second row is twice the first, so the row space is a line in $\mathbb{R}^3$, of dimension $1$.
The columns $(1, 2)$, $(2, 4)$ and $(3, 6)$ are the multiples $1$, $2$ and $3$ of $(1, 2)$, so the column space is a line in $\mathbb{R}^2$, also of dimension $1$.
The two lines live in different spaces, yet their dimensions agree.
That is the content of the theorem, and the [[example with a 3 by 4 matrix|MDB2CHQDXJ]] checks it for a larger case.

### Why the field is needed

Where does commutativity of the scalars enter?
Over the quaternions, take
$$A = \begin{pmatrix} 1 & i \\ j & k \end{pmatrix}.$$
The second column is $i$ times the first from the left, since $(i \cdot 1, i \cdot j) = (i, k)$, so the columns span a left space of dimension $1$.
The rows are not left multiples of each other: $\lambda (1, i) = (j, k)$ forces $\lambda = j$, and then $\lambda i = ji = -k \ne k$.
So the left row rank is $2$ while the left column rank is $1$.
Over a division ring, the correct statement pairs the left row rank with the right column rank, and those two agree.

The shape of the matrix is not restricted.
For $m \ne n$ the row space and the column space lie in spaces of different dimensions $n$ and $m$, and the theorem still says that the two subspaces have the same dimension.

### What it gives you

The rank is at most $\min(m, n)$, because the column space lies in $F^m$ and the row space lies in $F^n$.
So a $3 \times 5$ matrix has rank at most $3$, and its five columns are always dependent.
A square matrix has independent rows exactly when it has independent columns, so either property alone makes it invertible.
The [[four fundamental subspaces|73DVECPAT6]] get their dimensions $r$, $n - r$, $r$ and $m - r$ from the theorem together with rank-nullity.
In the [[rank of a product|02FDWY55AS]], the bound $\rank(AB) \le \rank A$ follows from the column spaces, and the bound $\rank(AB) \le \rank B$ then follows by transposing.

### The converse and what it does not say

The theorem compares dimensions only.
The row space and the column space are different subspaces in general, even for a square matrix.
For $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$, the row space is spanned by $(1, 1)$ and the column space by $(1, 0)$, and the [[example on square matrices|BGWTDZRS5T]] works this out.
They are equal for a symmetric matrix, since then the rows and the columns are the same vectors.

### Four proofs

The theorem has many proofs, and each one shows a different reason.
The [[proof by row reduction|WK6YWCWJD0]] counts the pivots of the reduced form, which count both the independent columns and the nonzero rows.
The [[proof by a factorization A = CR|S1C1ATEFW1]] writes the columns in a basis of the column space, and the same equation shows that $r$ rows span all rows.
The [[proof by orthogonality|4JYHHBC6J7]] works over $\mathbb{R}$ and shows that $A$ is injective on its row space.
The [[proof by duality|7DQXA4AY1D]] belongs to the sub-area on [[dual spaces|9K7FFF26QR]], and it shows that a linear map and its dual map have the same rank.

## Explanations

### L1 human

Count the independent rows of a matrix, then count its independent columns.
You always get the same number.
This is surprising, because a row of a $3 \times 5$ matrix has five entries while a column has three.
For example, in a matrix with rows $(1, 2, 3)$ and $(2, 4, 6)$, there is one independent row, and every column is a multiple of $(1, 2)$, so there is one independent column.

### L2 human

Here is a typical use: show that the columns of $A = \begin{pmatrix} 1 & 0 & 2 & 1 \\ 0 & 1 & 1 & 3 \\ 1 & 1 & 3 & 4 \end{pmatrix}$ span a plane.
The rows are easier to study, since row 3 is the sum of rows 1 and 2:
$$(1, 0, 2, 1) + (0, 1, 1, 3) = (1, 1, 3, 4).$$
Rows 1 and 2 are not proportional, because of their first two entries, so the row rank is $2$.
By the theorem the column rank is also $2$, so the four columns span a plane in $\mathbb{R}^3$, without any work on the columns.
Check: the columns $(1, 0, 1)$ and $(0, 1, 1)$ are independent, and $(2, 1, 3) = 2(1, 0, 1) + (0, 1, 1)$, $(1, 3, 4) = (1, 0, 1) + 3(0, 1, 1)$.
Watch out: the theorem gives the dimension of the column space, not a basis of it, and the rows found above are not vectors of the column space.

### L3 human

For the linear map $T(x) = Ax$, the rank of $A$ is $\dim \operatorname{im} T$, and the row rank is the rank of the [[dual map|0AZ5ARP287]] $T^*$, whose matrix in the dual bases is $A^{\mathsf{T}}$.
The duality proof shows $\operatorname{im} T^* = (\ker T)^0$, the annihilator of the kernel, which has dimension $n - \dim \ker T = \rank T$.
So the theorem says that taking duals keeps the rank, a statement that makes sense without any matrices.
The equality also holds for the [[determinantal rank|0BT9BYWVRY]], the largest size of a nonzero minor, because the minors of $A^{\mathsf{T}}$ are the minors of $A$.
In Mathlib the statement is `Matrix.rank_transpose`.
