---
tag: HMG6G0S2DJ
kind: definition
name: Bound state
msc: [81Q10, 35J10]
defines: 3XZFX39KH9
uses: [HM2HHE3J51, 0NEGN5CRSC, 0N6960W0BV, VXDEQB46GV]
sources:
  - url: https://en.wikipedia.org/wiki/Bound_state
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $H$ be a [[self-adjoint operator|0NEGN5CRSC]] on $\mathcal{H}$ with domain $D(H)$, the [[Hamiltonian|VXDEQB46GV]] of a quantum system.
A *bound state* of $H$ is a vector $\psi \in D(H)$ with $\norm{\psi} = 1$ such that $H\psi = E\psi$ for some $E \in \R$.
In other words, it is a normalised [[eigenvector|0N6960W0BV]] of $H$, and $E$ is its energy.

## Remarks

Example: for $H = -\frac12 \Delta - \frac{1}{\abs{x}}$ on $L^2(\R^3)$, the function $\psi(x) = \pi^{-1/2} e^{-\abs{x}}$ lies in $D(H)$, has norm $1$, and satisfies $H\psi = -\frac12 \psi$.
So it is a bound state, the ground state of the hydrogen atom.

Non-example: for $H = -\frac{d^2}{dx^2}$ on $L^2(\R)$ and $k \in \R$, the function $e^{ikx}$ satisfies $-\frac{d^2}{dx^2} e^{ikx} = k^2 e^{ikx}$.
It is not square-integrable, so it is not in $\mathcal{H}$ and is not a bound state.
In fact this $H$ has no eigenvalues at all.

The time evolution of a bound state only changes its phase: $e^{-iHt/\hbar}\psi = e^{-iEt/\hbar}\psi$, so it is a stationary state.
Some authors call every vector of the closed span of the eigenvectors of $H$ (the pure point subspace) a bound state.
For Schrödinger operators these are exactly the states that stay localised: for every $\varepsilon > 0$ there is $R$ with $\norm{\mathbf{1}_{\abs{x} > R}\, e^{-iHt/\hbar}\psi} < \varepsilon$ for all $t$.
