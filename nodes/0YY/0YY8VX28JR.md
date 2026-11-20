---
tag: 0YY8VX28JR
kind: concept
name: Moore-Penrose inverse
aliases: [pseudoinverse]
msc: [15A09]
topics: [SS4EVPKT3A]
audience: ug2
specializes: [FPHNJ5AAYF]
uses: [0PSRCMCM5X, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Singular value decomposition (SVD)
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linear least-squares
  - book: isbn:9781733146678
    locator: Chapter 7
same_as:
  wikidata: Q43219517
  wikipedia: Moore–Penrose inverse
inventory: [Z0BK2ZVY1Y]
---

## Summary

The Moore-Penrose inverse, or pseudoinverse, of an $m \times n$ complex matrix $A$ is the $n \times m$ matrix $A^+$ that satisfies the four Penrose conditions.
These conditions are $A A^+ A = A$, $A^+ A A^+ = A^+$, and that $A A^+$ and $A^+ A$ are Hermitian.
The [[formal definition|0PSRCMCM5X]] states them.
Every matrix has exactly one pseudoinverse, also a rectangular or singular matrix, by [[the theorem on the pseudoinverse from the SVD|Q9YN0F60ZW]].
For $b \in \C^m$, the vector $A^+ b$ is the least-squares solution of $Ax = b$ with the smallest norm.

## Motivation

Only square matrices with nonzero determinant have an inverse.
A system $Ax = b$ with a rectangular or singular $A$ can have no solution or many solutions.
In both cases we still want one best answer, given by a matrix applied to $b$.
The [[least-squares|0BYTQ4X1HC]] solutions minimize $\norm{Ax - b}$, and among them we take the one of least norm.
This choice depends linearly on $b$, and its matrix is $A^+$.
The four Penrose conditions describe this matrix by equations, without a minimization.

## Notation

- We write $A^+$. Some books write $A^\dagger$, and numerical software calls it `pinv`.
- If $A = U \Sigma V^*$ is a [[singular value decomposition|000NPTMX6J]], then $\Sigma^+$ is the $n \times m$ matrix with diagonal entries $1/\sigma_i$ for $\sigma_i > 0$ and zeros elsewhere. Then $A^+ = V \Sigma^+ U^*$.
- The words "pseudoinverse" and "generalized inverse" sometimes mean a wider class. A [[generalized inverse|FPHNJ5AAYF]] only needs $AGA = A$.

## Remarks

### Examples

- If $A$ is square and invertible, then $A^+ = A^{-1}$, since $A^{-1}$ satisfies the four conditions.
- The zero $m \times n$ matrix has the zero $n \times m$ matrix as pseudoinverse.
- [[The rank-one $3 \times 2$ matrix with columns $(1, 2, 3)$ and $(2, 4, 6)$|PHVR0HP7M5]] has $A^+ = \tfrac{1}{70} A^T$. All four conditions are checked there.
- [[The $3 \times 2$ matrix with independent columns|SYDSCH64X8]] has $A^+ = (A^T A)^{-1} A^T$.
- For a diagonal matrix $D$, $D^+$ inverts the nonzero diagonal entries and keeps the zeros. For example, $\operatorname{diag}(2, 0)^+ = \operatorname{diag}(\tfrac12, 0)$.
- If $A$ has independent rows, then $A^+ = A^* (A A^*)^{-1}$, by the [[minimum-norm solution theorem|QM2Y84VDX8]].

### Non-examples

- [[For $A = \operatorname{diag}(1, 0)$, the identity matrix|2GME1M2784]] satisfies conditions 1, 3 and 4, but not $XAX = X$. So $I$ is a generalized inverse of $A$, but not its pseudoinverse.
- In general $(AB)^+ \ne B^+ A^+$. For $A = (1\ 1)$ and $B = (1\ 0)^T$, $AB = (1)$ and $(AB)^+ = 1$, but $B^+ A^+ = (1\ 0) \cdot \tfrac12 (1\ 1)^T = \tfrac12$.

### Basic properties

- $(A^+)^+ = A$, $(A^*)^+ = (A^+)^*$, and $(cA)^+ = c^{-1} A^+$ for $c \ne 0$.
- $A A^+$ is the orthogonal projection onto the column space of $A$, and $A^+ A$ is the orthogonal projection onto the column space of $A^*$.
- $A^+$ has the same rank as $A$.
- If the columns of $A$ are independent, then $A^+ = (A^* A)^{-1} A^*$ and $A^+ A = I_n$.
- $A^+ b$ is the least-squares solution of $Ax = b$ of least norm. If $Ax = b$ has solutions, it is the [[minimum-norm solution|QM2Y84VDX8]].
- For real matrices, the [[least-squares solution from a reduced SVD|SBP2PCHH9M]] is $A^+ b$.

### History

The Wikipedia article states that Moore described the inverse in 1920, Bjerhammar in 1951, and Penrose in 1955.
It also states that Fredholm had introduced a pseudoinverse of integral operators in 1903.

### Common errors

- Students use $(A^* A)^{-1} A^*$ for every $A$. This formula needs independent columns, because otherwise $A^* A$ is singular.
- Students think that $A A^+ = I$. This holds only when the rows of $A$ are independent; in general $A A^+$ is a projection.
- Students compute $\Sigma^+$ by inverting every diagonal entry. The zero singular values stay zero, and $\Sigma^+$ is transposed in shape.

## Explanations

### L1 human

Many matrices have no inverse.
The pseudoinverse is the best replacement.
It takes the right side $b$ of a system $Ax = b$ and gives the best solution $x$.
"Best" means two things: $Ax$ is as close to $b$ as possible, and $x$ is as short as possible.
For an invertible matrix it is the usual inverse.

### L2 human

The fastest way to compute $A^+$ is the SVD: write $A = U \Sigma V^*$, then invert the nonzero $\sigma_i$ and swap the roles of $U$ and $V$.
For a matrix of rank one, $A = u v^*$, this gives $A^+ = \frac{v u^*}{\norm{u}^2 \norm{v}^2}$.
To check a candidate $X$, test the four Penrose conditions; all four are needed.
A trap: the formula $(A^* A)^{-1} A^*$ fails for dependent columns, and $A^+$ is not continuous in $A$ when the rank changes.
For example, $\operatorname{diag}(1, \varepsilon)^+ = \operatorname{diag}(1, 1/\varepsilon)$ for $\varepsilon \ne 0$, but $\operatorname{diag}(1, 0)^+ = \operatorname{diag}(1, 0)$.

### L3 human

The map $A$ restricts to a bijection from the column space of $A^*$ onto the column space of $A$.
The pseudoinverse is the inverse of this bijection on the column space of $A$, and it is zero on the null space of $A^*$.
So it is the natural inverse once both spaces carry inner products, and it changes when the inner products change.
Weighted pseudoinverses use other inner products.
For bounded operators on Hilbert spaces, the same four conditions define a bounded pseudoinverse exactly when the range is closed.
This belongs to functional analysis.
In numerical linear algebra, $A^+$ is computed from the SVD, with a threshold that treats small singular values as zero.
