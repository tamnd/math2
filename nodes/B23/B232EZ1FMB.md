---
tag: B232EZ1FMB
kind: concept
name: Invariant measure
msc: [37A05, 28D05, 37C40]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_measure
same_as:
  wikidata: Q4200518
  wikipedia: Invariant measure
---

## Summary

An invariant measure of a map is a [[measure|PR11BZQQPG]] that the map does not change: every set has the same measure as its preimage.
With respect to such a measure the map is a [[measure-preserving transformation|556WBDAHNP]], and the tools of ergodic theory apply.
Invariant probability measures describe the statistics of orbits, such as how often an orbit visits a region.
On a compact metric space every continuous map has at least one invariant probability measure, by the [[Krylov–Bogolyubov theorem|1DHZ81S0YE]].

## Explanations

### L1 human

Think of a measure as a way of spreading sand over the space.
Apply the map to every grain: the measure is invariant if the sand ends up spread exactly as before.
Lebesgue measure on the circle is invariant under every rotation, since rotating does not change lengths of arcs.
For the map $x \mapsto x/2$ on the real line, the point mass at $0$ is invariant, while Lebesgue measure is not, since the map squeezes everything towards $0$.
