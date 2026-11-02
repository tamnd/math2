---
tag: MXNDW6AFGZ
kind: definition
name: Kendall rank correlation coefficient
msc: [62H20, 62G10]
defines: DYFY16SFHZ
uses: [0DKRR22AEQ]
sources:
  - url: https://en.wikipedia.org/wiki/Kendall_rank_correlation_coefficient
---

## Definition

Let $(x_1, y_1), \dots, (x_n, y_n)$ be $n \ge 2$ pairs of real numbers, with $x_1, \dots, x_n$ distinct and $y_1, \dots, y_n$ distinct.
A pair of indices $i < j$ is *concordant* if $(x_i - x_j)(y_i - y_j) > 0$ and *discordant* if $(x_i - x_j)(y_i - y_j) < 0$.
Let $C$ and $D$ be the numbers of concordant and discordant pairs.
The *Kendall rank correlation coefficient* is
$$\tau = \frac{C - D}{n(n-1)/2}.$$

## Remarks

Since every pair is concordant or discordant, $C + D = n(n-1)/2$ and $-1 \le \tau \le 1$.
For a pair $(X, Y)$ of [[random variables|0DKRR22AEQ]] with a continuous joint law and an independent copy $(X', Y')$, the population version is $P\big((X - X')(Y - Y') > 0\big) - P\big((X - X')(Y - Y') < 0\big)$.

Example: $x = (1, 2, 3)$ and $y = (1, 3, 2)$.
The pairs $(1, 2)$ and $(1, 3)$ are concordant, and the pair $(2, 3)$ is discordant because $(2 - 3)(3 - 2) < 0$.
So $\tau = (2 - 1)/3 = 1/3$.

Non-example: with ties, for example $y = (1, 1, 2)$, the pair $(1, 2)$ is neither concordant nor discordant, and the clause on distinct values fails.
Variants such as $\tau_b$ adjust the denominator for ties.

Under independence of $X$ and $Y$, the sample $\tau$ has mean $0$ and variance $2(2n + 5)/(9n(n-1))$, which gives a test of independence.
