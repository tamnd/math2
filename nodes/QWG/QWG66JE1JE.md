---
tag: QWG66JE1JE
kind: concept
name: Cayley–Abels graph
msc: [22D05, 20F65, 05C25]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_graph
---

## Summary

Let $G$ be a compactly generated totally disconnected [[locally compact group|AHV05ZBCYW]].
A Cayley–Abels graph of $G$ is a connected locally finite graph on which $G$ acts vertex-transitively with compact open vertex stabilisers.
It generalises the [[Cayley graph|0GYQK9NDJF]] of a finitely generated group, which is the case of a discrete group.
Every such $G$ has a Cayley–Abels graph, and any two of them are [[quasi-isometric|6FKYSH729T]].
So $G$ has a well-defined large-scale geometry, as in geometric group theory.

## Explanations

### L1 human

For a finitely generated group, the Cayley graph draws one vertex for each element and joins elements that differ by a generator.
For a group like $\mathrm{PGL}_2(\Q_p)$ this is not possible with finitely many generators.
Instead one draws one vertex for each coset of a compact open subgroup $U$, and joins cosets using finitely many extra elements.
For $\mathrm{PGL}_2(\Q_p)$ with $U = \mathrm{PGL}_2(\Z_p)$, one can obtain in this way the regular tree in which each vertex has $p + 1$ neighbours.
