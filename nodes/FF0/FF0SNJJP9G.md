---
tag: FF0SNJJP9G
kind: definition
name: Quantum statistical mechanics
msc: [82B10, 82C10, 46L60]
defines: 259STBGWK8
uses: [M0JYTP1C8B, HM2HHE3J51, 0NEGN5CRSC, Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_statistical_mechanics
---

## Definition

*Quantum statistical mechanics* studies quantum systems through ensembles of quantum states.
A system is given by a complex separable [[Hilbert space|HM2HHE3J51]] $\mathcal{H}$ and a [[self-adjoint|0NEGN5CRSC]] Hamiltonian $H$ on $\mathcal{H}$.

1. A *density operator* is a positive [[trace-class operator|Z2CP530WDE]] $\rho$ on $\mathcal{H}$ with $\tr \rho = 1$; it is the quantum [[statistical ensemble|M0JYTP1C8B]].
2. The expected value of a bounded self-adjoint observable $A$ in the state $\rho$ is $\tr(\rho A)$.
3. If $e^{-\beta H}$ is trace class for some $\beta > 0$, the canonical (Gibbs) state is $\rho_\beta = e^{-\beta H} / Z(\beta)$, with partition function $Z(\beta) = \tr e^{-\beta H}$.

The time evolution of a density operator is $\rho(t) = e^{-itH/\hbar} \rho \, e^{itH/\hbar}$.

## Remarks

Example: a spin $\tfrac{1}{2}$ in a magnetic field has $\mathcal{H} = \C^2$ and $H = \operatorname{diag}(-\varepsilon, \varepsilon)$ with $\varepsilon > 0$.
Then $Z(\beta) = 2 \cosh(\beta \varepsilon)$ and $\rho_\beta = \operatorname{diag}(e^{\beta \varepsilon}, e^{-\beta \varepsilon}) / Z(\beta)$, a positive matrix of trace $1$.
Non-example: the operator $\operatorname{diag}(1, -\tfrac{1}{2}, \tfrac{1}{2})$ on $\C^3$ has trace $1$ but is not positive, so it is not a density operator.
For the free particle in $L^2(\R^3)$, $e^{-\beta H}$ is not trace class; one first confines the particle to a box.
For infinite systems, Gibbs states are replaced by KMS states on a C\*-algebra of observables.
