---
tag: NC44AJYHYC
kind: definition
name: De Broglie–Bohm theory
msc: [81P05, 81Q05]
defines: KN403Z7F1R
uses: [QRW6NE1VY7, E9WK6KJ4SM, EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/De_Broglie%E2%80%93Bohm_theory
---

## Definition

Consider $N$ particles in $\R^3$ with masses $m_1, \dots, m_N > 0$, and let $q = (q_1, \dots, q_N) \in \R^{3N}$ denote a configuration.
Let $\psi(q, t)$ be a [[wave function|E9WK6KJ4SM]] on $\R^{3N} \times \R$.
Assume that it solves the [[Schrödinger equation|EPZR6H2WJN]]
$$i\hbar \, \partial_t \psi = -\sum_{k=1}^N \frac{\hbar^2}{2m_k} \Delta_k \psi + V\psi$$
for a real potential $V$ on $\R^{3N}$, where $\Delta_k$ is the Laplacian in $q_k$.
The *de Broglie–Bohm theory* describes the system by the pair $(\psi, Q)$, where $Q(t) = (Q_1(t), \dots, Q_N(t))$ are the actual particle positions.
The positions obey the *guiding equation*
$$\frac{dQ_k}{dt} = \frac{\hbar}{m_k} \operatorname{Im}\left(\frac{\nabla_k \psi}{\psi}\right)(Q(t), t), \qquad k = 1, \dots, N,$$
wherever $\psi(Q(t), t) \ne 0$.
The initial configuration $Q(0)$ is random with probability density $\abs{\psi(q, 0)}^2$, for $\psi$ normalized.

## Remarks

Example: for a plane wave $\psi(q, t) = e^{i(p \cdot q - Et)/\hbar}$ of one particle, $\nabla\psi/\psi = ip/\hbar$, so $dQ/dt = p/m$ and the particle moves uniformly with momentum $p$.
For a real wave function, such as a stationary state of the harmonic oscillator, $\operatorname{Im}(\nabla\psi/\psi) = 0$ and the particle is at rest.
Non-example: a random $Q(0)$ with a density other than $\abs{\psi(\cdot, 0)}^2$ still gives a well-defined dynamics.
But it does not reproduce the Born rule, so it is not the de Broglie–Bohm theory of quantum mechanics.
Equivariance: if $Q(0)$ has density $\abs{\psi(\cdot, 0)}^2$, then $Q(t)$ has density $\abs{\psi(\cdot, t)}^2$ for all $t$, because $\abs{\psi}^2$ and the velocity field satisfy the continuity equation.
For spin, the guiding equation uses the spinor inner product in numerator and denominator.
