---
tag: M9X7Y3GZZD
kind: statement
role: theorem
name: Harish-Chandra's regularity theorem
msc: ["22E46", "22E45", "22E30"]
uses: [F2E3317P78, SZV8Y806Y7, 42ZCE14AD2, SCZ8PRVY00, VY0HXD3GC4, 0DEBXAJ5SA]
about: [F2E3317P78]
sources:
  - url: https://en.wikipedia.org/wiki/Harish-Chandra%27s_regularity_theorem
same_as:
  wikidata: Q5657833
  wikipedia: Harish-Chandra's regularity theorem
---

## Statement

Let $G$ be a connected [[real reductive Lie group|42ZCE14AD2]] with finite center and Haar measure $dg$.
Let $G'$ be the open dense subset of regular semisimple elements of $G$.
Let $\mathfrak Z$ be the center of the [[universal enveloping algebra|SCZ8PRVY00]] of the complexified Lie algebra of $G$.
It acts on distributions on $G$ as bi-invariant differential operators.
Let $\Theta$ be a distribution on $G$ such that:

1. $\Theta$ is invariant under conjugation by $G$;
2. there is a homomorphism $\chi \colon \mathfrak Z \to \C$ with $z \Theta = \chi(z) \Theta$ for all $z \in \mathfrak Z$.

Then there is a locally integrable function $F$ on $G$, real analytic on $G'$ and constant on [[conjugacy classes|0DEBXAJ5SA]], with the following property.
For every smooth compactly supported $f$ on $G$, one has $\Theta(f) = \int_G f(g) F(g) \, dg$.
In particular, the [[Harish-Chandra character|F2E3317P78]] $\Theta_\pi$ of an irreducible [[admissible representation|SZV8Y806Y7]] $\pi$ is given by such a function.

## Remarks

The character of an irreducible admissible representation satisfies the hypotheses, because $\mathfrak Z$ acts on such a representation by scalars, its infinitesimal character.
The proof first treats invariant eigendistributions on the Lie algebra, using the radial parts of invariant differential operators along Cartan subalgebras.
It then transfers the result to the group through the exponential map near each semisimple element.
On $G'$ the eigen-equations become an elliptic system, which gives analyticity there; the hard part is the local integrability across the singular set $G \setminus G'$.
For a finite-dimensional representation, $F$ is the ordinary character $g \mapsto \operatorname{tr} \pi(g)$, which is analytic on all of $G$.
For infinite-dimensional representations $F$ is usually singular on $G \setminus G'$, so analyticity on all of $G$ cannot be expected.

## Explanations

### L1 human

The character of an infinite-dimensional representation is a priori only a generalised function.
The theorem says that it is in fact an honest function, smooth away from a thin bad set, and still integrable near that set.
This makes it possible to write characters by explicit formulas, as for finite groups.

### L2 human

The theorem is the starting point of Harish-Chandra's harmonic analysis on real reductive groups.
Explicit formulas for the function $F$ on each Cartan subgroup lead to the construction of the discrete series and to the Plancherel formula.
An analogue holds for reductive groups over $p$-adic fields, also due to Harish-Chandra, where the proof is different.
