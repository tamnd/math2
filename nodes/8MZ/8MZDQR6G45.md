---
tag: 8MZDQR6G45
kind: concept
name: Littelmann path model
msc: [17B10, "05E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Littelmann_path_model
same_as:
  wikidata: Q6648763
  wikipedia: Littelmann path model
---

## Summary

The Littelmann path model is a combinatorial model of the finite-dimensional irreducible representations of a complex [[semisimple Lie algebra|EY9DN7QAX1]].
It replaces the weights of a representation by piecewise linear paths that start at $0$ in the real span of the weights.
Root operators act on these paths, and the endpoints of the paths reached from one dominant path give the [[weights|KFVNC2W720]] with multiplicities.
The model was introduced by Peter Littelmann and gives combinatorial rules for characters and tensor products.

## Explanations

### L1 human

Instead of counting weights directly, one draws paths in a space, all starting at the origin.
A simple path is the straight segment from $0$ to the highest weight $\lambda$.
Certain folding moves, one for each simple root, reflect part of a path and so create new paths.
The endpoints of all paths obtained in this way are the weights of the representation, each counted as often as it occurs.
For $\mathfrak{sl}_2$ and highest weight $n$, one gets $n + 1$ paths, with endpoints $n, n - 2, \dots, -n$.
