---
tag: 5WVZSM42XR
kind: statement
role: theorem
name: Domination principle
msc: [31B15, 31C15]
uses: [HZNEQQBCW4, DCMFQ01QGS, SFSRQCM3EG]
about: [DCMFQ01QGS]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_theory
---

## Statement

Let $n \ge 3$ and let $\mu$ and $\nu$ be positive [[Radon measures|HZNEQQBCW4]] on $\R^n$ with compact support.
For a positive measure $\lambda$, let $U^\lambda(x) = \int \abs{x - y}^{2-n} \, d\lambda(y)$ be its [[Newtonian potential|DCMFQ01QGS]].
Assume that $\mu$ has finite [[energy|SFSRQCM3EG]] $\int U^\mu \, d\mu < \infty$, and that $U^\mu(x) \le U^\nu(x)$ for $\mu$-almost every $x$.
Then $U^\mu(x) \le U^\nu(x)$ for every $x \in \R^n$.

## Remarks

Proof idea: standard proofs combine balayage with the positive definiteness of the Newtonian energy.
Balayage sweeps a measure onto a set without changing its potential there.
The finite energy of $\mu$ is what makes these energy arguments possible.

Example: let $\nu = \delta_0$, a unit point mass at the origin of $\R^3$.
Let $\mu$ be the uniform measure of mass $1$ on the sphere of radius $r$ centred at $0$.
On the sphere, $U^\mu = 1/r = U^\nu$, so the hypothesis holds.
The theorem gives $U^\mu \le U^\nu$ everywhere, and indeed $U^\mu(x) = \min(1/r, 1/\abs{x}) \le 1/\abs{x} = U^\nu(x)$.

The finite energy of $\mu$ is needed.
For $\mu = \delta_0$ and $\nu = \frac12 \delta_0$, both potentials are $+\infty$ at $0$, so $U^\mu \le U^\nu$ holds $\mu$-almost everywhere, but $U^\mu(x) = 1/\abs{x} > U^\nu(x)$ for $x \ne 0$.
Take for $\nu$ a uniform measure on a large sphere, whose potential equals a constant $M$ inside the sphere and is at most $M$ outside.
This gives back the maximum principle for potentials of finite energy with support inside the sphere.

## Explanations

### L1 human

The potential of a charge $\mu$ of finite energy is controlled everywhere as soon as it is controlled on the charge itself.
If the potential of $\nu$ is at least as large as that of $\mu$ wherever $\mu$ sits, then it is at least as large everywhere.
So comparing two potentials only needs a check on the support of one of them.

### L2 human

The domination principle is one of the basic properties of the Newtonian kernel, and it is taken as an axiom in abstract potential theory.
It is used in the theory of balayage and in comparison arguments for equilibrium potentials.
It holds for Riesz kernels $\abs{x - y}^{\alpha - n}$ with $0 < \alpha \le 2$ and $\alpha < n$.
In the plane with the logarithmic kernel, an extra condition on the total masses is needed.
