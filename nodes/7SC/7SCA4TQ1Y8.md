---
tag: 7SCA4TQ1Y8
kind: definition
name: Homotopy equivalence
msc: [55P10]
defines: XZG6MTSWCN
uses: [F2F143KQ2M, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Homotopy
---

## Definition

Let $X$ and $Y$ be topological spaces.
A [[continuous map|0VGFHTM75Y]] $f \colon X \to Y$ is a *homotopy equivalence* if there is a continuous map $g \colon Y \to X$ with these two properties.
The map $g \circ f$ is [[homotopic|F2F143KQ2M]] to $\id_X$, and $f \circ g$ is homotopic to $\id_Y$.
Such a map $g$ is a *homotopy inverse* of $f$.

## Remarks

Every homeomorphism is a homotopy equivalence, with its inverse as homotopy inverse.
Example: let $i \colon S^1 \to \R^2 \setminus \set{0}$ be the inclusion and $r(x) = x / \norm{x}$.
Then $r \circ i = \id_{S^1}$, and $H(x, t) = (1 - t) x + t x / \norm{x}$ is a homotopy in $\R^2 \setminus \set{0}$ from $\id$ to $i \circ r$, so $i$ is a homotopy equivalence.
Non-example: the constant map $S^1 \to \set{p}$ is not a homotopy equivalence, since the [[fundamental group|S1XK3HXHFX]] of $S^1$ is $\Z$ and that of a point is trivial.
Composites of homotopy equivalences are homotopy equivalences.
