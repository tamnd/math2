---
tag: 11FFYBNF0E
kind: statement
role: proposition
name: Homotopy lifting for covering maps
msc: [57M10, 55R05]
uses: [3XZRRE165N, 9YA6S6HD9V, 0CQHFPGJ45, S1XK3HXHFX]
about: [3XZRRE165N]
sources:
  - url: https://en.wikipedia.org/wiki/Covering_space
---

## Statement

Let $p \colon E \to B$ be a [[covering map|3XZRRE165N]], and let $X$ be a [[topological space|0CQHFPGJ45]].
Let $H \colon X \times [0, 1] \to B$ be a [[homotopy|9YA6S6HD9V]], and let $\tilde f \colon X \to E$ be a continuous map with $p \circ \tilde f = H(\cdot, 0)$.
Then there is a unique homotopy $\tilde H \colon X \times [0, 1] \to E$ such that $p \circ \tilde H = H$ and $\tilde H(\cdot, 0) = \tilde f$.

## Remarks

For each $x \in X$, cover $\{x\} \times [0, 1]$ by sets of the form $N \times [t_i, t_{i+1}]$ that $H$ maps into evenly covered open sets of $B$.
On each such piece the lift is forced: it is the composite with the inverse of $p$ on the sheet that contains the lift already built.
Uniqueness of lifts on the connected sets $\{x\} \times [0, 1]$ makes these local lifts agree, so they glue to a continuous $\tilde H$.
When $X$ is a point, the statement is the path lifting property: each path in $B$ lifts uniquely once the start point of the lift is chosen.
Applied to $X = [0, 1]$ and a homotopy of loops rel endpoints, it shows that $p_* \colon \pi_1(E, e_0) \to \pi_1(B, p(e_0))$ is injective, where $\pi_1$ is the [[fundamental group|S1XK3HXHFX]].
For example, take $p \colon \R \to S^1$, $p(t) = (\cos 2\pi t, \sin 2\pi t)$, and a loop at $(1, 0)$ whose lift runs from $0$ to $n \ne 0$.
This loop is not null-homotopic, because a null-homotopy would lift to a homotopy rel endpoints in $\R$.

## Explanations

### L1 human

A covering map looks locally like several stacked copies of the base.
If a movie of maps into the base is given, and the first frame is already lifted to the cover, then the whole movie lifts, and in only one way.
The picture is a helix over a circle: a motion on the circle can be followed upstairs on the helix without any choice once the starting level is fixed.

### L2 human

This property is the engine of covering space theory.
It gives the injectivity of $p_*$ on fundamental groups, the computation $\pi_1(S^1) \cong \Z$, and the lifting criterion behind the classification of covering spaces.
It also says that a covering map is a fibration with discrete fibers, so the long exact sequence of homotopy groups applies and gives $\pi_n(E) \cong \pi_n(B)$ for $n \ge 2$.
