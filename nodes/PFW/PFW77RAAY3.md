---
tag: PFW77RAAY3
kind: concept
name: Topological Hochschild homology
msc: [19D55, 55P42, "16E40"]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_Hochschild_homology
same_as:
  wikidata: Q105038900
  wikipedia: Topological Hochschild homology
---

## Summary

Topological Hochschild homology, written $THH$, is an analogue of [[Hochschild homology|S5H153HFWC]].
In it, tensor products over the integers are replaced by smash products over the sphere spectrum.
It is defined for ring spectra, and in particular for ordinary rings.
It carries an action of the [[circle group|04EAFVFTF7]], and from it one builds topological cyclic homology.
Through the cyclotomic trace it is one of the main tools to compute [[algebraic K-theory|5GVFZWMWC8]].

## Explanations

### L1 human

Hochschild homology of a ring is built from tensor powers $R \otimes R \otimes \cdots \otimes R$ arranged in a circle, with maps that multiply neighbours.
Topological Hochschild homology uses the same pattern, but works over the sphere spectrum instead of over $\Z$.
This makes it see more: even for $\Z$ or $\mathbb{F}_p$ it has interesting groups in positive degrees.
For instance, Bökstedt showed that the homotopy groups of $THH(\mathbb{F}_p)$ form a polynomial ring $\mathbb{F}_p[u]$ on one generator of degree $2$.
By contrast, ordinary Hochschild homology of $\mathbb{F}_p$ over itself is just $\mathbb{F}_p$ in degree $0$.
