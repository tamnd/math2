---
tag: 2X09GT6SMD
kind: example
name: A change of basis for a bilinear form on the rational plane
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [WJWNYSQKK8]
illustrates: [0SPYAGE7T0]
uses: [0SPYAGE7T0, 0P24YW565F, 0KWXYZPJKN]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: lead section
---

## Example

On $\mathbb{Q}^2$ let $B(x, y) = x^{\mathsf{T}} A y$ with
$$A = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}, \qquad B(x, y) = x_1 y_1 + 2x_1 y_2 + 3x_2 y_2.$$
Take the new basis $b'_1 = (1, 1)$ and $b'_2 = (1, -1)$.
We find the matrix of $B$ in the new basis in two ways, and we check that the two answers agree.

1. The [[change of basis matrix|0KWXYZPJKN]] has the columns $b'_1$ and $b'_2$:
$$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \qquad \det P = -1 - 1 = -2 \neq 0.$$
So $P$ is invertible and the two vectors form a basis.
2. First way, by the [[change of basis rule|0SPYAGE7T0]]. Multiply $A$ by $P$, and then multiply by $P^{\mathsf{T}}$ on the left:
$$AP = \begin{pmatrix} 1 + 2 & 1 - 2 \\ 0 + 3 & 0 - 3 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 3 & -3 \end{pmatrix}, \qquad P^{\mathsf{T}} (AP) = \begin{pmatrix} 3 + 3 & -1 - 3 \\ 3 - 3 & -1 + 3 \end{pmatrix} = \begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix}.$$
3. Second way, by the definition of the [[matrix of a form|0P24YW565F]]. Put each pair of new basis vectors into the formula for $B$:
$$B(b'_1, b'_1) = 1 + 2 + 3 = 6, \qquad B(b'_1, b'_2) = 1 - 2 - 3 = -4,$$
$$B(b'_2, b'_1) = 1 + 2 - 3 = 0, \qquad B(b'_2, b'_2) = 1 - 2 + 3 = 2.$$
4. Steps 2 and 3 give the same matrix
$$A' = \begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix}.$$
So $A' = P^{\mathsf{T}} A P$ with $P$ invertible, and $A$ and $A'$ are [[congruent|WJWNYSQKK8]].
5. The ranks agree: both determinants are nonzero, so both matrices have rank $2$.
6. The determinants obey the square rule:
$$\det A = 3, \qquad \det A' = 12 = (-2)^2 \cdot 3 = (\det P)^2 \det A.$$

## Remarks

The example shows that the product $P^{\mathsf{T}} A P$ gives exactly the values of the form on the pairs of new basis vectors.
Order matters in step 3: $B(b'_1, b'_2) = -4$ but $B(b'_2, b'_1) = 0$, because $B$ is not symmetric.
The new matrix $A'$ is not symmetric either, since congruence keeps symmetry and asymmetry alike.

Watch out for the rule of linear maps.
With $P^{-1} = \tfrac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, similarity gives
$$P^{-1} A P = \frac{1}{2} \begin{pmatrix} 6 & -4 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 3 & -2 \\ 0 & 1 \end{pmatrix},$$
which does not contain the value $B(b'_1, b'_1) = 6$.
Here the two answers differ by the factor $2$ because $P^{\mathsf{T}} = 2P^{-1}$ for this particular $P$.

Change one number and see what happens.
If we scale the new basis to $2b'_1$ and $2b'_2$, then $P$ doubles, and $A'$ is multiplied by $4$, since each slot gives one factor $2$.
The determinant becomes $16 \cdot 12 = 192$, which is still $3$ times a rational square, so the square class of the determinant stays the class of $3$ in $\mathbb{Q}^\times / (\mathbb{Q}^\times)^2$.

## Explanations

### L1 human

A form gives a number for each ordered pair of vectors.
In a new basis we store the four numbers for the pairs of new basis vectors in a square.
We can compute these four numbers one by one from the formula, or all at once with a product of three matrices.
Both ways give $6, -4, 0, 2$, so the shortcut and the slow way agree.

### L2 human

The general recipe has three steps.
Put the new basis vectors, in old coordinates, as the columns of $P$.
Compute $P^{\mathsf{T}} A P$.
Check one entry with the formula of the form, for example $B(b'_1, b'_1) = 6$.
The typical use is to choose $P$ so that the new matrix is simpler, for example diagonal or block diagonal.
Watch out: congruent matrices need not have the same eigenvalues.
Here $A$ is triangular with eigenvalues $1$ and $3$, while $A'$ is triangular with eigenvalues $6$ and $2$.
