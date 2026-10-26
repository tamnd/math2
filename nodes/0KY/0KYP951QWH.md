---
tag: 0KYP951QWH
kind: definition
name: Discrete uniform distribution
msc: ["60E05"]
defines: 02MY6WZXEQ
uses: [0WF4EJP91W, 0AKNPYQ04R, 0BBTH3YSZA]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_uniform_distribution
    locator: lead section
---

## Definition

Let $S$ be a nonempty [[finite set|0BBTH3YSZA]] with $n$ elements.
The discrete uniform distribution on $S$ is the distribution with the [[probability mass function|0WF4EJP91W]]
$$p(s) = \frac{1}{n} \quad \text{for } s \in S.$$
A random variable $X$ is uniform on $S$ if $P(X = s) = 1/n$ for each $s \in S$.

## Remarks

Then $P(X \in A) = |A| / n$ for each $A \subseteq S$. This is the [[classical definition of probability|0AKNPYQ04R]].
For $S = \{a, a + 1, \dots, b\}$ with integers $a \le b$ and $n = b - a + 1$, the mean is $(a + b)/2$ and the variance is $(n^2 - 1)/12$.
The result of a fair die is uniform on $\{1, \dots, 6\}$, with mean $7/2$.

## Explanations

### L1 human

The discrete uniform distribution is "all outcomes equally likely".
A fair die, a fair coin and a well-shuffled deck all give uniform distributions.
