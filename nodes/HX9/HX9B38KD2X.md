---
tag: HX9B38KD2X
kind: definition
name: Stress intensity factor
msc: [74R10, 74G70, 74B05]
defines: 8D619PN75J
uses: [H1J9Q4TVJ6, KG2XWEMJ30, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_intensity_factor
---

## Definition

Let a [[linear elastic|6W00ZECYT0]] isotropic body contain a crack with traction-free faces.
Let $P$ be a point of the crack front where the front is smooth.
Use the frame at $P$ of the [[modes of fracture|H1J9Q4TVJ6]]: $x_1$ ahead of the crack, $x_2$ normal to the crack plane, $x_3$ along the front.
Let $(r, \theta)$ be polar coordinates in the $x_1 x_2$-plane, with $\theta = 0$ ahead of the crack.
Let $\sigma_{ij}$ be the components of the [[Cauchy stress|KG2XWEMJ30]].
The *stress intensity factors* at $P$ are
$$K_I = \lim_{r \to 0} \sqrt{2 \pi r} \, \sigma_{22}(r, 0), \quad K_{II} = \lim_{r \to 0} \sqrt{2 \pi r} \, \sigma_{12}(r, 0), \quad K_{III} = \lim_{r \to 0} \sqrt{2 \pi r} \, \sigma_{23}(r, 0),$$
whenever these limits exist.

## Remarks

Example: a straight crack of length $2a$ in an infinite plate under remote tension $\sigma$ perpendicular to the crack has, ahead of each tip, $\sigma_{22}(r, 0) = \sigma (a + r) / \sqrt{r (2a + r)}$.
Then $\sqrt{2 \pi r} \, \sigma_{22}(r,0) \to \sigma \sqrt{2 \pi} \, a / \sqrt{2a} = \sigma \sqrt{\pi a}$, so $K_I = \sigma \sqrt{\pi a}$, while $K_{II} = K_{III} = 0$.
Non-example: for a circular hole in a plate the stress at the edge is finite, so $\sqrt{2\pi r}\,\sigma_{22} \to 0$; a hole has no stress intensity, only a stress concentration factor.
The units of $K$ are stress times the square root of length, for example $\mathrm{MPa}\sqrt{\mathrm{m}}$.

## Explanations

### L1 human

Multiply the stress just ahead of the crack tip by the square root of $2\pi$ times the distance to the tip, and let the distance go to zero.
The number that remains is the stress intensity factor.
