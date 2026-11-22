---
tag: HTRVMDMNH0
kind: example
name: A sesquilinear form on the complex plane that is not Hermitian
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
instance_of: [054YEQ0Y8M]
not_instance_of:
  - target: 48P4A1CX85
    note: h(e_1, e_2) = 2 but h(e_2, e_1) = 0, which is not the conjugate of 2, and h((1, i), (1, i)) = 4 - 2i is not real
uses: [0W44K2VNBD, 8NJ7XY6F1S, 0EKZCX4K3P]
sources:
  - url: https://en.wikipedia.org/wiki/Sesquilinear_form
    locator: Matrix representation
---

## Example

On $\mathbb{C}^2$, with the convention that the second slot is conjugate-linear, let
$$h(x, y) = x_1 \bar y_1 + 2 x_1 \bar y_2 + 3 x_2 \bar y_2.$$
We show that $h$ is sesquilinear, that it is not Hermitian, and that it takes a value on the diagonal that is not real.

1. Each term is a product of one entry of $x$ and the conjugate of one entry of $y$.
So $h$ is linear in $x$ and conjugate-linear in $y$, and $h$ is [[sesquilinear|0W44K2VNBD]].
2. Read the matrix $M_{ij} = h(e_i, e_j)$ from the coefficients:
$$M = \begin{pmatrix} h(e_1, e_1) & h(e_1, e_2) \\ h(e_2, e_1) & h(e_2, e_2) \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}.$$
3. The [[Hermitian condition|8NJ7XY6F1S]] asks for $h(e_2, e_1) = \overline{h(e_1, e_2)}$.
Here $h(e_1, e_2) = 2$ but $h(e_2, e_1) = 0 \ne \bar 2$, so $h$ is not Hermitian.
4. In matrix terms, $M^* = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix} \ne M$, so $M$ is not a [[Hermitian matrix|0EKZCX4K3P]].
5. Take $v = (1, i)$, so $\bar v = (1, -i)$, and evaluate term by term:
$$h(v, v) = 1 \cdot 1 + 2 \cdot 1 \cdot (-i) + 3 \cdot i \cdot (-i) = 1 - 2i + 3 = 4 - 2i.$$
This value is not real, which cannot happen for a Hermitian form.
6. The determinant is $\det M = 1 \cdot 3 - 2 \cdot 0 = 3 \ne 0$, so $h$ is nondegenerate.

## Remarks

The form is the sesquilinear twin of the [[bilinear form $x^{\mathsf{T}} A y$ with the same matrix|N9CJZW5596]] on the rational plane, which is not symmetric for the same reason.

Every sesquilinear form splits as a Hermitian form plus $i$ times a Hermitian form, as a complex number splits into real and imaginary parts.
Here the two parts have the matrices
$$H_1 = \tfrac12 (M + M^*) = \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}, \qquad H_2 = \tfrac{1}{2i} (M - M^*) = \tfrac{1}{2i} \begin{pmatrix} 0 & 2 \\ -2 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.$$
Both are Hermitian, and $i H_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
Check: $H_1 + i H_2 = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix} = M$.
On $v = (1, i)$ the parts give $H_1(v, v) = 1 - i + i + 3 = 4$ and $H_2(v, v) = (-i)(-i) + i \cdot i = -2$, and indeed $4 + i \cdot (-2) = 4 - 2i$.

What changes if we alter the matrix?
If the corner entry $0$ becomes $2$, the matrix $\begin{pmatrix} 1 & 2 \\ 2 & 3 \end{pmatrix}$ is real and symmetric, so it is Hermitian, and then $h(v, v)$ is real for every $v$.
If instead the top entry $2$ becomes $2i$ and the corner becomes $-2i$, the matrix $\begin{pmatrix} 1 & 2i \\ -2i & 3 \end{pmatrix}$ is Hermitian although it is not symmetric.
What matters is that the two corner entries are conjugates, not that they are equal.

## Explanations

### L1 human

This form is linear in the first vector and conjugate-linear in the second, so it is sesquilinear.
But when you swap the two vectors, the value does not just turn into its conjugate.
For the first and second basis vectors you get $2$ in one order and $0$ in the other.
So the form is not Hermitian, and the value of a vector with itself can fail to be real.

### L2 human

The test for the Hermitian property on $\mathbb{C}^n$ takes three steps.

1. Write the matrix $M_{ij} = h(e_i, e_j)$.
2. Take the conjugate transpose $M^*$.
3. The form is Hermitian exactly when $M = M^*$.

For the form above, step 3 fails at the entries $(1, 2)$ and $(2, 1)$.
The typical use is a quick filter: a form that is not Hermitian cannot be an inner product, so there is no need to test positivity.
Watch out: a real matrix gives a Hermitian form only when it is symmetric, and the upper triangular $M$ here is not.
