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

Let $A = \begin{pmatrix} 1 & 2 & 5 \\ 2 & 1 & 7 \\ 0 & 0 & 4 \end{pmatrix}$ act on $\R^3$, and let $U = \operatorname{span}(e_1, e_2)$, the plane $z = 0$.
We compute the restriction and the quotient operator, and then we use them to find all three eigenvalues and an eigenvector for each.

1. $U$ is [[invariant|0ACX5QT8TE]], since $A e_1 = (1, 2, 0)$ and $A e_2 = (2, 1, 0)$ lie in $U$.
2. The [[restriction|0KN7EPH7Z0]] $A|_U$ has the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ in the basis $e_1, e_2$.
   Its [[characteristic polynomial|0VSSPAFM2C]] is $(t - 1)^2 - 4 = t^2 - 2t - 3 = (t - 3)(t + 1)$.
3. The quotient $\R^3 / U$ has the basis $e_3 + U$.
   The quotient operator sends it to $A e_3 + U = (5, 7, 4) + U = 4 e_3 + U$, since $(5, 7, 0) \in U$.
   So its matrix is $(4)$, with characteristic polynomial $t - 4$.
4. Expanding $\det(tI - A)$ along the last row gives $(t - 4)\big((t - 1)^2 - 4\big) = (t - 3)(t + 1)(t - 4)$, the product of the polynomials of steps 2 and 3.
5. The eigenvalues $3$ and $-1$ have eigenvectors inside $U$:
$$A (1, 1, 0) = (3, 3, 0), \qquad A (1, -1, 0) = (-1, 1, 0).$$
6. The eigenvalue $4$ of the quotient operator has the eigenvector $e_3 + U$.
   But $e_3$ is not an eigenvector of $A$, since $A e_3 = (5, 7, 4)$.
7. Solving $(A - 4I) v = 0$, as in the L2 explanation, gives $v = (29, 31, 5)$.
   Check:
$$A v = (29 + 62 + 25, \; 58 + 31 + 35, \; 20) = (116, 124, 20) = 4 v.$$
8. The vector $v$ lies in the coset $5 e_3 + U$, so it lifts the eigenvector $5(e_3 + U)$ of the quotient operator.

## Remarks

The example shows that the quotient operator finds the eigenvalue $4$ before anyone finds its eigenvector in $\R^3$.
The lift in step 8 exists for a general reason.
If $\bar A (v_0 + U) = \lambda (v_0 + U)$, then $A v_0 - \lambda v_0 = u$ lies in $U$.
When $\lambda$ is not an eigenvalue of $A|_U$, the map $A|_U - \lambda \id_U$ is invertible, so $u = (A - \lambda I) u'$ for some $u' \in U$, and $v_0 - u'$ is an eigenvector of $A$ in the coset $v_0 + U$.

Change the entry $4$ to $3$, and the lift breaks.
The new matrix $A'$ still has the quotient eigenvector $e_3 + U$ with eigenvalue $3$, but now $3$ is also an eigenvalue of the restriction.
The system $(A' - 3I)v = 0$ reads $-2x + 2y + 5z = 0$ and $2x - 2y + 7z = 0$, and adding the two equations gives $12 z = 0$.
So every eigenvector for $3$ lies in $U$, and no eigenvector of $A'$ lies in the coset $e_3 + U$.

## Explanations

### L1 human

The matrix keeps the floor $z = 0$ of space in place.
On the floor, it acts like a smaller $2 \times 2$ matrix, with the stretch factors $3$ and $-1$.
If we look only at heights, the matrix multiplies every height by $4$.
So the three stretch factors of the whole matrix are $3$, $-1$ and $4$.

### L2 human

The lift in step 7 is found by elimination.
The system $(A - 4I) v = 0$ for $v = (x, y, z)$ is
$$-3x + 2y + 5z = 0, \qquad 2x - 3y + 7z = 0.$$
Set $z = 5$, so that $-3x + 2y = -25$ and $2x - 3y = -35$.
Multiply the first equation by $3$ and the second by $2$, and add, to get $-5x = -145$, so $x = 29$.
Then $2y = -25 + 3 \cdot 29 = 62$, so $y = 31$.
Check the second equation: $2 \cdot 29 - 3 \cdot 31 = 58 - 93 = -35$.
Watch out: stopping at $e_3$ is the usual mistake, because $e_3$ is an eigenvector only modulo $U$.
