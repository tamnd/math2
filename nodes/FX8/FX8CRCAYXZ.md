---
tag: FX8CRCAYXZ
kind: example
name: Variety of groups
msc: ["20E10", 08B99]
instance_of: [AJNZJD8442]
uses: [G5S1M9, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Example

Take the signature with a binary operation $\cdot$, a unary operation ${}^{-1}$ and a constant $e$.
The *variety of groups* is the class of algebras $(G, \cdot, {}^{-1}, e)$ of this signature that satisfy the [[identities|PKD440G2XW]]
$$(x \cdot y) \cdot z = x \cdot (y \cdot z), \qquad x \cdot e = e \cdot x = x, \qquad x \cdot x^{-1} = x^{-1} \cdot x = e.$$
These algebras are exactly the [[groups|G5S1M9]], with the inverse map and the identity element listed as operations.
The class is a [[variety|AJNZJD8442]], since it is defined by identities.
In this signature, a subalgebra of a group is a subgroup, a homomorphism is a group homomorphism, and a congruence corresponds to a normal subgroup.

## Remarks

The choice of signature matters.
With the binary operation $\cdot$ alone, the class of groups is not closed under subalgebras.
For example, $(\N, +)$ is closed under $+$ inside the group $(\Z, +)$, but it is not a group.
So the class of groups is not a variety in that signature.
Subvarieties of the variety of groups include the abelian groups, defined by $x \cdot y = y \cdot x$, and the groups of exponent $n$, defined by $x^n = e$.

## Explanations

### L1 human

Groups can be described entirely by equations, once the inverse and the identity element are treated as operations.
This makes the groups a variety, so all the general theorems about varieties apply to them.
For instance, free groups are the free algebras of this variety.
