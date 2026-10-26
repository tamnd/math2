---
tag: 0WF4EJP91W
kind: definition
name: Probability mass function
msc: ["60E05"]
defines: 0D6J4B671D
uses: [0J6Z6H5VQJ, 0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_mass_function
    locator: Formal definition
---

## Definition

Let $X$ be a [[discrete random variable|0J6Z6H5VQJ]] on a probability space $(\Omega, \mathcal{F}, P)$.
The probability mass function of $X$ is the function $p_X \colon \mathbb{R} \to [0, 1]$ with
$$p_X(x) = P(X = x) \quad \text{for } x \in \mathbb{R}.$$
More generally, a probability mass function on a countable set $S$ is a function $p \colon S \to [0, 1]$ with $\sum_{s \in S} p(s) = 1$.

## Remarks

The set $\{x : p_X(x) > 0\}$ is countable, and $\sum_x p_X(x) = 1$.
For each Borel set $B$, $P(X \in B) = \sum_{x \in B} p_X(x)$.
For a fair die, $p_X(k) = 1/6$ for $k = 1, \dots, 6$ and $p_X(x) = 0$ for other $x$.

## Explanations

### L1 human

The probability mass function is a table: each possible value with its probability.
The entries are never negative and they add up to $1$.
