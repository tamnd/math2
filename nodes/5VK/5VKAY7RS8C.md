---
tag: 5VKAY7RS8C
kind: definition
name: Kodaira dimension
msc: ["14E30", 14J10]
defines: ZW00Q0SAGR
uses: [HV6YBS0YDH, W05VYY4HBR, 36X2WTHYCB]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_dimension
---

## Definition

Let $X$ be a smooth projective [[variety|HV6YBS0YDH]] of [[dimension|36X2WTHYCB]] $n$ over a field $k$, and let $\omega_X$ be its [[canonical bundle|W05VYY4HBR]].
For $m \ge 1$, the *$m$-th plurigenus* is $P_m(X) = \dim_k H^0(X, \omega_X^{\otimes m})$.
The *Kodaira dimension* $\kappa(X)$ is defined as follows:

1. If $P_m(X) = 0$ for all $m \ge 1$, then $\kappa(X) = -\infty$.
2. Otherwise, $\kappa(X)$ is the least integer $\kappa \ge 0$ such that $P_m(X) / m^{\kappa}$ is bounded as $m \to \infty$.

## Remarks

Always $\kappa(X) \in \set{-\infty, 0, 1, \dots, n}$.
Equivalently, when some $P_m(X) > 0$, $\kappa(X)$ is the largest dimension of the image of the rational map $X \dashrightarrow \mathbb{P}(H^0(X, \omega_X^{\otimes m}))$ over all $m$ with $P_m(X) > 0$.
The variety $X$ is of *general type* if $\kappa(X) = n$.

Example: for $X = \mathbb{P}^n_k$ with $n \ge 1$, $\omega_X \cong \mathcal{O}(-n-1)$, so $\omega_X^{\otimes m} \cong \mathcal{O}(-m(n+1))$ has no nonzero sections and $\kappa(X) = -\infty$.
For a smooth projective curve of genus $g \ge 2$, $\deg \omega_X^{\otimes m} = m(2g-2)$ and Riemann–Roch gives $P_m = (2m-1)(g-1)$ for $m \ge 2$, which grows like $m^1$, so $\kappa(X) = 1$.

Non-example of clause 2 with $\kappa = 0$: the curve of genus $2$ has $P_m / m^0 = P_m$ unbounded, so its Kodaira dimension is not $0$.
