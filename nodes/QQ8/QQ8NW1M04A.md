---
tag: QQ8NW1M04A
kind: definition
name: Modes of fracture
msc: [74R10, 74A45]
defines: H1J9Q4TVJ6
uses: [SNRXGRZWR5]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_mechanics
---

## Definition

Let a body in $\R^3$ contain a crack whose faces are locally planar near a point $P$ of the crack front.
Choose an orthonormal frame $e_1, e_2, e_3$ at $P$ as follows.
The vector $e_1$ lies in the crack plane, is perpendicular to the front and points ahead of the crack.
The vector $e_2$ is normal to the crack plane, and $e_3$ is tangent to the front.
Let $[u] = u^+ - u^-$ be the jump of the displacement between the upper face ($x_2 > 0$) and the lower face ($x_2 < 0$) near $P$.
The crack-tip deformation is in

1. *mode I* (opening) when $[u]$ is parallel to $e_2$;
2. *mode II* (in-plane shear, sliding) when $[u]$ is parallel to $e_1$;
3. *mode III* (out-of-plane shear, tearing) when $[u]$ is parallel to $e_3$.

A general deformation is a *mixed mode*, a superposition of the three.

## Remarks

Example: a straight crack in a large plate under remote tension perpendicular to the crack is loaded in mode I only.
Its faces separate along $e_2$, and the field is symmetric with respect to the crack plane.
Non-example: the same crack under remote tension at $45^\circ$ to the crack line is not loaded in mode I only.
The remote shear component also makes the faces slide along $e_1$, so its loading mixes the first two modes.
In plane problems, modes I and II are the parts of the field that are symmetric and antisymmetric with respect to the crack line.
Mode III is the antiplane shear problem.

## Explanations

### L1 human

The two faces of a crack can move apart, slide past each other across the front, or slide past each other along the front.
These are modes I, II and III.
