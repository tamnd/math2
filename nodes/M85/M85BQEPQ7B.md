---
tag: M85BQEPQ7B
kind: definition
name: Quantum electrodynamics
msc: [81V10, 81T13]
defines: V329C7A1QP
uses: [BXVB6WCMEV, XNZX7VXXR2, TDPX0D7ZD0, BQFCNWFV9Q, 60K3E80KCV, SANYJGZ311]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_electrodynamics
---

## Definition

Work on Minkowski space $\R^{1,3}$ with metric of signature $(+,-,-,-)$, in units with $\hbar = c = 1$.
Let $\gamma^0, \dots, \gamma^3$ be the [[gamma matrices|TDPX0D7ZD0]], with $\gamma^\mu \gamma^\nu + \gamma^\nu \gamma^\mu = 2\eta^{\mu\nu} I_4$.
The fields are a real [[electromagnetic four-potential|BQFCNWFV9Q]] $A_\mu$ and a Dirac spinor field $\psi$ with values in $\C^4$; write $\bar\psi = \psi^\dagger \gamma^0$.
Fix a mass $m \ge 0$ and a coupling constant $e > 0$.
*Quantum electrodynamics* is the quantization of a [[gauge theory|2GKJQNQMVN]] with gauge group $U(1)$.
Its [[Lagrangian density|SANYJGZ311]] is
$$\mathcal{L} = \bar\psi \left( i \gamma^\mu D_\mu - m \right) \psi - \frac{1}{4} F_{\mu\nu} F^{\mu\nu},$$
where $D_\mu = \partial_\mu + i e A_\mu$ is the covariant derivative and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is the [[electromagnetic tensor|60K3E80KCV]].

## Remarks

Gauge invariance: for a real function $\lambda$, the transformation $\psi \mapsto e^{-ie\lambda}\psi$, $A_\mu \mapsto A_\mu + \partial_\mu \lambda$ leaves $\mathcal{L}$ unchanged.
Indeed $D_\mu \psi$ becomes $(\partial_\mu + ieA_\mu + ie\partial_\mu\lambda)(e^{-ie\lambda}\psi) = e^{-ie\lambda} D_\mu\psi$, and $F_{\mu\nu}$ does not change.

Non-example: the Lagrangian $\bar\psi (i\gamma^\mu \partial_\mu - m)\psi - \frac14 F_{\mu\nu}F^{\mu\nu}$ without the coupling term is invariant only when $\lambda$ is constant.
The term $-e \bar\psi \gamma^\mu \psi A_\mu$ inside $\bar\psi i\gamma^\mu D_\mu \psi$ is what makes the symmetry local, and it describes the emission and absorption of photons.

The Euler–Lagrange equations are the Dirac equation $(i\gamma^\mu D_\mu - m)\psi = 0$ and Maxwell's equations $\partial_\mu F^{\mu\nu} = e \bar\psi \gamma^\nu \psi$, with the Dirac current as source.
For the electron, $m$ is the electron mass and $e^2 / (4\pi) \approx 1/137$ is the fine-structure constant.
Sign conventions for $e$ and for the metric vary between books.
No construction of QED that satisfies the axioms of quantum field theory is known; in practice the theory is defined order by order in $e$ through [[renormalization|1X0W3AEBEJ]].
