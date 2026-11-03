---
tag: 3YDPFTQTJ6
kind: concept
name: Negative K-theory
msc: [19D35]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

Negative K-theory is the sequence of groups $K_{-1}(R), K_{-2}(R), \ldots$ that Bass attached to a ring $R$.
They extend algebraic K-theory below degree zero, so that the fundamental theorem for Laurent polynomial rings holds in every degree.
They vanish for regular Noetherian rings, so they measure singularities.
They also appear in topology, as obstruction groups for problems about bounded and controlled manifolds.

## Explanations

### L1 human

For many rings, the group $K_1$ of the Laurent polynomial ring $R[t, t^{-1}]$ contains a copy of $K_0(R)$, coming from the unit $t$.
Bass turned this around: he defined a new group one degree lower by the same recipe, starting from $K_0$.
Repeating the recipe gives groups in all negative degrees.
For a field, or any regular ring, these groups are zero.
For a curve with a node, such as $y^2 = x^3 + x^2$, the group $K_{-1}$ is $\Z$, and it detects the node.
