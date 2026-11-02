---
tag: ES6P7WHJG9
kind: example
name: Trivial variety
msc: [08B15]
instance_of: [AJNZJD8442]
uses: [PKD440G2XW, GJAYCVYZYF]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Example

Fix a signature $\sigma$.
The *trivial variety* of signature $\sigma$ is the class of all algebras of signature $\sigma$ that satisfy the [[identity|PKD440G2XW]] $x = y$.
An algebra satisfies $x = y$ exactly when any two of its elements are equal, so the trivial variety consists of the one-element algebras.
It is a [[variety|AJNZJD8442]] because it is defined by an identity.
The check by closure is also direct.
A subalgebra or a homomorphic image of a one-element algebra has one element.
A direct product of one-element algebras has one element, and the empty product is a one-element algebra too.

## Remarks

Every variety of signature $\sigma$ contains all one-element algebras of signature $\sigma$, since a one-element algebra satisfies every identity.
So the trivial variety is the least element of the [[lattice of subvarieties|GJAYCVYZYF]] of any variety.
Its equational theory is the largest one: it contains every identity of signature $\sigma$.

## Explanations

### L1 human

The trivial variety is the smallest possible variety: it only has algebras with one element.
In such an algebra, every operation has only one possible value, so there is nothing to compute.
Every other variety contains it.
