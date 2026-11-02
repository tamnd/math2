---
tag: X4DZR72B6N
kind: statement
role: corollary
name: Calabi–Weil rigidity
msc: ["53C24", "22E40", "53C35"]
uses: [V2HTMG4KT1, BTYF5Y5PFY, 0JYTG5K9Y4]
about: [BTYF5Y5PFY]
sources:
  - url: https://en.wikipedia.org/wiki/Local_rigidity
    locator: History
---

## Statement

Let $n \ge 3$ and let $G = \mathrm{SO}_0(n, 1)$ be the group of orientation-preserving isometries of hyperbolic space $\mathbb{H}^n$.
Let $\Gamma \subset G$ be a discrete torsion-free subgroup such that the hyperbolic manifold $M = \Gamma \backslash \mathbb{H}^n$ is compact.
Then the inclusion $\Gamma \to G$ is locally rigid.
That is, let $\rho \colon \Gamma \to G$ be a [[homomorphism|0JYTG5K9Y4]] close enough to the inclusion on a finite generating set of $\Gamma$.
Then $\rho$ is conjugate to the inclusion by an element of $G$.
Equivalently, the hyperbolic structure of $M$ admits no nontrivial small deformations.

## Remarks

Calabi proved this for compact hyperbolic manifolds, and Weil extended it to all uniform lattices in semisimple groups.
It follows from [[Weil's local rigidity theorem|V2HTMG4KT1]], since $\Gamma$ is a uniform [[lattice|BTYF5Y5PFY]] in $G$, which for $n \ge 3$ is simple, has trivial center and is not locally isomorphic to $\mathrm{SL}_2(\R)$.
The hypothesis $n \ge 3$ is necessary: for $n = 2$ the hyperbolic structures on a closed surface of genus $g \ge 2$ form a [[Teichmüller space|ZZGC6BZNJ5]] of real dimension $6g - 6$.
For $n = 3$ compactness is also needed: hyperbolic structures on cusped $3$-manifolds deform to incomplete structures, which give hyperbolic Dehn filling.

## Explanations

### L1 human

A closed surface of genus two can carry many different hyperbolic shapes, which can be changed continuously.
In dimension three and higher this freedom disappears.
A closed hyperbolic manifold cannot be bent slightly into a different hyperbolic manifold.
Its shape is locally fixed by its topology.

### L2 human

This theorem is the local version of [[Mostow rigidity|4BEWKR0EG7]], which states that the hyperbolic structure is determined by the fundamental group globally.
In the language of representations, the point of $\Hom(\Gamma, G)/G$ defined by $M$ is isolated.
The proof goes through the vanishing of the cohomology group $H^1(\Gamma, \mathfrak{g})$ with coefficients in the Lie algebra of $G$.
