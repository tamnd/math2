---
tag: PYYXEXMARY
kind: definition
name: Hilbert space
msc: [46C05]
defines: HM2HHE3J51
uses: [0QVNCJXRY3, 0MFJJV97RJ, 0BY52JW6NK]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_space
---

## Definition

Let $H$ be an [[inner product space|0QVNCJXRY3]] over $\R$ or $\C$ with inner product $\ip{\cdot}{\cdot}$.
Let $\norm{x} = \sqrt{\ip{x}{x}}$ be the [[induced norm|0MFJJV97RJ]] and $d(x, y) = \norm{x - y}$ the induced metric.
The space $H$ is a *Hilbert space* if the metric space $(H, d)$ is [[complete|0BY52JW6NK]].

## Remarks

Example: $\ell^2$, the space of real sequences $x$ with $\sum_n x_n^2 < \infty$ and $\ip{x}{y} = \sum_n x_n y_n$.
The series converges by the Cauchy–Schwarz inequality.
It is complete: a Cauchy sequence converges in each coordinate, and the coordinatewise limit is in $\ell^2$ and is the limit in norm.

Non-example: $C([0, 1])$ with $\ip{f}{g} = \int_0^1 f g \, dx$ is an inner product space but not complete.
The continuous functions $f_k$ equal to $0$ on $[0, 1/2]$, to $1$ on $[1/2 + 1/k, 1]$ and linear in between form a Cauchy sequence.
Their only possible limit is the indicator function of $(1/2, 1]$, which is not continuous.

Every finite-dimensional inner product space is a Hilbert space.
An inner product space that is not complete is often called a pre-Hilbert space, and its completion is a Hilbert space.
