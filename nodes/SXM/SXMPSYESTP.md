---
tag: SXMPSYESTP
kind: definition
name: Holonomy groupoid of a foliation
msc: [57R30, 22A22, 58H05]
defines: HMRP135M6K
uses: [98HTB7MSPX, FH3C0T643F, HNVW0E732J, 03NAMV1DHJ, VZXF7RNFKS, VKFW27WXEZ, W58NYR1DGR]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_groupoid
---

## Definition

Let $M$ be a smooth manifold of dimension $n$ with a [[foliation|98HTB7MSPX]] $\mathcal{F}$ of codimension $q$.
A *leafwise path* is a [[path|03NAMV1DHJ]] $\gamma \colon [0, 1] \to M$ whose image lies in a single leaf.
For each $x \in M$ fix a transversal $T_x$: a [[submanifold|VKFW27WXEZ]] of dimension $q$ through $x$ that meets the leaves transversally.
Let $\gamma$ be a leafwise path from $x$ to $y$.
Following the leaves near $\gamma$ from $T_x$ to $T_y$ defines a [[germ|VZXF7RNFKS]] at $x$ of a diffeomorphism $\operatorname{hol}(\gamma) \colon (T_x, x) \to (T_y, y)$, the *holonomy* of $\gamma$.
Two leafwise paths are *holonomy equivalent* if they have the same endpoints $x, y$ and the same holonomy germ.
The *holonomy groupoid* $\operatorname{Hol}(M, \mathcal{F})$ is the [[groupoid|FH3C0T643F]] with these data.

1. Its objects are the points of $M$.
2. Its arrows from $x$ to $y$ are the holonomy equivalence classes of leafwise paths from $x$ to $y$.
3. Composition is induced by concatenation of paths, and the inverse of the class of $\gamma$ is the class of the reversed path.

## Remarks

The holonomy germ does not depend on the choice of transversals up to the natural identifications, so the equivalence relation is well defined.
Homotopic leafwise paths with fixed endpoints have the same holonomy, so each arrow is a union of leafwise homotopy classes of paths.
The holonomy groupoid has a natural structure of a [[Lie groupoid|HNVW0E732J]] of dimension $2n - q$, whose manifold of arrows need not be Hausdorff.
Its source fibre over $x$ is the holonomy cover of the leaf through $x$.

Example: foliate $\R^2$ by the horizontal lines $y = c$.
All holonomy germs are identities, so there is one arrow from $(a, c)$ to $(b, c)$ for all $a, b, c$, and no arrow between points with different second coordinates.
The holonomy groupoid is the equivalence relation $\set{((b, c), (a, c))}$, a manifold of dimension $3 = 2 \cdot 2 - 1$.

Non-example: the monodromy groupoid, whose arrows are leafwise homotopy classes of leafwise paths, is in general different.
For the foliation of $S^1 \times \R$ by the circles $S^1 \times \set{c}$, a loop going once around a circle has trivial holonomy but is not null-homotopic in its leaf.
So it gives the identity arrow of the holonomy groupoid but a nontrivial arrow of the monodromy groupoid.
In the [[Reeb foliation|W58NYR1DGR]], the compact leaf has nontrivial holonomy, so some loops in it give nontrivial arrows in both.

## Explanations

### L1 human

The holonomy groupoid records all ways of walking from one point to another inside a leaf, counting two walks as equal when they drag nearby leaves in the same way.
