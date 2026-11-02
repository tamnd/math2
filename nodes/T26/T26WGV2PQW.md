---
tag: T26WGV2PQW
kind: statement
role: proposition
name: Resolvent equation for kernels
msc: [45B05, 45P05]
uses: [ARTJV1XCRX, 9QNBFERMHD, ZM5G144PZG]
about: [ARTJV1XCRX]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Statement

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]] with $M = \max \abs{K}$, and let $\rho = 1 / (M (b - a))$.
For $\abs{\lambda} < \rho$ let $R(x, s; \lambda)$ be the [[resolvent kernel|ARTJV1XCRX]] of $K$.
Then the following hold.

1. For $\abs{\lambda} < \rho$ and all $x, s \in [a, b]$,
$$R(x, s; \lambda) - K(x, s) = \lambda \int_a^b K(x, t) R(t, s; \lambda) \, dt = \lambda \int_a^b R(x, t; \lambda) K(t, s) \, dt.$$
2. For $\abs{\lambda} < \rho$, $\abs{\mu} < \rho$ and all $x, s \in [a, b]$,
$$R(x, s; \lambda) - R(x, s; \mu) = (\lambda - \mu) \int_a^b R(x, t; \lambda) R(t, s; \mu) \, dt.$$

## Remarks

Proof idea: write $R = \sum_{n \ge 1} \lambda^{n-1} K_n$ with the [[iterated kernels|9QNBFERMHD]] and use $K_{n+1}(x, s) = \int K(x, t) K_n(t, s) \, dt = \int K_n(x, t) K(t, s) \, dt$; uniform convergence allows integration term by term.
For part 2, multiply out the two series and use $K_{n+m}(x, s) = \int K_n(x, t) K_m(t, s) \, dt$; the coefficient identity is $\lambda^{k} - \mu^{k} = (\lambda - \mu) \sum_{i + j = k - 1} \lambda^i \mu^j$.
In operator form, with $R_\lambda = K (I - \lambda K)^{-1}$, the identities read $R_\lambda - K = \lambda K R_\lambda = \lambda R_\lambda K$ and $R_\lambda - R_\mu = (\lambda - \mu) R_\lambda R_\mu$.

Example: for $K(x, s) = x s$ on $[0, 1]$, $R(x, s; \lambda) = 3 x s / (3 - \lambda)$.
Then $\lambda \int_0^1 x t \cdot 3 t s / (3 - \lambda) \, dt = \lambda x s / (3 - \lambda)$, and $3 x s / (3 - \lambda) - x s = \lambda x s / (3 - \lambda)$, as part 1 says.

Both identities stay true, by analytic continuation, for all $\lambda$ and $\mu$ that are not poles of the meromorphic extension of $R$.

## Explanations

### L1 human

The resolvent kernel solves an integral equation of its own, with the kernel $K$ itself as the free term.
A second identity compares the resolvent kernels at two values of the parameter.
These rules let one compute with resolvent kernels as one computes with inverse matrices.

### L2 human

Part 1 is the kernel form of $(I + \lambda R_\lambda)(I - \lambda K) = (I - \lambda K)(I + \lambda R_\lambda) = I$, which says that $I + \lambda R_\lambda$ inverts $I - \lambda K$.
It is often taken as the definition of the resolvent kernel beyond the disc of convergence of the series.
Part 2 is the analogue of the resolvent identity of operator theory, and it shows that $R$ is analytic in $\lambda$ with $\partial_\lambda R(x, s; \lambda) = \int_a^b R(x, t; \lambda) R(t, s; \lambda) \, dt$.
