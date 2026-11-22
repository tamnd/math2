---
tag: QG8VQCE4QC
kind: example
name: The Gram matrix of two vectors in R3
msc: ["15A63", "15A15"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [00SPJSDT3Z]
uses: [0HX8HZ1WTQ, 0N5N15HWZ7, 08WE2W7DYS, A1Y41YZFB6]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Gram determinant
---

## Example

In $\mathbb{R}^3$ with the dot product, let $v_1 = (1, 1, 0)$ and $v_2 = (1, 0, 1)$.
We compute their [[Gram matrix|0HX8HZ1WTQ]] and then check its determinant against the area of the parallelogram in three independent ways.

1. The three inner products are $v_1 \cdot v_1 = 2$, $v_1 \cdot v_2 = 1$ and $v_2 \cdot v_2 = 2$, so
$$G = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det G = 4 - 1 = 3.$$
2. The matrix $G$ is symmetric and $\det G > 0$, so $v_1$ and $v_2$ are independent.
3. First check, by the [[cross product|0N5N15HWZ7]]:
$$v_1 \times v_2 = (1 \cdot 1 - 0 \cdot 0, \ 0 \cdot 1 - 1 \cdot 1, \ 1 \cdot 0 - 1 \cdot 1) = (1, -1, -1),$$
and $\norm{v_1 \times v_2}^2 = 1 + 1 + 1 = 3 = \det G$.
4. Second check, by minors. The matrix $A$ with the columns $v_1, v_2$ has the rows $(1, 1)$, $(1, 0)$ and $(0, 1)$, and its three $2 \times 2$ minors are $1 \cdot 0 - 1 \cdot 1 = -1$, $1 \cdot 1 - 1 \cdot 0 = 1$ and $1 \cdot 1 - 0 \cdot 0 = 1$.
5. The squares of the minors add up to $1 + 1 + 1 = 3$, as the [[Cauchy-Binet formula|08WE2W7DYS]] predicts for $\det(A^{\mathsf{T}} A)$.
6. Third check, by the [[Gram-Schmidt process|A1Y41YZFB6]]: $u_1 = v_1$ and $u_2 = v_2 - \frac{1}{2} v_1 = (\frac12, -\frac12, 1)$.
7. Check: $u_2 \cdot v_1 = \frac12 - \frac12 + 0 = 0$. The squared lengths are $\norm{u_1}^2 = 2$ and $\norm{u_2}^2 = \frac14 + \frac14 + 1 = \frac32$, and $2 \cdot \frac32 = 3 = \det G$.

So the parallelogram with sides $v_1$ and $v_2$ has area $\sqrt{3}$.

## Remarks

The example shows why the Gram determinant is useful: the two vectors live in $\mathbb{R}^3$, so $A$ is $3 \times 2$ and has no determinant, but $G$ is $2 \times 2$ and does.
The angle between the vectors gives a fourth check.
From $\cos \theta = \frac{1}{\sqrt2 \sqrt2} = \frac12$ we get $\theta = \frac{\pi}{3}$, and then
$$\text{area} = \norm{v_1} \norm{v_2} \sin \theta = \sqrt2 \cdot \sqrt2 \cdot \frac{\sqrt3}{2} = \sqrt3.$$

If you replace $v_2$ by $(1, 1, 1)$, the inner product with $v_1$ becomes $2$ and $\norm{v_2}^2 = 3$, so $\det G = 6 - 4 = 2$ and the area is $\sqrt2$.
If you replace $v_2$ by $(2, 2, 0) = 2 v_1$, then $G = \begin{pmatrix} 2 & 4 \\ 4 & 8 \end{pmatrix}$ and $\det G = 16 - 16 = 0$: the parallelogram is flat.

## Explanations

### L1 human

Two arrows in space that start at the same point span a parallelogram.
The table of their dot products is $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
Its determinant, $3$, is the square of the area of the parallelogram, so the area is $\sqrt3$, about $1.73$.

### L2 human

The three checks use three different tools: the cross product, the minors of $A$, and the Gram-Schmidt process.
They agree because each one computes the same squared area.
The cross product works only in $\mathbb{R}^3$, while the minors and the Gram-Schmidt process work for any number of vectors in any $\mathbb{R}^n$.
Watch out: $\det G$ is the squared area, so the area is $\sqrt3$, not $3$.
