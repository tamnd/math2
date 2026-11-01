---
tag: ETRF2FHAEE
kind: object
name: Gromov–Hausdorff space
msc: [53C23, "54E35"]
sources:
  - url: https://en.wikipedia.org/wiki/Gromov%E2%80%93Hausdorff_convergence
---

## Description

Let $Z$ be a [[metric space|0VKD1TP7F3]] and let $A, B \subseteq Z$ be nonempty.
The *Hausdorff distance* $d_H(A, B)$ is the infimum of the numbers $r \ge 0$ with the following property.
Each point of $A$ lies within distance $r$ of $B$, and each point of $B$ lies within distance $r$ of $A$.

Let $X$ and $Y$ be nonempty [[compact|0TVJZYB6SH]] metric spaces.
Their *Gromov–Hausdorff distance* is
$$d_{GH}(X, Y) = \inf d_H(f(X), g(Y)),$$
where the infimum runs over all metric spaces $Z$ and all [[isometric embeddings|02HPP5VCZH]] $f \colon X \to Z$ and $g \colon Y \to Z$.

The *Gromov–Hausdorff space* is the set of isometry classes of nonempty compact metric spaces, with the distance $d_{GH}$.

## Remarks

The function $d_{GH}$ is a metric on isometry classes.
In particular, $d_{GH}(X, Y) = 0$ for compact $X$ and $Y$ only when $X$ and $Y$ are isometric.
The Gromov–Hausdorff space is a [[complete metric space|0BY52JW6NK]] and is [[separable|0Z2P41SVDP]].
Finite metric spaces with rational distances form a countable dense subset.

For a one-point space $P$ and a compact metric space $X$, one has $d_{GH}(P, X) = \operatorname{diam}(X) / 2$.

## Explanations

### L1 human

The Gromov–Hausdorff space is a space whose points are themselves shapes, namely compact metric spaces.
Two shapes are close when they can be placed in a common space so that each is near the other.
For example, a fine finite grid of points is close to the square it sits in.
This lets one speak of a sequence of spaces converging to a limit space.
