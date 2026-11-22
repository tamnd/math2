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

When we change the basis, the matrix of a bilinear form changes by $P^{\mathsf{T}} M P$, and its rank and the square class of its determinant stay the same.

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$, with two bases $\mathcal{B} = (b_1, \dots, b_n)$ and $\mathcal{B}' = (b'_1, \dots, b'_n)$.
Let $P$ be the [[change of basis matrix|0KWXYZPJKN]] whose column $k$ is the coordinate vector of $b'_k$ in $\mathcal{B}$.
Let $B$ be a bilinear form on $V$, with [[matrix|0P24YW565F]] $M = (B(b_i, b_j))$ in $\mathcal{B}$ and $M' = (B(b'_k, b'_l))$ in $\mathcal{B}'$.
Then the following hold.

1. The two matrices satisfy
$$M' = P^{\mathsf{T}} M P.$$
2. $\operatorname{rank} M' = \operatorname{rank} M$, so the rank of $B$, defined as the [[rank|0ZC9YTXZRY]] of its matrix in any basis, does not depend on the basis.
3. $\det M' = (\det P)^2 \det M$ with $\det P \neq 0$, so $\det M$ is fixed up to a factor that is a nonzero square in $F$.

The [[proof|RATQ474V7S]] expands $B(b'_k, b'_l)$ by bilinearity.

## Remarks

### A first computation

Take the form $B(x, y) = x_1 y_2 + x_2 y_1$ on $\mathbb{Q}^2$, with matrix $M = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ in the standard basis.
Choose the new basis $b'_1 = (1, 1)$ and $b'_2 = (1, -1)$, so $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
Multiply out the three factors:
$$MP = \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}, \qquad P^{\mathsf{T}} M P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}.$$
Check: $B(b'_1, b'_1) = 1 \cdot 1 + 1 \cdot 1 = 2$ and $B(b'_2, b'_2) = 1 \cdot (-1) + (-1) \cdot 1 = -2$.
So in the new basis the form is $2x'_1 y'_1 - 2x'_2 y'_2$, and its matrix is diagonal.
The determinant went from $-1$ to $-4 = (\det P)^2 \cdot (-1)$, since $\det P = -2$.
A [[second worked case|2X09GT6SMD]] does the same for a form that is not symmetric.

### Why each hypothesis is needed

The new vectors must form a basis, so that $P$ is [[invertible|0EB9N0S33C]].
For a matrix $P$ that is not invertible, $P^{\mathsf{T}} M P$ can lose rank, and $P = 0$ even gives the zero matrix.
Then $P^{\mathsf{T}} M P$ is still the table of values of $B$ on the columns of $P$, but it is no longer the matrix of $B$ in a basis.

The space must be finite-dimensional, since a matrix has finitely many rows and columns.
The rule is for bilinear forms only.
A [[sesquilinear form|054YEQ0Y8M]], linear in the first slot and conjugate-linear in the second, changes by $M' = P^{\mathsf{T}} M \overline{P}$, and its determinant changes by the factor $\lvert \det P \rvert^2$.

### What it gives you

Two matrices are the matrices of one form in two bases exactly when they are [[congruent|WJWNYSQKK8]].
So every question about forms up to a change of basis is a question about matrices up to congruence.

Part 2 makes the rank of a form well defined.
A form on $V$ is [[nondegenerate|01NHFZF2SK]] exactly when its rank is $\dim V$.

Part 3 makes the determinant an invariant up to squares.
When $B$ is nondegenerate, the class of $\det M$ in the [[square class group|9160DW40TE]] $F^\times / (F^\times)^2$ is the discriminant of $B$.
Over $\mathbb{R}$ every nonzero square is positive, so the sign of $\det M$ does not depend on the basis.
For example, the forms with matrices $I_2$ and $\operatorname{diag}(1, -1)$ have determinants $1$ and $-1$, so no change of basis over $\mathbb{R}$ turns one into the other.
Over $\mathbb{Q}$ the same test shows that $I_2$ and $\operatorname{diag}(1, 2)$ [[are not congruent|R4ZDJG99Q0]], since $2$ is not a rational square.

### Watch out

