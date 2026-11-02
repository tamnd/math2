---
tag: PPEWPSQB9K
kind: definition
name: Horocycle
msc: [51M10, 53A35]
defines: 1E8WCHSAE2
uses: [GN4N94GQ0Z, NSYMQMHPDN, RHKSMPBSQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Horocycle
---

## Definition

Let $\mathbb{H}^2$ be the [[hyperbolic plane|GN4N94GQ0Z]] with distance $d$, and let $\omega$ be an ideal point, a point at infinity of $\mathbb{H}^2$.
Let $\gamma \colon [0, \infty) \to \mathbb{H}^2$ be a [[geodesic|NSYMQMHPDN]] ray parametrized by arc length with $\gamma(t) \to \omega$.
The *Busemann function* of $\gamma$ is
$$b(x) = \lim_{t \to \infty} \bigl( d(x, \gamma(t)) - t \bigr), \qquad x \in \mathbb{H}^2.$$
A *horocycle centred at* $\omega$ is a level set $\set{x \in \mathbb{H}^2 : b(x) = c}$ with $c \in \R$.

## Remarks

Another ray to $\omega$ changes $b$ by an additive constant, so the set of horocycles centred at $\omega$ depends only on $\omega$.
Example: in the [[Poincaré half-plane model|RHKSMPBSQ1]], take $\omega = \infty$ and $\gamma(t) = i e^t$.
For $x = u + iy$, the distance formula $\cosh d(z, w) = 1 + \abs{z - w}^2 / (2 \operatorname{Im} z \operatorname{Im} w)$ gives $d(x, i e^t) = t - \ln y + o(1)$ as $t \to \infty$.
So $b(x) = -\ln y$, and the horocycles centred at $\infty$ are the horizontal lines $y = \text{const}$.
Their normal geodesics are the vertical half-lines, which all end at $\infty$.
Horocycles centred at a real point $\omega$ are Euclidean circles tangent to the real axis at $\omega$, without $\omega$.
Non-example: the ray $\set{r e^{i\theta} : r > 0}$ with $0 < \theta < \pi/2$ is not a horocycle.
Its normal geodesics are the semicircles centred at $0$, and they end at different real points, so no single ideal point $\omega$ works.
This ray is a curve at constant distance from the imaginary axis, called a hypercycle.
