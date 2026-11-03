---
tag: 3FRKDK0FGA
kind: definition
name: World line
msc: [83A05, 53B30]
defines: Z788G6MJ9E
uses: [G49G4R1K04, JZ9ADDZX8D, 0G7WM8DX4P, 0ZCZK72B45]
sources:
  - url: https://en.wikipedia.org/wiki/World_line
---

## Definition

Let $M$ be [[Minkowski space|G49G4R1K04]] with metric $\eta$ of signature $(-, +, +, +)$ and inertial coordinates $(x^0, x^1, x^2, x^3)$, $x^0 = ct$.
Let $I \subseteq \R$ be an interval.
A *timelike world line* is the image of a smooth [[parametrised curve|0G7WM8DX4P]] $\sigma \colon I \to M$ such that, for every $s \in I$, the [[tangent vector|0ZCZK72B45]] $\sigma'(s)$ satisfies:

1. $\eta(\sigma'(s), \sigma'(s)) < 0$, that is, $\sigma'(s)$ is timelike;
2. $(\sigma^0)'(s) > 0$, that is, $\sigma'(s)$ points to the future.

A *null world line* is defined in the same way with $\eta(\sigma'(s), \sigma'(s)) = 0$ and $\sigma'(s) \ne 0$ in clause 1.
The world line of a massive point particle is a timelike world line.
The world line of a light pulse in vacuum is a null straight line.

## Remarks

Example: $\sigma(t) = (ct, vt, 0, 0)$ with $\abs{v} < c$ is a timelike world line.
Check: $\eta(\sigma', \sigma') = -c^2 + v^2 < 0$ and $(\sigma^0)' = c > 0$.
Non-example: $\sigma(t) = (ct, 2ct, 0, 0)$ fails clause 1, since $\eta(\sigma', \sigma') = -c^2 + 4c^2 > 0$; it would describe motion faster than light.
Clause 1 says that the tangent lies inside the [[light cone|JZ9ADDZX8D]], and clause 2 that it lies inside the future half.
A timelike world line can always be parametrised by the time coordinate $t$, as $t \mapsto (ct, \mathbf{x}(t))$ with $\abs{d\mathbf{x}/dt} < c$.
The definition depends only on the image and on its future orientation, not on the chosen parametrisation.
