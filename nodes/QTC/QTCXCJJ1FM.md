---
tag: QTCXCJJ1FM
kind: definition
name: Statistical ensemble
msc: [82B03, 82B05]
defines: M0JYTP1C8B
uses: [S1NST0AG71, 059TJN0NZ1, N4KDT83V3S, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Ensemble_(mathematical_physics)
---

## Definition

Let $\Omega$ be the set of [[microstates|S1NST0AG71]] of a classical system, made into a [[measurable space|N4KDT83V3S]].
A *statistical ensemble* for the system is a [[probability measure|059TJN0NZ1]] $\mu$ on $\Omega$.
The ensemble average of an integrable observable $A \colon \Omega \to \R$ is its [[expected value|0WQNRCNY3M]] $\langle A \rangle_\mu = \int_\Omega A \, d\mu$.
For a quantum system with Hilbert space $\mathcal{H}$, an ensemble is a density operator $\rho$.
This is a positive trace-class operator on $\mathcal{H}$ with trace $1$.
The average of a bounded observable $A$ is then $\tr(\rho A)$.
An ensemble is *stationary* (an equilibrium ensemble) if it is invariant under the time evolution of the system.

## Remarks

Example: for a system with finitely many microstates $\Omega = \set{1, \dots, n}$, any probability vector $(p_1, \dots, p_n)$ with $p_i \ge 0$ and $\sum_i p_i = 1$ is an ensemble, and $\langle A \rangle = \sum_i p_i A(i)$.
Non-example: the weights $p_i = 1$ for all $i$ with $n \ge 2$ do not form an ensemble, since they sum to $n \ne 1$; dividing by $n$ gives the uniform ensemble.
In classical mechanics, let an ensemble have a density $\rho$ with respect to Liouville measure on phase space.
It is stationary when $\rho$ is constant along trajectories.
Any density of the form $\rho = g(H)$, with $H$ the Hamiltonian, is stationary.
