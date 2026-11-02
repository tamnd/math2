---
tag: 35FFCR3GRH
kind: definition
name: Minakshisundaram–Pleijel zeta function
msc: [58J50, 11M41, 58J52]
defines: T1039Q9FY0
uses: [7CBT4SM83Y, B8TYKV7AA1, 45P2SEGGR1, 0M3YQJ81NB, 1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Minakshisundaram–Pleijel_zeta_function
---

## Definition

Let $(M, g)$ be a closed connected [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$.
Let $0 = \lambda_0 < \lambda_1 \le \lambda_2 \le \cdots$ be the [[spectrum of the Laplace–Beltrami operator|B8TYKV7AA1]], with an orthonormal basis of real eigenfunctions $\phi_0, \phi_1, \ldots$ of $L^2(M)$.
The *Minakshisundaram–Pleijel zeta function* is
$$Z(s, x, y) = \sum_{j \ge 1} \frac{\phi_j(x) \phi_j(y)}{\lambda_j^{s}}, \qquad x, y \in M,$$
and its trace on the diagonal is the *spectral zeta function*
$$Z(s) = \int_M Z(s, x, x) \, dv(x) = \sum_{j \ge 1} \lambda_j^{-s}.$$
Both series converge for $\operatorname{Re} s > n/2$.

## Remarks

By the [[Minakshisundaram–Pleijel expansion|45P2SEGGR1]] of the heat trace and the formula $\Gamma(s) Z(s) = \int_0^\infty t^{s-1} \big( \sum_{j \ge 0} e^{-t\lambda_j} - 1 \big) \, dt$, the function $Z(s)$ has a meromorphic [[continuation|0M3YQJ81NB]] to $\C$.
Its poles are simple and lie among the points $s = n/2 - k$, $k = 0, 1, 2, \ldots$, other than $0, -1, -2, \ldots$; in particular $Z$ is holomorphic at $s = 0$.
The residue at $s = n/2$ is $\operatorname{vol}(M) / \big( (4\pi)^{n/2} \Gamma(n/2) \big)$, which is equivalent to Weyl's law.

Example: for $M = \R / 2\pi\Z$ the nonzero eigenvalues are $k^2$, $k \ge 1$, each with multiplicity $2$.
So $Z(s) = 2 \sum_{k \ge 1} k^{-2s} = 2 \zeta(2s)$, with $\zeta$ the [[Riemann zeta function|1XWBY4N0VT]].
It has a single simple pole at $s = 1/2$ with residue $1$, and $Z(0) = 2\zeta(0) = -1$.

Non-example: the sum $\sum_{j \ge 0} \lambda_j^{-s}$ that includes $\lambda_0 = 0$ is not defined, since $0^{-s}$ has no meaning; this is why the zero eigenvalue is left out.
