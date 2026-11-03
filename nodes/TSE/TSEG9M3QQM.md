---
tag: TSEG9M3QQM
kind: definition
name: Wave function
msc: ["81Q05", "81P16"]
defines: E9WK6KJ4SM
uses: [SASP14MA1Z, 4NQN47A92F, 0ZY9DX8FBF, EPZR6H2WJN]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_function
---

## Definition

Let $n \ge 1$, and consider a quantum particle without spin moving in $\R^n$, with Hilbert space [[$L^2(\R^n)$|SASP14MA1Z]].
A *wave function* of the particle is a measurable function $\psi \colon \R^n \to \C$ such that
$$\int_{\R^n} \abs{\psi(x)}^2 \, dx = 1.$$
It describes the pure [[quantum state|4NQN47A92F]] with unit vector $\psi$ in $L^2(\R^n)$.
The function $\abs{\psi}^2$ is the [[probability density|0ZY9DX8FBF]] of the position of the particle.
Two wave functions equal almost everywhere are the same vector.
Two that differ by a constant factor $e^{i\theta}$, $\theta \in \R$, give the same state.

## Remarks

For $N$ particles in $\R^3$, a wave function is a unit vector of $L^2(\R^{3N})$, a function of all the positions together.
A time-dependent wave function $\psi(x, t)$ is a family of wave functions that solves the [[Schrödinger equation|EPZR6H2WJN]].

Example: $\psi(x) = \pi^{-1/4} e^{-x^2/2}$ on $\R$.
Indeed $\int_\R \pi^{-1/2} e^{-x^2}\, dx = 1$, so $\psi$ is a wave function, and the position is normally distributed with mean $0$ and variance $1/2$.

Non-example: the plane wave $\psi(x) = e^{ikx}$ with $k \in \R$ has $\abs{\psi}^2 = 1$, so $\int_\R \abs{\psi}^2 \, dx = \infty$.
It is not in $L^2(\R)$ and is not a wave function, although it is used as a generalised eigenfunction of the momentum.
