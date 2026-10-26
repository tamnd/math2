---
tag: 0K9GBTZ1FX
kind: definition
name: Parallelepiped
msc: [51M20]
defines: 0SQV2VJTGY
uses: [0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Parallelepiped
    locator: Volume
---

## Definition

Let $p$ be a point of $\mathbb{R}^3$, and let $a$, $b$ and $c$ be linearly independent [[vectors|0QN3D80AWP]] in $\mathbb{R}^3$.
The parallelepiped with the vertex $p$ and the edges $a$, $b$ and $c$ is the set
$$\{\, p + s a + t b + u c \;:\; s, t, u \in [0, 1] \,\}.$$

## Remarks

The parallelepiped has 8 vertices $p + s a + t b + u c$ with $s, t, u \in \{0, 1\}$, 12 edges and 6 faces. Opposite faces are congruent parallelograms in parallel planes.
Its volume is the absolute value of the [[scalar triple product|059Q2XWJDC]] $a \cdot (b \times c)$.
In Mathlib, the parallelepiped of a finite family of vectors $v_i$ is the set of the sums $\sum_i t_i v_i$ with each $t_i \in [0, 1]$. It does not ask for linear independence.
A cube and a rectangular cuboid are special parallelepipeds.

## Explanations

### L1 human

Take a cube and push it sideways so that its faces lean, but stay flat. The result is a parallelepiped. Each face is a parallelogram, and opposite faces are copies of each other.
