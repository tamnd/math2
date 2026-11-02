---
tag: NGQMPVNZDP
kind: example
name: Swallowtail catastrophe
msc: [58K35, 58K05]
illustrates: [6FKJ6SXP3G, 23RVD8K8RB]
uses: [6FKJ6SXP3G, JV45S0KQE6, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Example

The *swallowtail catastrophe* is the family of functions of one variable $x \in \R$
$$V(x; a, b, c) = x^5 + a x^3 + b x^2 + c x,$$
with three control parameters $(a, b, c) \in \R^3$.
For $a = b = c = 0$ the function is $x^5$, whose [[critical point|0YTCMFB4HC]] at $0$ is degenerate: the first four derivatives vanish there.

The critical points solve $V'(x) = 5x^4 + 3a x^2 + 2b x + c = 0$, and such a point is degenerate when also $V''(x) = 20x^3 + 6a x + 2b = 0$.
Solving these two equations for $b$ and $c$ in terms of $x$ and $a$ gives
$$b = -10x^3 - 3a x, \qquad c = 15x^4 + 3a x^2.$$
So the [[bifurcation set|JV45S0KQE6]] is the surface in $\R^3$ swept out by these curves as $a$ varies.

Fix $a$ and follow the curve $x \mapsto (b, c)$.
Its velocity is $(-30x^2 - 3a, \; 60x^3 + 6a x) = -3(10x^2 + a)\,(1, -2x)$.
For $a > 0$ the velocity never vanishes, and the slice is a smooth curve.
For $a < 0$ the velocity vanishes at $x = \pm\sqrt{-a/10}$, so the slice has two cusps, and between them the curve crosses itself.
This slice, with its two cusps and its crossing point, is the shape that gives the swallowtail its name.

## Explanations

### L1 human

The swallowtail is the third of Thom's seven elementary catastrophes, after the fold and the cusp.
Its potential depends on one state variable and three control knobs.
The set of knob settings where the potential has a degenerate critical point is a surface in space.
Cut it by a plane with $a < 0$ and you see a curve with two sharp points and a loop, like the tail of a swallow.
Crossing this surface changes the number of critical points of the potential by two.
