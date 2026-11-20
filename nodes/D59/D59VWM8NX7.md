---
tag: D59VWM8NX7
kind: example
name: Restriction and quotient of a 3 × 3 matrix
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0KN7EPH7Z0, 0ACX5QT8TE]
illustrates: [ENVF51H5S3]
uses: [0PFPWKBDTJ, 0EP59ESQ94, 039HF58KQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9780135367971
    locator: Section 6.4
---

## Example

Let $A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ act on $\R^3$, and let $U = \operatorname{span}(e_1, e_2)$.

1. $U$ is [[invariant|0ACX5QT8TE]]: $A e_1 = (1, 2, 0)$ and $A e_2 = (2, 1, 0)$ lie in $U$.
2. The [[restriction|0KN7EPH7Z0]] $A|_U$ has the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ in $(e_1, e_2)$. Its [[characteristic polynomial|0VSSPAFM2C]] is $(t - 1)^2 - 4 = t^2 - 2t - 3 = (t - 3)(t + 1)$.
3. The quotient $\R^3 / U$ has the basis $e_3 + U$. The quotient operator sends it to $A e_3 + U = (5, 7, 4) + U = 4 e_3 + U$, since $(5, 7, 0) \in U$. So its matrix is $(4)$, with characteristic polynomial $t - 4$.
4. Expanding $\det(t I - A)$ along the last row gives $(t - 4)\big((t - 1)^2 - 4\big) = (t - 3)(t + 1)(t - 4)$. This is the product of the polynomials of steps 2 and 3.
5. The eigenvalues $3$ and $-1$ have eigenvectors $(1, 1, 0)$ and $(1, -1, 0)$ in $U$. Indeed, $A(1, 1, 0) = (3, 3, 0)$ and $A(1, -1, 0) = (-1, 1, 0)$.
6. The eigenvalue $4$ of the quotient operator has the eigenvector $e_3 + U$. But $e_3$ is not an eigenvector of $A$, since $A e_3 = (5, 7, 4)$.
7. Solving $(A - 4I) v = 0$ gives $v = (29, 31, 5)$. Check: $A v = (29 + 62 + 25, 58 + 31 + 35, 20) = (116, 124, 20) = 4v$.
8. The vector $v$ lies in the coset $5 e_3 + U$, so it is a lift of the eigenvector $5(e_3 + U)$ of the quotient operator.

## Remarks

The example shows that the quotient operator finds the eigenvalue $4$ without finding its eigenvector in $\R^3$.
An eigenvector of $\bar A$ always lifts to an eigenvector of $A$ when its eigenvalue is not an eigenvalue of $A|_U$, as here.
If the entry $4$ is replaced by $3$, the eigenvalue $3$ becomes a double root of $p_A$, and the lift can fail.
For $\begin{pmatrix} 3 & 1 \\ 0 & 3 \end{pmatrix}$ and $U = \R e_1$, the quotient has the eigenvector $e_2 + U$, but no eigenvector of the matrix lies outside $U$.

## Explanations

### L1 human

The matrix keeps the floor $z = 0$ of space in place.
On the floor, it acts like a smaller $2 \times 2$ matrix, with the stretch factors $3$ and $-1$.
If we look only at heights, the matrix multiplies every height by $4$.
So the three stretch factors of the whole matrix are $3$, $-1$ and $4$.

### L2 human

The lift in step 7 is found by elimination.

1. The system $(A - 4I) v = 0$ is $-3x + 2y + 5z = 0$ and $2x - 3y + 7z = 0$.
2. Set $z = 5$. Then $-3x + 2y = -25$ and $2x - 3y = -35$.
3. Multiply the first equation by $3$ and the second by $2$, and add: $-5x = -145$, so $x = 29$.
4. Then $2y = -25 + 87 = 62$, so $y = 31$.

The trap is to stop at $e_3$, which is an eigenvector only modulo $U$.
