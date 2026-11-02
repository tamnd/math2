---
tag: EBD8TWFNS0
kind: concept
name: Wolff potential
msc: [31C45, 31B15]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Summary

The Wolff potential of a measure is a nonlinear potential that measures how much mass the measure puts near a point at all scales.
At each scale a power $1/(p - 1)$ is applied before the scales are summed.
For $p = 2$ it reduces to a [[Riesz potential|1V2N8MFSHC]], up to a constant factor.
Hedberg and Wolff showed that it controls the energy of measures in nonlinear [[capacity|4YZVFGJVSZ]] theory.
Kilpeläinen and Malý showed that it gives pointwise bounds for $p$-superharmonic functions in terms of their Riesz measure, a basic tool of [[nonlinear potential theory|M923VKQVZM]].

## Explanations

### L1 human

A potential adds up the influence of a mass distribution on a point.
The Wolff potential looks at balls of every radius around the point and asks how much mass each ball holds, compared with what its size allows.
Each of these ratios is raised to the power $1/(p - 1)$ and the results are summed over all scales.
For a single point mass at the origin, the Wolff potential at $x$ is a negative power of $\abs{x}$, like the fundamental solution of the $p$-Laplace equation.
