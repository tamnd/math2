---
tag: 49VHC2VWNF
kind: definition
name: Hopf algebra
msc: [16T05]
defines: 7XFYP0N84H
uses: [Q9HHVN606G, PG3ECG5D0G, MNP2HBWB5Q]
sources:
  - url: https://en.wikipedia.org/wiki/Hopf_algebra
---

## Definition

Let $K$ be a field.
A *Hopf algebra* over $K$ is a [[bialgebra|Q9HHVN606G]] $(H, m, \eta, \Delta, \varepsilon)$ over $K$ together with a linear map $S \colon H \to H$ such that
$$m \circ (S \otimes \id_H) \circ \Delta = \eta \circ \varepsilon = m \circ (\id_H \otimes S) \circ \Delta.$$
The map $S$ is the [[antipode|PG3ECG5D0G]] of $H$.

## Remarks

Example: the [[group algebra|MNP2HBWB5Q]] $KG$ of a group $G$, with $\Delta(g) = g \otimes g$, $\varepsilon(g) = 1$ and $S(g) = g^{-1}$.
The check on a basis element $g$: $m(S \otimes \id)\Delta(g) = g^{-1} g = 1 = \varepsilon(g) 1$, and likewise $g g^{-1} = 1$.
Example: the universal enveloping algebra of a Lie algebra $\mathfrak{g}$, with $\Delta(x) = x \otimes 1 + 1 \otimes x$, $\varepsilon(x) = 0$ and $S(x) = -x$ for $x \in \mathfrak{g}$.
Non-example: the monoid algebra $K[x]$ of $(\N, +)$, with $\Delta(x) = x \otimes x$ and $\varepsilon(x) = 1$, is a bialgebra but not a Hopf algebra.
An antipode would need $S(x) x = \varepsilon(x) 1 = 1$, but $x$ has no inverse in $K[x]$.
The antipode of a Hopf algebra is unique, because it is the inverse of $\id_H$ in the convolution algebra $\End_K(H)$.
