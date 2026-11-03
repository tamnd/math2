---
tag: 5QM8GM3NRD
kind: definition
name: Phonon dispersion in lattices
msc: [74J05, "74E15", 74A25]
defines: 6T7S8QEBKY
uses: [0YG0ZJPTWG, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Phonon
---

## Definition

Let $\Lambda = \set{R_n}$ be a lattice of translations of $\R^d$, and let a crystal have $r$ atoms in each cell, with masses $m_1, \dots, m_r > 0$.
Write $u_{n\kappa}(t) \in \R^d$ for the displacement of atom $\kappa$ of cell $n$ from its rest position.
The harmonic approximation gives these equations of motion:
$$m_\kappa \, \ddot u_{n\kappa\alpha} = -\sum_{n', \kappa', \beta} \Phi_{\kappa\alpha, \kappa'\beta}(R_{n'} - R_n) \, u_{n'\kappa'\beta}.$$
The force constants $\Phi$ are real, depend only on the difference of the cells, and satisfy $\Phi_{\kappa\alpha,\kappa'\beta}(R) = \Phi_{\kappa'\beta,\kappa\alpha}(-R)$.
For a wave vector $k \in \R^d$ the *dynamical matrix* $D(k)$ is the $dr \times dr$ matrix with entries
$$D_{\kappa\alpha, \kappa'\beta}(k) = \frac{1}{\sqrt{m_\kappa m_{\kappa'}}} \sum_{R \in \Lambda} \Phi_{\kappa\alpha, \kappa'\beta}(R) \, e^{i k \cdot R}.$$
The matrix $D(k)$ is Hermitian.
The *phonon dispersion relation* is the family of maps $k \mapsto \omega_j(k)$, $j = 1, \dots, dr$, where $\omega_j(k)^2$ are the [[eigenvalues|0BQAA2BK3Q]] of $D(k)$.
For each $j$, the motions $u_{n\kappa} = m_\kappa^{-1/2} e_\kappa \, e^{i(k \cdot R_n - \omega_j(k) t)}$, with $e$ an eigenvector, are the plane-wave solutions.

## Remarks

Example: the one-dimensional chain with $d = r = 1$, spacing $a$, mass $m$ and springs $K$ between neighbours has $m \ddot u_n = K(u_{n+1} - 2u_n + u_{n-1})$.
Inserting $u_n = e^{i(kna - \omega t)}$ gives $m \omega^2 = 2K(1 - \cos ka) = 4K \sin^2(ka/2)$, so $\omega(k) = 2\sqrt{K/m} \, \abs{\sin(ka/2)}$.
For small $k$ this is $\omega \approx a\sqrt{K/m}\,\abs{k}$, a sound wave with speed $a\sqrt{K/m}$.

Non-example: if the interatomic potential is kept beyond second order, the equations of motion are nonlinear, and plane waves with a fixed frequency are no longer exact solutions.

The crystal is stable exactly when every $D(k)$ is positive semidefinite, and then all $\omega_j(k)$ are real.
Each $\omega_j$ is periodic under translations of $k$ by the reciprocal lattice, so it suffices to study $k$ in one Brillouin zone.
In $d = 3$ there are $3$ acoustic branches, which vanish at $k = 0$, and $3r - 3$ optical branches.
Each normal mode is a [[harmonic oscillator|0YG0ZJPTWG]], and its quantum is called a phonon.
