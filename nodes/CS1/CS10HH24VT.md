---
tag: CS10HH24VT
kind: definition
name: Gross–Pitaevskii equation
msc: [35Q55, 35Q40]
defines: F5EAWFMC8A
uses: [GEJHRXC176, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Gross–Pitaevskii_equation
---

## Definition

Let $d \ge 1$, let $\hbar, m > 0$ and $g \in \R$ be constants, and let $V \colon \R^d \to \R$ be a given function, the external potential.
The *Gross–Pitaevskii equation* is the equation
$$i \hbar \, \partial_t \psi = - \frac{\hbar^2}{2m} \Delta \psi + V(x) \psi + g \abs{\psi}^2 \psi$$
for an unknown function $\psi \colon \R \times \R^d \to \C$, $(t, x) \mapsto \psi(t, x)$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in $x$.
The constant $g$ measures the strength of the interaction, repulsive for $g > 0$ and attractive for $g < 0$.

## Remarks

For $V = 0$ it is, after scaling, the cubic [[nonlinear Schrödinger equation|GEJHRXC176]].
A standing wave $\psi(t, x) = e^{-i\mu t/\hbar} \phi(x)$ solves it exactly when $\phi$ solves the stationary equation $\mu \phi = -\tfrac{\hbar^2}{2m} \Delta \phi + V \phi + g \abs{\phi}^2 \phi$, and $\mu$ is the chemical potential.

Example: for $V = 0$ and $n > 0$, the constant state $\phi = \sqrt{n}$ solves the stationary equation with $\mu = g n$, since $\Delta \phi = 0$ and $g \abs{\phi}^2 \phi = g n \phi$.

Non-example: if $V$ is not constant, then no nonzero constant $\phi$ solves the stationary equation, because $\mu \phi = (V(x) + g \abs{\phi}^2) \phi$ would force $V$ to be constant.

The ground state minimises the Gross–Pitaevskii energy $\int \big( \tfrac{\hbar^2}{2m} \abs{\nabla \phi}^2 + V \abs{\phi}^2 + \tfrac{g}{2} \abs{\phi}^4 \big) dx$ under the constraint $\int \abs{\phi}^2 \, dx = N$, the number of particles.
