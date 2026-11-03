---
tag: XSVHFDJHRJ
kind: statement
role: proposition
name: Jeans equations
msc: [85A05, 35Q85]
uses: [SJH7M2VCTE, 01XAHPADBA, RW0JK9VDZE, 4V8BT1ZD00]
about: [SJH7M2VCTE, 4V8BT1ZD00]
sources:
  - url: https://en.wikipedia.org/wiki/Jeans_equations
same_as:
  wikidata: Q17050625
  wikipedia: Jeans equations
---

## Statement

Let $\Phi(t, x)$ be a smooth potential.
Let $f(t, x, v) \ge 0$ be a smooth solution of the collisionless Boltzmann equation, the [[Vlasov equation|SJH7M2VCTE]]
$$\partial_t f + v_i \, \partial_{x_i} f - \partial_{x_i} \Phi \, \partial_{v_i} f = 0$$
with summation over repeated indices $i, j \in \set{1, 2, 3}$.
Assume that $f$ and $\abs{v}^2 f$ tend to $0$ fast enough as $\abs{v} \to \infty$.
Then the [[moments|01XAHPADBA]] below exist, and the boundary terms of integration by parts in $v$ vanish.
Let $\nu = \int f \, dv$ be the density, $\bar v_i = \nu^{-1} \int v_i f \, dv$ the mean velocity and $\sigma_{ij}^2 = \nu^{-1} \int (v_i - \bar v_i)(v_j - \bar v_j) f \, dv$ the velocity dispersion tensor.
Then
$$\partial_t \nu + \partial_{x_i} (\nu \bar v_i) = 0,$$
$$\nu \, \partial_t \bar v_j + \nu \bar v_i \, \partial_{x_i} \bar v_j = -\nu \, \partial_{x_j} \Phi - \partial_{x_i} \left( \nu \sigma_{ij}^2 \right), \qquad j = 1, 2, 3.$$

## Remarks

The first equation is the integral of the collisionless Boltzmann equation over all $v$; the term with $\partial_{v_i} f$ integrates to $0$.
The second comes from multiplying by $v_j$ and integrating, which gives $\partial_t (\nu \bar v_j) + \partial_{x_i} (\nu \overline{v_i v_j}) + \nu \partial_{x_j} \Phi = 0$, and then subtracting $\bar v_j$ times the first equation.
They have the form of the [[Euler equations|RW0JK9VDZE]] of a fluid, with the anisotropic stress $\nu \sigma_{ij}^2$ in place of the pressure.
They do not close: the dispersions are new unknowns, and extra assumptions, such as isotropy, are needed to solve them.

For a steady, spherical, non-rotating system with radial dispersion $\sigma_r^2$ and anisotropy $\beta = 1 - (\sigma_\theta^2 + \sigma_\phi^2)/(2\sigma_r^2)$, the equations reduce to
$$\frac{d(\nu \sigma_r^2)}{dr} + \frac{2 \beta}{r} \nu \sigma_r^2 = -\nu \frac{d\Phi}{dr}.$$
With $d\Phi/dr = G M(r)/r^2$, this gives the mass $M(r)$ inside radius $r$ from measured densities and dispersions of stars.
This is how the masses of galaxies and of their dark matter are estimated.

## Explanations

### L1 human

The Jeans equations are the equations of fluid flow, written for a swarm of stars instead of a gas.
They link the density of stars, their mean motion and the spread of their velocities with the gravitational pull.
The faster the stars move at random in a region, the stronger the gravity must be to keep them there.
Astronomers use this to weigh galaxies from the motions of their stars.

### L2 human

The equations are the first two velocity moments of the [[collisionless Boltzmann equation|SJH7M2VCTE]] of [[stellar dynamics|4V8BT1ZD00]].
They are easier to compare with observations than the full equation, because they involve only averaged quantities.
The price is that they are not closed: each moment equation brings in the next moment.
Spherical Jeans models, together with an assumption on the anisotropy $\beta$, are standard tools to infer dark matter profiles, and the mass–anisotropy degeneracy is their main limitation.
