---
tag: TZ6Y9XXQJW
kind: definition
name: Gaussian binomial coefficient
msc: [05A30, 11B65, 05A10]
defines: YS09Z1YNEK
uses: [GFSDMJHHVA, 0GBZM0MT0F]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_binomial_coefficient
---

## Definition

Let $q$ be an indeterminate and let $n, k$ be integers with $n \ge 0$.
For $0 \le k \le n$, the *Gaussian binomial coefficient* is
$$\binom{n}{k}_q = \frac{(1 - q^n)(1 - q^{n-1}) \cdots (1 - q^{n-k+1})}{(1 - q)(1 - q^2) \cdots (1 - q^k)} = \frac{[n]_q!}{[k]_q!\, [n - k]_q!},$$
where $[m]_q!$ is the q-factorial of the [[q-analog|GFSDMJHHVA]] node.
For $k < 0$ or $k > n$, $\binom{n}{k}_q = 0$.

## Remarks

The coefficients satisfy the q-Pascal rule $\binom{n}{k}_q = \binom{n-1}{k-1}_q + q^k \binom{n-1}{k}_q$ for $n \ge 1$.
By induction, $\binom{n}{k}_q$ is a polynomial in $q$ with nonnegative integer coefficients, of degree $k(n - k)$.
At $q = 1$ it equals the [[binomial coefficient|0GBZM0MT0F]] $\binom{n}{k}$.
If $q$ is a prime power, it is the number of $k$-dimensional subspaces of $\F_q^n$.

Example: $\binom{4}{2}_q = \frac{(1 - q^4)(1 - q^3)}{(1 - q)(1 - q^2)} = (1 + q^2)(1 + q + q^2) = 1 + q + 2q^2 + q^3 + q^4$.
At $q = 2$ this is $35$.
Counting directly, $\F_2^4$ has $\frac{(2^4 - 1)(2^4 - 2)}{(2^2 - 1)(2^2 - 2)} = \frac{15 \cdot 14}{3 \cdot 2} = 35$ subspaces of dimension $2$.

Non-example: $q^{k(n-k)} \binom{n}{k}$ also equals $\binom{n}{k}$ at $q = 1$, but it is not the Gaussian binomial coefficient.
For $n = 4$, $k = 2$ and $q = 2$ it gives $96$, not $35$.

The coefficient of $q^j$ in $\binom{n}{k}_q$ is the number of integer partitions of $j$ with at most $k$ parts, each at most $n - k$.
Another common notation is $\left[ {n \atop k} \right]_q$.
