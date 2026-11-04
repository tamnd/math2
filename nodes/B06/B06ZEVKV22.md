---
tag: B06ZEVKV22
kind: proof
name: Proof that the exponential function is positive
msc: [33B10]
proves: 0P9BNBW2W3
uses: [0RMVS7RXZX, 0E8HNVBCSP]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
---

## Proof

We show that $\exp(x)$ is a square and is not zero.

1. Let $\exp$ be the [[exponential function|0RMVS7RXZX]]. At $0$, every term $\frac{0^n}{n!}$ with $n \ge 1$ is $0$, and the term with $n = 0$ is $1$. So $\exp(0) = 1$.
2. Let $x$ be real. By the [[exponential of a sum|0E8HNVBCSP]], $\exp(x) = \exp\left(\frac{x}{2} + \frac{x}{2}\right) = \exp\left(\frac{x}{2}\right)^2$. A square of a real number is nonnegative, so $\exp(x) \ge 0$.
3. By the exponential of a sum and step 1, $\exp(x) \exp(-x) = \exp(x + (-x)) = \exp(0) = 1$.
4. If $\exp(x) = 0$, the left side of step 3 would be $0$, not $1$. So $\exp(x) \ne 0$.
5. By steps 2 and 4, $\exp(x) > 0$ for every real $x$.

## Idea

The functional equation writes $\exp(x)$ as the square of $\exp(x/2)$, so it is never negative. It also gives $\exp(x) \exp(-x) = 1$, so it is never zero.
