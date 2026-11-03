---
tag: GZDTG2HR38
kind: definition
name: Stationary state
msc: ["81Q10", "81Q05"]
defines: J0S11FEEWK
uses: [VXDEQB46GV, 0N6960W0BV, 4NQN47A92F, RC1C7WXX1H, EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Stationary_state
---

## Definition

Let $H$ be the [[Hamiltonian|VXDEQB46GV]] of a quantum system with Hilbert space $\mathcal{H}$, and let $\hbar > 0$.
A *stationary state* is a pure [[state|4NQN47A92F]] whose unit vector $\psi \in D(H)$ is an [[eigenvector|0N6960W0BV]] of $H$:
$$H\psi = E\psi$$
for some $E \in \R$, the *energy* of the state.

## Remarks

The time evolution of a stationary state is $e^{-itH/\hbar}\psi = e^{-iEt/\hbar}\psi$.
So $\psi(t)$ stays on the ray of $\psi$ in the [[projective Hilbert space|RC1C7WXX1H]], and every probability and expectation value is constant in time.
The equation $H\psi = E\psi$ is the time-independent [[Schrödinger equation|EPZR6H2WJN]].

Example: let $\hbar = m = \omega = 1$ and $H = -\frac12 \frac{d^2}{dx^2} + \frac12 x^2$ on $L^2(\R)$, the harmonic oscillator.
For $\psi_0(x) = \pi^{-1/4} e^{-x^2/2}$ one has $\psi_0'' = (x^2 - 1)\psi_0$, so $H\psi_0 = -\frac12 (x^2 - 1)\psi_0 + \frac12 x^2 \psi_0 = \frac12 \psi_0$.
So $\psi_0$ is a stationary state with energy $\frac12$.

Non-example: with the same $H$, let $\psi_1(x) = \sqrt{2}\, \pi^{-1/4} x e^{-x^2/2}$, a stationary state with energy $\frac32$, and $\psi = (\psi_0 + \psi_1)/\sqrt{2}$.
Then $\psi(t) = (e^{-it/2}\psi_0 + e^{-3it/2}\psi_1)/\sqrt{2}$, and the relative phase $e^{-it}$ changes with $t$.
So $\psi(t)$ leaves the ray of $\psi$, and $\psi$ is not an eigenvector of $H$.
