---
tag: MDH7VXDCVF
kind: concept
name: Proper group action
msc: [54H15, 57S20, "22F05"]
specializes: [0WCY42EV9V]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_map
---

## Summary

A continuous action of a topological group $G$ on a space $X$ is proper when the map $(g, x) \mapsto (g \cdot x, x)$ is a [[proper map|15XEBGNGHC]].
Informally, group elements that move a compact set back onto itself form a compact set.
Proper actions have Hausdorff orbit spaces, closed orbits and compact stabilizers.
They are the right setting for quotients such as homogeneous spaces $G/H$ and for the action of discrete groups on manifolds.

## Explanations

### L1 human

Think of a group moving the points of a space around.
The action is proper when only a "small", compact, part of the group can bring a given bounded region back near itself.
Integer translations of the real line are proper: to move $[0, 1]$ to a place where it meets itself, only the shifts by $-1$, $0$ and $1$ work.
Scaling the line by positive numbers is not proper, because every scaling keeps the point $0$ in place.
