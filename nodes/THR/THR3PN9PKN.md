---
tag: THR3PN9PKN
kind: statement
role: proposition
name: Lensmaker's equation
msc: [78A05]
uses: [N111BHFQ2H, 9VGK0SP6EQ, QDV9SBK6W0]
about: [9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Lens
    locator: Lensmaker's equation
---

## Statement

Let a lens be made of a homogeneous material of [[refractive index|9VGK0SP6EQ]] $n$ and be surrounded by air of index $1$.
Let its two surfaces be spherical with radii of curvature $R_1$ (the surface met first by the light) and $R_2$.
A radius is positive when its centre of curvature lies beyond the surface in the direction of travel of the light.
Let $d$ be the thickness of the lens on its axis.
Then, in the [[paraxial approximation|N111BHFQ2H]], the focal length $f$ of the lens satisfies
$$\frac{1}{f} = (n - 1)\left[\frac{1}{R_1} - \frac{1}{R_2} + \frac{(n - 1) d}{n R_1 R_2}\right].$$
For a thin lens, with $d$ negligible, this becomes
$$\frac{1}{f} = (n - 1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right).$$

## Remarks

A single spherical surface of radius $R$ between indices $n_1$ and $n_2$ has paraxial power $(n_2 - n_1)/R$; this follows from the paraxial form of [[Snell's law|QDV9SBK6W0]].
The lens is two such surfaces with a gap $d$ of glass between them, and combining the two refractions gives the formula.
With ray transfer matrices, $1/f$ is minus the $C$ entry of the product of the three matrices (surface, thickness $d$ with reduced angle, surface).

Example: a symmetric biconvex lens with $n = 1.5$ and $R_1 = 20$ cm, $R_2 = -20$ cm.
The thin-lens formula gives $1/f = 0.5 \cdot (1/20 + 1/20) = 1/20$, so $f = 20$ cm.

For a lens in a medium of index $n_m$, replace $n - 1$ by $(n - n_m)/n_m$ in the thin-lens formula.
A glass lens that converges in air therefore converges less strongly in water.

## Explanations

### L1 human

The lensmaker's equation tells a lens maker how to grind a lens to get a wanted focal length.
Strongly curved surfaces and glass of high index give a short focal length and a strong lens.
A lens that is thicker in the middle than at the edge brings light together, and one that is thinner in the middle spreads it out.

### L2 human

The equation reduces the design of a simple lens to two radii and an index.
Because $n$ depends on the wavelength, $f$ does too, which is chromatic aberration; achromatic doublets combine two glasses to cancel it to first order.
For a thick lens, the focal length is measured from the principal planes, and the full formula above is needed.
