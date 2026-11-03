---
tag: C8MKHQG55T
kind: definition
name: Crack tip opening displacement
msc: [74R20, 74R10]
defines: 8HFZYWW7SP
uses: [SNRXGRZWR5]
sources:
  - url: https://en.wikipedia.org/wiki/Crack_tip_opening_displacement
---

## Definition

Let a two-dimensional body contain a crack whose tip is blunted by plastic deformation.
Let $x_1$ be the crack direction and $x_2$ the normal to the crack, with the original tip at the origin.
Let $u_2^{\pm}$ be the normal displacement of the upper and lower crack faces in the deformed body.
The *crack tip opening displacement* is the opening $\delta = u_2^+ - u_2^-$ of the crack faces at the tip, defined in one of two standard ways:

1. as the opening at the position of the original crack tip;
2. as the distance between the points where the deformed faces meet the two lines from the tip at $\pm 45^\circ$ to the crack line.

## Remarks

Example: in the Dugdale model of a crack of length $2a$ in a thin plate under remote tension $\sigma$, $\delta = \frac{8 \sigma_Y a}{\pi E} \ln \sec\left( \frac{\pi \sigma}{2 \sigma_Y} \right)$, where $\sigma_Y$ is the yield stress and $E$ Young's modulus.
For small $\sigma / \sigma_Y$, $\ln \sec x \approx x^2/2$ gives $\delta \approx \pi \sigma^2 a / (E \sigma_Y) = K_I^2 / (E \sigma_Y)$ with $K_I = \sigma \sqrt{\pi a}$.
Non-example: the opening of a crack in a purely linear elastic body at its tip is zero, since the faces close like $\sqrt{r}$.
A positive CTOD requires blunting or a cohesive zone.
The second definition in the list is called the $90^\circ$ intercept definition.
In general $\delta = d_n J / \sigma_Y$, where $J$ is the J-integral and $d_n$ a dimensionless factor of order one that depends on the strain hardening and on plane stress or plane strain.

## Explanations

### L1 human

CTOD is the width of the gap between the faces of a blunted crack, measured right at its tip.
