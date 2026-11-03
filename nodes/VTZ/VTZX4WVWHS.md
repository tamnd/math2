---
tag: VTZX4WVWHS
kind: object
name: Monster Lie algebra
msc: [17B67, 11F22, 20D08]
instance_of: [X3770KMKRD]
uses: [X3770KMKRD, C9VY20TAPT, FEC2XH822R, GHRPQAJY43, E0Y7Y75T6C]
sources:
  - url: https://en.wikipedia.org/wiki/Monster_Lie_algebra
same_as:
  wikidata: Q17099049
  wikipedia: Monster Lie algebra
---

## Description

Write the [[j-invariant|FEC2XH822R]] as $j(q) - 744 = \sum_{n \ge -1} c(n)\, q^n = q^{-1} + 196884\, q + 21493760\, q^2 + \cdots$, so $c(-1) = 1$, $c(0) = 0$ and $c(1) = 196884$.
The *monster Lie algebra* $\mathfrak{m}$ is a [[generalized Kac–Moody algebra|X3770KMKRD]] graded by $\Z^2$ with these properties:

1. its Cartan subalgebra is the degree $(0, 0)$ part, of dimension $2$;
2. for $(m, n) \neq (0, 0)$, the part of degree $(m, n)$ has dimension $c(mn)$;
3. it has one real simple root, of degree $(1, -1)$, and for each $n \ge 1$ it has $c(n)$ imaginary simple roots of degree $(1, n)$.

Its denominator identity is the product formula
$$j(p) - j(q) = p^{-1} \prod_{m > 0,\ n \in \Z} \left(1 - p^m q^n\right)^{c(mn)}.$$
Borcherds constructed $\mathfrak{m}$ from the moonshine module $V^\natural$, a [[vertex operator algebra|GHRPQAJY43]] on which the [[Monster group|C9VY20TAPT]] acts.
The construction also uses the vertex algebra of the even unimodular Lorentzian lattice of rank $2$ and the no-ghost theorem from string theory.
The Monster group acts on $\mathfrak{m}$ by automorphisms preserving the grading.

## Remarks

Borcherds used $\mathfrak{m}$ and its twisted denominator identities to prove the [[monstrous moonshine|E0Y7Y75T6C]] conjecture of Conway and Norton, in work published in 1992.
The twisted identities show that the McKay–Thompson series of the Monster are completely replicable.
This property, together with a check of finitely many coefficients, identifies them with the Hauptmoduln predicted by Conway and Norton.

## Explanations

### L1 human

The monster Lie algebra is an infinite-dimensional Lie algebra whose pieces have dimensions given by the coefficients of the $j$-function.
The largest sporadic simple group, the Monster, acts on it.
Its denominator identity writes $j(p) - j(q)$ as an infinite product.
This Lie algebra was the bridge that Borcherds used to connect the Monster group with modular functions and to prove the moonshine conjectures.
