---
tag: 1Y7AH9QTEQ
kind: definition
name: Analytic torsion
msc: [58J52, 57Q10]
defines: MZT9D34B0A
uses: [7CBT4SM83Y, S1XK3HXHFX, 74BPYJNZTM, YT3ZQ2F7FG, PWG3GKZG80]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_torsion
---

## Definition

Let $(M, g)$ be a closed oriented [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$.
Let $\rho \colon \pi_1(M) \to U(N)$ be a [[unitary representation|74BPYJNZTM]] of the [[fundamental group|S1XK3HXHFX]], and let $E_\rho$ be the associated flat Hermitian vector bundle.
Assume that $\rho$ is acyclic, that is, the cohomology $H^*(M; E_\rho)$ vanishes.
For $0 \le q \le n$ let $\Delta_q$ be the [[Hodge Laplacian|PWG3GKZG80]] on $E_\rho$-valued $q$-forms.
By acyclicity, all eigenvalues of $\Delta_q$ are positive.
Let $\zeta_q(s) = \sum_\lambda \lambda^{-s}$ be its spectral zeta function, summed over its eigenvalues with multiplicity.
The *analytic torsion* $T(M, \rho) > 0$ is defined by
$$\log T(M, \rho) = \frac12 \sum_{q = 0}^{n} (-1)^q \, q \, \zeta_q'(0).$$

## Remarks

Equivalently, $T(M, \rho) = \prod_q \big( \det_\zeta \Delta_q \big)^{(-1)^{q+1} q/2}$ in terms of [[zeta-regularized determinants|YT3ZQ2F7FG]].
Ray and Singer showed that $T(M, \rho)$ does not depend on the metric $g$ when $n$ is odd, and that $T(M, \rho) = 1$ when $n$ is even.
Without acyclicity, one defines the torsion as a metric on the determinant line of the cohomology, the Ray–Singer metric.
Conventions differ: some authors use the inverse of $T$, or omit the factor $\tfrac12$.

Example: let $M = \R / 2\pi\Z$ and let $\rho$ send the generator of $\pi_1(M) = \Z$ to $e^{2\pi i a}$ with $0 < a < 1$.
Sections of $E_\rho$ are functions with $f(\theta + 2\pi) = e^{2\pi i a} f(\theta)$, with eigenfunctions $e^{i(k + a)\theta}$, $k \in \Z$.
So $\Delta_0$ and $\Delta_1$ both have eigenvalues $(k + a)^2$, and $\zeta_1(s) = \zeta(2s, a) + \zeta(2s, 1 - a)$, with Hurwitz zeta functions.
From $\zeta'(0, a) = \log \Gamma(a) - \tfrac12 \log(2\pi)$ and $\Gamma(a)\Gamma(1 - a) = \pi / \sin(\pi a)$ one gets $\zeta_1'(0) = -2 \log(2 \sin \pi a)$, hence $T(M, \rho) = 2 \sin(\pi a) = \abs{1 - e^{2\pi i a}}$.

Non-example: for the trivial representation of $\pi_1(S^1)$, $H^0(S^1; \C) = \C$ is nonzero, so the representation is not acyclic, $\Delta_0$ has the eigenvalue $0$, and the formula above does not apply as stated.
