---
tag: D2KC8NEAPS
kind: example
name: Liénard equation
msc: [34C15, 34C07]
instance_of: [0NT64JV96A]
uses: [0FP31SX5EA, 0673D85QKZ, 0YG0ZJPTWG]
sources:
  - url: https://en.wikipedia.org/wiki/Li%C3%A9nard_equation
---

## Example

Let $f \colon \R \to \R$ be a continuous [[even function|0FP31SX5EA]] and let $g \colon \R \to \R$ be a continuous odd function.
The Liénard equation is the second-order [[ordinary differential equation|0NT64JV96A]]
$$x'' + f(x)\, x' + g(x) = 0.$$
Let $F(x) = \int_0^x f(s)\, ds$.
With $y = x' + F(x)$, the equation becomes the planar [[autonomous system|0673D85QKZ]]
$$x' = y - F(x), \qquad y' = -g(x).$$
Check: from $x' = y - F(x)$ follows $x'' = y' - f(x) x' = -g(x) - f(x) x'$, which is the Liénard equation.

## Remarks

The term $f(x) x'$ is a damping that depends on the position.
Where $f(x) < 0$ it pumps energy into the motion, and where $f(x) > 0$ it removes energy.
The term $g(x)$ is a restoring force.
For $f = 0$ and $g(x) = x$, the equation is the [[harmonic oscillator|0YG0ZJPTWG]].
For $f(x) = -\mu (1 - x^2)$ with $\mu > 0$ and $g(x) = x$, it is the van der Pol equation $x'' - \mu (1 - x^2) x' + x = 0$.
Liénard's theorem gives conditions on $f$ and $g$ under which the system has exactly one limit cycle.

## Explanations

### L1 human

The Liénard equation describes a particle on a line pulled back toward the origin by the force $-g(x)$, with a friction coefficient $f(x)$ that depends on where the particle is.
If the friction is negative near the origin and positive far away, small motions grow and large motions shrink.
The motion then settles on one oscillation of a definite size.
