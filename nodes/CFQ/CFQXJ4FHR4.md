---
tag: CFQXJ4FHR4
kind: definition
name: Finite-dimensional distributions
msc: [60G05, 60G07]
defines: Y0CN7V3B7E
uses: [0QH5ENKZM1, 0NFPJVJJHX, 01EQPZ6RYZ, 0SV8K0TDGY]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-dimensional_distribution
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0NFPJVJJHX]], and let $(S, \mathcal{S})$ be a measurable space.
Let $X = (X_t)_{t \in T}$ be a [[stochastic process|0QH5ENKZM1]] with values in $S$, indexed by a set $T$.
Let $\mathcal{S}^{\otimes k}$ be the product [[sigma-algebra|0SV8K0TDGY]] on $S^k$.
For $k \ge 1$ and distinct $t_1, \dots, t_k \in T$, the *finite-dimensional distribution* of $X$ at $(t_1, \dots, t_k)$ is the measure $\mu_{t_1, \dots, t_k}$ on $(S^k, \mathcal{S}^{\otimes k})$ given by
$$\mu_{t_1, \dots, t_k}(B) = P\bigl((X_{t_1}, \dots, X_{t_k}) \in B\bigr) \quad \text{for } B \in \mathcal{S}^{\otimes k}.$$
So $\mu_{t_1, \dots, t_k}$ is the [[law|01EQPZ6RYZ]] of the random vector $(X_{t_1}, \dots, X_{t_k})$.
The *finite-dimensional distributions* of $X$ are the family of all these measures.

## Remarks

The family is consistent.
Permuting the times permutes the coordinates of the measure, and $\mu_{t_1, \dots, t_k}(B \times S) = \mu_{t_1, \dots, t_{k-1}}(B)$.
Conversely, for $S$ a Polish space, the Kolmogorov extension theorem gives a process with any prescribed consistent family.

Example: for the standard [[Wiener process|22735FGJV6]] $W$ on $T = [0, \infty)$, the law of $(W_{t_1}, \dots, W_{t_k})$ is the [[multivariate normal distribution|0XN3K7RSZY]] with mean $0$ and covariance matrix $(\min(t_i, t_j))_{i, j}$.

Two processes with the same finite-dimensional distributions can have different paths.
Let $U$ be uniform on $[0, 1]$, let $X_t = 0$ and let $Y_t = \mathbf{1}_{\set{t = U}}$ for $t \in [0, 1]$.
For any fixed times, $P(Y_{t_i} = 0 \text{ for all } i) = 1$, so $X$ and $Y$ have the same finite-dimensional distributions.
But every path of $X$ is continuous, and no path of $Y$ is continuous.
