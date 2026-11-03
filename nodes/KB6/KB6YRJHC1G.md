---
tag: KB6YRJHC1G
kind: definition
name: Tide-generating potential
msc: [86A05, 70F15, 86A30]
defines: 2E2KCFNMHE
uses: [48JY6FBEHB, QFYGJVA996]
sources:
  - url: https://en.wikipedia.org/wiki/Tide
---

## Definition

Let a point mass $M$ be at position $d\,e$ relative to the centre of mass of the Earth, with $d > 0$ and $\norm{e} = 1$.
Let $G$ be the gravitational constant.
The *tide-generating potential* of $M$ is the function, defined for $\norm{x} < d$,
$$V(x) = \frac{GM}{\norm{d\,e - x}} - \frac{GM}{d} - \frac{GM\,(x \cdot e)}{d^2}.$$
Its gradient $\nabla V$ is the [[tidal acceleration|48JY6FBEHB]], with the sign convention that force is the gradient of potential.

## Remarks

Writing $r = \norm{x}$ and $\cos\psi = x \cdot e / r$, the generating function of the [[Legendre polynomials|QFYGJVA996]] gives
$$V = \frac{GM}{d} \sum_{n \ge 2} \left(\frac{r}{d}\right)^{n} P_n(\cos\psi),$$
since the terms $n = 0$ and $n = 1$ are exactly the two subtracted terms.
The degree two term is $V_2 = \frac{GM r^2}{2 d^3}\,(3\cos^2\psi - 1)$.
Example: on the Earth's surface, $V_2$ is largest, $GMr^2/d^3$, at $\psi = 0$ and $\psi = \pi$, and smallest, $-GMr^2/(2d^3)$, at $\psi = \pi/2$.
Non-example: the full potential $GM/\norm{d\,e - x}$ is not the tide-generating potential; its linear term produces a uniform acceleration of the whole Earth and no tide.
For the Moon, $r/d \approx 1/60$, so the degree three term is only about $2\%$ of the degree two term.
