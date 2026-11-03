---
tag: CZ2BZQN2EV
kind: statement
role: theorem
name: Moufang identities
msc: [17D05, 20N05]
uses: [N8K9SSVMRN]
about: [N8K9SSVMRN, H0TJPNCMXD]
sources:
  - url: https://en.wikipedia.org/wiki/Moufang_loop
---

## Statement

Let $A$ be an [[alternative algebra|N8K9SSVMRN]] over a commutative ring $R$.
Then for all $x, y, z \in A$:

1. $z(x(zy)) = ((zx)z)y$.
2. $x(z(yz)) = ((xz)y)z$.
3. $(zx)(yz) = (z(xy))z$.
4. $(zx)(yz) = z((xy)z)$.

## Remarks

The proof expands the differences of the two sides in terms of associators and uses that the associator of an alternative algebra is alternating.
Since $A$ is flexible, $(zx)z = z(xz)$, so the element $zxz$ in the first identity has no ambiguity.
Example: in the [[octonions|1HRMT3DSX2]] the identities hold for all triples, although $(xy)z \neq x(yz)$ for some triples.
The nonzero octonions under multiplication satisfy the same identities, so they form a [[Moufang loop|H0TJPNCMXD]].

## Explanations

### L1 human

The Moufang identities are rules for moving brackets in products of four factors where one factor appears twice.
They hold in every alternative algebra, even when general products of three factors do not associate.
They give a substitute for the associative law.

### L2 human

The identities are named after Ruth Moufang.
A loop that satisfies them is a Moufang loop, and the unit octonions are the standard example of a Moufang loop that is not a group.
Together with [[Artin's theorem|PBRCDXKQFR]], they are the main tools for computing in alternative algebras.
