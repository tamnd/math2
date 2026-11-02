---
tag: W58NYR1DGR
kind: example
name: Reeb foliation
msc: [57R30, 53C12]
instance_of: [98HTB7MSPX]
sources:
  - url: https://en.wikipedia.org/wiki/Reeb_foliation
same_as:
  wikidata: Q564842
  wikipedia: Reeb foliation
---

## Example

Let $D = \set{u \in \R^2 : \abs{u} < 1}$ be the open unit disc.
On $D \times \R$ consider, for each $c \in \R$, the surface
$$L_c = \set{(u, t) \in D \times \R : t = c + e^{1/(1 - \abs{u}^2)}}.$$
These surfaces are disjoint graphs over $D$, and they fill $D \times \R$.
Together with the boundary cylinder $\partial D \times \R$, they form a codimension one [[foliation|98HTB7MSPX]] of the closed solid cylinder $\bar D \times \R$.
Each $L_c$ is a plane that bends upwards and approaches the boundary cylinder as $\abs{u} \to 1$, since $e^{1/(1 - \abs{u}^2)} \to \infty$.
The translation $t \mapsto t + 1$ maps $L_c$ to $L_{c+1}$, so the foliation passes to the quotient solid torus $\bar D \times (\R / \Z)$.
This foliated solid torus is a *Reeb component*.
Its boundary torus is one leaf, and every interior leaf is a plane that spirals towards the boundary.

The $3$-sphere is the union of two solid tori glued along their boundary tori.
The gluing sends the meridian of each solid torus to the longitude of the other.
Putting a Reeb component on each solid torus gives a smooth codimension one foliation of $S^3$, the *Reeb foliation*.
The leaves are one torus and infinitely many planes.

## Remarks

The construction shows that $S^3$, which has Euler characteristic $0$, carries a codimension one foliation.
Novikov proved that every codimension one foliation of class $C^2$ on $S^3$ has a compact leaf, a torus bounding a Reeb component.
The torus leaf has infinite fundamental group, so the [[Reeb stability theorem|Z93KMZ9R37]] does not force the other leaves to be compact, and indeed they are planes.

## Explanations

### L1 human

Imagine a stack of bowls inside a solid cylinder, each bowl a little higher than the last, with rims climbing ever higher along the wall.
Roll the cylinder into a doughnut, and the bowls become sheets spiralling towards the doughnut's surface.
Two such doughnuts glued together make up the $3$-sphere, foliated by one torus and many planes.
