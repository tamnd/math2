---
tag: W007WWX7AN
kind: definition
name: Quasi-compact morphism
msc: [14A15]
defines: 41009J4M5D
uses: [JXRKH6P1Z4, B3V3XJ2W8G, 0TVJZYB6SH, J4YW23MD6N]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-compact_morphism
---

## Definition

A topological space is *quasi-compact* if every open cover of it has a finite subcover, as for a [[compact space|0TVJZYB6SH]] without any separation axiom.
A [[morphism of schemes|JXRKH6P1Z4]] $f \colon X \to Y$ is *quasi-compact* if for every open [[affine|B3V3XJ2W8G]] subscheme $V \subseteq Y$ the open set $f^{-1}(V)$ is quasi-compact.

## Remarks

It is enough to check this for the sets $V_i$ of one cover of $Y$ by open affine subschemes.
Every affine scheme is quasi-compact, by [[quasi-compactness of the spectrum|J4YW23MD6N]].
Example: every closed immersion $f \colon Z \to Y$ is quasi-compact.
For $V$ open affine, $f^{-1}(V)$ is homeomorphic to a closed subset of the quasi-compact space $V$, and closed subsets of quasi-compact spaces are quasi-compact.
Example: if $X$ is a Noetherian scheme, every morphism $X \to Y$ is quasi-compact, since every subset of a Noetherian space is quasi-compact.
Non-example: let $X$ be the disjoint union of infinitely many copies of $\operatorname{Spec} k$ for a field $k$, and $f \colon X \to \operatorname{Spec} k$ the obvious map.
Then $f^{-1}(\operatorname{Spec} k) = X$ is covered by the copies, with no finite subcover, so $f$ is not quasi-compact.
