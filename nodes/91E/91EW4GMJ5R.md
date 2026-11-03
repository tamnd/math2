---
tag: 91EW4GMJ5R
kind: concept
name: Universal central extension
msc: [19C09, "20E22", 20J06]
specializes: [MF4N3VGGFV]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_multiplier
---

## Summary

A universal central extension of a group $G$ is a central extension of $G$ with a special property.
It maps in exactly one way to every other central extension of $G$.
It exists exactly when $G$ is perfect, and then it is unique up to unique isomorphism.
Its kernel is the Schur multiplier $H_2(G, \Z)$.
In algebraic K-theory, the Steinberg group is the universal central extension of the elementary group, and its kernel is $K_2$.

## Explanations

### L1 human

A central extension of $G$ is a bigger group that maps onto $G$, with the extra part sitting in the center.
The universal one is the largest such extension in a precise sense: every other central extension receives exactly one map from it that is compatible with the maps onto $G$.
For example, the group $SL_2(\F_5)$ of $2 \times 2$ matrices of determinant $1$ over the field with five elements maps onto the simple group $A_5$, with kernel $\set{\pm I}$.
This is the universal central extension of $A_5$.
