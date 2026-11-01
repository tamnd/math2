---
tag: 5EJ7SW1RCV
kind: statement
role: theorem
name: Uniformization theorem
msc: [30F10, 30F35]
uses: [5K0N8QMV6Q, 8AJEMCZ29B, 0CDMXGPSES, 0CTE7A31XQ, 8G5ABXRK85]
about: [5K0N8QMV6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Uniformization_theorem
same_as:
  wikidata: Q2109761
  wikipedia: Uniformization theorem
---

## Statement

Let $X$ be a simply connected [[Riemann surface|5K0N8QMV6Q]], that is, its fundamental group is trivial.
Then $X$ is [[biholomorphic|8AJEMCZ29B]] to exactly one of the following three Riemann surfaces:

1. the [[Riemann sphere|0CDMXGPSES]] $\hat\C$;
2. the [[complex plane|0CTE7A31XQ]] $\C$;
3. the open [[unit disc|8G5ABXRK85]] $\mathbb{D}$.

## Remarks

The three surfaces are pairwise not biholomorphic: $\hat\C$ is compact and the others are not, and a holomorphic map $\C \to \mathbb{D}$ is constant by Liouville's theorem.
Applied to the universal cover, the theorem shows that every Riemann surface $X$ is biholomorphic to a quotient $\tilde X / \Gamma$.
Here $\tilde X$ is one of the three surfaces and $\Gamma$ is a group of automorphisms of $\tilde X$ acting freely and properly discontinuously.
Only $\hat\C$ itself is covered by $\hat\C$, and only $\C$, $\C \setminus \set{0}$ and the tori $\C / \Lambda$ are covered by $\C$.
Every other Riemann surface is a quotient $\mathbb{D} / \Gamma$ with $\Gamma$ a Fuchsian group.
For simply connected open subsets of $\C$ the theorem contains the [[Riemann mapping theorem|02WHMEG5ZR]].

The theorem was proved in 1907, independently by Koebe and by Poincaré.
One proof constructs a harmonic Green's function or a harmonic dipole function on $X$ and uses it to build a holomorphic injection into $\hat\C$.

Example: $\C \setminus \set{0}$ is not simply connected; its universal cover is $\exp \colon \C \to \C \setminus \set{0}$, and $\C \setminus \set{0} \cong \C / 2\pi i \Z$.

## Explanations

### L1 human

There are infinitely many Riemann surfaces, but only three that have no loops that cannot be shrunk: the sphere, the plane and the disc.
Every other Riemann surface is obtained from one of these three by rolling it up, that is, by identifying points that differ by a group of symmetries.
So the study of all Riemann surfaces reduces to the study of these three and their symmetry groups.

### L2 human

The theorem gives every Riemann surface a metric of constant curvature $+1$, $0$ or $-1$ compatible with its complex structure.
Compact surfaces of genus $0$ are spherical, genus $1$ flat, and genus at least $2$ hyperbolic, a fact that links complex analysis to hyperbolic geometry.
It is the starting point of Teichmüller theory, because a complex structure on a surface of genus $g \ge 2$ becomes a Fuchsian group up to conjugation.
