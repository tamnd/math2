---
tag: 6VC9JQD45M
kind: definition
name: Cesàro summation
msc: ["40G05"]
defines: N8ZGG7EW6J
uses: [8X25Q4XYMN, 0NB643K60Q, 0P0DJHBGBB]
sources:
  - url: https://en.wikipedia.org/wiki/Cesàro_summation
---

## Definition

Let $\sum_{n \ge 0} a_n$ be a series of complex numbers with [[partial sums|0NB643K60Q]] $s_n = a_0 + \cdots + a_n$.

1. The series is *Cesàro summable* to $s$, or $(C, 1)$ summable to $s$, if the [[Cesàro means|0P0DJHBGBB]] of the partial sums converge to $s$:
$$\sigma_n = \frac{s_0 + s_1 + \cdots + s_n}{n + 1} \to s \quad (n \to \infty).$$
2. More generally, let $\alpha > -1$ be real, and put $A^{\alpha}_0 = 1$ and $A^{\alpha}_m = \frac{(\alpha + 1)(\alpha + 2) \cdots (\alpha + m)}{m!}$ for $m \ge 1$.
The series is $(C, \alpha)$ summable to $s$ if
$$\sigma^{\alpha}_n = \frac{1}{A^{\alpha}_n} \sum_{k=0}^{n} A^{\alpha}_{n-k} a_k \to s \quad (n \to \infty).$$

## Remarks

For $\alpha = 0$ one has $\sigma^0_n = s_n$, which is ordinary convergence.
For $\alpha = 1$ one has $A^1_m = m + 1$, and $\sigma^1_n = \frac{1}{n+1} \sum_{k=0}^{n} (n - k + 1) a_k = \sigma_n$, so clause 2 extends clause 1.

Example: for $1 - 1 + 1 - \cdots$ the partial sums are $1, 0, 1, 0, \dots$.
So $\sigma_{2m} = \frac{m+1}{2m+1}$ and $\sigma_{2m+1} = \frac{1}{2}$, and both tend to $1/2$.
The series is $(C, 1)$ summable to $1/2$.

Non-example: for $1 - 2 + 3 - 4 + \cdots$ the partial sums are $1, -1, 2, -2, 3, \dots$.
Their sums are $1, 0, 2, 0, 3, 0, \dots$, so $\sigma_{2m} = \frac{m+1}{2m+1} \to \frac12$ and $\sigma_{2m+1} = 0$.
The means oscillate, so the series is not $(C, 1)$ summable.
It is $(C, 2)$ summable to $1/4$.

If a series is $(C, \alpha)$ summable to $s$, it is $(C, \beta)$ summable to $s$ for every $\beta > \alpha$.
