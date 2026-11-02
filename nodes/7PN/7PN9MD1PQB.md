---
tag: 7PN9MD1PQB
kind: concept
name: Whitney C-infinity topology
msc: [58D15, 58C25]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_topologies
---

## Summary

The Whitney $C^\infty$ topology, also called the strong $C^\infty$ topology, is a topology on the set $C^\infty(M, N)$ of smooth maps between [[smooth manifolds|F45VQ47GPV]].
Two maps are close in it when their values and derivatives up to some order are close at every point.
The allowed error may shrink towards infinity.
It is the standard topology in which one says that a property of maps is generic, stable or open.
With it, $C^\infty(M, N)$ is a [[Baire space|0ZH5AJ2ED7]], which makes transversality arguments work.

## Explanations

### L1 human

Think of a smooth function on the real line and draw a thin tube around its graph.
The tube may get thinner and thinner far out, like the function $1/(1 + x^2)$.
In the Whitney topology, the functions whose graphs stay inside such a tube form a neighbourhood, and one can ask the same of the derivatives.
So the constant function $1/n$ is never close to $0$ in this topology, however large $n$ is: far out, the tube around $0$ is thinner than $1/n$.
This strict control at infinity is what makes many sets of nice maps open.
