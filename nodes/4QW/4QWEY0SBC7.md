---
tag: 4QWEY0SBC7
kind: definition
name: Tidal force
msc: [70F15, 86A05]
defines: 48JY6FBEHB
uses: [29WRN5J730]
sources:
  - url: https://en.wikipedia.org/wiki/Tidal_force
---

## Definition

Let a point mass $M$ be at position $d\,e$ relative to the centre of mass of a body.
Here $d > 0$ and $e$ is a unit vector.
Let $G$ be the gravitational constant.
Let $x$ be a point of the body with $x \ne d\,e$.
The *tidal acceleration* due to $M$ at $x$ is
$$a(x) = GM\left( \frac{d\,e - x}{\norm{d\,e - x}^3} - \frac{e}{d^2} \right),$$
the [[Newtonian attraction|29WRN5J730]] of $M$ at $x$ minus its attraction at the centre of mass.
The *tidal force* on a mass $m$ at $x$ is $m\,a(x)$.

## Remarks

For $\norm{x} \ll d$, a Taylor expansion gives
$$a(x) \approx \frac{GM}{d^3}\big( 3 (x \cdot e)\, e - x \big).$$
Example: at $x = r e$, the point facing $M$, this gives $a \approx 2GMr/d^3$ pointing towards $M$; at $x = -re$ it gives $2GMr/d^3$ pointing away from $M$; at $x \perp e$ it gives $GMr/d^3$ towards the centre.
For the Moon acting on the Earth, $2GMr/d^3 \approx 1.1 \cdot 10^{-6}\ \mathrm{m/s^2}$, about $10^{-7}$ of surface gravity.
Non-example: the full lunar attraction $GM(d\,e - x)/\norm{d\,e - x}^3$ is not the tidal acceleration.
Its value at the centre of mass is a uniform pull that accelerates the whole Earth without deforming it, and only the difference from that value is tidal.
The tidal acceleration is the gradient of the [[tide-generating potential|2E2KCFNMHE]].
