---
tag: DZ0B0JD11D
kind: definition
name: Minimal variety
msc: [08B15]
defines: JXH66D0XD5
uses: [AJNZJD8442, 4YSCK1DF26]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The variety $\mathcal{V}$ is *minimal* if both of these hold:

1. $\mathcal{V}$ contains an algebra with more than one element.
2. Every [[subvariety|4YSCK1DF26]] of $\mathcal{V}$ is either $\mathcal{V}$ itself or the trivial variety of one-element algebras.

## Remarks

Example: the variety of Boolean algebras is minimal.
Every nontrivial Boolean algebra contains the two-element Boolean algebra $\mathbf{2}$ as a subalgebra, and $\mathbf{2}$ generates the variety of all Boolean algebras.
So a subvariety with a nontrivial member contains $\mathbf{2}$ and hence every Boolean algebra.
Non-example: the variety of all groups is not minimal.
Its subvariety of abelian groups contains $\Z/2\Z$, so it is not trivial, and it is a proper subvariety.
In the [[lattice of subvarieties|GJAYCVYZYF]] of a variety, the minimal varieties are exactly the atoms, the elements that cover the trivial variety.

## Explanations

### L1 human

A minimal variety cannot be cut down further by identities without becoming trivial.
