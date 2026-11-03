---
tag: 2JTTJ3XHH4
kind: concept
name: Chevalley basis
msc: ["17B20", "17B45"]
sources:
  - url: https://en.wikipedia.org/wiki/Chevalley_basis
same_as:
  wikidata: Q5094304
  wikipedia: Chevalley basis
---

## Summary

A Chevalley basis of a complex semisimple Lie algebra is a basis adapted to the root space decomposition in which all structure constants are integers.
It consists of the coroots of the simple roots, which span a Cartan subalgebra, and one root vector for each root, normalized so that $[x_\alpha, x_\beta] = \pm (r+1) x_{\alpha + \beta}$.
Chevalley proved that such a basis always exists, and its integer span is the starting point for Chevalley groups over arbitrary fields.

## Explanations

### L1 human

A Lie algebra is described by the brackets of its basis vectors.
For a general basis these brackets involve arbitrary complex numbers.
Chevalley found, for each semisimple Lie algebra, a basis where every bracket is an integer combination of basis vectors.
For $\mathfrak{sl}_2(\C)$ the basis $e, h, f$ with $[h, e] = 2e$, $[h, f] = -2f$, $[e, f] = h$ is such a basis.
Integer brackets let one reduce the Lie algebra modulo a prime and build analogues over finite fields.
