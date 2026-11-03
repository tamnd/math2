---
tag: XSTFW4AW3N
kind: definition
name: Hidden-variable theory
msc: [81P05]
defines: QRW6NE1VY7
uses: [059TJN0NZ1, HM2HHE3J51, 4NQN47A92F, MF4DYZ4YAX]
sources:
  - url: https://en.wikipedia.org/wiki/Hidden-variable_theory
---

## Definition

Let $\mathcal{H}$ be a finite-dimensional complex [[Hilbert space|HM2HHE3J51]].
A *hidden-variable theory*, or *ontological model*, of quantum mechanics on $\mathcal{H}$ consists of the following data:

1. a measurable space $(\Lambda, \mathcal{F})$, whose points $\lambda$ are the hidden variables, or ontic states;
2. for each pure [[quantum state|4NQN47A92F]] $\psi$, a [[probability measure|059TJN0NZ1]] $\mu_\psi$ on $\Lambda$;
3. for each orthonormal basis $M = (m_1, \dots, m_d)$ of $\mathcal{H}$, measurable functions $\xi_M(k \mid \cdot) \colon \Lambda \to [0, 1]$ with $\sum_{k=1}^d \xi_M(k \mid \lambda) = 1$ for all $\lambda$.

It must reproduce the [[Born rule|MF4DYZ4YAX]]: $\int_\Lambda \xi_M(k \mid \lambda)\, d\mu_\psi(\lambda) = \abs{\langle m_k, \psi \rangle}^2$ for all $\psi$, $M$ and $k$.
The theory is *deterministic* if all values $\xi_M(k \mid \lambda)$ are $0$ or $1$.

## Remarks

Example: the Beltrametti–Bugajski model takes $\Lambda$ to be the set of unit vectors up to phase, $\mu_\psi$ the point mass at $\psi$, and $\xi_M(k \mid \lambda) = \abs{\langle m_k, \lambda \rangle}^2$.
The Born rule holds by construction, so every quantum system has this trivial model.
Non-example: taking $\xi_M(k \mid \lambda) = 1/d$ for all $k$ satisfies clause 3, but it gives probability $1/d$ instead of $1$ when $\psi = m_1$ and $k = 1$.
A deterministic theory is *noncontextual* if the value of $\xi_M(k \mid \lambda)$ depends only on the ray of $m_k$ and not on the rest of the basis $M$.
For a bipartite system, the theory is *local* if the response functions for a product measurement factorize into a function of the local setting on each side.

## Explanations

### L1 human

A hidden-variable theory replaces each quantum state by a probability distribution over more detailed "real" states.
Each real state decides, or gives probabilities for, the outcome of every measurement.
Averaged over the distribution, these outcomes must match the quantum predictions.
