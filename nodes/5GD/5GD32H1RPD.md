---
tag: 5GD32H1RPD
kind: definition
name: Hypergeometric series
msc: ["33C05"]
defines: 428M453CR2
uses: [YZHM3HSM0F, 0MZB06ST2B, 0N288P2TB5]
sources:
  - url: https://en.wikipedia.org/wiki/Hypergeometric_function
---

## Definition

Let $a, b, c \in \C$ with $c \notin \set{0, -1, -2, \ldots}$.
For $x \in \C$ and an integer $n \ge 0$, let $(x)_n = x(x+1)\cdots(x+n-1)$ be the [[Pochhammer symbol|YZHM3HSM0F]], with $(x)_0 = 1$.
The *hypergeometric series* is the [[power series|0MZB06ST2B]]
$${}_2F_1(a, b; c; z) = \sum_{n=0}^{\infty} \frac{(a)_n (b)_n}{(c)_n} \, \frac{z^n}{n!}.$$

## Remarks

If $a$ or $b$ is a non-positive integer $-m$, then $(a)_n$ or $(b)_n$ vanishes for $n > m$ and the series is a polynomial of degree at most $m$.
Otherwise the ratio test gives [[radius of convergence|0N288P2TB5]] $1$.
On the circle $\abs{z} = 1$ the series converges absolutely when $\operatorname{Re}(c - a - b) > 0$.

Example: for $a = b = 1$, $c = 2$, the coefficient is $\frac{n! \, n!}{(n+1)! \, n!} = \frac{1}{n+1}$, so ${}_2F_1(1, 1; 2; z) = \sum_n \frac{z^n}{n+1} = -\frac{\log(1 - z)}{z}$ for $0 < \abs{z} < 1$.
Also ${}_2F_1(a, b; b; z) = \sum_n \frac{(a)_n}{n!} z^n = (1 - z)^{-a}$ by the binomial series.

Non-example: $c = 0$ is excluded, because $(0)_n = 0$ for every $n \ge 1$ and the coefficients are undefined.
For $c = -m$ a negative integer the series is still meaningful when $a = -k$ with $0 \le k \le m$ and the sum is cut at $n = k$, but this needs a separate convention.

The notation $F(a, b; c; z)$ is also common.
