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

On $\C^2$ let $h(x, y) = x_1 \bar y_1 + 2 x_1 \bar y_2 + 3 x_2 \bar y_2$.

1. Each term is a product of one coordinate of $x$ and one conjugated coordinate of $y$. So $h$ is linear in $x$ and conjugate-linear in $y$, and $h$ is [[sesquilinear|0W44K2VNBD]].
2. The matrix is $M = \begin{pmatrix} h(e_1, e_1) & h(e_1, e_2) \\ h(e_2, e_1) & h(e_2, e_2) \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 0 & 3 \end{pmatrix}$.
3. $h(e_1, e_2) = 2$, but $h(e_2, e_1) = 0 \neq \bar 2$. So $h$ is not [[Hermitian|8NJ7XY6F1S]].
4. Equivalently, $M^* = \begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix} \neq M$, so $M$ is not a [[Hermitian matrix|0EKZCX4K3P]].
5. For $v = (1, i)$, $\bar v = (1, -i)$, and $h(v, v) = 1 \cdot 1 + 2 \cdot 1 \cdot (-i) + 3 \cdot i \cdot (-i) = 1 - 2i + 3 = 4 - 2i$.
6. So $h(v, v)$ is not real, which cannot happen for a Hermitian form.
7. $\det M = 3 \neq 0$, so $h$ is nondegenerate.

## Remarks

The form is the sesquilinear analogue of the nonsymmetric bilinear form [[$x^T A y$ with the same matrix|N9CJZW5596]].
Each sesquilinear form is the sum of a Hermitian form and $i$ times a Hermitian form.
Here $M = H_1 + i H_2$ with $H_1 = \frac12 (M + M^*) = \begin{pmatrix} 1 & 1 \\ 1 & 3 \end{pmatrix}$ and $H_2 = \frac{1}{2i}(M - M^*) = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$.
A check: $H_1 + i H_2 = \begin{pmatrix} 1 & 1 + 1 \\ 1 - 1 & 3 \end{pmatrix} = M$.

## Explanations

### L1 human

This form is linear in the first vector and conjugate-linear in the second, so it is sesquilinear.
But swapping the two vectors does not just conjugate the value.
So it is not Hermitian, and its values on the diagonal need not be real.

### L2 human

The recipe to test a sesquilinear form on $\C^n$ for the Hermitian property is the following.

1. Write the matrix $M_{ij} = h(e_i, e_j)$.
2. Compare $M$ with its conjugate transpose $M^*$.
3. $h$ is Hermitian exactly when $M = M^*$.

The typical use is to check quickly whether a form can be an inner product: a form that is not Hermitian cannot be one.
A trap: a real matrix gives a Hermitian form only when it is symmetric; the upper triangular $M$ here is not.
