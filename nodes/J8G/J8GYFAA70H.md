---
tag: J8GYFAA70H
kind: definition
name: Diamond principle
msc: ["03E65", "03E05"]
defines: HFQSSB1Z23
uses: [6FDYJVG1CK, 0QE8STGJH2]
sources:
  - url: https://en.wikipedia.org/wiki/Diamond_principle
---

## Definition

Let $\omega_1$ be the least uncountable ordinal.
The diamond principle $\diamondsuit$ is the following statement.
There is a [[sequence|0QE8STGJH2]] $(A_\alpha)_{\alpha < \omega_1}$ with $A_\alpha \subseteq \alpha$ for each $\alpha$, such that for each $A \subseteq \omega_1$ the set
$$\set{\alpha < \omega_1 : A \cap \alpha = A_\alpha}$$
is [[stationary|6FDYJVG1CK]] in $\omega_1$.
Such a sequence is called a $\diamondsuit$-sequence.

## Remarks

Example: Jensen proved that $\diamondsuit$ holds in the constructible universe $L$, so it is consistent with ZFC if ZFC is consistent.
Non-example: the sequence with $A_\alpha = \varnothing$ for all $\alpha$ is not a $\diamondsuit$-sequence.
For $A = \omega_1$, the set $\set{\alpha : \alpha \cap \omega_1 = \varnothing} = \set{0}$ is not stationary.
$\diamondsuit$ implies the continuum hypothesis: each $A \subseteq \omega$ equals $A \cap \alpha = A_\alpha$ for some $\alpha > \omega$, so there are at most $\aleph_1$ subsets of $\omega$.
$\diamondsuit$ implies that there is a Suslin tree, and so it settles Suslin's problem negatively.
More generally, $\diamondsuit_\kappa(S)$ is defined for a regular uncountable cardinal $\kappa$ and a stationary $S \subseteq \kappa$, with guesses only at points of $S$.
