---
tag: 05MW7MPRBS
kind: definition
name: Cross-ratio
aliases: [cross-ratio, double-ratio, anharmonic-ratio]
msc: [30C35]
defines: 09ASMRMD67
uses: [0CDMXGPSES]
sources:
  - url: https://en.wikipedia.org/wiki/Cross-ratio
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Cross-ratio
    locator: Transformational approach
---

## Definition

Let $z_1, z_2, z_3, z_4$ be four distinct complex numbers.
Their cross-ratio is
$$(z_1, z_2; z_3, z_4) = \frac{(z_3 - z_1)(z_4 - z_2)}{(z_3 - z_2)(z_4 - z_1)}.$$
If one of the four points is the point $\infty$ of the [[Riemann sphere|0CDMXGPSES]] and the other three are distinct complex numbers, the cross-ratio is the same formula without the two factors that contain $\infty$.

## Remarks

Other books use other orders of the four points in the formula, so one must check the convention.
For each [[Möbius transformation|0B346DDAM5]] $f$, the cross-ratio $(f(z_1), f(z_2); f(z_3), f(z_4))$ is equal to $(z_1, z_2; z_3, z_4)$.
With this convention, the map $z \mapsto (z, z_2; z_3, z_4)$ is the Möbius transformation that sends $z_2$, $z_3$, $z_4$ to $1$, $0$, $\infty$.
The cross-ratio is a real number exactly when the four points are on one circle or on one line.

## Explanations

### L1 human

The cross-ratio is one number made from four points.
Möbius transformations change distances and angles of figures in complicated ways, but they do not change this number.
So the cross-ratio helps to find a Möbius map that sends given points to other given points.
