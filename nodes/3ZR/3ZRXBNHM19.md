---
tag: 3ZRXBNHM19
kind: example
name: Composition of two plane rotations and the addition formulas
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
illustrates: [05Q1B7MH0M]
uses: [0YYMY95FWS, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

Turning the plane by one angle and then by another is a turn by the sum, and the matrix product turns this picture into the addition formulas of trigonometry.
Let $R_\theta \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the rotation by the angle $\theta$ about the origin.
It sends $e_1$ to $(\cos\theta, \sin\theta)$ and $e_2$ to $(-\sin\theta, \cos\theta)$, so its [[matrix|0YYMY95FWS]] in the standard basis is
$$M_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$

1. The rotation by $\alpha$ followed by the rotation by $\beta$ is the rotation by $\alpha + \beta$, so $R_\beta \circ R_\alpha = R_{\alpha + \beta}$.
2. By the theorem on the [[matrix of a composition|05Q1B7MH0M]], $M_{\alpha + \beta} = M_\beta M_\alpha$.
3. Row 1 of $M_\beta$ times column 1 of $M_\alpha$ gives entry $(1, 1)$ of the [[product|076JGP6R3T]], which is $\cos\beta \cos\alpha - \sin\beta \sin\alpha$.
4. Row 2 of $M_\beta$ times column 1 of $M_\alpha$ gives entry $(2, 1)$, which is $\sin\beta \cos\alpha + \cos\beta \sin\alpha$.
5. Column 1 of $M_{\alpha + \beta}$ is $(\cos(\alpha + \beta), \sin(\alpha + \beta))$, so steps 2 to 4 give
$$\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta, \qquad \sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta.$$
6. As a numerical check, take $\alpha = \beta = \pi/4$, so $M_{\pi/4} = \frac{1}{\sqrt 2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$ and
$$M_{\pi/4}^2 = \frac12 \begin{pmatrix} 1 - 1 & -1 - 1 \\ 1 + 1 & -1 + 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = M_{\pi/2}.$$

## Remarks

The example proves the addition formulas from two facts: the geometry of turning, and the rule that composition is multiplication.
Column 2 of the product gives nothing new, since it repeats the same two formulas with signs changed.

Rotations of the plane commute, because $\alpha + \beta = \beta + \alpha$, so here $M_\alpha M_\beta = M_\beta M_\alpha$.
For most pairs of linear maps the order matters.
Take the reflection $Q(x, y) = (x, -y)$ and the quarter turn $R_{\pi/2}$.
Then $R_{\pi/2} \circ Q$ sends $e_1$ to $R_{\pi/2}(e_1) = e_2$, but $Q \circ R_{\pi/2}$ sends $e_1$ to $Q(e_2) = -e_2$.
In matrices,
$$M_{\pi/2} \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} M_{\pi/2} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}.$$

## Explanations

### L1 human

Turning by one angle and then by another is the same as turning by the sum of the angles.
For example, two turns by $45$ degrees make one turn by $90$ degrees.
Multiplying the two rotation matrices shows this, and the entries of the product give the addition formulas of trigonometry.

### L2 human

The geometric fact $R_\beta \circ R_\alpha = R_{\alpha + \beta}$ and the matrix theorem together prove the addition formulas.
The matrix of the map that acts first stands on the right in the product.
For rotations this makes no difference, but the remarks show that a reflection and a rotation do not commute.
Watch out: from $M_\beta M_\alpha = M_\alpha M_\beta$ for rotations you cannot conclude that matrices commute in general.
