---
tag: YGJZCD37ZY
kind: statement
role: theorem
name: Chebyshev–Markov–Stieltjes inequalities
msc: [44A60, 42C05, 65D32]
uses: [DYR1QFNGNJ, 01XAHPADBA, 8TXASARQN1, PQ1D8FQB3E, 0KX66CZMBB]
about: [01XAHPADBA, 8TXASARQN1]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev%E2%80%93Markov%E2%80%93Stieltjes_inequalities
same_as:
  wikidata: Q5089020
  wikipedia: Chebyshev–Markov–Stieltjes inequalities
---

## Statement

Let $m \ge 1$ and let $\mu$ be a positive [[Borel measure|DYR1QFNGNJ]] on $\R$ with finite [[moments|01XAHPADBA]] $m_k = \int_\R x^k \, d\mu(x)$ for $0 \le k \le 2m - 1$.
Assume that the [[Hankel matrix|PQ1D8FQB3E]] $(m_{i+j})_{i,j=0}^{m-1}$ is [[positive definite|0KX66CZMBB]].
Let $P_m$ be the monic polynomial of degree $m$ that is [[orthogonal|8TXASARQN1]] to all polynomials of degree less than $m$ in $L^2(\mu)$.
Then $P_m$ has $m$ simple real zeros $\xi_1 < \xi_2 < \cdots < \xi_m$.
Let $\rho_1, \ldots, \rho_m > 0$ be the Christoffel numbers, that is, the unique numbers with $\int_\R p \, d\mu = \sum_{j=1}^{m} \rho_j \, p(\xi_j)$ for every real polynomial $p$ of degree at most $2m - 1$.
Let $\nu$ be any positive Borel measure on $\R$ with $\int_\R x^k \, d\nu(x) = m_k$ for $0 \le k \le 2m - 1$.
Then for each $k$ with $1 \le k \le m$,
$$\sum_{j=1}^{k-1} \rho_j \;\le\; \nu\bigl((-\infty, \xi_k)\bigr) \;\le\; \nu\bigl((-\infty, \xi_k]\bigr) \;\le\; \sum_{j=1}^{k} \rho_j.$$

## Remarks

For the upper bound one builds, by Hermite interpolation, a polynomial $q$ of degree $2m - 2$ with $q(\xi_j) = 1$ for $j \le k$, $q(\xi_j) = 0$ for $j > k$, and $q'(\xi_j) = 0$ for $j \ne k$.
One shows that $q \ge 1$ on $(-\infty, \xi_k]$ and $q \ge 0$ on $\R$.
Then $\nu((-\infty, \xi_k]) \le \int q \, d\nu = \int q \, d\mu = \sum_j \rho_j q(\xi_j) = \sum_{j \le k} \rho_j$, since the integrals of $q$ depend only on the moments; the lower bound follows by the reflection $x \mapsto -x$.
The measure $\sum_j \rho_j \delta_{\xi_j}$ of Gaussian quadrature has the given moments, and it attains every bound.
In particular, the mass that any such $\nu$ puts at the point $\xi_k$ is at most $\rho_k$.
For example, for $m = 1$ with $m_0 = 1$ and $m_1 = 0$, one gets $\xi_1 = 0$ and $\rho_1 = 1$, and the inequalities say only $0 \le \nu((-\infty, 0)) \le \nu((-\infty, 0]) \le 1$.
The positive definiteness of the Hankel matrix holds exactly when $\mu$ is supported on at least $m$ points; it is needed for $P_m$ and the numbers $\rho_j$ to exist.

## Explanations

### L1 human

Suppose only the first few moments of a mass distribution on the line are known.
Then the distribution is not known, but the amount of mass to the left of certain special points is trapped between two explicit numbers.
The special points are the zeros of an orthogonal polynomial, and the numbers are sums of the weights of Gaussian quadrature.

### L2 human

The inequalities say that the distribution functions of all solutions of a truncated moment problem pass through a band around the staircase of the Gaussian quadrature measure.
The bound on point masses, $\nu(\set{\xi_k}) \le \rho_k$, also follows from the extremal property of the Christoffel function.
