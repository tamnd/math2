---
tag: TRMYSF91EV
kind: statement
role: corollary
name: Endomorphism ring of a simple module is a division ring
msc: [16D60, 16S50]
uses: [G00C22AEDH, AWSBZWWMG9, 0EA5BTA0CX, X4M2FFKQJ6]
about: [AWSBZWWMG9, G00C22AEDH]
sources:
  - url: https://en.wikipedia.org/wiki/Schur%27s_lemma
---

## Statement

Let $R$ be a ring and let $M$ be a [[simple|G00C22AEDH]] left $R$-module.
Then the [[endomorphism ring|AWSBZWWMG9]] $\End_R(M)$ is a [[division ring|0EA5BTA0CX]].

## Remarks

$\End_R(M)$ is nonzero, since $M \ne 0$ gives $\id_M \ne 0$.
By [[Schur's lemma|X4M2FFKQJ6]] every nonzero endomorphism of $M$ is an isomorphism, so its inverse map is again an endomorphism and is its inverse in $\End_R(M)$.
Example: $\End_\Z(\Z/p\Z) \cong \Z/p\Z$, a field, for $p$ prime.
Simplicity is needed: for the semisimple $\Z$-module $M = \Z/p\Z \oplus \Z/p\Z$, the ring $\End_\Z(M) \cong M_2(\Z/p\Z)$ has the nonzero non-invertible element $E_{11}$.
If $R$ is an algebra over an algebraically closed field $k$ and $M$ has finite dimension over $k$, then $\End_R(M) = k$.

## Explanations

### L1 human

The self-maps of a simple module that are not zero can always be undone.
So the self-maps form a ring in which one can divide by every nonzero element, just as in a field, except that the order of multiplication may matter.

### L2 human

This is how division rings enter the structure theory of rings.
In the Artin–Wedderburn theorem, a simple Artinian ring is a matrix ring over the division ring $\End_R(M)^{\mathrm{op}}$ for a simple module $M$.
In representation theory over $\C$, it says that endomorphisms of a finite-dimensional irreducible representation are scalars.
