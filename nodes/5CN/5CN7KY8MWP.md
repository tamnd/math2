---
tag: 5CN7KY8MWP
kind: statement
role: theorem
name: Karhunen–Loève theorem
msc: [60G12, 60G15]
uses: [0QH5ENKZM1, 0KBFAWYRTE, 0BQAA2BK3Q, 0S9GGTR0EX, 0WQNRCNY3M]
about: [0QH5ENKZM1, 0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Kosambi%E2%80%93Karhunen%E2%80%93Lo%C3%A8ve_theorem
same_as:
  wikidata: Q2046647
  wikipedia: Kosambi–Karhunen–Loève theorem
---

## Statement

Let $a < b$ and let $(X_t)_{t \in [a, b]}$ be a real [[stochastic process|0QH5ENKZM1]] such that the map $(t, \omega) \mapsto X_t(\omega)$ is jointly measurable, $E[X_t] = 0$ and $E[X_t^2] < \infty$ for every $t$.
Assume that the [[covariance|0KBFAWYRTE]] function $K(s, t) = E[X_s X_t]$ is continuous on $[a, b]^2$.
Let $T_K$ be the integral operator on $L^2[a, b]$ given by $(T_K f)(s) = \int_a^b K(s, t) f(t) \, dt$.
Let $(\lambda_k)_{k \ge 1}$ be its non-zero [[eigenvalues|0BQAA2BK3Q]], listed with multiplicity, and let $(e_k)$ be corresponding [[orthonormal|0S9GGTR0EX]] eigenfunctions.
Then:

1. each $\lambda_k$ is positive and each $e_k$ is continuous;
2. the random variables $Z_k = \int_a^b X_t \, e_k(t) \, dt$ satisfy $E[Z_k] = 0$ and $E[Z_j Z_k] = \lambda_k$ if $j = k$ and $0$ otherwise;
3. $X_t = \sum_{k} Z_k e_k(t)$, where the series converges in mean square uniformly in $t$:
$$\lim_{n \to \infty} \sup_{t \in [a, b]} E\left[\left(X_t - \sum_{k=1}^{n} Z_k e_k(t)\right)^2\right] = 0.$$

If $X$ is moreover a Gaussian process, the $Z_k$ are independent normal random variables.

## Remarks

The proof rests on Mercer's theorem: $K$ is continuous, symmetric and positive semidefinite, so $K(s, t) = \sum_k \lambda_k e_k(s) e_k(t)$ with uniform convergence on $[a, b]^2$.
Fubini's theorem gives the moments of the $Z_k$ and $E[X_t Z_k] = \lambda_k e_k(t)$.
Expanding the square then gives
$$E\left[\left(X_t - \sum_{k \le n} Z_k e_k(t)\right)^2\right] = K(t, t) - \sum_{k \le n} \lambda_k e_k(t)^2,$$
which tends to $0$ uniformly in $t$ by Mercer's theorem.

Example: for the standard [[Wiener process|22735FGJV6]] on $[0, 1]$, $K(s, t) = \min(s, t)$.
Solving the eigenvalue equation gives $e_k(t) = \sqrt{2} \sin\left((k - \tfrac{1}{2})\pi t\right)$ and $\lambda_k = \dfrac{1}{(k - \frac{1}{2})^2 \pi^2}$ for $k \ge 1$.
So $W_t = \sum_{k \ge 1} \sqrt{2} \, \xi_k \dfrac{\sin\left((k - \frac{1}{2})\pi t\right)}{(k - \frac{1}{2})\pi}$ with i.i.d. standard normal $\xi_k$.

## Explanations

### L1 human

A random curve can be written as a sum of fixed shapes multiplied by random coefficients.
The Karhunen–Loève theorem gives the best such shapes for a given process: the eigenfunctions of its covariance.
With this choice, the random coefficients are uncorrelated, and the first few terms capture as much of the variance as possible.

### L2 human

The expansion is the continuous analogue of principal component analysis, which diagonalises a covariance matrix.
Truncating it after $n$ terms gives the best approximation by $n$ terms for the mean square error integrated over $[a, b]$, among all expansions in an orthonormal basis of $L^2[a, b]$.
It is used to simulate Gaussian processes, to reduce dimension in signal processing and uncertainty quantification, and to compute laws of quadratic functionals such as $\int_0^1 W_t^2 \, dt = \sum_k \lambda_k \xi_k^2$.
