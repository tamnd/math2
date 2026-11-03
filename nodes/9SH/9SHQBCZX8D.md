---
tag: 9SHQBCZX8D
kind: definition
name: Electronic band structure
msc: [82D20, 81Q10]
defines: QP0TK2M29V
uses: [2ASPT0SP6Z, EKTERAYFJ2, 89AA6XJY5K, 0NEGN5CRSC, BMKATJ802A]
sources:
  - url: https://en.wikipedia.org/wiki/Electronic_band_structure
---

## Definition

Let $\Lambda \subset \R^n$ be a [[Bravais lattice|2ASPT0SP6Z]] with reciprocal lattice $\Lambda^*$ and [[Brillouin zone|EKTERAYFJ2]] $B$.
Let $V \colon \R^n \to \R$ be a bounded measurable function with $V(x + R) = V(x)$ for all $R \in \Lambda$.
Consider the periodic [[Schrödinger operator|89AA6XJY5K]] $H = -\Delta + V$ on $L^2(\R^n)$, in units where $\hbar^2 / 2m = 1$.
For $k \in \R^n$, let $H(k) = (-i\nabla + k)^2 + V$ act on $\Lambda$-periodic functions, that is, on $L^2(\R^n / \Lambda)$.
Each $H(k)$ is [[self-adjoint|0NEGN5CRSC]] with compact resolvent, so its spectrum is a sequence of eigenvalues $E_1(k) \le E_2(k) \le \cdots$, repeated with multiplicity and tending to $+\infty$.
The functions $E_m \colon B \to \R$, $m \ge 1$, are the *band functions*, and together they form the *band structure* of $H$.

## Remarks

If $u$ is an eigenfunction of $H(k)$, then $\psi(x) = e^{i k \cdot x} u(x)$ solves $H\psi = E\psi$ and satisfies $\psi(x + R) = e^{ik \cdot R} \psi(x)$; this is Bloch's theorem.
Each $E_m$ is continuous and $\Lambda^*$-periodic, since $H(k + G)$ is unitarily equivalent to $H(k)$ through multiplication by $e^{-iG \cdot x}$.
The [[spectrum|BMKATJ802A]] of $H$ is the union of the bands $E_m(B)$, which are closed intervals, and the open intervals between them that are not covered are the spectral gaps.

Example: the free electron in dimension $1$, with $\Lambda = \Z$ and $V = 0$.
Then $H(k) = (-i\, d/dx + k)^2$ on $L^2(\R/\Z)$ has eigenfunctions $e^{2\pi i m x}$, $m \in \Z$, with eigenvalues $(k + 2\pi m)^2$.
Sorting these for $k \in [-\pi, \pi]$ gives the bands $[0, \pi^2], [\pi^2, 4\pi^2], [4\pi^2, 9\pi^2], \dots$, with no gaps, and their union is $[0, \infty)$.

Non-example: if $V$ is not periodic, for instance a random potential, the operators $H(k)$ are not defined, and there is no band structure.
