---
tag: JZNQAN00ZJ
kind: concept
name: Torsion tensor
msc: [53B05]
specializes: [WX302T93TW]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_tensor
same_as:
  wikidata: Q13229797
  wikipedia: Torsion tensor
---

## Summary

The torsion tensor of an [[affine connection|JX65KSVHSJ]] measures how far covariant derivatives are from being symmetric in the two vector fields.
The Lie bracket is subtracted to make this a tensor.
It is a tensor field of type $(1, 2)$, antisymmetric in its two arguments.
Connections with zero torsion are called torsion-free or symmetric; the Levi-Civita connection is the unique torsion-free connection compatible with a given Riemannian metric.
Geometrically, torsion describes how infinitesimal parallelograms built by parallel transport fail to close.

## Explanations

### L1 human

Start at a point, move a little in direction $X$, then a little in direction $Y$, carrying each direction along with the connection.
Do the same in the other order.
For a torsion-free connection the two endpoints agree to second order, so the small parallelogram closes.
Torsion measures the small gap that remains.
The flat connection of the plane has no torsion, while a connection that twists directions as you move, like a screw, can have torsion.
