---
tag: SK1Q8B6MEA
kind: definition
name: Expectation value
msc: ["81Q10", "81P15"]
defines: JNK7GJ3AKE
uses: [DF5RN297GE, 4NQN47A92F, V1JTB52E8C, Z2CP530WDE]
sources:
  - url: https://en.wikipedia.org/wiki/Expectation_value_(quantum_mechanics)
---

## Definition

Let $\mathcal{H}$ be a complex Hilbert space with inner product $\ip{\cdot}{\cdot}$, conjugate-linear in the first argument.
Let $A$ be an [[observable|DF5RN297GE]] on $\mathcal{H}$ with domain $D(A)$.

1. For a unit vector $\psi \in D(A)$, the *expectation value* of $A$ in the pure [[state|4NQN47A92F]] $\psi$ is $\langle A \rangle_\psi = \ip{\psi}{A\psi}$.
2. For a [[density operator|V1JTB52E8C]] $\rho$ and a bounded observable $A$, the expectation value of $A$ in the state $\rho$ is $\langle A \rangle_\rho = \operatorname{tr}(\rho A)$.

## Remarks

Both numbers are real, because $A$ is self-adjoint.
In clause 2 the product $\rho A$ is a [[trace class operator|Z2CP530WDE]], since the trace class operators form an ideal.
For a pure state $\rho = \lvert \psi \rangle\langle \psi \rvert$ and a bounded $A$, the two clauses agree: $\operatorname{tr}(\rho A) = \ip{\psi}{A\psi}$.
If $\psi \in D(A)$ and $P^A$ is the projection-valued measure of $A$, then $\ip{\psi}{A\psi} = \int_\R \lambda \, d\mu(\lambda)$ with $\mu(B) = \norm{P^A(B)\psi}^2$, the mean of the distribution of results.

Example: on $\C^2$, let $\sigma_z = \mathrm{diag}(1, -1)$ and $\psi = (1, 1)/\sqrt{2}$.
Then $\sigma_z \psi = (1, -1)/\sqrt{2}$ and $\langle \sigma_z \rangle_\psi = \frac12 (1 - 1) = 0$.

Non-example: on $L^2(\R)$, let $X$ be the position operator and $\psi(x) = \pi^{-1/2} (1 + x^2)^{-1/2}$.
Then $\norm{\psi} = 1$, but $x\psi(x)$ is not square-integrable, so $\psi \notin D(X)$ and $\langle X \rangle_\psi$ is not defined.
Here $\abs{\psi}^2$ is the Cauchy density, which has no mean.
