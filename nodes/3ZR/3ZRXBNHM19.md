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

Let $R_\theta \colon \R^2 \to \R^2$ be the rotation by the angle $\theta$ about the origin.
In the standard basis, $R_\theta(e_1) = (\cos\theta, \sin\theta)$ and $R_\theta(e_2) = (-\sin\theta, \cos\theta)$.
So its [[matrix|0YYMY95FWS]] is $M_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$.

1. The rotation by $\alpha$ followed by the rotation by $\beta$ is the rotation by $\alpha + \beta$. So $R_\beta \circ R_\alpha = R_{\alpha + \beta}$.
2. By the theorem on the [[matrix of a composition|05Q1B7MH0M]], $M_{\alpha + \beta} = M_\beta M_\alpha$.
3. Entry $(1, 1)$ of the [[product|076JGP6R3T]] $M_\beta M_\alpha$ is $\cos\beta \cos\alpha - \sin\beta \sin\alpha$.
4. Entry $(2, 1)$ of $M_\beta M_\alpha$ is $\sin\beta \cos\alpha + \cos\beta \sin\alpha$.
5. Compare with column 1 of $M_{\alpha + \beta}$: $\cos(\alpha + \beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta$ and $\sin(\alpha + \beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta$.
6. Numerical check with $\alpha = \beta = \pi/4$: $M_{\pi/4} = \frac{1}{\sqrt 2}\begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix}$, and $M_{\pi/4}^2 = \frac12 \begin{pmatrix} 1 - 1 & -1 - 1 \\ 1 + 1 & -1 + 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = M_{\pi/2}$.

## Remarks

- The rotations of the plane commute, so here $M_\alpha M_\beta = M_\beta M_\alpha$. For most pairs of linear maps the order matters.
- For a non-commuting pair, take the reflection $Q(x, y) = (x, -y)$ and $R_{\pi/2}$. Then $R_{\pi/2} \circ Q$ sends $e_1 \mapsto e_2$, but $Q \circ R_{\pi/2}$ sends $e_1 \mapsto -e_2$.

## Explanations

### L1 human

Turning by one angle and then by another is the same as turning by the sum of the angles.
Multiplying the two rotation matrices shows this, and the entries give the addition formulas of trigonometry.

### L2 human

The geometric fact $R_\beta \circ R_\alpha = R_{\alpha + \beta}$ and the matrix theorem together prove the addition formulas.
The matrix of the map that acts first stands on the right in the product.
The last remark shows that a reflection and a rotation do not commute, so the order of the factors matters in general.
