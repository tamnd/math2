---
tag: 0QFV5Y1Z5X
kind: statement
role: theorem
name: Gauss's lemma
msc: [13F20]
uses: [08C1NWBNHA, 06YMXJMXYS, 0VF11ZTTMD, 00X2A9G9W3, 0SP14DZN0G]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(polynomials)
    locator: Statements for unique factorization domains
same_as:
  wikidata: Q587938
  wikipedia: Gauss's lemma (polynomials)
---

## Statement

Let $R$ be a [[unique factorisation domain|06YMXJMXYS]] with [[field of fractions|0VF11ZTTMD]] $K$ and let $f \in R[x]$ be a [[primitive polynomial|0SP14DZN0G]].
Then $f$ is [[irreducible|00X2A9G9W3]] in $R[x]$ if and only if $f$ is irreducible in $K[x]$.

## Remarks

The key step: if $f = g h$ in $K[x]$, then one can scale $g$ and $h$ by elements of $K$ so that they are in $R[x]$ and $f = g h$ still holds. This uses that the [[product of primitive polynomials is primitive|08C1NWBNHA]].
For $R = \mathbb{Z}$: a primitive integer polynomial that factors over $\mathbb{Q}$ already factors over $\mathbb{Z}$, into factors of the same degrees.
The hypothesis that $f$ is primitive is necessary: $2x$ is irreducible in $\mathbb{Q}[x]$, but $2x = 2 \cdot x$ is a product of two nonunits in $\mathbb{Z}[x]$.

## Explanations

### L1 human

To show that an integer polynomial has no factorisation over the rationals, it is enough to check factorisations over the integers.
Fractions do not help to factor a primitive polynomial.
This is why criteria such as Eisenstein's work with integer coefficients.
