---
tag: J9QYGM8AKF
kind: definition
name: Henselization
msc: [13J15, 13B40]
defines: 917PGHVZPM
uses: [MZ02BKPHJA, RNXPV3KC5J, P8YTMGEN9R]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Definition

Let $(R, \mathfrak{m})$ be a [[local ring|MZ02BKPHJA]].
A *Henselization* of $R$ is a local ring $R^h$ together with a [[local homomorphism|P8YTMGEN9R]] $i \colon R \to R^h$ such that:

1. $R^h$ is a [[Henselian local ring|RNXPV3KC5J]].
2. For every Henselian local ring $S$ and every local homomorphism $f \colon R \to S$, there is exactly one local homomorphism $g \colon R^h \to S$ with $g \circ i = f$.

## Remarks

A Henselization exists for every local ring, and the universal property makes it unique up to a unique isomorphism.
One construction takes the direct limit of the localizations of [[étale|FTRW0679E2]] $R$-algebras at primes over $\mathfrak{m}$ with trivial residue field extension.
The map $i$ is [[faithfully flat|C31PYYPRGC]], the ideal $\mathfrak{m} R^h$ is the maximal ideal of $R^h$, and $i$ induces an isomorphism of residue fields.
If $R$ is Noetherian, then $R^h$ is Noetherian and has the same [[completion|KBN13NPYJQ]] as $R$.

Example: if $R$ is already Henselian, then $R$ with the identity map is a Henselization, because $g = f$ is the only choice in clause 2.

Non-example: $\Z_{(5)}$ with the identity map is not its own Henselization, because it fails clause 1.
The polynomial $x^2 - 6$ has the simple root $1$ modulo $5$, but $6$ is not a square in $\Q$, so the root does not lift to $\Z_{(5)}$.
