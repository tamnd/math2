---
tag: C82AXZK2BS
kind: statement
role: theorem
name: Hochster's theorem on spectral spaces
msc: [14A05, 13A15, 54F65]
uses: [FB45BHHA2J, 8SQK7RTB63, 0CQHFPGJ45, 0TVJZYB6SH, 0ZCK8DQYN1]
about: [FB45BHHA2J]
sources:
  - url: https://en.wikipedia.org/wiki/Spectral_space
---

## Statement

A [[topological space|0CQHFPGJ45]] $X$ is *spectral* if:

1. $X$ is quasi-compact;
2. the quasi-compact open subsets of $X$ form a basis of the topology and are closed under finite intersections;
3. $X$ is sober: every irreducible [[closed subset|0ZCK8DQYN1]] $Z$ of $X$ has exactly one point $z$ whose closure is $Z$.

Here a closed set is irreducible if it is nonempty and not the union of two closed proper subsets.

Hochster's theorem: a topological space $X$ is spectral if and only if it is homeomorphic to $\operatorname{Spec} R$ for some [[commutative ring|0310REJJY8]] $R$.
Here $\operatorname{Spec} R$ is the [[spectrum|FB45BHHA2J]] with the [[Zariski topology|8SQK7RTB63]].

## Remarks

One direction is a direct check.
$\operatorname{Spec} R$ is [[quasi-compact|J4YW23MD6N]], the [[basic open sets|N6JX9BCKQP]] $D(f) \cong \operatorname{Spec} R_f$ are quasi-compact, and a quasi-compact open set is a finite union of them, so finite intersections stay quasi-compact by $D(f) \cap D(g) = D(fg)$.
An irreducible closed set is $V(\mathfrak p)$ for a unique prime $\mathfrak p$, which is its generic point.
The other direction, building a ring from a spectral space, is the hard part of the theorem.

Example: a finite $T_0$ space is spectral, so it is the spectrum of some ring.
Non-example: the real line with its usual topology is not spectral; it is not quasi-compact.
A Hausdorff spectral space is a Stone space, and every Stone space is the spectrum of a Boolean ring.
An infinite Stone space is never the spectrum of a Noetherian ring.

## Explanations

### L1 human

The theorem says exactly which spaces arise as spaces of prime ideals.
There are three conditions, all of them about finiteness and about "generic points".
Any space with these properties, however strange, comes from some ring.

### L2 human

The conditions make the class of spectra purely topological, with no reference to rings.
To show that a space is homeomorphic to a spectrum, one may check the three conditions instead of finding a ring.
Spectral spaces also appear in logic and lattice theory, as the spaces dual to bounded distributive lattices.
