---
tag: TA8NQQCQCF
kind: definition
name: Hölder summation
msc: ["40G05"]
defines: M5YRA6CK4G
uses: [8X25Q4XYMN, 0NB643K60Q, 0P0DJHBGBB]
sources:
  - url: https://en.wikipedia.org/wiki/Hölder_summation
---

## Definition

Let $\sum_{n \ge 0} a_n$ be a series of complex numbers with [[partial sums|0NB643K60Q]] $s_n = a_0 + \cdots + a_n$.
Put $H^0_n = s_n$, and for each integer $k \ge 1$ let $H^k_n$ be the [[Cesàro mean|0P0DJHBGBB]] of the sequence $(H^{k-1}_n)$:
$$H^k_n = \frac{H^{k-1}_0 + H^{k-1}_1 + \cdots + H^{k-1}_n}{n + 1}.$$
The series is *Hölder summable of order $k$*, or $(H, k)$ summable, to $s$ if $H^k_n \to s$ as $n \to \infty$.

## Remarks

The method $(H, 0)$ is ordinary convergence, and $(H, 1)$ is Cesàro summation of order $1$.

Example: for $1 - 2 + 3 - 4 + \cdots$ the partial sums are $1, -1, 2, -2, 3, \dots$.
Then $H^1_{2m} = \frac{m+1}{2m+1}$ and $H^1_{2m+1} = 0$.
So $H^1_n$ is the sequence $\frac12, 0, \frac12, 0, \dots$ up to terms that tend to $0$, and its averages $H^2_n$ tend to $\frac14$.
The series is $(H, 2)$ summable to $1/4$.

Non-example: the same series is not $(H, 1)$ summable, since $H^1_n$ has the two limit points $1/2$ and $0$.

By a theorem of Knopp and Schur, for each $k$ a series is $(H, k)$ summable to $s$ if and only if it is Cesàro $(C, k)$ summable to $s$.
