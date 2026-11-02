---
tag: WX1Z2F3DCB
kind: example
name: Borromean rings
msc: [57K10]
instance_of: [1A5WRCNTM3]
sources:
  - url: https://en.wikipedia.org/wiki/Borromean_rings
same_as:
  wikidata: Q894166
  wikipedia: Borromean rings
---

## Example

Take three [[ellipses|0VKCCEXBJ1]] in the three coordinate planes of $\R^3$:
$$C_1 = \set{(x, y, 0) : \tfrac{x^2}{4} + y^2 = 1}, \quad C_2 = \set{(0, y, z) : \tfrac{y^2}{4} + z^2 = 1}, \quad C_3 = \set{(x, 0, z) : x^2 + \tfrac{z^2}{4} = 1}.$$
They are pairwise disjoint.
For instance, a common point of $C_1$ and $C_2$ has $x = 0$ and $z = 0$.
Then $y = \pm 1$ from $C_1$ and $y = \pm 2$ from $C_2$, which is impossible.
The other pairs are similar.
So $C_1 \cup C_2 \cup C_3$ is a [[link|1A5WRCNTM3]] with $3$ components, the *Borromean rings*.
Any two of the components form the unlink of two components.
For example, $C_2$ meets the plane $z = 0$ only at $(0, \pm 2, 0)$, outside the region bounded by $C_1$.
So $C_1$ bounds a flat disk disjoint from $C_2$, and it can be shrunk in that disk to a tiny circle far from $C_2$.
But the three components together cannot be pulled apart: the link is not equivalent to the unlink of three components.

## Remarks

All three pairwise [[linking numbers|SFJ329YB9F]] are $0$, so linking numbers do not detect the Borromean rings.
Their nontriviality is detected by Milnor's triple linking number, or by the fact that their link group is not free.
A nontrivial link in which removing any one component leaves an unlink is called Brunnian, and the Borromean rings are the simplest example.
They have a diagram with $6$ crossings that is alternating.
Their complement in $S^3$ carries a complete hyperbolic metric of finite volume, and it can be built from two regular ideal octahedra.
Michael Freedman and Richard Skora showed that the Borromean rings cannot be built from three round circles.

## Explanations

### L1 human

The Borromean rings are three rings that hold together as a group, although no two of them are linked.
If any one ring is cut and removed, the other two fall apart.
They appear in old coats of arms, among them that of the Borromeo family of Italy, which gives the name.
