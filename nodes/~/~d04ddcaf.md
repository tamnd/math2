---
tag: ~d04ddcaf
kind: example
name: The Gram matrix of two vectors in R3
msc: ["15A63", "15A15"]
topics: [1D4JTZ9VS3]
audience: ug1
instance_of: [00SPJSDT3Z]
uses: [0HX8HZ1WTQ, 0N5N15HWZ7, 08WE2W7DYS, ~53ebde52]
sources:
  - url: https://en.wikipedia.org/wiki/Gram_matrix
    locator: Gram determinant
---

## Example

In $\mathbb{R}^3$ with the dot product, let $v_1 = (1, 1, 0)$ and $v_2 = (1, 0, 1)$.
We compute the [[Gram matrix|0HX8HZ1WTQ]] and check its determinant in three ways.

1. The entries are $v_1 \cdot v_1 = 2$, $v_1 \cdot v_2 = 1$ and $v_2 \cdot v_2 = 2$.
2. So $G = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, and $\det G = 4 - 1 = 3$.
3. $G$ is symmetric, and $\det G > 0$, so $v_1$ and $v_2$ are independent.
4. The [[cross product|0N5N15HWZ7]] is $v_1 \times v_2 = (1 \cdot 1 - 0 \cdot 0,\ 0 \cdot 1 - 1 \cdot 1,\ 1 \cdot 0 - 1 \cdot 1) = (1, -1, -1)$.
5. Its squared length is $3 = \det G$. So the parallelogram with sides $v_1$ and $v_2$ has area $\sqrt{3}$.
6. The matrix $A$ with the columns $v_1, v_2$ has the rows $(1, 1)$, $(1, 0)$ and $(0, 1)$.
7. Its $2 \times 2$ minors are $-1$, $1$ and $1$. The squares add up to $3$, as the [[Cauchy-Binet formula|08WE2W7DYS]] predicts.
8. The [[Gram-Schmidt process|~53ebde52]] gives $u_1 = v_1$ and $u_2 = v_2 - \frac12 v_1 = (\frac12, -\frac12, 1)$.
9. Then $\norm{u_1}^2 \norm{u_2}^2 = 2 \cdot \frac32 = 3 = \det G$.

## Remarks

The angle $\theta$ between $v_1$ and $v_2$ has $\cos\theta = \frac{1}{2}$, so $\theta = \frac{\pi}{3}$.
The area is also $\norm{v_1}\norm{v_2}\sin\theta = 2 \cdot \frac{\sqrt3}{2} = \sqrt3$.
The two vectors lie in $\mathbb{R}^3$, so the ordinary determinant of $A$ is not defined, but the Gram determinant is.

## Explanations

### L1 human

Two arrows in space span a parallelogram.
The table of their dot products is $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
Its determinant, $3$, is the square of the area of the parallelogram.

### L2 human

The three checks use different tools: the cross product, the minors of $A$, and the Gram-Schmidt process.
All give $3$, because each one computes the squared area.
A trap: $\det G$ is the squared area, not the area.
The area is $\sqrt{3}$, not $3$.
