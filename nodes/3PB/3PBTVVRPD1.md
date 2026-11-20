---
tag: 3PBTVVRPD1
kind: example
name: Polar decomposition of a 2 × 2 matrix
msc: [15A23]
topics: [SS4EVPKT3A]
audience: ug2
illustrates: [0J2C7BDJQA, EQ98KW1ZN4]
uses: [0QRBVFJ50X, 0B9QNFGTHM]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_decomposition
    locator: Derivation for invertible matrices
---

## Example

Let $A = \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix}$.
It is invertible, since $\det A = -1 + 4 = 3$.

1. $A^T A = \begin{pmatrix} -1 & 2 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} = \begin{pmatrix} 1 + 4 & 2 + 2 \\ 2 + 2 & 4 + 1 \end{pmatrix} = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}$.
2. By [[the square root example|QTV6Y0710E]], $P = (A^T A)^{1/2} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$. It has eigenvalues $3$ and $1$.
3. $\det P = 4 - 1 = 3$, and $P^{-1} = \tfrac13 \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.
4. $U = A P^{-1} = \tfrac13 \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \tfrac13 \begin{pmatrix} -2 + 2 & 1 - 4 \\ 4 - 1 & -2 + 2 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
5. $U$ is the [[rotation|0B9QNFGTHM]] by $90^\circ$. It is [[orthogonal|0QRBVFJ50X]]: $U^T U = I$.
6. Multiply back: $UP = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} = A$.
7. Determinants: $\det U \det P = 1 \cdot 3 = 3 = \det A$.

## Remarks

- The left polar decomposition is $A = P' U$ with $P' = U P U^T = A U^T = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$. Check: $P'^2 = \begin{pmatrix} 5 & -4 \\ -4 & 5 \end{pmatrix} = A A^T$.
- The singular values of $A$ are the eigenvalues $3$ and $1$ of $P$.
- $A$ maps the unit circle to an ellipse with semi-axes $3$ and $1$. The factor $P$ makes the ellipse, and $U$ turns it by $90^\circ$.

## Explanations

### L1 human

We split the matrix into a stretch and a rotation.
The stretch $P$ pulls the direction $(1, 1)$ by $3$ and keeps the direction $(1, -1)$.
The rotation $U$ then turns the plane by a quarter turn.

### L2 human

The recipe is: compute $A^T A$, take its square root $P$, and put $U = A P^{-1}$.
Step 6 checks the answer, and step 5 checks that $U$ is orthogonal.
A trap: $P$ is not the matrix of absolute values of the entries of $A$, which would be $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ here.
