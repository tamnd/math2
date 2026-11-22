---
tag: TR48YQGCCA
kind: statement
role: theorem
name: Rank-nullity theorem for matrices
msc: ["15A03", "15A04"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY, 0PHDYNR24D]
uses: [0ZC9YTXZRY, 0PHDYNR24D, 0APCFW7639]
sources:
  - url: https://en.wikipedia.org/wiki/Rank%E2%80%93nullity_theorem
    locator: Matrices
  - book: isbn:9780321982384
    locator: Section 4.6
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4974
    locator: ap-linear-algebra.tex:4974
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L1162
    locator: src/section3-5.xml:1162
---

## Statement

The columns of a matrix split into the part that the matrix keeps and the part that it sends to zero, and the two parts add up to the number of columns.
Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Let $r$ be the [[rank|0ZC9YTXZRY]] of $A$, and let $k$ be the [[nullity|0APCFW7639]] of $A$, the dimension of the [[null space|0PHDYNR24D]] $\operatorname{Null}(A) = \{x \in F^n : Ax = 0\}$.
Then
$$r + k = n.$$

## Remarks

### A first check

Take the $3 \times 4$ matrix
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}.$$
Its reduced row echelon form has the rows $(1, 2, 0, 1)$, $(0, 0, 1, 2)$ and $(0, 0, 0, 0)$, with pivots in columns 1 and 3, so $r = 2$.
The equations $x_1 = -2x_2 - x_4$ and $x_3 = -2x_4$ leave $x_2$ and $x_4$ free, and they give the null space basis
$$s_1 = (-2, 1, 0, 0), \qquad s_2 = (-1, 0, -2, 1).$$
So $k = 2$, and $r + k = 4 = n$.
Check: $As_1 = -2a_1 + a_2 = 0$ and $As_2 = -a_1 - 2a_3 + a_4 = 0$, where $a_j$ is column $j$ of $A$; the [[null space example|GG03BSSZ43]] gives the details.

### Why each hypothesis is needed

The count uses the number of columns $n$, not the number of rows $m$.
For the $1 \times 3$ matrix $\begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$, the rank is $1$ and the null space is spanned by $(0, 1, 0)$ and $(0, 0, 1)$, so $r + k = 3 = n$, while $m = 1$.

The entries must lie in a field, so that the null space is a vector space and has a dimension.
Over the ring $\mathbb{Z}/4$, the $1 \times 1$ matrix $(2)$ has the null space $\{0, 2\}$, and this set has no basis, because $2 \cdot 2 = 0$ is a nontrivial relation.
So the nullity is not even defined there.

### What it gives you

If $n > m$, then $k = n - r \ge n - m > 0$, so a homogeneous system with more unknowns than equations has a nonzero solution.
For a square matrix, $k = 0$ exactly when $r = n$, so a trivial null space and full rank are the same property, and each one makes the matrix invertible.
Applied to the transpose, the theorem gives the dimension $m - r$ of the left null space, since $A^{\mathsf{T}}$ has $m$ columns and the same rank $r$ by [[row rank equals column rank|0TZAG60ZYT]].
Together these give the dimensions of the [[four fundamental subspaces|73DVECPAT6]].

### Every pair of numbers occurs

For all $m$ and $n$ and every $r \le \min(m, n)$, some $m \times n$ matrix has rank $r$ and nullity $n - r$.
The matrix with $r$ ones in the positions $(1, 1), \dots, (r, r)$ and zeros elsewhere is one, since its null space is spanned by the standard vectors $e_{r+1}, \dots, e_n$.
So the theorem is the only constraint between the two numbers.

### Generalizations

The [[rank-nullity theorem|0W4FSW1TVB]] for a linear map $T \colon V \to W$ with $V$ finite-dimensional says $\dim V = \dim \operatorname{im} T + \dim \ker T$.
The matrix form is the case $T(x) = Ax$ on $V = F^n$, where the image is the column space and the kernel is the null space.

## Explanations

### L1 human

Every column of a matrix is either a pivot column or a free column after row reduction.
The pivot columns count the rank.
The free columns count the free choices in the solutions of $Ax = 0$, which is the nullity.
So rank plus nullity is the number of columns, and for a matrix with $4$ columns and rank $2$ there are $2$ free choices.

### L2 human

Here is a typical use: without solving anything, find the dimension of the solution set of five homogeneous equations in eight unknowns whose coefficient matrix has rank $5$.
The coefficient matrix is $5 \times 8$, so $n = 8$ and $r = 5$.
The theorem gives $k = 8 - 5 = 3$, so the solutions form a $3$-dimensional subspace of $F^8$.
If the rank were only $4$, one equation would follow from the others, and the solution space would have dimension $4$.
Watch out: use the number of columns, which is the number of unknowns, and not the number of equations.

### L3 human

The theorem is the statement that the sequence
$$0 \to \operatorname{Null}(A) \to F^n \xrightarrow{A} \operatorname{Col}(A) \to 0$$
is exact, together with the additivity of dimension along short exact sequences of vector spaces.
Every short exact sequence of vector spaces splits, so $F^n \cong \operatorname{Null}(A) \oplus \operatorname{Col}(A)$ as vector spaces, and over $\mathbb{R}$ the [[four fundamental subspaces|73DVECPAT6]] make this splitting concrete as $\mathbb{R}^n = \operatorname{Row}(A) \oplus \operatorname{Null}(A)$.
Over a ring the analogous count fails, as the example over $\mathbb{Z}/4$ shows.
