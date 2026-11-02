---
tag: MB52NDA6WN
kind: statement
role: theorem
name: Resolution of singularities
msc: ["14E15", 14B05, 32S45]
uses: [HV6YBS0YDH, D86X15A8WS, 9537RKBZPP, KA5890R9YM, C4KGYAFPN7, M2FAMD9HZN]
about: [D86X15A8WS]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_of_singularities
same_as:
  wikidata: Q10942247
  wikipedia: Resolution of singularities
---

## Statement

Let $k$ be a field of characteristic $0$ and let $X$ be an integral [[algebraic variety|HV6YBS0YDH]] over $k$.
Then there is a nonsingular variety $\tilde{X}$ over $k$ with a [[proper|9537RKBZPP]] [[birational|KA5890R9YM]] morphism $\pi \colon \tilde{X} \to X$.
Moreover $\pi$ can be chosen to be an isomorphism over the set of nonsingular points of $X$.

## Remarks

This is Hironaka's theorem.
The morphism $\pi$ can be chosen as a composition of [[blow-ups|C4KGYAFPN7]] along nonsingular centres that lie over the [[singular points|D86X15A8WS]] of $X$.
The proof is an induction on dimension: one restricts to a hypersurface of maximal contact and uses an invariant of the singularity that drops after each blow-up.
For curves, in any characteristic, the [[normalization|M2FAMD9HZN]] is a resolution.
Example: the cusp $y^2 = x^3$ is resolved by $\mathbb{A}^1 \to X$, $t \mapsto (t^2, t^3)$, which is bijective and an isomorphism away from $t = 0$.
In characteristic $p > 0$ the statement is known in dimension at most $3$, and it is open in general.

## Explanations

### L1 human

A singular variety has points where it is not smooth, such as a cusp or a place where it crosses itself.
The theorem says that one can always replace it by a smooth variety that differs from it only over the bad points.
The smooth variety maps onto the old one and keeps all its good points unchanged.

### L2 human

Resolution lets one prove results for smooth varieties and then transfer them to singular ones.
It is used to define invariants of singularities, such as rational singularities, and to compactify smooth varieties by a divisor with simple normal crossings.
Resolution by blow-ups is also a basic step of the minimal model program, which starts from a smooth model of a birational class.
