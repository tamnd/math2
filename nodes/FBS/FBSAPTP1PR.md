---
tag: FBSAPTP1PR
kind: statement
role: theorem
name: Invertible iff the determinant is nonzero
aliases: [a-square-matrix-is-invertible-iff-its-determinant-is-nonzero]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0EB9N0S33C, 0C3CFHDN6R, 0QA8CHH8MG, 0CRMGPAH83]
sources:
  - locator: ap-linear-algebra.tex:6604
    url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L6604
  - locator: ch-systems.tex:1083
    url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L1083
  - locator: src/section3-4.xml:766
    url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-4.xml#L766
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Invertibility
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: History
---

## Statement

One number decides whether a square matrix over a field can be undone: the matrix is invertible exactly when its determinant is not zero.
Let $F$ be a [[field|0QA8CHH8MG]], and let $A$ be an $n \times n$ matrix over $F$.
Then the following four conditions are equivalent.

1. $A$ is [[invertible|0EB9N0S33C]].
2. $\det A \neq 0$, where $\det$ is the [[determinant|0C3CFHDN6R]].
3. The columns of $A$ are [[linearly independent|0CRMGPAH83]].
4. The rows of $A$ are linearly independent.

In particular, the homogeneous system $Ax = 0$ has a solution $x \neq 0$ if and only if $\det A = 0$.

## Remarks

### A singular matrix and its neighbor

Take the matrix with the entries $1$ to $9$ in order, and expand along the first row:
$$\det \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix} = 1(45 - 48) - 2(36 - 42) + 3(32 - 35) = -3 + 12 - 9 = 0.$$
So the theorem predicts a nonzero solution of $Ax = 0$, and $x = (1, -2, 1)$ is one.
Check: the three rows give $1 - 4 + 3 = 0$, $4 - 10 + 6 = 0$ and $7 - 16 + 9 = 0$.
This says that the first column minus twice the second plus the third is zero, so the columns are dependent.

Now change the last entry from $9$ to $10$:
$$\det \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 10 \end{pmatrix} = 1(50 - 48) - 2(40 - 42) + 3(32 - 35) = 2 + 4 - 9 = -3.$$
The determinant is not zero, so this matrix is invertible, and $Ax = b$ has exactly one solution for each $b$.

### Why the field is needed

The proof divides by $\det A$, and that needs an inverse of a nonzero scalar.
Over the integers, the $1 \times 1$ matrix $(2)$ has determinant $2 \neq 0$ and an independent column.
Its only possible inverse is $(1/2)$, which is not an integer matrix.
So conditions 2 and 3 hold while condition 1 fails over $\mathbb{Z}$.
The correct test over a commutative ring asks that $\det A$ be a unit, and the [[criterion over commutative rings|03Q7RE2HXR]] proves it.
The matrix must also be square, since only square matrices have a determinant.

### What it gives you

The theorem turns questions about solutions into one computation.
A homogeneous system of $n$ equations in $n$ unknowns has a nonzero solution exactly when its determinant is $0$.
Applied to $A - \lambda I$, this says that $\lambda$ is an [[eigenvalue|0BQAA2BK3Q]] of $A$ exactly when $\det(A - \lambda I) = 0$, and that is the [[root test for eigenvalues|053QVHF6N7]] behind the [[characteristic polynomial|0VSSPAFM2C]].
Applied to columns, it says that $n$ vectors of $F^n$ form a basis exactly when the matrix with these columns has a nonzero determinant, as in the [[basis criterion|5D1CHPV9Z3]].
Over $\mathbb{R}$, the singular matrices are the zeros of the polynomial $\det$ in the $n^2$ entries, so they form a closed set of measure zero.

### The converse and a one-sided inverse

The statement is already an equivalence, so there is no separate converse.
It gives a useful bonus: a one-sided inverse of a square matrix is two-sided.
Suppose $AB = I_n$ for square $A$ and $B$ over $F$.
Then $\det A \det B = 1$, so $\det A \neq 0$ and $A$ is invertible.
Multiply $AB = I_n$ on the left by $A^{-1}$ to get $B = A^{-1}$.

### Watch out

A small determinant does not mean that a matrix is nearly singular.
The $10 \times 10$ matrix $0.1\, I_{10}$ has determinant $0.1^{10} = 10^{-10}$, yet its inverse $10\, I_{10}$ is as harmless as a matrix can be.
The theorem only separates zero from nonzero.
To measure how close a matrix is to a singular one, numerical analysis uses the condition number, not the determinant.

### Generalizations

The [[rank by minors|HVHQ50TJB1]] refines the theorem to every matrix, square or not: the rank is the largest size of a nonzero minor.
Over a commutative ring, $A$ is invertible exactly when $\det A$ is a unit, and the [[inverse via the adjugate|0ENVM493VK]] then gives the inverse.
Two proofs are given, one [[by row reduction|EB3DSF9HPM]] and one [[by the adjugate|8A6WRWSGQZ]].

## History

Determinants were first studied as expressions attached to systems of linear equations, as a test for a unique solution.
This use came long before matrices were treated as objects of their own, so the criterion is older than the language in which it is now stated.

## Explanations

### L1 human

A square table of numbers describes a way to mix the entries of a list into a new list.
You can undo the mixing exactly when the determinant is not $0$.
A determinant of $0$ means that two different lists give the same result, so some information is lost.
For example, the table with rows $(1, 2)$ and $(2, 4)$ has determinant $1 \cdot 4 - 2 \cdot 2 = 0$.
Its second column is twice its first, so the lists $(2, -1)$ and $(0, 0)$ both give $(0, 0)$.

### L2 human

For which real numbers $t$ is the matrix
$$A = \begin{pmatrix} 1 & t \\ t & 4 \end{pmatrix}$$
invertible?
The determinant is $\det A = 1 \cdot 4 - t \cdot t = 4 - t^2$.
It is zero exactly for $t = 2$ and $t = -2$.
For $t = 2$ the columns are $(1, 2)$ and $(2, 4)$, and the second is twice the first.
For $t = -2$ the columns are $(1, -2)$ and $(-2, 4)$, and the second is $-2$ times the first.
For every other real $t$ the matrix is invertible.
The typical use is just this: decide invertibility for a family of matrices without computing a single inverse.
Watch out over rings: for the integer matrix with $t = 1$, the determinant is $3$, so $A$ is invertible over $\mathbb{Q}$ but not over $\mathbb{Z}$.

### L3 human

The theorem says that the general linear group $\mathrm{GL}_n(F)$ is the set where the polynomial $\det$ does not vanish.
In algebraic geometry, $\mathrm{GL}_n$ is the open subset of the space of matrices defined by $\det \neq 0$, with coordinate ring $\mathbb{Z}[x_{ij}, 1/\det]$.
Over $\mathbb{R}$ and $\mathbb{C}$ this set is open and dense, so many identities can be proved first for invertible matrices and then extended to all matrices by continuity.
Over a commutative ring the same idea gives the unit criterion, and in the [[general linear group|0FCHE902D7]] the determinant becomes a group homomorphism to the units of the ring.
