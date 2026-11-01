---
tag: CKGN4ZH6P2
kind: definition
name: Strict Henselization
msc: [13J15, 13B40]
defines: GJHAF85F4S
uses: [MZ02BKPHJA, RNXPV3KC5J, P8YTMGEN9R, NJ3APQ8BHH, JJ91A1V8NQ, 8B57B7EGK4]
sources:
  - url: https://en.wikipedia.org/wiki/Henselian_ring
---

## Definition

Let $(R, \mathfrak{m}, k)$ be a [[local ring|MZ02BKPHJA]] with [[residue field|NJ3APQ8BHH]] $k$, and let $k^{s}$ be a [[separable closure|JJ91A1V8NQ]] of $k$.
A local ring is *strictly Henselian* if it is a [[Henselian local ring|RNXPV3KC5J]] and its residue field is [[separably closed|8B57B7EGK4]].
A *strict Henselization* of $R$ is a local ring $R^{sh}$ with a [[local homomorphism|P8YTMGEN9R]] $i \colon R \to R^{sh}$.
The residue field of $R^{sh}$ is identified with $k^{s}$, and the following hold:

1. $R^{sh}$ is strictly Henselian.
2. The map of residue fields induced by $i$ is the inclusion $k \subseteq k^{s}$.
3. Let $S$ be a strictly Henselian local ring with residue field $\kappa_S$, let $f \colon R \to S$ be a local homomorphism, and let $\sigma \colon k^{s} \to \kappa_S$ be a $k$-embedding.
Then there is exactly one local homomorphism $g \colon R^{sh} \to S$ with $g \circ i = f$ that induces $\sigma$ on residue fields.

## Remarks

A strict Henselization exists and is unique up to a unique isomorphism once $k^{s}$ is fixed.
It is a direct limit of localizations of [[étale|FTRW0679E2]] $R$-algebras, and the map $i$ is [[faithfully flat|C31PYYPRGC]].
The map $i$ factors through the [[Henselization|917PGHVZPM]] of $R$.

Example: for a field $k$, the field $k^{s}$ with the inclusion $k \to k^{s}$ is a strict Henselization.
A field is a Henselian local ring with maximal ideal $0$, its residue field is itself, and $k^{s}$ is separably closed.

Non-example: the ring $\Z_p$ of $p$-adic integers with the identity map fails clause 1.
It is Henselian, but its residue field $\F_p$ is not separably closed.
