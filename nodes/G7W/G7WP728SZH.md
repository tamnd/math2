---
tag: G7WP728SZH
kind: concept
name: Projection body
msc: [52A20, 52A21, 52A40]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_body
same_as:
  wikidata: Q7249443
  wikipedia: Projection body
---

## Summary

Let $K$ be a [[convex body|437FSG3419]] in $\R^n$.
Its projection body $\Pi K$ is a convex body given by its [[support function|1H92CYA4ZC]].
At a unit vector $u$, this function is the volume of the shadow of $K$ on the hyperplane orthogonal to $u$.
It packs all the shadows of $K$ into one convex body, which is always symmetric about the origin.
Projection bodies were introduced by Minkowski and are central in the study of affine isoperimetric inequalities.

## Explanations

### L1 human

Shine light on a solid from direction $u$ and measure the area of its shadow on a wall perpendicular to $u$.
The projection body is the convex shape whose width profile is given by these shadow areas.
A cube of side $1$ has shadow area $\abs{u_1} + \abs{u_2} + \abs{u_3}$ for a unit direction $u$, and its projection body is the cube $[-1, 1]^3$.
