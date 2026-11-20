---
tag: 5AG0M5GR5T
kind: example
name: The plain transpose of a nonzero complex vector can give length zero
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: 0DXKE10PHF
    note: for x = (1, i) the plain transpose gives xᵀx = 0, so xᵀ is not the conjugate transpose and does not measure length
uses: [0W809K6AW0, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_transpose
    locator: Properties
---

## Example

Let $x = \begin{pmatrix} 1 \\ i \end{pmatrix} \in \mathbb{C}^2$.

1. The plain [[transpose|0W809K6AW0]] is $x^{\mathsf{T}} = \begin{pmatrix} 1 & i \end{pmatrix}$.
2. $x^{\mathsf{T}} x = 1 \cdot 1 + i \cdot i = 1 - 1 = 0$.
3. But $x \neq 0$, so $x^{\mathsf{T}} x$ is not the squared length of $x$.
4. The [[conjugate transpose|0EX045E2BP]] $x^* = \begin{pmatrix} 1 & -i \end{pmatrix}$ gives $x^* x = 2$.

## Remarks

Vectors with $x^{\mathsf{T}} x = 0$ and $x \neq 0$ are called isotropic for the bilinear form $x^{\mathsf{T}} y$.
On $\mathbb{C}^n$ with $n \ge 2$ such vectors always exist, so $x^{\mathsf{T}} y$ is not an inner product.

## Explanations

### L1 human

Without conjugates, the squares of complex numbers can cancel.
Here $1^2 + i^2 = 0$, although the vector is not zero.

### L2 human

The complex symmetric bilinear form $x^{\mathsf{T}} y$ is not positive definite.
The Hermitian form $y^* x$ is, and that is why complex linear algebra uses $A^*$ in place of $A^{\mathsf{T}}$.
