---
tag: 0KNJWEVSMG
kind: example
name: p-norm on R^n
aliases: [lp-norm-on-rn]
msc: [46B20]
instance_of: [06GZ956657]
uses: [0TFDZN6AXP, 0ABP2F2ZP7]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
    locator: The p-norm in finite dimensions
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: p-norm
---

## Example

Let $n \ge 1$ be an integer and let $p \ge 1$ be a real number.
For $x = (x_1, \ldots, x_n) \in \mathbb{R}^n$, let
$$\|x\|_p = \left( \sum_{i=1}^{n} |x_i|^p \right)^{1/p}, \qquad \|x\|_\infty = \max_{1 \le i \le n} |x_i|.$$
Then $\|\cdot\|_p$ and $\|\cdot\|_\infty$ are norms on $\mathbb{R}^n$.
They are $0$ only at $x = 0$, they satisfy $\|\lambda x\| = |\lambda| \, \|x\|$ for real $\lambda$, and they satisfy the triangle inequality $\|x + y\| \le \|x\| + \|y\|$.

## Remarks

The triangle inequality for $\|\cdot\|_p$ is the Minkowski inequality.
The metric $\|x - y\|_p$ is the [[p-metric|0TFDZN6AXP]]. For $p = 2$, the norm is the Euclidean norm.
For each $x$, $\|x\|_p \to \|x\|_\infty$ as $p \to \infty$.
All these norms are [[equivalent|03MC70ZRNR]], and $\mathbb{R}^n$ is a [[Banach space|0BDTTM24DP]] with each of them.

## Explanations

### L1 human

The p-norms give different ways to measure the length of a vector from its coordinates.
For $p = 1$, you add the absolute values. For $p = 2$, you get the usual length. For $p = \infty$, you take the largest coordinate.
