---
tag: Y4YPA5V3KJ
kind: example
name: A dilation that fixes a line is not a transvection
msc: ["15A23"]
topics: [P8J6QR66TJ]
audience: ug1
not_instance_of:
  - target: 0DTCBCKEJP
    note: diag(2, 1) fixes the y-axis pointwise, but it has determinant 2 and moves points off the direction of the fixed line, so it is a dilation and not a transvection
uses: [0NMN00FNW1, 044JNC7ZAA, 0CCQV3884B]
sources:
  - url: https://en.wikipedia.org/wiki/Shear_mapping
    locator: lead section
---

## Example

Fixing a line pointwise is not enough to be a transvection, as the dilation
$$D = \operatorname{diag}(2, 1) = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}, \qquad D \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 2x \\ y \end{pmatrix}$$
over $\mathbb{R}$ shows.
It fixes the $y$-axis pointwise, since $D(0, y)^{\mathsf{T}} = (0, y)^{\mathsf{T}}$, just as a transvection fixes its hyperplane.

The difference is in the direction of motion.
For a [[transvection|0NMN00FNW1]] $x \mapsto x + \varphi(x)v$, each point moves along the line through $v$, and $v$ lies in the fixed hyperplane $\ker\varphi$.
For $D$,
$$D \begin{pmatrix} x \\ y \end{pmatrix} - \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x \\ 0 \end{pmatrix},$$
so points move along the $x$-axis, which is not inside the fixed line.
The determinant confirms this: $\det D = 2$, while every transvection has determinant $1$.
Finally, $D = I_2 + E_{11}$ has the form $I + cE_{ij}$ only with equal indices, which the definition of a transvection excludes.

## Remarks

The condition $\varphi(v) = 0$ is the heart of the definition, and the dilation fails exactly there: in the coordinate-free form $D(x) = x + \varphi(x)v$ with $\varphi(x) = x_1$ and $v = e_1$, we get $\varphi(v) = 1$.
If we replace $2$ by $1$, we get $I_2$, which some books count as the trivial transvection $T_{12}(0)$.
The matrix $D$ is an elementary matrix of the scaling type $D_1(2)$, so it is invertible, with inverse $\operatorname{diag}(\tfrac{1}{2}, 1)$.

## Explanations

### L1 human

This matrix stretches the plane to double its width.
It keeps the $y$-axis fixed, like a shear, but it doubles all areas.
A shear never changes area, so this is not a shear.

### L2 human

There are two quick tests: the determinant must be $1$, and $D - I$ must square to $0$.
Here $D - I = E_{11}$ and $E_{11}^2 = E_{11} \ne 0$, so both tests fail.
A trap: $I + E_{11}$ looks like the formula $I + cE_{ij}$, but the indices must be different.
