---
tag: JJCKCYTBXD
kind: statement
role: proposition
name: Gravitational deflection of light
msc: [83C10, 83B05]
uses: [6Y50T68WKY, RNRTS8WWNM, 29WRN5J730, 2TAW8GAMM1]
about: [RNRTS8WWNM]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_lens
---

## Statement

Let $M$ be a mass, $G$ the gravitational constant and $c$ the speed of light.
Consider a null [[geodesic|RNRTS8WWNM]] of the [[Schwarzschild metric|6Y50T68WKY]] of mass $M$ that comes from infinity and returns to infinity, with impact parameter $b$ satisfying $GM/(c^2 b) \ll 1$.
Then, to first order in $GM/(c^2 b)$, the angle between the incoming and outgoing directions is
$$\alpha = \frac{4 G M}{c^2 b},$$
and the ray bends towards the mass.

## Remarks

For a null geodesic with $u = 1/r$, the orbit equation is $u'' + u = 3GM u^2/c^2$.
The zeroth-order solution is the straight line $u_0 = \sin\varphi / b$.
Inserting it into the right side and solving to first order gives $u = \sin\varphi/b + (GM/(c^2 b^2))(1 + \cos^2\varphi)$, and setting $u = 0$ at the two ends gives the deflection $4GM/(c^2 b)$.
A Newtonian computation that treats light as particles moving at speed $c$ gives only half this value, $2GM/(c^2b)$.
For a ray grazing the Sun the formula gives about $1.75$ arcseconds; the eclipse expedition of 1919 led by Eddington confirmed a value of this size.
In the [[parameterized post-Newtonian formalism|2TAW8GAMM1]] the deflection is $\frac{1 + \gamma}{2} \cdot \frac{4GM}{c^2 b}$.

## Explanations

### L1 human

Light passing near a heavy body does not travel in a straight line: it bends towards the body.
The amount is tiny for the Sun, less than two thousandths of a degree for starlight grazing its edge.
General relativity predicts exactly twice what a naive Newtonian argument gives, and the measurement of this bending in 1919 made Einstein famous.

### L2 human

The bending of light is the basis of gravitational lensing.
A galaxy or a cluster of galaxies between us and a distant source can produce several images of the source, arcs, or a full ring when the alignment is perfect.
Half of the general-relativistic deflection comes from the time part of the metric, as in the Newtonian picture, and the other half from the curvature of space.
