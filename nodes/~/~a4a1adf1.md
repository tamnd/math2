---
tag: ~a4a1adf1
kind: example
name: The integer order has the small index property
aliases: [integer-order-small-index-property]
msc: ["03C15", "20B27"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [~22edb57f]
uses: [~22edb57f, ~e359ec59, FVGB8ZP67B, 4K9RYSNPG3]
sources:
  - book: isbn:9780521587136
---

## Example

Let $G = \operatorname{Aut}(\Z, <)$.
We show that $(\Z, <)$ has the [[small index property|~22edb57f]].

1. The automorphisms of $(\Z, <)$ are the translations $x \mapsto x + k$; see [[this example|~e359ec59]].
2. A translation fixing $0$ has $k = 0$, so the stabilizer $G_0$ is trivial.
3. $G_0$ is open in the [[topology of pointwise convergence|FVGB8ZP67B]], so $G$ is discrete.
4. Every subgroup of a discrete group is [[open|4K9RYSNPG3]], so SIP holds.

## Remarks

As an abstract group, $G \cong \Z$, and its subgroups are $n\Z$, with index $n$ or, for $n = 0$, countable index.
So SIP can hold for a structure that is not ultrahomogeneous.
SIP is about the automorphism group, not about how symmetric the structure is.

## Explanations

### L1 human

The symmetries of the integers are shifts.
Knowing where $0$ goes determines the shift.
So the topology is discrete, and every subgroup is open.

### L2 human

We check that the subgroup $2\Z$ of even shifts is open.

1. It contains the stabilizer $G_0 = \set{\mathrm{id}}$.
2. A subgroup that contains a basic open subgroup is open.

The typical use is as a non-homogeneous example where SIP holds for a trivial reason.
A trap is to expect SIP to imply homogeneity; it does not.
