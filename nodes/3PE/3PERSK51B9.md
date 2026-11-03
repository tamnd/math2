---
tag: 3PERSK51B9
kind: definition
name: Method of image charges
msc: [78A30, 35J05]
defines: 2V7HXD0H8S
uses: [SAEDXNM3Y1, FC64B1A65B, CC7NZRPMBB, 2F6AJ1DM11]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_image_charges
---

## Definition

Let $\Omega \subseteq \R^3$ be an open set, and let point charges $q_1, \dots, q_n$ lie at points $x_1, \dots, x_n \in \Omega$.
The problem is to find a potential $\varphi$ that solves [[Poisson's equation|FC64B1A65B]] in $\Omega$ with these charges and has $\varphi = 0$ on $\partial \Omega$.
When $\Omega$ is unbounded, $\varphi(x) \to 0$ as $\abs{x} \to \infty$ is also required.
The *method of image charges* looks for *image charges* $q'_1, \dots, q'_m$ at points $x'_1, \dots, x'_m$ outside $\overline{\Omega}$.
They must make the [[electric potential|SAEDXNM3Y1]] of all real and image charges together vanish on $\partial \Omega$.
The restriction of that potential to $\Omega$ is then the solution, by the [[uniqueness theorem|CC7NZRPMBB]].

## Remarks

Example (plane): let $\Omega = \set{x_3 > 0}$ and let a charge $q$ sit at $a = (0, 0, d)$ with $d > 0$.
The image is the charge $-q$ at $a' = (0, 0, -d)$.
Each point $x$ with $x_3 = 0$ is at the same distance from $a$ and $a'$, so the two potentials cancel there.
Example (sphere): let $\Omega$ be the exterior of the ball of radius $R$ centred at $0$, and let a charge $q$ sit at distance $d > R$ from $0$.
The image is the charge $-qR/d$ at the point on the same ray at distance $R^2/d$ from $0$.
Non-example: for the plane, the charge $+q$ at $a'$ is not an image charge, since the potential on $x_3 = 0$ is then twice that of $q$, not zero.
With $q = 1$ and $\varepsilon_0$ removed, the potential of the charge and its images is the [[Green's function|2F6AJ1DM11]] of $\Omega$ for the Dirichlet problem, up to a constant factor.
