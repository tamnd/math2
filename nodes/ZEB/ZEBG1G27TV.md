---
tag: ZEBG1G27TV
kind: statement
role: theorem
name: Smirnov's theorem on conformal invariance of percolation
msc: [82B43, 60K35, 30C35]
uses: [BH7YPXCYDK, MP8VSZK19A, 0YYT36R4YD, AKRJ7MDNMW]
about: [BH7YPXCYDK]
sources:
  - url: https://en.wikipedia.org/wiki/Cardy_formula
---

## Statement

Let $\Omega \subset \C$ be a bounded simply connected domain whose boundary is a Jordan curve.
Let $a, b, c, d$ be four distinct points on $\partial \Omega$, in counterclockwise order.
Write $ab$ for the arc of $\partial \Omega$ from $a$ to $b$ that contains no other marked point, and $cd$ likewise.
For $\delta > 0$, consider critical site [[percolation|BH7YPXCYDK]], with $p = 1/2$, on the triangular lattice with mesh $\delta$.
Let $P_\delta(\Omega; a, b, c, d)$ be the probability that some path of open sites inside $\Omega$ joins the boundary arc $ab$ with the boundary arc $cd$.
Then:

1. The limit $P(\Omega; a, b, c, d) = \lim_{\delta \to 0} P_\delta(\Omega; a, b, c, d)$ exists.
2. The limit is conformally invariant: if $\varphi$ is a [[conformal map|0YYT36R4YD]] from $\Omega$ onto another such domain $\Omega'$, extended to the boundary, then $P(\Omega'; \varphi(a), \varphi(b), \varphi(c), \varphi(d)) = P(\Omega; a, b, c, d)$.
3. If $\Omega$ is an equilateral triangle with vertices $a, b, c$, and $d$ lies on the side from $c$ to $a$, then
$$P(\Omega; a, b, c, d) = \frac{\abs{d - c}}{\abs{a - c}}.$$

## Remarks

Stanislav Smirnov proved the theorem in 2001.
By the Riemann mapping theorem, parts 2 and 3 determine the limit for every domain, and the result is [[Cardy's formula|AKRJ7MDNMW]].

Idea of the proof: take a point $z$ inside the triangle.
Let $h_a(z)$ be the limit of the probability that an open simple path separates $z$ from the side opposite to $a$, and define $h_b$, $h_c$ in the same way.
A colour-switching argument, special to the triangular lattice at $p = 1/2$, shows that the discrete versions satisfy discrete Cauchy–Riemann relations in the limit.
So with $\tau = e^{2\pi i/3}$, the function $h_a + \tau h_b + \tau^2 h_c$ is holomorphic, and $h_a + h_b + h_c$ is constant.
The boundary values force each $h$ to be a linear function on the triangle, and evaluating $h_a$ at the point $d$ gives part 3.

Check on the extreme cases: for $d = c$ the target arc is a single point and the probability is $0$.
For $d = a$ the two arcs meet at $a$ and the probability is $1$.

The proof uses the exact symmetry of the triangular lattice; the same statement for bond percolation on $\Z^2$ is believed to be true but is not proved.

## Explanations

### L1 human

Colour the cells of a fine honeycomb black or white with fair coins, and look at a region with four marked boundary points.
The theorem says that the chance of a black crossing between two opposite boundary arcs settles to a limit as the cells shrink.
The limit does not change when the region is deformed by an angle-preserving map.
In an equilateral triangle the answer is as simple as possible: it grows linearly as the fourth point moves along a side.

### L2 human

This was the first rigorous proof of conformal invariance for a critical lattice model, which physicists had predicted from conformal field theory.
Together with later work, it shows that the boundaries of large critical clusters converge to the [[Schramm–Loewner evolution|AQ75M2JTB2]] with parameter $6$.
From this, many critical exponents of site percolation on the triangular lattice have been computed exactly.
