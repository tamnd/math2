---
tag: Y1DX99NPEK
kind: definition
name: Ecological stability
msc: [92D40, 34D20]
defines: 7ZR8Y9QBB4
uses: [1YEMFQ1H32, 0N8NGKDZDZ, 0NB689782W, 047NDTEPCV, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Ecological_stability
---

## Definition

Consider a [[population model|1YEMFQ1H32]] $x' = f(x)$ of a community of $n$ species, with $f$ continuously differentiable, and let $x^*$ be an [[equilibrium point|0N8NGKDZDZ]], so that $f(x^*) = 0$.
The [[Jacobian matrix|047NDTEPCV]] $J = Df(x^*)$ is called the *community matrix* at $x^*$.
The equilibrium community $x^*$ is *ecologically stable*, in the local sense, if it is [[asymptotically stable|0NB689782W]].
Assume that every [[eigenvalue|0BQAA2BK3Q]] of $J$ has negative real part; then $x^*$ is ecologically stable.
In this case the number $\rho = -\max_\mu \operatorname{Re} \mu$, with the maximum over the eigenvalues $\mu$ of $J$, is the *resilience* of $x^*$.

## Remarks

Example: for the logistic model $N' = N(1 - N/10)$ at $N^* = 10$, the community matrix is the $1 \times 1$ matrix $(-1)$, so the equilibrium is stable with resilience $1$.
Non-example: for the same model, the equilibrium $N^* = 0$ has community matrix $(1)$, with a positive eigenvalue, so it is unstable: a few individuals make the population grow away from $0$.
The resilience measures the rate of return: small deviations decay roughly like $e^{-\rho t}$, where $\rho$ is the resilience.
In ecology the word stability is also used for other properties, such as persistence of all species, constancy of population sizes, and resistance to disturbances.
