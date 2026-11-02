---
tag: ADJZ99KY2Q
kind: definition
name: Fredholm index
msc: [47A53]
defines: 2V9Q4KHY1T
uses: [8HWGKWD6ZM, 0S23E6YE83, 0WSFKKT6FF, 0BR3FY5Q8M, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_operator
---

## Definition

Let $X$ and $Y$ be Banach spaces, and let $T \colon X \to Y$ be a [[Fredholm operator|8HWGKWD6ZM]].
The *index* of $T$ is the integer $\operatorname{ind} T = \dim \ker T - \dim \operatorname{coker} T$.
Here $\ker T$ is the [[kernel|0S23E6YE83]] of $T$.
The cokernel $\operatorname{coker} T = Y / T(X)$ is the [[quotient|0BR3FY5Q8M]] of $Y$ by the [[image|0WSFKKT6FF]] of $T$.

## Remarks

Example: the right shift $S$ on $\ell^2$ has $\ker S = \set{0}$ and $\operatorname{coker} S$ of dimension $1$, so $\operatorname{ind} S = -1$.
The left shift $S^*(x_1, x_2, \ldots) = (x_2, x_3, \ldots)$ is onto with a kernel of dimension $1$, so $\operatorname{ind} S^* = 1$.
Non-example: the diagonal operator $D(x_n) = (x_n / n)$ on $\ell^2$ is not Fredholm, so it has no index.
For a linear map $T \colon X \to Y$ between finite-dimensional spaces, the rank–nullity theorem gives $\operatorname{ind} T = \dim X - \dim Y$.
For Fredholm operators $T \colon X \to Y$ and $S \colon Y \to Z$, the product $ST$ is Fredholm and $\operatorname{ind}(ST) = \operatorname{ind} S + \operatorname{ind} T$.
If $K \colon X \to Y$ is a [[compact operator|M2NEP1K5AE]], then $T + K$ is Fredholm and $\operatorname{ind}(T + K) = \operatorname{ind} T$.
The Fredholm operators form an open subset of the bounded operators, and the index is constant on its connected components.
