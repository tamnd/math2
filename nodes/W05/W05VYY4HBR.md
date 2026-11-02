---
tag: W05VYY4HBR
kind: concept
name: Canonical bundle
msc: [14C20, 14F10]
sources:
  - url: https://en.wikipedia.org/wiki/Canonical_bundle
same_as:
  wikidata: Q844128
  wikipedia: Canonical bundle
---

## Summary

The canonical bundle $\omega_X$ of a smooth variety $X$ of dimension $n$ is the line bundle of differential forms of top degree $n$.
It is the $n$-th exterior power of the [[sheaf of differentials|6VC6HQTFSA]].
A divisor $K_X$ with $\mathcal{O}_X(K_X) \cong \omega_X$ is a canonical divisor.
The canonical bundle appears in [[Serre duality|N3QPQATSRN]], in the [[adjunction formula|RYB6F7JFGV]] and in the [[Kodaira dimension|ZW00Q0SAGR]].
Its sign governs the broad classification of varieties: Fano varieties have anti-ample $\omega_X$, Calabi–Yau varieties trivial $\omega_X$, and varieties of general type big $\omega_X$.

## Explanations

### L1 human

On a surface, a differential form of top degree looks locally like $g \, dx \wedge dy$, a way to measure small areas.
The canonical bundle is the line bundle whose sections are such top-degree forms.
On a curve these are the forms $g \, dz$.
On the projective line, the form $dz$ has a double pole at infinity, since $w = 1/z$ gives $dz = -dw / w^2$.
So the canonical bundle of $\mathbb{P}^1$ has degree $-2$, and for a curve of genus $g$ its degree is $2g - 2$.
