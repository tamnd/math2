---
tag: B30ACDNS76
kind: statement
role: theorem
name: Uhlenbeck's removable singularity theorem
msc: ["58E15", 53C07, 81T13]
uses: [8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, JJWETW5AT8, 707DEWCCFX]
about: [JJWETW5AT8]
sources:
  - url: https://en.wikipedia.org/wiki/Gauge_theory_(mathematics)
---

## Statement

Let $B \subseteq \R^4$ be the open unit ball with a smooth Riemannian metric, and let $G$ be a compact Lie group.
Let $P \to B \setminus \set{0}$ be a [[principal $G$-bundle|8E37E74XVP]].
Let $A$ be a smooth [[connection|NJ21PN5ZGJ]] on $P$ that satisfies the [[Yang–Mills equations|JJWETW5AT8]] $d_A^* F_A = 0$ on $B \setminus \set{0}$.
Assume that $A$ has finite energy:
$$\int_{B \setminus \set{0}} \abs{F_A}^2 < \infty,$$
where $F_A$ is the [[curvature|ZAJFW1S078]] of $A$.
Then $P$ extends to a principal $G$-bundle $\bar{P}$ over $B$.
There is a [[gauge transformation|707DEWCCFX]] $u$ on $B \setminus \set{0}$ such that $u^* A$ extends to a smooth Yang–Mills connection on $\bar{P}$.

## Remarks

The proof uses the conformal invariance of the energy in dimension $4$.
On dyadic annuli around $0$ the energy tends to $0$, so Uhlenbeck's gauge fixing gives good gauges on each annulus.
A decay estimate shows that $\abs{F_A}$ is in fact bounded near $0$.
Then a Coulomb gauge on the whole ball and elliptic regularity give the smooth extension.
The finite energy hypothesis cannot be dropped.
A connection that extends smoothly over $0$ has bounded curvature near $0$, and the energy is gauge invariant.
So a Yang–Mills connection with infinite energy on every punctured ball around $0$ never extends over $0$ in any gauge.
Example: a finite-energy anti-self-dual connection on $\R^4$ pulls back, via stereographic projection, to an instanton on $S^4$ minus a point.
The theorem extends it over that point, so it comes from a bundle over $S^4$.
Its energy is a fixed constant times the absolute value of the second Chern number of that bundle.

## Explanations

### L1 human

A Yang–Mills field defined everywhere except at one point of four-dimensional space might be badly singular there.
The theorem says that if the total energy of the field is finite, then the singularity is only apparent.
After a change of gauge, the field extends smoothly across the point.

### L2 human

The theorem is the reason why finite-energy instantons on $\R^4$ correspond to instantons on the sphere $S^4$, and why their energy is quantised.
It is also the second ingredient, next to the Uhlenbeck compactness theorem, in the description of limits of sequences of instantons.
The limit connection away from the bubble points has finite energy, so it extends over those points to a connection on a new bundle.
