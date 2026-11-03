---
tag: 4THA6F9HFN
kind: definition
name: Fidelity of quantum states
msc: [81P47, 81P16]
defines: A8D05RKX8M
uses: [V1JTB52E8C, 3JY5HNFRMF, 0XC1RDBY7A]
sources:
  - url: https://en.wikipedia.org/wiki/Fidelity_of_quantum_states
---

## Definition

Let $H$ be a finite-dimensional complex Hilbert space, and let $\rho$ and $\sigma$ be [[density operators|V1JTB52E8C]] on $H$.
The *fidelity* of $\rho$ and $\sigma$ is
$$F(\rho, \sigma) = \left( \tr \sqrt{\sqrt{\rho}\, \sigma \sqrt{\rho}} \right)^2,$$
where $\sqrt{A}$ is the [[square root|3JY5HNFRMF]] of a positive operator $A$ and $\tr$ is the [[trace|0XC1RDBY7A]].

## Remarks

Example: let $\rho = \lvert \psi \rangle\langle \psi \rvert$ be pure.
Then $\sqrt\rho = \rho$ and $\sqrt\rho\, \sigma \sqrt\rho = \langle \psi \rvert\sigma\lvert \psi \rangle\, \rho$, so $F(\rho, \sigma) = \langle \psi \rvert\sigma\lvert \psi \rangle$.
If $\sigma = \lvert \phi \rangle\langle \phi \rvert$ is pure too, then $F = \abs{\ip{\psi}{\phi}}^2$.

Non-example: the overlap $\tr(\rho\sigma)$ is not the fidelity for mixed states.
For $\rho = \sigma = I/2$ on $\C^2$, $\tr(\rho\sigma) = 1/2$, while $F(\rho, \sigma) = (\tr (I/2))^2 = 1$.

Standard properties: $0 \le F(\rho, \sigma) \le 1$; $F(\rho, \sigma) = 1$ if and only if $\rho = \sigma$; $F(\rho, \sigma) = F(\sigma, \rho)$.
Equivalently $F(\rho, \sigma) = \norm{\sqrt\rho \sqrt\sigma}_1^2$, where $\norm{A}_1 = \tr\sqrt{A^* A}$ is the trace norm.
Some authors call the square root $\sqrt{F}$ the fidelity, so the convention must be checked.
