---
tag: 57GZX8S4ES
kind: example
name: Congruent symmetric matrices with different eigenvalues
msc: ["15A63", "15A21"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [WJWNYSQKK8]
not_instance_of:
  - target: 0E89HQATM8
    note: the matrices [[1, 2], [2, 1]] and diag(1, -3) are congruent, but they are not similar, because their eigenvalues 3, -1 and 1, -3 differ
uses: [NZJDNC6EP6, 0E89HQATM8]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: Congruence over the reals
---

## Example

Over $\Q$ let $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$ and $P = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}$.
We show that $A$ is [[congruent|NZJDNC6EP6]] to a diagonal matrix with other eigenvalues.

1. $\det P = 1$, so $P$ is invertible.
2. $AP = \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix}$.
3. $P^T = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix}$, so $D = P^T A P = \begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}$.
4. The characteristic polynomial of $A$ is $(1 - t)^2 - 4 = (t - 3)(t + 1)$. So the eigenvalues of $A$ are $3$ and $-1$.
5. The eigenvalues of the diagonal matrix $D$ are $1$ and $-3$.
6. [[Similar matrices|0E89HQATM8]] have the same eigenvalues. So $A$ and $D$ are not similar.
7. For the same $P$, $P^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ and $P^{-1} A P = \begin{pmatrix} 5 & -6 \\ 2 & -3 \end{pmatrix}$, which is not diagonal.

## Remarks

The example shows that congruence and similarity are different relations.
The form $x^T A y = x_1 y_1 + 2x_1 y_2 + 2x_2 y_1 + x_2 y_2$ becomes $x'_1 y'_1 - 3x'_2 y'_2$ in the basis $(1, 0), (-2, 1)$.
The two matrices agree in what congruence keeps: rank $2$, symmetry, and the sign of the determinant, $-3$ for both.
The signs of the eigenvalues agree too, one positive and one negative, as [[Sylvester's law of inertia|0WFED3K3DQ]] predicts.
An orthogonal $P$ gives congruence and similarity at once, and then the diagonal entries are $3$ and $-1$, by the [[principal axis theorem|0PR5P9Z4KM]].

## Explanations

### L1 human

The same form can look different in different coordinates.
Here one square of numbers has the special values $3$ and $-1$.
After a change of coordinates for the form, we get a square with $1$ and $-3$ on the diagonal.
So the special values of a matrix are not properties of the form.

### L2 human

The computation is the symmetric version of row reduction.

1. Subtract $2$ times row 1 from row 2 of $A$, which gives $\begin{pmatrix} 1 & 2 \\ 0 & -3 \end{pmatrix}$.
2. Subtract $2$ times column 1 from column 2, which gives $\begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}$.
3. The row step is multiplication by $P^T$ on the left, and the column step is multiplication by $P$ on the right.

The typical use is the diagonalization of a symmetric form without eigenvalues.
A trap: the diagonal entries of $P^T A P$ are not eigenvalues of $A$, unless $P$ is orthogonal.
