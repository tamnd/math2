---
tag: 0RJ5TZH6G0
kind: statement
role: proposition
name: Limit of the cumulative distribution function at infinity
msc: ["60E05"]
uses: [0MXMS3AE13, 0X8HBKCSYB]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulative_distribution_function
    locator: Properties
---

## Statement

Let $X$ be a real random variable with [[cumulative distribution function|0MXMS3AE13]] $F_X$.
Then
$$\lim_{x \to +\infty} F_X(x) = 1.$$

## Remarks

The proof: the events $\{X \le n\}$ increase with $n$ and their union is $\Omega$. So [[continuity from below|0X8HBKCSYB]] gives $F_X(n) \to 1$, and $F_X$ is nondecreasing.
In the same way, $\lim_{x \to -\infty} F_X(x) = 0$, because the events $\{X \le -n\}$ decrease to $\varnothing$.
The proof uses that $X$ takes only real values. For a random variable with values in $[-\infty, +\infty]$, the limit is $1 - P(X = +\infty)$.

## Explanations

### L1 human

For a very large $x$, it is almost sure that $X \le x$, because $X$ is some real number.
So the probability $F_X(x)$ gets as close to $1$ as we like.
