---
tag: 0PVCTCKD3C
kind: statement
role: proposition
name: Expectation with respect to the binomial distribution
aliases: [mean-of-binomial-distribution]
msc: ["60E05"]
uses: [0VRWZDWW6B, 0DCT0QZVQ1, 0P7PTC8DDE, 0J97P5KZY0]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_distribution
    locator: Expected value and variance
---

## Statement

Let $n \ge 1$ be an integer, let $p \in [0, 1]$, and let $X$ have the [[binomial distribution|0VRWZDWW6B]] $\operatorname{Bin}(n, p)$. Then
$$E[X] = \sum_{k=0}^{n} k \binom{n}{k} p^k (1 - p)^{n - k} = np.$$

## Remarks

A short proof: $X$ has the same law as $Y_1 + \dots + Y_n$ with independent [[Bernoulli|0J97P5KZY0]] $Y_i$ with $E[Y_i] = p$. Then [[linearity of expectation|0P7PTC8DDE]] gives $np$.
A direct proof uses $k \binom{n}{k} = n \binom{n-1}{k-1}$ and the binomial theorem.
The variance of $X$ is $np(1 - p)$.

## Explanations

### L1 human

In $n$ trials with success probability $p$, you expect $np$ successes.
For $100$ tosses of a fair coin, the expected number of heads is $50$.
