---
tag: 08W2CW8PKW
kind: definition
name: Median
msc: ["60E05"]
defines: 07Y2E7P9NP
uses: [0DKRR22AEQ, 0MXMS3AE13]
sources:
  - url: https://en.wikipedia.org/wiki/Median
    locator: Probability distributions
---

## Definition

Let $X$ be a real random variable on a probability space $(\Omega, \mathcal{F}, P)$.
A median of $X$ is a real number $m$ with
$$P(X \le m) \ge \frac{1}{2} \quad \text{and} \quad P(X \ge m) \ge \frac{1}{2}.$$

## Remarks

Each real random variable has a median, and the medians form a closed bounded interval. For example, $Q(1/2)$ is a median, where $Q$ is the [[quantile function|0B3Q3XDM5X]].
The median can be different from the mean. For the exponential distribution with rate $\lambda$, the median is $\ln 2 / \lambda$ and the mean is $1/\lambda$.
For a fair coin coded as $0$ and $1$, each $m \in [0, 1]$ is a median.
For a sorted data set $x_1 \le \dots \le x_n$ with $n$ odd, the median is $x_{(n+1)/2}$. For $n$ even, one usually takes the mean of the two middle values.

## Explanations

### L1 human

The median is the middle value: half of the chance lies on each side of it.
The median of the incomes in a country is often more useful than the mean.
A few very large incomes do not move the median much.
