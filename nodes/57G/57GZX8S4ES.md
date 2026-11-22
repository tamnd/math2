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

Over $\mathbb{Q}$ let
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}, \qquad P = \begin{pmatrix} 1 & -2 \\ 0 & 1 \end{pmatrix}.$$
We show that $A$ is [[congruent|NZJDNC6EP6]] to a diagonal matrix $D$, and that $A$ and $D$ have different eigenvalues, so they are not similar.

1. The matrix $P$ is invertible, since $\det P = 1 \cdot 1 - (-2) \cdot 0 = 1$.
2. Multiply $A$ by $P$ on the right:
$$AP = \begin{pmatrix} 1 & -2 + 2 \\ 2 & -4 + 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix}.$$
3. Multiply by $P^{\mathsf{T}}$ on the left:
$$D = P^{\mathsf{T}} A P = \begin{pmatrix} 1 & 0 \\ -2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}.$$
So $A$ and $D$ are congruent.
4. The characteristic polynomial of $A$ is
$$\det(A - tI) = (1 - t)^2 - 4 = t^2 - 2t - 3 = (t - 3)(t + 1),$$
so the eigenvalues of $A$ are $3$ and $-1$.
5. The eigenvalues of the diagonal matrix $D$ are its diagonal entries $1$ and $-3$.
6. [[Similar matrices|0E89HQATM8]] have the same characteristic polynomial, hence the same eigenvalues. So $A$ and $D$ are not similar.
7. For comparison, similarity by the same $P$ does not even give a diagonal matrix. With $P^{-1} = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$,
$$P^{-1} A P = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 2 & -3 \end{pmatrix} = \begin{pmatrix} 5 & -6 \\ 2 & -3 \end{pmatrix}.$$
Check: its trace $2$ and its determinant $-3$ are those of $A$, as similarity requires.

## Remarks

The example shows that congruence and similarity are different relations, even for symmetric matrices.
In the language of forms, $x^{\mathsf{T}} A y = x_1 y_1 + 2x_1 y_2 + 2x_2 y_1 + x_2 y_2$ becomes $x'_1 y'_1 - 3x'_2 y'_2$ in the basis $(1, 0), (-2, 1)$, the columns of $P$.

The two matrices agree in everything that congruence keeps.
Both have rank $2$, both are symmetric, and both have determinant $-3$, which here happens to be equal because $\det P = 1$.
The signs of the eigenvalues agree too, one positive and one negative, as [[Sylvester's law of inertia|0WFED3K3DQ]] predicts: the signs survive congruence over $\mathbb{R}$, but the sizes do not.

What changes when $P$ changes?
Replace $P$ by $P \operatorname{diag}(1, c)$ with $c \neq 0$, and the diagonal entry $-3$ becomes $-3c^2$, so the second entry can be $-3$ times any nonzero square.
If $P$ is orthogonal, congruence and similarity coincide, and then the diagonal entries must be the eigenvalues $3$ and $-1$, by the [[principal axis theorem|0PR5P9Z4KM]].
For example, $P = \tfrac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ gives $P^{\mathsf{T}} A P = \operatorname{diag}(3, -1)$, but it needs $\sqrt{2}$ and so it works over $\mathbb{R}$, not over $\mathbb{Q}$.

## Explanations

### L1 human

The same form can look different in different coordinates.
Here one square table of numbers has the special values $3$ and $-1$, its eigenvalues.
After a change of coordinates for the form, we get a table with $1$ and $-3$ on its diagonal.
So the eigenvalues of the table are not properties of the form.
What does survive is the pattern of signs: one plus and one minus.

### L2 human

The computation is the symmetric version of row reduction.
Subtract $2$ times row $1$ from row $2$ of $A$, which gives $\begin{pmatrix} 1 & 2 \\ 0 & -3 \end{pmatrix}$.
Then subtract $2$ times column $1$ from column $2$, which gives $\begin{pmatrix} 1 & 0 \\ 0 & -3 \end{pmatrix}$.
The row step is multiplication by $P^{\mathsf{T}}$ on the left, and the column step is multiplication by $P$ on the right.
The typical use is to diagonalize a symmetric form over any field with $1 + 1 \neq 0$, with no eigenvalues and no square roots.
Watch out: the diagonal entries of $P^{\mathsf{T}} A P$ are eigenvalues of $A$ only when $P$ is orthogonal.
