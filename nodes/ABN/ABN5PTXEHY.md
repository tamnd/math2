---
tag: ABN5PTXEHY
kind: statement
role: theorem
name: Cantor's isomorphism theorem
msc: [06A05, 03C15]
uses: [C9GDH7264N, JB9HJ9CPEN, 0ZG61TFBES, 0Y74KN99A5]
about: [K4D3S1MBZH, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_isomorphism_theorem
same_as:
  wikidata: Q3527028
  wikipedia: Cantor's isomorphism theorem
---

## Statement

Let $(A, <)$ and $(B, <)$ be [[strict total orders|C9GDH7264N]] with these properties.

1. $A$ and $B$ are nonempty and [[countable|0ZG61TFBES]].
2. Both orders are [[dense|JB9HJ9CPEN]].
3. Neither $A$ nor $B$ has a least element or a greatest element.

Then there is an [[order isomorphism|0Y74KN99A5]] from $A$ onto $B$.
In particular, each such order is order isomorphic to $(\Q, <)$.

## Remarks

A standard proof is the back-and-forth method.
List $A = \set{a_0, a_1, \dots}$ and $B = \set{b_0, b_1, \dots}$, and build finite order-preserving partial maps step by step.
At even steps, the first element of $A$ not yet in the domain gets an image.
At odd steps, the first element of $B$ not yet in the range gets a preimage.
Density and the lack of endpoints guarantee that a suitable partner exists at each step.
The union of the finite maps is the isomorphism.
For example, the dyadic rationals $\set{m / 2^k : m \in \Z, k \in \N}$ and the rationals in the open interval $(0, 1)$ are both order isomorphic to $\Q$.
Countability is needed: $\R$ satisfies the other hypotheses but is not order isomorphic to $\Q$, because $\R$ is uncountable.
The condition on endpoints is needed: $\Q \cap [0, 1]$ has a least element and $\Q$ has none.
Density is needed: $\Z$ is countable without endpoints but not dense.
In model theory, the theorem says that the theory of dense linear orders without endpoints is $\aleph_0$-categorical.

## Explanations

### L1 human

The rationals have a very particular shape: countably many points, no ends, and always something between two points.
The theorem says this shape is unique.
Any other countable line with no ends and no gaps of the "next element" kind can be matched point by point with the rationals, keeping the order.
So the rationals between $0$ and $1$ and all the rationals have the same order, even though one sits inside the other.

### L2 human

The theorem is the basic example of the back-and-forth method, which is used widely in model theory.
It shows that the [[order type|28PE4GRFD7]] $\eta$ of $\Q$ is the unique countable dense order type without endpoints.
Every countable total order embeds into $\Q$; the proof is the "forth" half of the same argument.
The analogous question for uncountable orders is much harder; [[Suslin's problem|D1T39KHPDN]] is a famous case.
