---
tag: 4BT3Y8TCDN
kind: definition
name: Schrödinger equation
msc: [35Q41, 81Q05, 35Q40]
defines: EPZR6H2WJN
uses: [0E0B6RA8K0, 89AA6XJY5K, GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Schr%C3%B6dinger_equation
---

## Definition

Let $n \ge 1$, let $\hbar > 0$ and $m > 0$ be constants, and let $V \colon \R^n \to \R$ be a measurable function, the *potential*.
Let $\psi(x, t)$, for $x \in \R^n$ and $t \in \R$, be an unknown complex-valued function, and let $\Delta$ be the [[Laplacian|0E0B6RA8K0]] in $x$.
The *Schrödinger equation* with potential $V$ is the [[partial differential equation|GC5BDZ6QBC]]
$$i\hbar \, \frac{\partial \psi}{\partial t}(x, t) = -\frac{\hbar^2}{2m} \Delta \psi(x, t) + V(x) \psi(x, t).$$
With $H = -\frac{\hbar^2}{2m}\Delta + V$, the [[Schrödinger operator|89AA6XJY5K]], it reads $i\hbar\, \partial_t \psi = H\psi$.
The *time-independent* Schrödinger equation is the eigenvalue equation $H\varphi = E\varphi$; if it holds, then $\psi(x, t) = e^{-iEt/\hbar}\varphi(x)$ solves the time-dependent equation.

## Remarks

In mathematics one often sets $\hbar = 1$ and $2m = 1$, giving $i\partial_t u = -\Delta u + Vu$.

When $H$ is self-adjoint on $L^2(\R^n)$, Stone's theorem gives the solution $\psi(t) = e^{-itH/\hbar}\psi(0)$ for every initial value in $L^2(\R^n)$, and $e^{-itH/\hbar}$ is unitary, so $\norm{\psi(t)}_{L^2} = \norm{\psi(0)}_{L^2}$.

Example: with $V = 0$, $\hbar = 1$, $2m = 1$ and $k \in \R^n$, the plane wave $u(x, t) = e^{i(k \cdot x - \abs{k}^2 t)}$ is a solution.
Indeed $i\partial_t u = i \cdot (-i\abs{k}^2) u = \abs{k}^2 u$ and $-\Delta u = \abs{k}^2 u$.

Non-example: the heat equation $\partial_t u = \Delta u$ differs only by the factor $i$, but it is not a Schrödinger equation.
Its solutions decay in $L^2$ instead of keeping their norm: $u = e^{i k\cdot x - \abs{k}^2 t}$ solves it, and its modulus $e^{-\abs{k}^2 t}$ decreases.

## Explanations

### L1 human

The Schrödinger equation says that the time derivative of the wave function, times $i\hbar$, equals the energy operator applied to the wave function.
The factor $i$ makes solutions oscillate and spread rather than decay, and it keeps the total probability equal to one.
