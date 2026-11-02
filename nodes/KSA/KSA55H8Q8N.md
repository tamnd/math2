---
tag: KSA55H8Q8N
kind: definition
name: Turing pattern
msc: [35B36, 35K57, 92C15]
defines: RM94KBV8P7
uses: [TAAHWE917M, 047NDTEPCV, 0BQAA2BK3Q, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_pattern
---

## Definition

Let $m \ge 2$, let $D$ be a diagonal $m \times m$ matrix with positive diagonal entries, and let $f \colon \R^m \to \R^m$ be smooth.
Consider the [[reaction–diffusion system|TAAHWE917M]] $\partial_t u = D \Delta u + f(u)$ for $u \colon \R^n \times [0, \infty) \to \R^m$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]].
Let $u^* \in \R^m$ satisfy $f(u^*) = 0$ and let $J$ be the [[Jacobian matrix|047NDTEPCV]] of $f$ at $u^*$.
The uniform state $u^*$ is *Turing unstable*, or has a *diffusion-driven instability*, if:

1. every [[eigenvalue|0BQAA2BK3Q]] of $J$ has negative real part, so $u^*$ is stable without diffusion;
2. there is $k > 0$ such that $J - k^2 D$ has an eigenvalue with positive real part.

A *Turing pattern* is a stationary, spatially non-constant solution near $u^*$ that bifurcates from a Turing unstable uniform state.
It is typically periodic, with a wave number $k$ as in clause 2.

## Remarks

The perturbation $u = u^* + e^{\lambda t} e^{i q \cdot x} w$ with a wave vector $q \in \R^n$, $\abs{q} = k$, solves the linearised system exactly when $\lambda$ is an eigenvalue of $J - k^2 D$ with eigenvector $w$, which explains clause 2.
Example: $m = 2$, $J = \begin{pmatrix} 1 & -1 \\ 3 & -2 \end{pmatrix}$, $D = \operatorname{diag}(1, 10)$.
Then $\tr J = -1 < 0$ and $\det J = 1 > 0$, so clause 1 holds.
For $k^2 = 0.3$, $\det(J - k^2 D) = (0.7)(-5) + 3 = -0.5 < 0$, so $J - k^2 D$ has a positive real eigenvalue and clause 2 holds.
Non-example: if $D$ is a multiple $d I$ of the identity, the eigenvalues of $J - k^2 D$ are those of $J$ shifted by $-d k^2$, so clause 2 fails whenever clause 1 holds.
For $m = 2$, a necessary condition is that the two diffusion coefficients differ.
