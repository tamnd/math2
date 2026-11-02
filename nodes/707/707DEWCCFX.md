---
tag: 707DEWCCFX
kind: object
name: Gauge group
msc: [58D19, 53C07, 81T13]
instance_of: [G5S1M9]
uses: [8E37E74XVP, 7JBRGCVJRB, NJ21PN5ZGJ, ZAJFW1S078, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Gauge_group_(mathematics)
same_as:
  wikidata: Q11301672
  wikipedia: Gauge group (mathematics)
---

## Description

Let $G$ be a [[Lie group|7JBRGCVJRB]] and $P \to X$ a smooth [[principal $G$-bundle|8E37E74XVP]] over a smooth manifold $X$, with $G$ acting on $P$ on the right.
The *gauge group* $\mathcal{G}(P)$ is the set of diffeomorphisms $u \colon P \to P$ such that $\pi \circ u = \pi$ and $u(p g) = u(p) g$ for all $p \in P$ and $g \in G$, with composition as product.

It is a group: the identity map has both properties, and so does the composite of two such maps.
The inverse of such a map $u$ commutes with $\pi$ and with the right action, because $u$ does.

## Remarks

Equivalent forms: a gauge transformation $u$ is the same as a $G$-equivariant map $\sigma \colon P \to G$, with $\sigma(p g) = g^{-1} \sigma(p) g$, through $u(p) = p \, \sigma(p)$.
So $\mathcal{G}(P)$ is the group of sections of the bundle $P \times_G G$ associated with the conjugation action.
If $P = X \times G$ is trivial, then $\mathcal{G}(P)$ is the group $C^\infty(X, G)$ of smooth maps with pointwise product.

The gauge group acts on the space of [[connections|NJ21PN5ZGJ]] on $P$ by pullback.
Take a trivial bundle and a matrix group $G$, and write a connection as a $\mathfrak{g}$-valued $1$-form $A$.
Then a map $g \colon X \to G$ sends $A$ to $g^{-1} A g + g^{-1} dg$, and the [[curvature|ZAJFW1S078]] changes to $g^{-1} F_A g$.


## Explanations

### L1 human

A principal bundle attaches a copy of the group $G$ to each point of $X$, with no preferred identity element in each copy.
A gauge transformation changes the identification in each copy independently, point by point.
Physical quantities, such as the curvature of a connection up to conjugation, do not depend on these choices, so the gauge group is a symmetry group of gauge theory.
For a trivial bundle over $X$ it is simply the group of smooth maps from $X$ to $G$.
