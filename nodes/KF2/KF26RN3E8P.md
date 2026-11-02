---
tag: KF26RN3E8P
kind: definition
name: L-curve
msc: [65F22, 65J20]
defines: 5SE9H1SPBN
uses: [WTY54BFC46, M68V0M5A3R, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/L-curve
---

## Definition

Let $A \in \R^{m \times n}$, $b \in \R^m$ and $L \in \R^{p \times n}$ with $\ker A \cap \ker L = \set{0}$.
For $\lambda > 0$ let $x_\lambda$ be the unique minimizer of the [[Tikhonov|M68V0M5A3R]] functional
$$\norm{A x - b}_2^2 + \lambda^2 \norm{L x}_2^2.$$
The *L-curve* is the plane curve
$$\lambda \mapsto \bigl( \log \norm{A x_\lambda - b}_2, \ \log \norm{L x_\lambda}_2 \bigr), \qquad \lambda > 0,$$
defined where both norms are positive.
The *L-curve criterion* chooses $\lambda$ at the point of maximal curvature of this curve.

## Remarks

The residual norm $\norm{A x_\lambda - b}$ is non-decreasing in $\lambda$, and the seminorm $\norm{L x_\lambda}$ is non-increasing.
So the curve runs from upper left (small $\lambda$, noise-dominated) to lower right (large $\lambda$, over-smoothed).
Example: for $A = L = I$ and $b \ne 0$, one gets $x_\lambda = b/(1 + \lambda^2)$.
Then $\norm{A x_\lambda - b} = \lambda^2 \norm{b}/(1 + \lambda^2)$ and $\norm{x_\lambda} = \norm{b}/(1 + \lambda^2)$, so the first increases and the second decreases with $\lambda$, as stated.
Non-example: the curve $\lambda \mapsto (\lambda, \norm{A x_\lambda - b})$ is not the L-curve, since it plots the parameter itself instead of the solution seminorm.
Some authors use the squared norms or linear axes, but the corner is clearest on log-log axes.
The criterion is a heuristic: it is not a convergent [[regularization|WTY54BFC46]] parameter choice in the worst-case sense, yet it works well on many practical problems.

## Explanations

### L1 human

The L-curve shows the trade-off between fitting the data and keeping the solution tame, one point for each value of the regularization parameter.
Its corner marks a good compromise.
