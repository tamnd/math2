---
tag: RSC5KTVNZD
kind: definition
name: Scheme
msc: [14A15]
defines: 5A35TYZD02
uses: [B7FPT8JTXR, B3V3XJ2W8G]
sources:
  - url: https://en.wikipedia.org/wiki/Scheme_(mathematics)
---

## Definition

A *scheme* is a [[locally ringed space|B7FPT8JTXR]] $(X, \mathcal{O}_X)$ such that every point $x \in X$ has an open neighbourhood $U$ for which $(U, \mathcal{O}_X|_U)$ is an [[affine scheme|B3V3XJ2W8G]].

## Remarks

Example: every affine scheme $\operatorname{Spec} A$ is a scheme, with $U = X$ for every point.
Example: the projective line $\mathbb{P}^1_k$ over a field $k$ is a scheme: it is covered by two open sets, each isomorphic to $\operatorname{Spec} k[t]$.
It is not affine, since its ring of global functions is $k$, while $\operatorname{Spec} k$ is a single point.
Non-example: the one-point space with sheaf $\Z$ is a ringed space but not a scheme.
Its stalk $\Z$ is not a local ring, so it is not even locally ringed.
An open subset $U$ of a scheme, with the restricted sheaf $\mathcal{O}_X|_U$, is again a scheme, called an open subscheme.
