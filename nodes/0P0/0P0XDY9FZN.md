---
tag: 0P0XDY9FZN
kind: statement
role: theorem
name: Classification of isometries of the plane
msc: [51F20]
uses: [0J1N3WTKM4, 087VJM5Q77, 0HFREYRSZP, 06BRDF3F0E, 0167F9B344]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Classification
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Recognition
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Isometries as reflection group
---

## Statement

Let $f$ be a [[Euclidean isometry|0J1N3WTKM4]] of the plane $\mathbb{R}^2$. Then $f$ is of exactly one of these five types:
- the identity,
- a [[translation|087VJM5Q77]] by a nonzero vector,
- a [[rotation|0HFREYRSZP]] about a point through an angle $\theta \notin 2\pi\mathbb{Z}$,
- a [[reflection|06BRDF3F0E]] in a line,
- a [[glide reflection|0167F9B344]] with a nonzero glide vector.

## Remarks

Write $f(x) = A x + b$ with $A$ orthogonal. If $\det A = 1$, then $f$ is the identity, a translation or a rotation. If $\det A = -1$, then $f$ is a reflection or a glide reflection.
The fixed points tell the types apart. A translation and a glide reflection have no fixed point. A rotation has one, and a reflection fixes a whole line.
Each isometry of the plane is the composite of at most three reflections in lines.

## Explanations

### L1 human

Each rigid motion of the plane is a shift, a turn, a mirror image, or a mirror image with a shift along the mirror. A turn and a shift keep the clockwise order of points. A mirror image and a glide reverse it.
