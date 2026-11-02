---
tag: PXPC6E40ZW
kind: statement
role: theorem
name: Dahlberg's theorem on harmonic measure
msc: [31B25, 31B05, 35J25]
uses: [1GNKQ7NBAG, CFD7BPM51W, Q1TGZK8RN6, P0P21KDV6E, SASP14MA1Z, PYJ7T889KC, X9V1E3V145]
about: [CFD7BPM51W, 1GNKQ7NBAG]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded [[Lipschitz domain|1GNKQ7NBAG]] that is connected.
Let $\sigma$ be the surface measure on $\partial\Omega$, that is, the $(n-1)$-dimensional [[Hausdorff measure|Q1TGZK8RN6]] restricted to $\partial\Omega$.
Let $x \in \Omega$ and let $\omega^x$ be the [[harmonic measure|CFD7BPM51W]] of $\Omega$ at $x$.
Then $\omega^x$ and $\sigma$ are mutually [[absolutely continuous|P0P21KDV6E]], and the density $k^x = d\omega^x / d\sigma$ belongs to [[Lp space|SASP14MA1Z]] $L^2(\partial\Omega, \sigma)$.

## Remarks

More precisely, $k^x$ satisfies a reverse Hölder inequality with exponent $2$ on surface balls, and by Gehring's lemma it lies in $L^{2 + \varepsilon}(\sigma)$ for some $\varepsilon > 0$ depending on $\Omega$.
As a consequence, the Dirichlet problem on $\Omega$ is solvable for boundary data in $L^p(\sigma)$ with $p \ge 2$, with nontangential convergence to the data and a nontangential maximal function estimate.
Idea of the proof: the [[boundary Harnack principle|PYJ7T889KC]] compares $\omega^x$ of a surface ball with the Green function at a nearby interior point.
One proof then uses a Rellich-type integral identity for harmonic functions on Lipschitz domains to get the $L^2$ bound.
Example: for a ball, $k^x$ is the Poisson kernel, which is bounded, so $k^x \in L^p$ for every $p$.
The exponent $2$ cannot be replaced by a fixed larger one for all Lipschitz domains.
In the plane, at the vertex of a sector of opening $\theta \in (\pi, 2\pi)$, the density behaves like $t^{\pi/\theta - 1}$ at distance $t$ from the vertex.
It lies in $L^p$ near the vertex only for $p < 1 / (1 - \pi/\theta)$, and this bound tends to $2$ as $\theta \to 2\pi$.

## Explanations

### L1 human

Harmonic measure tells where a random path started at $x$ first hits the boundary.
On a domain with corners but no cusps, this hitting distribution has a density with respect to surface area, and the density is square-integrable.
So a set of zero area is never hit, and a set that is hit with probability zero has zero area.

### L2 human

Dahlberg's theorem made Lipschitz domains the natural setting for harmonic analysis on rough domains.
It is the basis of the $L^p$ theory of the Dirichlet and Neumann problems and of layer potentials on Lipschitz boundaries.
It shows that harmonic measure is an $A_\infty$ weight with respect to surface measure, a property later studied on much more general domains.
In the plane, for a Jordan domain with rectifiable boundary, the [[F. and M. Riesz theorem|X9V1E3V145]] already gives mutual absolute continuity with arc length.
