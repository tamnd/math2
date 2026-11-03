---
tag: CPMD36AH43
kind: definition
name: Euler–Bernoulli beam equation
msc: [74K10, 74B05, 34B60]
defines: 13FGKM7NQ0
uses: [GDM0J9ZCBT, Q6XAPXMGH0, 1QCSARFXQ0, T8ENJX1905]
sources:
  - url: https://en.wikipedia.org/wiki/Euler–Bernoulli_beam_theory
---

## Definition

Let a straight beam occupy $0 \le x \le L$ along its axis.
Let $E(x) > 0$ be the [[Young's modulus|T8ENJX1905]] of its material and $I(x) > 0$ the [[second moment of area|1QCSARFXQ0]] of its cross-section about the neutral axis.
Let $q(x)$ be the transverse load per unit length and $w(x)$ the deflection of the axis, both measured in the same direction.
The *Euler–Bernoulli beam equation* is
$$\frac{d^2}{dx^2}\left( E I \frac{d^2 w}{dx^2} \right) = q.$$
The [[bending moment|Q6XAPXMGH0]] and the shear force are $M = -E I w''$ and $V = M'$.
For a beam with mass $\mu(x)$ per unit length the dynamic equation is
$$\frac{\partial^2}{\partial x^2}\left( E I \frac{\partial^2 w}{\partial x^2} \right) + \mu \frac{\partial^2 w}{\partial t^2} = q(x, t).$$

## Remarks

Example: a cantilever with constant $EI$, clamped at $x = 0$ and loaded by a point force $P$ at $x = L$, has $w(x) = P x^2 (3L - x) / (6EI)$.
Check: $w'''' = 0$ on $(0, L)$, $w(0) = w'(0) = 0$, $w''(L) = 0$ so $M(L) = 0$, and $V = -EI w''' = P$.
The tip deflection is $w(L) = PL^3/(3EI)$.
A simply supported beam with constant $EI$ under a uniform load $q$ has the largest deflection $5qL^4/(384EI)$ at mid-span.

Non-example: $w(x) = x^2$ with $q = 0$ and constant $EI$ satisfies the equation.
It fails the condition $w(L) = 0$ of a simply supported beam, so it is not the deflection of such a beam.

The usual boundary conditions are $w = w' = 0$ at a clamped end, $w = w'' = 0$ at a simply supported end, and $w'' = w''' = 0$ at a free end when $EI$ is constant.
The equation assumes small deflections and neglects shear deformation; [[Timoshenko–Ehrenfest beam theory|K4W0JQ1K6Z]] adds the shear.
