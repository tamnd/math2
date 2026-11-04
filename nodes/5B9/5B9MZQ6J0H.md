---
tag: 5B9MZQ6J0H
kind: proof
name: Proof of the sum of a finite geometric progression by telescoping
msc: [05A19]
proves: 03X8V7D64M
uses: [0FGENPMPJX]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_series
    locator: Proof of convergence
---

## Proof

We multiply the sum by $x$ and subtract.
We compute in the field $\mathbb{R}$, see [[the reals form a field|0FGENPMPJX]].
Let $x \neq 1$ be real, let $n$ be a natural number, and let $s = \sum_{k=0}^{n-1} x^k$.

1. If $n = 0$, the sum is empty, so $s = 0$. Also $\frac{x^0 - 1}{x - 1} = \frac{0}{x - 1} = 0$. So the formula holds.
2. Now let $n \ge 1$. By distributivity, $x s = \sum_{k=0}^{n-1} x^{k+1} = \sum_{k=1}^{n} x^k$.
3. We write $s = 1 + \sum_{k=1}^{n-1} x^k$ and $x s = \sum_{k=1}^{n-1} x^k + x^n$.
4. Subtracting the first equation of step 3 from the second, the common sum $\sum_{k=1}^{n-1} x^k$ cancels. So $x s - s = x^n - 1$.
5. By distributivity, $x s - s = (x - 1) s$. So $(x - 1) s = x^n - 1$.
6. Since $x \neq 1$, the number $x - 1$ is not $0$, so it has an inverse in the field $\mathbb{R}$.
7. Multiplying step 5 by $(x - 1)^{-1}$ gives $s = \frac{x^n - 1}{x - 1}$.

## Idea

Multiplying by $x$ shifts every power up by one.
The shifted sum and the original sum share all terms except $1$ and $x^n$, so their difference is $x^n - 1$.
