---
tag: PE5H892XVS
kind: statement
role: theorem
name: Chebyshev iteration
msc: [65F10]
uses: [0GT4WWGWH2, 0KX66CZMBB, 0BQAA2BK3Q, M6EAR1JHPP, AB3S6MHJ8X, 2RPE77ACER, 7CESYMHQEA, QB45PCGQPV]
about: [2RPE77ACER, M6EAR1JHPP]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_iteration
same_as:
  wikidata: Q2457511
  wikipedia: Chebyshev iteration
---

## Statement

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, and let $b \in \R^n$.
Let $0 < \alpha < \beta$ be numbers such that every [[eigenvalue|0BQAA2BK3Q]] of $A$ lies in $[\alpha, \beta]$, and let $\kappa = \beta / \alpha$.
Let $T_k$ be the [[Chebyshev polynomial|M6EAR1JHPP]] of the first kind of degree $k$, and set $\theta = (\beta + \alpha) / (\beta - \alpha)$.
The *Chebyshev iteration* produces iterates $x^{(k)}$ whose errors $e_k = x^{(k)} - A^{-1} b$ satisfy $e_k = p_k(A) e_0$, where
$$p_k(t) = \frac{T_k\!\left( \frac{\beta + \alpha - 2t}{\beta - \alpha} \right)}{T_k(\theta)}.$$
The iterates can be computed by a three-term recurrence that uses one product with $A$ per step and no inner products.
For every $k \ge 0$,
$$\norm{e_k}_2 \le \frac{\norm{e_0}_2}{T_k(\theta)} \le 2 \left( \frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1} \right)^k \norm{e_0}_2.$$

## Remarks

Since $A$ is symmetric, $\norm{p_k(A)}_2 = \max_\lambda \abs{p_k(\lambda)}$ over its eigenvalues, and on $[\alpha, \beta]$ the numerator of $p_k$ is at most $1$ in absolute value.
The bound $T_k(\theta) \ge \frac12 \sigma^{-k}$ with $\sigma = (\sqrt{\kappa} - 1)/(\sqrt{\kappa} + 1)$ follows from $T_k(x) = \frac12 \big( (x + \sqrt{x^2 - 1})^k + (x - \sqrt{x^2 - 1})^k \big)$ for $x \ge 1$.
Among all polynomials of degree $k$ with value $1$ at $0$, the scaled Chebyshev polynomial $p_k$ has the least maximum on $[\alpha, \beta]$.
So no method of the form $e_k = q(A) e_0$ with such $q$ can do better in the worst case over matrices with spectrum in $[\alpha, \beta]$.
For comparison, the optimal [[Richardson iteration|7CESYMHQEA]] contracts by $(\kappa - 1)/(\kappa + 1)$ per step.
Example: for $\kappa = 100$ the Chebyshev factor is $9/11 \approx 0.82$, while the Richardson factor is $99/101 \approx 0.98$.
If the interval does not contain the whole spectrum, the bound fails and the method can diverge.

## Explanations

### L1 human

Chebyshev iteration is Richardson's method with a cleverly varying step size.
The steps are chosen so that the error is damped evenly over the whole range of eigenvalues.
The price is that one must know bounds for the smallest and largest eigenvalues in advance.

### L2 human

The error factor depends on $\sqrt{\kappa}$ instead of $\kappa$, like the conjugate gradient method, where $\kappa$ is the [[condition number|AB3S6MHJ8X]].
Unlike conjugate gradients it needs no inner products, which helps on parallel machines where global sums are costly.
Its iterates lie in the [[Krylov subspace|QB45PCGQPV]] shifted by $x^{(0)}$, and the conjugate gradient method finds an iterate there that is at least as good in the energy norm.
Chebyshev polynomials are also used as smoothers in multigrid and as polynomial preconditioners.
