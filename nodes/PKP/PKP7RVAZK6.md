---
tag: PKP7RVAZK6
kind: statement
role: theorem
name: Nielsen–Thurston classification
msc: ["57K20", "37E30"]
uses: [GYW7GYABD9, JV5NYG913V, VGJJVBZ1MQ, 0QT00PB5G2, ZZGC6BZNJ5, 0V9PMN0RBH, W890NRHGS4]
about: [JV5NYG913V, GYW7GYABD9]
sources:
  - url: https://en.wikipedia.org/wiki/Nielsen%E2%80%93Thurston_classification
same_as:
  wikidata: Q7031628
  wikipedia: Nielsen–Thurston classification
---

## Statement

Let $S$ be a closed orientable [[surface|VGJJVBZ1MQ]], and let $f \colon S \to S$ be an orientation-preserving [[homeomorphism|0QT00PB5G2]].
Then $f$ is isotopic to a homeomorphism $g$ of at least one of the following three kinds:

1. $g$ is periodic: $g^n = \id_S$ for some $n \ge 1$.
2. $g$ is reducible: $g$ maps to itself a nonempty finite union $C$ of pairwise disjoint simple closed curves on $S$. No curve of $C$ bounds a disc, and no two are isotopic.
3. $g$ is [[pseudo-Anosov|GYW7GYABD9]].

A pseudo-Anosov homeomorphism is neither periodic nor reducible, and it is not isotopic to a homeomorphism of the first two kinds.

## Remarks

The statement is about the elements of the [[mapping class group|JV5NYG913V]] of $S$: each mapping class is periodic, reducible or pseudo-Anosov, and the third kind excludes the first two.
A mapping class can be both periodic and reducible.
The theorem also holds for compact surfaces with boundary and for surfaces with finitely many punctures.

Example: on the torus, mapping classes correspond to matrices $A$ in the [[special linear group|0V9PMN0RBH]] $SL(2, \Z)$.
If $\abs{\tr A} < 2$, then $A$ has finite order and the class is periodic.
If $\abs{\tr A} = 2$, then $A$ has an integer eigenvector, and the class preserves the corresponding simple closed curve.
For $A \neq \pm I$ it is a power of a [[Dehn twist|W890NRHGS4]] up to sign and is reducible.
If $\abs{\tr A} > 2$, then $A$ has real eigenvalues $\lambda^{\pm 1}$ with $\abs{\lambda} > 1$, and the class is Anosov, a pseudo-Anosov class without singularities.

Thurston's proof considers the action of $f$ on a compactification of the [[Teichmüller space|ZZGC6BZNJ5]] of $S$ by projective measured foliations.
This compactification is a closed ball, and the proof uses the Brouwer fixed-point theorem.
A fixed point inside the ball gives a periodic class.
A fixed point on the boundary gives either a reducing curve system or the stable and unstable foliations of a pseudo-Anosov map.
Bers gave another proof by minimizing a quasiconformal dilatation over the isotopy class.

## Explanations

### L1 human

Any way of deforming a surface back onto itself can be straightened out into one of three basic types.
It may repeat itself after finitely many steps, like a rotation.
It may keep some curves in place, and so split the surface into simpler pieces.
Or it stretches and squeezes the whole surface everywhere, mixing it thoroughly.
The third type, pseudo-Anosov, is the generic and most interesting one.

### L2 human

The theorem is the surface analogue of the classification of $2 \times 2$ integer matrices into elliptic, parabolic and hyperbolic ones.
By cutting along the reducing curves and repeating, every mapping class decomposes into periodic and pseudo-Anosov pieces on subsurfaces.
This decomposition controls the dynamics: the least topological entropy in an isotopy class is the largest $\log \lambda$ of its pseudo-Anosov pieces.
By Thurston's hyperbolization theorem for fibered 3-manifolds, if $S$ has genus at least $2$, the mapping torus of $f$ has a hyperbolic structure exactly when $f$ is pseudo-Anosov.
