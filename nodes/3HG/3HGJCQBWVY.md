---
tag: 3HGJCQBWVY
kind: statement
role: proposition
name: Leapfrog integration
msc: [65P10, 65L06, 37M15]
uses: [0EDKGA2FAK, B4C25SXFRE, 0FXDW992DS]
about: [B4C25SXFRE]
sources:
  - url: https://en.wikipedia.org/wiki/Leapfrog_integration
---

## Statement

Let $V \colon \R^d \to \R$ be three times continuously differentiable, put $a = -\nabla V$, and consider the equation $x'' = a(x)$ with $x(0) = x_0$ and $x'(0) = v_0$.
Fix a step size $h > 0$.
The leapfrog method, in its kick-drift-kick form, maps $(x_n, v_n)$ to $(x_{n+1}, v_{n+1})$ by
$$v_{n+1/2} = v_n + \tfrac{h}{2} a(x_n), \qquad x_{n+1} = x_n + h\, v_{n+1/2}, \qquad v_{n+1} = v_{n+1/2} + \tfrac{h}{2} a(x_{n+1}).$$
Let $\Phi_h \colon \R^{2d} \to \R^{2d}$ denote this map.

1. $\Phi_h$ is symplectic: it preserves the symplectic form $\sum_{i=1}^d dx_i \wedge dv_i$.
2. $\Phi_h$ is time-reversible: $\Phi_{-h}(\Phi_h(x, v)) = (x, v)$ for all $(x, v)$.
3. The method has order $2$: on a bounded time interval $[0, T]$, the error $\max_{nh \le T} \abs{(x_n, v_n) - (x(nh), x'(nh))}$ is $O(h^2)$ as $h \to 0$.

## Remarks

The equation is the [[Hamiltonian system|0EDKGA2FAK]] with $H(x, v) = \frac12 \abs{v}^2 + V(x)$.
Each of the three substeps is the exact flow, for time $h/2$, $h$ or $h/2$, of the Hamiltonian $V(x)$ or $\frac12\abs{v}^2$.
Exact Hamiltonian flows are symplectic, and so is their composition, which gives clause 1.
The composition is symmetric, which gives clause 2, and a symmetric method has even order, which together with consistency gives clause 3.
So leapfrog is a [[symplectic integrator|B4C25SXFRE]], and its energy error stays bounded over very long times instead of growing.
Example: for $a(x) = -x$ in one dimension, $\Phi_h$ is a linear map with determinant $1$ and trace $2 - h^2$.
For $0 < h < 2$ its eigenvalues are distinct and lie on the unit circle, so all orbits stay bounded.

## Explanations

### L1 human

Positions and velocities are updated in turn, as if they leapt over each other.
The velocity takes half a kick from the force, the position drifts for a full step, and the velocity takes the second half kick.
The method costs one force evaluation per step, and it keeps the energy of a planet or a molecule from slowly creeping away.

### L2 human

Leapfrog is the Störmer–Verlet method written in one-step form, and it is the standard integrator of molecular dynamics and of $N$-body simulations.
It is the simplest example of a splitting method: it is the Strang composition of the kinetic and potential flows.
Higher-order symplectic methods are often built by composing leapfrog steps with well-chosen step sizes.
