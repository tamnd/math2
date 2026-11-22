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
It is invertible, since $\det A = (-1)(1) - (-2)(2) = 3$.
We compute its [[polar decomposition|0J2C7BDJQA]] $A = UP$ and check each factor.

1. Form $A^{\mathsf{T}} A$. The columns of $A$ are $(-1, 2)$ and $(-2, 1)$, with squared lengths $5$ and $5$ and dot product $2 + 2 = 4$, so
$$A^{\mathsf{T}} A = \begin{pmatrix} 5 & 4 \\ 4 & 5 \end{pmatrix}.$$
2. By [[the square root example|QTV6Y0710E]], $P = (A^{\mathsf{T}} A)^{1/2} = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, with the eigenvalues $3$ and $1$.
3. Since $\det P = 4 - 1 = 3$, the inverse is $P^{-1} = \tfrac13 \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.
4. The unitary factor is
$$U = A P^{-1} = \tfrac13 \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = \tfrac13 \begin{pmatrix} -2 + 2 & 1 - 4 \\ 4 - 1 & -2 + 2 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
5. This $U$ is the [[rotation|0B9QNFGTHM]] by $90^\circ$. It is [[orthogonal|0QRBVFJ50X]], because its columns $(0, 1)$ and $(-1, 0)$ are orthonormal, so $U^{\mathsf{T}} U = I$.
6. Multiply back:
$$UP = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} = \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} = A.$$
7. Determinants agree: $\det U \cdot \det P = 1 \cdot 3 = 3 = \det A$.

## Remarks

The left form $A = P' U$ uses the same $U$ and the matrix $P' = U P U^{\mathsf{T}} = A U^{\mathsf{T}}$:
$$P' = \begin{pmatrix} -1 & -2 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}.$$
Check: $P'^2 = \begin{pmatrix} 5 & -4 \\ -4 & 5 \end{pmatrix}$, and the rows of $A$ have squared lengths $5$ and $5$ and dot product $-2 - 2 = -4$, so $P'^2 = A A^{\mathsf{T}}$.
The two stretches differ, because $A$ is not normal, but they have the same eigenvalues $3$ and $1$.

These eigenvalues are the [[singular values|09VMDSRXWJ]] of $A$.
Geometrically, $P$ maps the unit circle to an ellipse with semi-axes $3$ along $(1, 1)$ and $1$ along $(1, -1)$, and $U$ then turns that ellipse by a quarter turn.
The eigenvalues of $A$ itself are different: its characteristic polynomial is $t^2 + 3$, so they are $\pm i\sqrt3$, and their absolute value $\sqrt 3$ is neither singular value.

If we replace $A$ by the singular matrix $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, then $A^{\mathsf{T}} A = 2A = A^2$ and $P = A$, and now $U$ is no longer unique.
Both $U = I$ and the reflection $U = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ satisfy $UP = A$, since that reflection fixes each column of $P$.

## Explanations

### L1 human

We split the matrix into a stretch followed by a turn.
The stretch $P$ pulls the direction $(1, 1)$ to $3$ times its length and keeps the direction $(1, -1)$ as it is.
The turn $U$ then rotates the whole plane by a quarter turn.
Doing the stretch and then the turn has the same effect as $A$.

### L2 human

The recipe is: compute $A^{\mathsf{T}} A$, take its square root $P$, and set $U = A P^{-1}$.
Step 6 checks the answer, and step 5 checks that $U$ is orthogonal, and both checks are worth doing every time.
Watch out: $P$ is not the matrix of absolute values of the entries of $A$, which here is $\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ with the eigenvalue $-1$.
