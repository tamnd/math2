---
tag: 5SGDSVT2FC
kind: definition
name: Molecular dynamics
msc: [82M37, 65P10]
defines: P6HAX0MH0B
uses: [KNBP19FG6K, ESWE8Y3JD4, 0EDKGA2FAK, B4C25SXFRE, 3MY6RYD0PD, TDGEGWHXCT]
sources:
  - url: https://en.wikipedia.org/wiki/Molecular_dynamics
---

## Definition

Consider $N$ particles in $\R^3$ with masses $m_i > 0$, positions $q_i(t)$ and velocities $v_i(t)$, and a differentiable potential energy $U(q_1, \dots, q_N)$.
The equations of motion are [[Newton's equations|KNBP19FG6K]] $m_i \ddot q_i = F_i(q)$ with forces $F_i = -\nabla_{q_i} U$.
A *molecular dynamics* simulation with time step $\Delta t > 0$ computes approximations $(q^k, v^k)$ of the state at times $k \Delta t$.
It uses a numerical integrator, usually the velocity [[Verlet scheme|ESWE8Y3JD4]]:
$$q_i^{k+1} = q_i^k + \Delta t \, v_i^k + \frac{\Delta t^2}{2 m_i} F_i(q^k), \qquad v_i^{k+1} = v_i^k + \frac{\Delta t}{2 m_i} \big( F_i(q^k) + F_i(q^{k+1}) \big).$$
It estimates the average of an observable $A$ by the time average $\frac{1}{K} \sum_{k=1}^{K} A(q^k, v^k)$.

## Remarks

The exact flow is a [[Hamiltonian system|0EDKGA2FAK]] that conserves the energy $\sum_i \frac12 m_i \abs{v_i}^2 + U(q)$.
The velocity Verlet scheme is a [[symplectic integrator|B4C25SXFRE]] of second order and is time-reversible, so the computed energy does not drift but oscillates near its initial value for long times.
Under the [[ergodic hypothesis|3MY6RYD0PD]], time averages approximate averages in the [[microcanonical ensemble|TDGEGWHXCT]]; thermostats, such as stochastic Langevin forces, are added to sample the canonical ensemble instead.
Example: one particle of mass $m$ in the potential $U(q) = \frac12 k q^2$ is a harmonic oscillator, and velocity Verlet is stable exactly when $\Delta t < 2 / \omega$ with $\omega = \sqrt{k/m}$.
Non-example: the explicit Euler scheme $q^{k+1} = q^k + \Delta t \, v^k$, $v^{k+1} = v^k + \Delta t \, F(q^k)/m$ is not symplectic, and for the harmonic oscillator its energy grows by the factor $1 + \omega^2 \Delta t^2$ at every step.

## Explanations

### L1 human

The definition says: write down the forces, solve Newton's equations step by step, and average along the computed path.
The choice of integrator matters, because a simulation runs for millions of steps and small systematic errors add up.
