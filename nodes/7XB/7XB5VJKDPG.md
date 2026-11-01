---
tag: 7XB5VJKDPG
kind: concept
name: Dirichlet character
msc: [11A25, 11M06]
specializes: [0RXKW044R4]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_character
same_as:
  wikidata: Q1063579
  wikipedia: Dirichlet character
---

## Summary

A Dirichlet character modulo $q$ is a function $\chi \colon \Z \to \C$ that comes from a homomorphism $(\Z/q\Z)^\times \to \C^\times$.
It is periodic with period $q$ and completely multiplicative.
There are exactly $\varphi(q)$ characters modulo $q$, and their orthogonality relations isolate a single residue class.
Dirichlet introduced them to prove [[Dirichlet's theorem on arithmetic progressions|0GNVN3CA2P]], through the [[Dirichlet L-functions|9D2Z543EJQ]] $L(s, \chi)$.

## Explanations

### L1 human

A Dirichlet character tags each integer with a complex number that depends only on its remainder modulo $q$.
Integers that share a factor with $q$ get $0$, and the others get a [[root of unity|0YV2CKP2AV]].
The tags multiply: the tag of a product is the product of the tags.
For $q = 4$, the character gives $0$ to even numbers, $1$ to numbers $1 \bmod 4$, and $-1$ to numbers $3 \bmod 4$.
