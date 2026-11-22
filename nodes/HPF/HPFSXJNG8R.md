---
tag: HPFSXJNG8R
kind: example
name: An indefinite Hermitian form on the complex plane
msc: ["15A63", "11E39"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [48P4A1CX85]
not_instance_of:
  - target: 0NB0AWGJBW
    note: h(x, y) = x_1 conj(y_1) - x_2 conj(y_2) has h(e_2, e_2) = -1 < 0 and h((1, 1), (1, 1)) = 0, so it is not positive definite
uses: [8NJ7XY6F1S, AXH4S084MR]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Hermitian form
---

## Example

On $\mathbb{C}^2$, with the second slot conjugate-linear, let
$$h(x, y) = x_1 \bar y_1 - x_2 \bar y_2, \qquad M = \operatorname{diag}(1, -1).$$
We show that $h$ is Hermitian, that it takes both signs, and that it has a basis with the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

1. The matrix $M$ is real and diagonal, so $M^* = M$, and $h$ is Hermitian by the [[characterization of Hermitian forms|AXH4S084MR]].
2. On the diagonal, $h(v, v) = v_1 \bar v_1 - v_2 \bar v_2 = \lvert v_1 \rvert^2 - \lvert v_2 \rvert^2$, which is real for every $v$.
3. The basis vectors give $h(e_1, e_1) = 1 > 0$ and $h(e_2, e_2) = -1 < 0$. So $h$ is indefinite, and it is not an inner product.
4. The value $h(v, v)$ is $0$ exactly when $\lvert v_1 \rvert = \lvert v_2 \rvert$. Examples are $(1, 1)$, $(1, i)$ and $(1, e^{i\theta})$ for every real $\theta$.
5. Let $u = (1, 1)$ and $w = \tfrac12 (1, -1)$. Then
$$h(u, w) = 1 \cdot \tfrac12 - 1 \cdot \left(-\tfrac12\right) = 1, \qquad h(w, w) = \tfrac14 - \tfrac14 = 0, \qquad h(u, u) = 1 - 1 = 0.$$
6. Since $h$ is Hermitian, $h(w, u) = \overline{h(u, w)} = 1$. So in the basis $(u, w)$ the matrix of $h$ is $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

Check of step 6 by the change of basis rule: with $P = \begin{pmatrix} 1 & \tfrac12 \\ 1 & -\tfrac12 \end{pmatrix}$, which is real, $P^{\mathsf{T}} M \bar P = P^{\mathsf{T}} M P$, and
$$M P = \begin{pmatrix} 1 & \tfrac12 \\ -1 & \tfrac12 \end{pmatrix}, \qquad P^{\mathsf{T}} M P = \begin{pmatrix} 1 & 1 \\ \tfrac12 & -\tfrac12 \end{pmatrix} \begin{pmatrix} 1 & \tfrac12 \\ -1 & \tfrac12 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.$$

## Remarks

The form is nondegenerate, since $\det M = -1 \ne 0$.
Its vectors with $h(v, v) = 0$ form a real cone of real dimension $3$ in $\mathbb{C}^2$, which has real dimension $4$.
This cone is the union of infinitely many complex lines, one through each $(1, e^{i\theta})$, while the real form $x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$ has only the two lines $x_2 = \pm x_1$.
Step 6 shows a Hermitian hyperbolic plane, the analogue of the [[real hyperbolic plane of $x_1 y_1 - x_2 y_2$|X6C1Z0W252]].
The isometry group of this form is the unitary group $U(1, 1)$.

What changes when a sign changes?
With $M = \operatorname{diag}(1, 1)$ we get the standard inner product, which has no nonzero vectors with $h(v, v) = 0$.
With $M = \operatorname{diag}(1, 0)$ the form is degenerate, and $e_2$ is orthogonal to every vector.

## Explanations

### L1 human

This Hermitian form gives a positive number on some vectors and a negative number on others.
For example, $(1, 0)$ gives $1$ and $(0, 1)$ gives $-1$.
So it cannot measure lengths, and it is not an inner product.
On the vectors whose two entries have the same size, such as $(1, i)$, it gives $0$.

### L2 human

For a diagonal Hermitian form, read the signs of the diagonal entries.
Here they are $+1$ and $-1$, so the form is indefinite.
By the Hermitian version of Sylvester's law of inertia, no change of basis can remove the $-1$.

Watch out: over $\mathbb{C}$ the bilinear form $x_1 y_1 - x_2 y_2$ becomes $x_1 y_1 + x_2 y_2$ after the substitution $x_2 \mapsto i x_2$, $y_2 \mapsto i y_2$, because $i \cdot i = -1$.
The same trick fails for the Hermitian form, since $(i x_2)\overline{(i y_2)} = x_2 \bar y_2$.
So $x_1 \bar y_1 - x_2 \bar y_2$ is not equivalent to the standard inner product, and its negative values $h(v, v) < 0$ show this directly.
