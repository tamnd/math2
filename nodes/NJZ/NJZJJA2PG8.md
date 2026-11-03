---
tag: NJZJJA2PG8
kind: definition
name: Thin airfoil theory
msc: [76G25, 76B10]
defines: EYCZ9SGBND
uses: [84K7TEWZ2Z, BTHH4Y71QR, DSWYGZCGM5, TZM7XNR4V0, W6Z6CWRE25, 0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Airfoil
    locator: Thin airfoil theory
---

## Definition

Consider a steady, two-dimensional, incompressible, inviscid and irrotational [[flow|84K7TEWZ2Z]] of speed $V$ past an airfoil of chord $c$ placed along $0 \le x \le c$.
Let $z = z_c(x)$ be its camber line and $\alpha$ its angle of attack, and assume that $\alpha$, $z_c / c$, $z_c'$ and the relative thickness are small.
*Thin airfoil theory* is the linearised model of this flow in which:

1. the airfoil is replaced by a vortex sheet on the segment $0 \le x \le c$, with strength $\gamma(x)$ per unit length;
2. the flow is tangent to the camber line, which to first order reads
$$\frac{1}{2\pi}\, \mathrm{PV}\!\int_0^c \frac{\gamma(\xi)}{x - \xi}\, d\xi = V\bigl(\alpha - z_c'(x)\bigr), \quad 0 < x < c,$$
where $\mathrm{PV}$ is the [[Cauchy principal value|0SYR10HD4R]];
3. the [[Kutta condition|DSWYGZCGM5]] $\gamma(c) = 0$ holds at the trailing edge.

The lift per unit span is $L' = \rho V \Gamma$, with $\Gamma = \int_0^c \gamma(\xi)\, d\xi$ the [[circulation|BTHH4Y71QR]] and $\rho$ the density, as in the [[Kutta–Joukowski theorem|TZM7XNR4V0]].

## Remarks

Example: for a flat plate, $z_c = 0$.
With $x = \frac{c}{2}(1 - \cos\theta)$, the function $\gamma(\theta) = 2\alpha V \frac{1 + \cos\theta}{\sin\theta}$ solves condition 2 and vanishes at $\theta = \pi$, which is $x = c$.
Then $\Gamma = \pi \alpha c V$, and the lift coefficient is $c_l = L' / (\frac{1}{2}\rho V^2 c) = 2\pi\alpha$.
For a cambered section the result is $c_l = 2\pi(\alpha - \alpha_0)$, where the zero-lift angle $\alpha_0$ depends only on the camber line.
Non-example: a thick section at a large angle of attack does not fit the model, because the small-perturbation assumptions fail, and real flow separates there.
After scaling the chord to $[-1, 1]$, condition 2 is the [[airfoil equation|W6Z6CWRE25]].
