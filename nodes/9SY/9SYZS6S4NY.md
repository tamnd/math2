---
tag: 9SYZS6S4NY
kind: definition
name: Response surface methodology
msc: [62K20]
defines: 42NZSQ65DQ
uses: [2TE42ZWJ3E, EHJ3R589ZX, 0BYTQ4X1HC, 0693Y2METT]
sources:
  - url: https://en.wikipedia.org/wiki/Response_surface_methodology
---

## Definition

Let $x = (x_1, \dots, x_k)$ be the settings of $k$ controllable factors in a region $R \subseteq \R^k$.
Assume that the observed response is $y = \eta(x) + \varepsilon$, where $\eta \colon R \to \R$ is an unknown smooth function and $\varepsilon$ is a random error with mean $0$.
*Response surface methodology* is the sequential strategy for locating an optimum of $\eta$ that repeats these steps:

1. Run an experiment, planned by the methods of [[design of experiments|2TE42ZWJ3E]], in a small neighbourhood of the current point.
2. While curvature is negligible, fit by [[least squares|0BYTQ4X1HC]] a first-order model $\hat y = b_0 + \sum_i b_i x_i$. Then move the current point along the path of steepest ascent, the direction $(b_1, \dots, b_k)$.
3. When the first-order model shows lack of fit, fit a second-order model $\hat y = b_0 + \sum_i b_i x_i + \sum_{i \le j} b_{ij} x_i x_j$, and locate and classify its stationary point.

## Remarks

Example: a fitted second-order model can be written $\hat y = b_0 + x^T b + x^T B x$ with a symmetric $k \times k$ matrix $B$.
When $B$ is invertible, its stationary point is $x_s = -\frac12 B^{-1} b$, since the gradient $b + 2 B x$ vanishes there.
The [[Hessian matrix|0693Y2METT]] of $\hat y$ is $2B$, so if all eigenvalues of $B$ are negative, $x_s$ is the maximum of the fitted surface.
This eigenvalue check is called canonical analysis.

Non-example: a single [[factorial experiment|EHJ3R589ZX]] analysed once, with no move to new settings, is not response surface methodology, because step 2 is missing.

Typical designs are two-level factorial designs with centre points for the first-order stage, and central composite designs or Box–Behnken designs for the second-order stage.
