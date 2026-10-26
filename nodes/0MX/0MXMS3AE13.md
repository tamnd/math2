---
tag: 0MXMS3AE13
kind: definition
name: Cumulative distribution function
msc: ["60E05"]
defines: 0H8H7ZTHW2
uses: [0DKRR22AEQ, 0QB913WM5E]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulative_distribution_function
    locator: Definition
---

## Definition

Let $X$ be a real [[random variable|0DKRR22AEQ]] on a probability space $(\Omega, \mathcal{F}, P)$.
The cumulative distribution function of $X$ is the function $F_X \colon \mathbb{R} \to [0, 1]$ with
$$F_X(x) = P(X \le x) \quad \text{for } x \in \mathbb{R}.$$
More generally, the cumulative distribution function of a [[probability distribution|0QB913WM5E]] $\mu$ on $\mathbb{R}$ is $F(x) = \mu((-\infty, x])$.

## Remarks

For $a < b$, $P(a < X \le b) = F_X(b) - F_X(a)$.
$F_X$ is nondecreasing and right-continuous, with limit $0$ at $-\infty$ and limit $1$ at $+\infty$. Conversely, each function with these properties is the cumulative distribution function of some distribution.
The jump of $F_X$ at $x$ is $P(X = x) = F_X(x) - \lim_{t \to x^-} F_X(t)$.
For a fair die, $F_X(x) = \lfloor x \rfloor / 6$ for $0 \le x < 6$, $F_X(x) = 0$ for $x < 1$, and $F_X(x) = 1$ for $x \ge 6$.

## Explanations

### L1 human

The cumulative distribution function adds up the probability from the left up to the point $x$.
Its graph starts at height $0$ on the far left, never goes down, and reaches height $1$ on the far right.
