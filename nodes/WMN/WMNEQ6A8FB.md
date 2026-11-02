---
tag: WMNEQ6A8FB
kind: definition
name: Regular category
msc: ["18E08"]
defines: 2SM3JRJXA4
uses: [PYSBNWCHCF, E70DQGM8X5, DVSTWGVCSZ, Q05K04QJ71, RVXDSY04KG]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_category
---

## Definition

A morphism is a *regular epimorphism* if it is the [[coequalizer|DVSTWGVCSZ]] of some pair of morphisms.
A category $\mathcal{C}$ is *regular* if these three conditions hold.

1. $\mathcal{C}$ is [[finitely complete|PYSBNWCHCF]].
2. For every morphism $f$ of $\mathcal{C}$, the [[kernel pair|E70DQGM8X5]] of $f$ has a coequalizer.
3. Regular epimorphisms are stable under [[pullback|Q05K04QJ71]]: the pullback of a regular epimorphism $e \colon A \to B$ along any $g \colon C \to B$ is a regular epimorphism.

## Remarks

A regular epimorphism is an [[epimorphism|RVXDSY04KG]].
In a regular category every morphism $f$ factors as $f = m \circ e$ with $e$ a regular epimorphism and $m$ a monomorphism.
Here $e$ is the coequalizer of the kernel pair of $f$, and $m$ is called the image of $f$.

Example: the category of sets is regular.
It has all finite limits, and the kernel pair of $f \colon A \to B$ is the relation $\set{(a, a') : f(a) = f(a')}$, whose coequalizer is the quotient of $A$ by it.
Regular epimorphisms are the surjections, and a pullback of a surjection is a surjection.

Non-example: the category of topological spaces satisfies clauses 1 and 2 but not clause 3.
Its regular epimorphisms are the quotient maps, and a pullback of a quotient map need not be a quotient map.
