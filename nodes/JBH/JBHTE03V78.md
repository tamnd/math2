---
tag: JBHTE03V78
kind: concept
name: Spectral synthesis
msc: [43A45, 43A20]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener%27s_Tauberian_theorem
---

## Summary

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with [[group algebra|6GD25S53ND]] $L^1(G)$.
Spectral synthesis asks whether a closed ideal of $L^1(G)$ is determined by the characters where all its Fourier transforms vanish.
A closed set $E$ of the [[dual group|FMW57WNPDB]] is a set of spectral synthesis if exactly one closed ideal has $E$ as zero set.
[[Wiener's Tauberian theorem|V20376HXHD]] is the case $E = \emptyset$, and points are also sets of synthesis.
By [[Malliavin's theorem|2R3ZF9TY8N]], synthesis fails for some closed set as soon as the dual group is not discrete.

## Explanations

### L1 human

Think of a closed ideal of $L^1(G)$ as a family of functions whose Fourier transforms all vanish on a common set of frequencies $E$.
The largest such family consists of all integrable functions whose transforms vanish on $E$.
Spectral synthesis for $E$ means that no smaller closed family has the same set of zeros.
On the real line this is true for a single point, but it fails for some complicated closed sets.
