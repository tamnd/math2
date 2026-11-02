---
tag: Q5B5YGY7D6
kind: definition
name: Fredholm operator
msc: [47A53]
defines: 8HWGKWD6ZM
uses: [06GZ956657, 03TM135G0N, 0S23E6YE83, 0WSFKKT6FF, 0BR3FY5Q8M, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Definition

Let $X$ and $Y$ be [[Banach spaces|06GZ956657]], and let $T \colon X \to Y$ be a [[bounded linear map|03TM135G0N]].
The map $T$ is a *Fredholm operator* if both of the following hold.

1. The [[kernel|0S23E6YE83]] $\ker T$ is finite-dimensional.
2. The cokernel $\operatorname{coker} T = Y / T(X)$, the [[quotient|0BR3FY5Q8M]] of $Y$ by the [[image|0WSFKKT6FF]] of $T$, is finite-dimensional.

## Remarks

If $T$ is Fredholm, then its image $T(X)$ is automatically closed in $Y$.
Example: let $S$ be the right shift on $\ell^2$, $S(x_1, x_2, \ldots) = (0, x_1, x_2, \ldots)$.
Its kernel is $\set{0}$, and its image is $\set{x \in \ell^2 : x_1 = 0}$, of codimension $1$, so $S$ is Fredholm.
Non-example: the diagonal operator $D(x_n) = (x_n / n)$ on $\ell^2$ has kernel $\set{0}$.
Its image contains every finitely supported sequence, so it is dense, but it misses $(1/n)$, so it is not closed.
By the previous remark, the image of a bounded operator with finite-dimensional cokernel is closed, so clause 2 fails.
If $K \colon X \to X$ is a [[compact operator|M2NEP1K5AE]], then $I - K$ is Fredholm.
Every linear map between finite-dimensional spaces is Fredholm.
