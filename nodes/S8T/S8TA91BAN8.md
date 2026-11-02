---
tag: S8TA91BAN8
kind: definition
name: Foliation
msc: [57R30, 53C12]
defines: 98HTB7MSPX
uses: [F45VQ47GPV, WY6K3P4YCG]
sources:
  - url: https://en.wikipedia.org/wiki/Foliation
---

## Definition

Let $M$ be a smooth manifold of dimension $n$, and let $p, q \ge 0$ be integers with $p + q = n$.
A *foliation of dimension $p$* (and *codimension $q$*) of $M$ is a maximal atlas of charts $\varphi_i \colon U_i \to \R^p \times \R^q$ with the following property.
The transition maps have the local form
$$\varphi_j \circ \varphi_i^{-1}(x, y) = \bigl(g_{ij}(x, y), h_{ij}(y)\bigr), \qquad x \in \R^p, \ y \in \R^q.$$
In such a chart, the sets $\varphi_i^{-1}(\R^p \times \set{y}) \cap U_i$ are the *plaques*.
Call two points of $M$ equivalent when they can be joined by a finite chain of plaques, each meeting the next.
The *leaves* of the foliation are the equivalence classes of this relation.

## Remarks

Each leaf is a connected injectively immersed submanifold of dimension $p$, and the leaves partition $M$.
The tangent spaces of the leaves form a subbundle of the [[tangent bundle|WY6K3P4YCG]] that is involutive; by the [[Frobenius theorem|5Q4BHBFXJY]], foliations of dimension $p$ correspond to involutive rank $p$ subbundles.

Example: on the torus $\R^2 / \Z^2$, the lines of slope $\alpha$ give a foliation of dimension $1$.
The charts are restrictions of the linear map $(s, t) \mapsto (s + \alpha t, t - \alpha s)$ composed with local inverses of the quotient map, and transition maps are translations, which have the required form.
If $\alpha$ is irrational, each leaf is dense in the torus.

Non-example: on $\R^3$ with coordinates $(x, y, z)$, the plane field spanned by $\partial_x$ and $\partial_y + x \, \partial_z$ is not involutive, because the bracket of these two fields is $\partial_z$.
So it is not the tangent field of any foliation by surfaces.

## Explanations

### L1 human

A foliation is a way to slice a manifold into thin sheets of one fixed dimension.
In small pieces the slicing looks like the horizontal slices of a stack.
The charts must respect the slices: when you change chart, slices go to slices.
A leaf is what you get by following one slice as far as it goes.
