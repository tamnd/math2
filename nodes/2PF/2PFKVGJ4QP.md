---
tag: 2PFKVGJ4QP
kind: definition
name: Normal moveout
msc: [86A22, 86A15]
defines: 8E7KGS4ZQH
uses: [0WN5G117YC]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_moveout
---

## Definition

Consider a horizontal reflector at depth $z > 0$ below a homogeneous layer of wave speed $v > 0$.
A source and a receiver at the surface are at distance $x \ge 0$ (the offset), placed symmetrically about a fixed midpoint.
The reflection arrives at time
$$t(x) = \sqrt{t_0^2 + \frac{x^2}{v^2}}, \qquad t_0 = \frac{2z}{v},$$
where $t_0$ is the zero-offset two-way time.
The *normal moveout* at offset $x$ is the difference
$$\Delta t_{\mathrm{NMO}}(x) = t(x) - t_0.$$
The *NMO correction* moves the sample recorded at time $t(x)$ to time $t_0$, so the reflection appears at the same time on all offsets.

## Remarks

The formula follows from the Pythagorean theorem: the reflected path consists of two segments of length $\sqrt{z^2 + (x/2)^2}$.
So $t(x)^2 - x^2/v^2 = t_0^2$, and the reflection is a branch of a [[hyperbola|0WN5G117YC]] in the $(x, t)$ plane.
Example: $z = 1000$ m and $v = 2000$ m/s give $t_0 = 1$ s; at $x = 2000$ m, $t = \sqrt{1 + 1} \approx 1.414$ s, so the moveout is about $0.414$ s.
Non-example: for a reflector dipping at angle $\theta$ in the plane of the profile, the time curve is $t(x)^2 = t_0^2 + x^2 \cos^2\theta / v^2$.
So the formula with the true speed $v$ fails; the curve is still a hyperbola, but with moveout velocity $v / \cos\theta$.
For horizontally layered media the formula holds approximately at small offsets, with $v$ replaced by an NMO velocity, close to the root-mean-square speed of the layers.

## Explanations

### L1 human

Normal moveout is the extra time that a reflection needs when source and receiver are apart.
For a flat layer the extra time follows a simple square-root formula.
