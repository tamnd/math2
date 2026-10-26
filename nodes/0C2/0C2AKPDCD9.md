---
tag: 0C2AKPDCD9
kind: definition
name: Hamiltonian system
msc: [37J06, 70H05]
defines: 0EDKGA2FAK
uses: [07BNRFQ0PJ, 0SS1P1YC9A]
sources:
  - url: https://en.wikipedia.org/wiki/Hamiltonian_system
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Hamiltonian_system
    locator: Time-independent Hamiltonian systems
---

## Definition

Let $n \ge 1$, let $U$ be an open subset of $\mathbb{R}^n \times \mathbb{R}^n$ with coordinates $(q, p) = (q_1, \ldots, q_n, p_1, \ldots, p_n)$, and let $H : U \to \mathbb{R}$ be continuously differentiable.
The Hamiltonian system with Hamiltonian $H$ is the [[autonomous system|07BNRFQ0PJ]]
$$q_i' = \frac{\partial H}{\partial p_i}(q, p), \qquad p_i' = -\frac{\partial H}{\partial q_i}(q, p), \qquad i = 1, \ldots, n.$$

## Remarks

The function $H$ is a [[first integral|0SS1P1YC9A]] when it is not constant on an open set: along a solution, $\frac{d}{dt} H = \sum_i \left( \frac{\partial H}{\partial q_i} q_i' + \frac{\partial H}{\partial p_i} p_i' \right) = 0$.
For $H(q, p) = \frac{1}{2} p^2 + V(q)$ with $n = 1$, the system is $q' = p$, $p' = -V'(q)$. This is Newton's law $q'' = -V'(q)$ for a particle with potential energy $V$.
The [[harmonic oscillator|0YG0ZJPTWG]] has $V(q) = \frac{1}{2} q^2$, and the [[pendulum|0SHPXM2HWH]] has $V(q) = -\cos q$ in suitable units.
A time-dependent Hamiltonian $H(t, q, p)$ gives a non-autonomous Hamiltonian system, and then $H$ need not be conserved.

## Explanations

### L1 human

A Hamiltonian system describes a mechanical system without friction by one function, the total energy $H$.
The positions $q$ and the momenta $p$ change according to the partial derivatives of $H$, and the energy stays constant.
