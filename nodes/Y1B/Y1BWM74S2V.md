---
tag: Y1BWM74S2V
kind: definition
name: Madelung equations
msc: [76Y05, 35Q40, 81Q05]
defines: 2FQB3CKQH0
uses: [EPZR6H2WJN, RW0JK9VDZE, FD4NR553YR]
sources:
  - url: https://en.wikipedia.org/wiki/Madelung_equations
---

## Definition

Let $m > 0$ be a mass, $\hbar > 0$ the reduced Planck constant and $V(x, t)$ a real potential on $\R^3$.
Let $\psi$ be a solution of the [[Schrödinger equation|EPZR6H2WJN]]
$$i \hbar \, \partial_t \psi = -\frac{\hbar^2}{2m} \Delta \psi + V \psi,$$
and write $\psi = \sqrt{\rho} \, e^{i S / \hbar}$ on a region where $\psi \ne 0$, with $\rho > 0$ and $S$ real and smooth.
Set $\mathbf{u} = \nabla S / m$.
The *Madelung equations* are the system
$$\partial_t \rho + \nabla \cdot (\rho \mathbf{u}) = 0, \qquad \partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{m} \nabla (V + Q),$$
where $Q$ is the *quantum potential*
$$Q = -\frac{\hbar^2}{2m} \frac{\Delta \sqrt{\rho}}{\sqrt{\rho}}.$$

## Remarks

The imaginary part of the Schrödinger equation gives the [[continuity equation|FD4NR553YR]], and the real part gives the quantum Hamilton–Jacobi equation $\partial_t S + \abs{\nabla S}^2 / (2m) + V + Q = 0$, whose gradient is the momentum equation.
The momentum equation is the [[Euler equation|RW0JK9VDZE]] of a potential flow with the extra force $-\nabla Q / m$.
Example: the plane wave $\psi = e^{i (k x - \omega t)}$ with $V = 0$ has $\rho = 1$, $S = \hbar (k x - \omega t)$ and $\mathbf{u} = (\hbar k / m) \mathbf{e}_x$.
Then $Q = 0$, and both equations hold since $\rho$ and $\mathbf{u}$ are constant.
The Hamilton–Jacobi equation gives $\omega = \hbar k^2 / (2m)$, the free dispersion relation.
Non-example: at a zero of $\psi$ the phase is not defined, so the equations do not apply there.
Around such a zero the circulation of $\mathbf{u}$ is a multiple of $2\pi\hbar/m$.
To recover the Schrödinger equation from a solution of the Madelung equations, one needs this quantisation condition on the circulation.
