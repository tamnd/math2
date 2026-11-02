---
tag: PF4RHTZWXH
kind: definition
name: Complete statistic
msc: [62B05]
defines: DED6JFAV1K
uses: [JZ6R7J36K5, 036756NFD6, 0DCT0QZVQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_(statistics)
    locator: Definition
---

## Definition

Let $\set{P_\theta : \theta \in \Theta}$ be a [[statistical model|JZ6R7J36K5]] and let $T = T(X)$ be a [[statistic|036756NFD6]] with values in a measurable space $\mathcal{T}$.
The statistic $T$ is *complete* if the following holds for every measurable $g \colon \mathcal{T} \to \R$ such that $g(T)$ is integrable under every $P_\theta$.
The condition
$$E_\theta[g(T)] = 0 \quad \text{for all } \theta \in \Theta$$
implies $P_\theta(g(T) = 0) = 1$ for all $\theta \in \Theta$.
Here $E_\theta$ is the [[expected value|0DCT0QZVQ1]] under $P_\theta$.
The statistic is *boundedly complete* if this implication holds for every bounded measurable $g$.

## Remarks

Every complete statistic is boundedly complete.
Example: let $T$ have the binomial law with parameters $n$ and $p \in (0, 1)$.
If $E_p[g(T)] = (1 - p)^n \sum_{t=0}^{n} g(t)\binom{n}{t} r^t = 0$ with $r = p/(1 - p)$ for all $p$, the polynomial in $r$ vanishes on $(0, \infty)$, so each $g(t) = 0$; thus $T$ is complete.
Non-example: let $X_1, X_2$ be i.i.d. $\mathcal{N}(\theta, 1)$ and $T = (X_1, X_2)$.
The function $g(T) = X_1 - X_2$ has $E_\theta[g(T)] = 0$ for all $\theta$, but $g(T) \ne 0$ with probability $1$; so $T$ is not complete.
Completeness is a property of the family of laws $\set{P_\theta \circ T^{-1} : \theta \in \Theta}$; enlarging $\Theta$ can only help it.
