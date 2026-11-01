---
tag: NPF42DJMBX
kind: statement
role: theorem
name: Completion is flat
msc: [13B35, 13C11, 13J10]
uses: [0670T59HGE, 096Z9MP2ME, NS84D2920R, 73RYYEVDKA, C31PYYPRGC, XA0DCNH7WY, 05QY1VEBYD, F0HQXQ0HCD, 30H6B0G2FT]
about: [KBN13NPYJQ, 73RYYEVDKA]
sources:
  - url: https://en.wikipedia.org/wiki/Completion_of_a_ring
---

## Statement

Let $R$ be a commutative [[Noetherian ring|0670T59HGE]], let $I$ be an [[ideal|096Z9MP2ME]] of $R$, and let $\hat R$ be the [[$I$-adic completion|NS84D2920R]] of $R$.

1. For every [[finitely generated|05QY1VEBYD]] $R$-module $M$, the natural map $\hat R \otimes_R M \to \hat M$ is an isomorphism, where $\hat M = \varprojlim_n M/I^n M$.
2. $\hat R$ is a [[flat|73RYYEVDKA]] $R$-module.
3. If $I$ is contained in the [[Jacobson radical|XA0DCNH7WY]] of $R$, then $\hat R$ is a [[faithfully flat|C31PYYPRGC]] $R$-module; this applies when $R$ is local and $I \neq R$.

## Remarks

By the [[Artin–Rees lemma|30H6B0G2FT]], completion $M \mapsto \hat M$ is an exact functor on finitely generated $R$-modules.
Both $M \mapsto \hat R \otimes_R M$ and $M \mapsto \hat M$ are right exact and agree on finite free modules, so they agree on finitely presented modules, which gives clause 1.
Then for an ideal $J$ of $R$ the map $\hat R \otimes_R J \to \hat R$ is the injective map $\hat J \to \hat R$, which gives clause 2 by the ideal criterion for flatness.
For clause 3, each maximal ideal $\mathfrak n$ contains $I$, so $\hat R/\mathfrak n \hat R \cong R/\mathfrak n \neq 0$.
Clause 3 can fail without its hypothesis.
The $p$-adic completion $\Z_p$ of $\Z$ is flat over $\Z$, but $\Z_p \otimes_\Z \Z/q\Z = 0$ for a prime $q \neq p$, because $q$ is a unit in $\Z_p$.
So $\Z_p$ is not faithfully flat over $\Z$.

## Explanations

### L1 human

Completing a ring adds limits of approximations, like passing from integers to $p$-adic integers.
Flatness means that this operation does not destroy injectivity of maps between modules.
So information about a Noetherian ring and its modules is kept faithfully when one passes to the completion, at least near the ideal used for completing.

### L2 human

Flatness lets one move properties between a Noetherian local ring $R$ and its completion $\hat R$.
For instance $\dim \hat R = \dim R$, and $R$ is regular, or Cohen–Macaulay, if and only if $\hat R$ is.
Combined with the [[Cohen structure theorem|N3XH42KVV3]], this reduces many questions about local rings to quotients of power series rings.
