---
tag: YQB7ZC31GW
kind: definition
name: Shamir's secret sharing
msc: [94A62, 11T71]
defines: CE49J8T213
uses: [RF8K6DV805, 0ZXZ82FTX2, 0SDC934R52, 237KR6FRCK]
sources:
  - url: https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing
---

## Definition

Let $\F$ be a [[finite field|0ZXZ82FTX2]], let $1 \le t \le n$ be integers with $n < \abs{\F}$, and let $x_1, \dots, x_n$ be distinct nonzero elements of $\F$, made public.
*Shamir's secret sharing* with threshold $t$ is the following $(t, n)$ [[secret sharing|RF8K6DV805]] scheme with secrets in $\F$.

1. Dealing: to share $s \in \F$, choose $a_1, \dots, a_{t-1}$ uniformly and independently in $\F$, and let $f(x) = s + a_1 x + \cdots + a_{t-1} x^{t-1}$ in the [[polynomial ring|0SDC934R52]] $\F[x]$.
2. Shares: participant $i$ receives $y_i = f(x_i)$.
3. Reconstruction: from the shares of a set $A$ with $\abs{A} = t$, compute $s = f(0)$ by [[Lagrange interpolation|237KR6FRCK]]:
$$s = \sum_{i \in A} y_i \prod_{j \in A,\ j \ne i} \frac{x_j}{x_j - x_i}.$$

## Remarks

Correctness holds, since a polynomial of degree less than $t$ is determined by its values at $t$ distinct points.
Privacy holds, since for $t - 1$ shares and any candidate secret $s'$ there is exactly one polynomial of degree less than $t$ with $f(0) = s'$ through those points.

Example: $\F = \F_7$, $t = 2$, $n = 3$, $x_i = i$, secret $s = 3$ and $a_1 = 2$, so $f(x) = 3 + 2x$.
The shares are $y_1 = 5$, $y_2 = 0$, $y_3 = 2$.
From the first two: $s = 5 \cdot \frac{2}{2 - 1} + 0 = 10 \equiv 3 \pmod 7$, as it should be.

Non-example: if some $x_i = 0$ were allowed, participant $i$ would receive $f(0) = s$, so privacy fails for $t \ge 2$.
