---
tag: RDFRDH3E45
kind: definition
name: Gelfand–Levitan–Marchenko equation
msc: [34A55, 34L25, 45B05]
defines: X35RWR285S
uses: [R3SG1SN7JQ, 6GY3X4Y8X5]
sources:
  - url: https://en.wikipedia.org/wiki/Marchenko_equation
---

## Definition

Let $u \colon \R \to \R$ be a potential with $\int_{\R} (1 + \abs{x}) \abs{u(x)} \, dx < \infty$, and consider $-\psi'' + u \psi = k^2 \psi$ on $\R$.
Let its scattering data be the reflection coefficient $r(k)$ for $k \in \R$, the bound state energies $-\kappa_1^2, \ldots, -\kappa_N^2$ with $\kappa_j > 0$, and the norming constants $\beta_1, \ldots, \beta_N > 0$.
Put
$$F(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} r(k) \, e^{ikx} \, dk + \sum_{j=1}^{N} \beta_j e^{-\kappa_j x}.$$
The *Gelfand–Levitan–Marchenko equation* is the equation for an unknown function $K(x, y)$, $y \ge x$:
$$K(x, y) + F(x + y) + \int_x^\infty K(x, z) \, F(z + y) \, dz = 0, \quad y > x.$$
For each fixed $x$ it is a linear integral equation of the second kind on $(x, \infty)$, and the potential is recovered as $u(x) = -2 \frac{d}{dx} K(x, x)$.

## Remarks

Example: the reflectionless data $r = 0$, $N = 1$, give $F(x) = \beta e^{-\kappa x}$.
Try $K(x, y) = L(x) e^{-\kappa y}$; the equation becomes $L(x) + \beta e^{-\kappa x} + L(x) \frac{\beta}{2\kappa} e^{-2\kappa x} = 0$.
With $w(x) = \frac{\beta}{2\kappa} e^{-2\kappa x}$ this gives $K(x, x) = -\frac{2\kappa w}{1 + w}$, and since $w' = -2\kappa w$,
$$u(x) = -2 \frac{d}{dx} K(x, x) = -\frac{8 \kappa^2 w}{(1 + w)^2} = -2\kappa^2 \operatorname{sech}^2\!\big(\kappa (x - x_0)\big),$$
where $e^{2\kappa x_0} = \frac{\beta}{2\kappa}$.
This potential has the single bound state energy $-\kappa^2$ and reflects nothing.

Non-example: the equation $K(x, y) + F(x - y) + \int_x^\infty K(x, z) F(z - y) \, dz = 0$ has kernels $F(x - y)$ and $F(z - y)$ that depend on differences; in the Gelfand–Levitan–Marchenko equation they must depend on the sums $x + y$ and $z + y$.

Several conventions are in use, with other signs and with data on the left instead of the right.
The Gelfand–Levitan equation of [[Gelfand–Levitan theory|R4MRNP9EQT]] is a related equation, with an integral over $(0, x)$, that recovers a potential on a half-line from its spectral function.
