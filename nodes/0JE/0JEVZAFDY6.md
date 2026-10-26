---
tag: 0JEVZAFDY6
kind: statement
role: theorem
name: The cumulative distribution function determines the distribution
msc: ["60E05"]
uses: [0MXMS3AE13, 0QB913WM5E, 0BVHZXWKCD]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulative_distribution_function
    locator: Properties
---

## Statement

Let $\mu$ and $\nu$ be [[probability distributions|0QB913WM5E]] on $\mathbb{R}$ with its Borel σ-algebra.
If $\mu((-\infty, x]) = \nu((-\infty, x])$ for each $x \in \mathbb{R}$, then $\mu(B) = \nu(B)$ for each Borel set $B \subseteq \mathbb{R}$.

## Remarks

In other words, two real random variables with the same [[cumulative distribution function|0MXMS3AE13]] are identically distributed.
The half-lines $(-\infty, x]$ are closed under finite intersections and generate the [[Borel σ-algebra|0BVHZXWKCD]]. The proof uses Dynkin's π-λ theorem to pass from these half-lines to all Borel sets.
So to describe a real distribution, it is enough to give its cumulative distribution function.

## Explanations

### L1 human

If you know $P(X \le x)$ for every $x$, then you know the probability of every reasonable event about $X$.
For example, $P(a < X \le b)$ is a difference of two values of the function, and more complex sets come from such intervals.