A matrix that describes a form is not a matrix of a linear map, and the two change by different rules.
A linear map $V \to V$ changes by similarity, $P^{-1} A P$.
For the matrix $M$ of the first computation, the two rules give
$$P^{-1} M P = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad P^{\mathsf{T}} M P = \begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}.$$
Only the second matrix has the values $B(b'_k, b'_l)$ as its entries.
The two rules agree when $P^{\mathsf{T}} = P^{-1}$, that is, when $P$ is orthogonal, and that is why the mistake often goes unnoticed in examples with rotations.

### The converse and a generalization

The converse holds.
If $M' = P^{\mathsf{T}} M P$ for an invertible $P$, take the form with matrix $M$ in $\mathcal{B}$ and the basis $\mathcal{B}'$ whose coordinate vectors are the columns of $P$.
Part 1 says that the matrix of this form in $\mathcal{B}'$ is $M'$.

The same expansion works for a bilinear map $V \times W \to F$ on two spaces.
If $P$ changes the basis of $V$ and $Q$ changes the basis of $W$, the matrix changes to $P^{\mathsf{T}} M Q$.
With two independent changes of basis, every matrix of rank $r$ can be brought to the block form $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$, so only the rank survives.

### Try it

First, find the matrix of $B(x, y) = x_1 y_1 + x_2 y_2$ on $\mathbb{Q}^2$ in the basis $(1, 2), (0, 1)$.
With $P = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$ we get $P^{\mathsf{T}} P = \begin{pmatrix} 5 & 2 \\ 2 & 1 \end{pmatrix}$, and its determinant $1 = 1^2 \cdot 1$ agrees with part 3.

Second, can the form with matrix $I_2$ over $\mathbb{R}$ have the matrix $\operatorname{diag}(1, -4)$ in some basis?
No, because the determinant would change sign, and part 3 allows only positive factors over $\mathbb{R}$.

## History

Gauss, in his Disquisitiones Arithmeticae of 1801, studied binary quadratic forms under linear substitutions of the variables, and this is the same change of basis rule for symmetric matrices.
Sylvester's law of inertia of 1852 is a statement about real quadratic forms under invertible linear substitutions.
In the language of matrices it describes which real symmetric matrices have the form $P^{\mathsf{T}} M P$.

## Explanations

### L1 human

A bilinear form gives a number for each pair of vectors.
In a basis we store the numbers for the pairs of basis vectors in a square table.
When we change the basis, both vectors of each pair get new coordinates.
So the change of coordinates acts twice, once from the left and once from the right, and the table changes by $P^{\mathsf{T}} M P$.
For a linear map only one vector moves in and one comes out, so the rule is $P^{-1} A P$ instead.

### L2 human

Here is a typical use: find a basis in which the form $B(x, y) = x_1 y_1 + 2x_1 y_2 + 2x_2 y_1 + 5x_2 y_2$ on $\mathbb{Q}^2$ has a diagonal matrix.
Its matrix is $M = \begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}$.
Completing the square suggests the new basis $b'_1 = (1, 0)$ and $b'_2 = (-2, 1)$, so $P = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$.
Now compute:
$$MP = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}, \qquad P^{\mathsf{T}} M P = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
Check: $B(b'_2, b'_2) = 4 - 4 - 4 + 5 = 1$.
So the form is the dot product in disguise, and $\det M = 1$ agrees with $\det I_2 = 1$.
Watch out: the eigenvalues of $M$ are $3 \pm 2\sqrt{2}$, not $1$ and $1$, because congruence does not keep eigenvalues.

### L3 human

The rule $P^{\mathsf{T}} M P$ is the change of basis law for a linear map $V \to V^*$ into the [[dual space|07JBSZE0V4]].
The basis of $V$ changes by $P$, the dual basis changes by $(P^{-1})^{\mathsf{T}}$, and the inverse of that factor is $P^{\mathsf{T}}$.
So $GL_n(F)$ acts on $M_n(F)$ by $M \mapsto (P^{-1})^{\mathsf{T}} M P^{-1}$, an action that differs from conjugation.
Its orbits are the [[congruence classes|WJWNYSQKK8]], and their first invariants are the rank, the discriminant and, over ordered fields, the [[signature|07EZA80NEH]].
The sub-area on quadratic forms uses these invariants to [[diagonalize|0Z3FEWZ8HA]] and classify forms.
