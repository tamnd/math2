---
tag: 0SPYAGE7T0
kind: statement
role: proposition
name: Change of basis for a bilinear form
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
about: [0QK6K857HS, WJWNYSQKK8]
uses: [0P24YW565F, 0KWXYZPJKN, 0MQXVZEBMT, 02FDWY55AS, 04CPJ6AF00, 0ZZQ2E1MTE]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester%27s_law_of_inertia
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Coordinate representation
  - book: isbn:9780135367971
    locator: Chapter 10
---

## Statement

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$, with two bases $\mathcal{B}$ and $\mathcal{B}'$.
Let $P$ be the [[change of basis matrix|0KWXYZPJKN]] whose columns are the coordinate vectors of the vectors of $\mathcal{B}'$ in $\mathcal{B}$.
Let $B$ be a bilinear form on $V$, with [[matrix|0P24YW565F]] $M$ in $\mathcal{B}$ and $M'$ in $\mathcal{B}'$.

1. The two matrices satisfy
$$M' = P^T M P.$$
2. $\rank M' = \rank M$. So the rank of $B$, defined as the [[rank|0ZC9YTXZRY]] of its matrix in any basis, does not depend on the basis.
3. $\det M' = (\det P)^2 \det M$, with $\det P \neq 0$. So $\det M$ is fixed up to a factor that is a nonzero square in $F$.

The [[proof|RATQ474V7S]] expands $B(b'_k, b'_l)$ by bilinearity.

## Remarks

### Why each hypothesis is needed

- $\mathcal{B}'$ must be a basis, so that $P$ is [[invertible|0EB9N0S33C]]. For a noninvertible $P$ the product $P^T M P$ can lose rank: $P = 0$ gives the zero matrix.
- $V$ must be finite-dimensional, because a matrix has finitely many rows and columns.
- The rule is for bilinear forms. For a [[sesquilinear form|054YEQ0Y8M]] the rule is $M' = P^T M \overline{P}$, and the determinant changes by $\abs{\det P}^2$.

### Consequences

- Two matrices represent the same form in two bases exactly when they are [[congruent|WJWNYSQKK8]].
- The rank of a form is well defined. A form on $V$ is [[nondegenerate|01NHFZF2SK]] exactly when its rank is $\dim V$.
- When $B$ is nondegenerate, the class of $\det M$ in the [[square class group|9160DW40TE]] $F^\times / (F^\times)^2$ is the discriminant of $B$. It does not depend on the basis.
- Over $\R$ the sign of $\det M$ does not depend on the basis, since $(\det P)^2 > 0$.
- The [[worked example|2X09GT6SMD]] shows the rule for a form on $\Q^2$.

### Converse

If $M' = P^T M P$ for an invertible $P$, then $M$ and $M'$ are the matrices of one form in two bases.
Take the form with matrix $M$ in $\mathcal{B}$, and the basis $\mathcal{B}'$ whose coordinate vectors are the columns of $P$.
Part 1 gives the matrix $M'$.

### Generalizations

For a bilinear map $V \times W \to F$ with changes of basis $P$ in $V$ and $Q$ in $W$, the matrix changes to $P^T M Q$.
For a [[sesquilinear form|054YEQ0Y8M]] it changes to $P^T M \overline{P}$.

## History

Sylvester published his law of inertia for real quadratic forms in 1852, according to the Wikipedia article on that law.
The law is a statement about this change of basis rule for symmetric matrices.

## Explanations

### L1 human

When we change the basis, the matrix of a bilinear form changes by $P^T M P$.
Both vectors change coordinates, so $P$ appears twice.
For a linear map the rule is $P^{-1} A P$ instead.
So the same square of numbers changes in two different ways, according to what it describes.

### L2 human

We change the basis for $B(x, y) = x^T M y$ on $\Q^2$ with $M = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.

1. Take the new basis $b'_1 = (1, 1)$ and $b'_2 = (1, -1)$. Then $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
2. $MP = \begin{pmatrix} 3 & -1 \\ 3 & -3 \end{pmatrix}$ and $P^T M P = \begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix}$.
3. A direct check: $B(b'_1, b'_1) = 1 + 2 + 3 = 6$ and $B(b'_2, b'_1) = 1 + 2 - 3 = 0$.
4. $\det M = 3$ and $\det M' = 12 = (-2)^2 \cdot 3$, as part 3 states.

The typical use is to find a basis in which the matrix is simple, for example diagonal.
A trap: $P^{-1} M P$ is the wrong formula for a form.
Here $P^{-1} M P = \begin{pmatrix} 3 & -2 \\ 0 & 1 \end{pmatrix}$, which is not $M'$.

### L3 human

The rule $P^T M P$ is the law of a map $V \to V^*$ under a change of basis, because the dual basis changes by the inverse transpose of $P$.
So the matrices of forms make a representation of $GL_n(F)$ on $M_n(F)$ that differs from conjugation.
The orbits of this action are the [[congruence classes|WJWNYSQKK8]], and their invariants are the rank, the discriminant and, over ordered fields, the [[signature|07EZA80NEH]].
The square class of the discriminant is the first invariant of the theory of quadratic forms over number fields.
