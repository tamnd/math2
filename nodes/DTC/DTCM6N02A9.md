---
tag: DTCM6N02A9
kind: example
name: A translation of the plane is not linear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: school
not_instance_of:
  - target: 0NRYHJPQG2
    note: the translation by (1, 0) sends (0, 0) to (1, 0), so it fails additivity and homogeneity
uses: [0RJF668P1T, 087VJM5Q77]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Translation_(geometry)
    locator: lead section
---

## Example

A translation slides the whole plane, origin included, and a linear map can never move the origin.
Let $t \colon \R^2 \to \R^2$ be the [[translation|087VJM5Q77]] by the vector $(1, 0)$, so $t(x, y) = (x + 1, \; y)$.
We test the image of $0$ and the two conditions of a [[linear map|0RJF668P1T]].

1. Zero: $t(0, 0) = (1, 0) \ne (0, 0)$, while a linear map sends $0$ to $0$ by the [[lemma on zero|STYEWH8R4E]].
2. Additivity: take $u = v = (0, 0)$; then $t(u + v) = (1, 0)$, but $t(u) + t(v) = (1, 0) + (1, 0) = (2, 0)$.
3. Homogeneity: take $a = 2$ and $v = (1, 1)$; then $t(2v) = t(2, 2) = (3, 2)$, but $2\,t(v) = 2\,(2, 1) = (4, 2)$.

Each test fails, so $t$ is not a linear map.

## Remarks

The same argument works for the translation by any vector $w_0$, since $t(0) = w_0$.
So a translation is linear only when $w_0 = 0$, and then it is the identity.

A translation keeps lengths and angles, so it is an isometry of the plane, but it is an [[affine map|0JF0TVYGWT]] and not a linear map.
Every affine map of $\R^n$ is a linear map followed by a translation, $x \mapsto Ax + b$.
This is also why the school "linear function" $y = 2x + 1$ is affine in linear algebra: its constant term $1$ plays the role of $b$.

## Explanations

### L1 human

Sliding every point of the plane one step to the right is a translation.
It moves the origin, and a linear map never moves the origin.
So a slide is not linear, even though it does not bend or stretch anything.

### L2 human

The quickest test for linearity is the image of $0$.
Here $t(0, 0) = (1, 0)$, so the test fails at once and no further work is needed.
Watch out for the other direction: a map that fixes $0$ can still fail to be linear, as the [[squaring map|RMC0D67M01]] shows.
