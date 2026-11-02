---
tag: 9NPY7BF6ZJ
kind: definition
name: Natural boundary condition
msc: [49K05, 49K10, 35A15]
defines: QTRPNFDFJ8
uses: [JRQZ803Q5Y, G7T008BEWY, 5B8NFYB2XQ, PS0VV149ET, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Definition

Let $a < b$ and $A \in \R$, and let $L \colon [a, b] \times \R \times \R \to \R$, written $L(x, z, p)$, be of class $C^1$, with [[partial derivative|09EGC6F8PT]] $L_p$ in $p$.
Consider the [[integral functional|JRQZ803Q5Y]] $J(y) = \int_a^b L(x, y, y') \, dx$ on the class of [[admissible functions|G7T008BEWY]] $y \in C^1([a, b])$ with $y(a) = A$ and no condition on $y(b)$.
The *natural boundary condition* at the free end $b$ is
$$L_p\big(b, y(b), y'(b)\big) = 0.$$
The natural boundary condition at a free end $a$ is defined in the same way, with $a$ in place of $b$.

## Remarks

Let $L$ be of class $C^2$ and let $y \in C^2([a, b])$ minimise $J$ on this class.
For $\eta \in C^1([a, b])$ with $\eta(a) = 0$, integration by parts in the [[first variation|5B8NFYB2XQ]] gives
$$0 = \delta J(y; \eta) = \int_a^b \Big( L_z - \frac{d}{dx} L_p \Big) \eta \, dx + L_p\big(b, y(b), y'(b)\big) \, \eta(b).$$
Variations with $\eta(b) = 0$ give the [[Euler–Lagrange equation|PS0VV149ET]], so the integral vanishes; a variation with $\eta(b) = 1$ then gives the natural boundary condition.

Example: let $J(y) = \int_0^1 \big( \frac{1}{2} y'^2 - y \big) \, dx$ with $y(0) = 0$ and $y(1)$ free.
The Euler–Lagrange equation is $y'' = -1$ and the natural boundary condition is $y'(1) = 0$.
The function $y(x) = x - x^2/2$ satisfies both: $y'' = -1$, $y(0) = 0$ and $y'(1) = 1 - 1 = 0$.
Non-example: $y(x) = x$ has $y(0) = 0$, but $L_p = y' = 1$ at $x = 1$, so it fails the natural boundary condition.

In several variables, for $J(u) = \int_\Omega \big( \frac{1}{2} \abs{\nabla u}^2 - f u \big) \, dx$ with no condition on $\partial \Omega$, the natural boundary condition is $\partial u / \partial \nu = 0$, where $\nu$ is the outer normal.
