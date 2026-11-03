---
tag: 6A102ZKNQT
kind: definition
name: Quantum Fisher information
msc: [81P50, 62B10, 81P16]
defines: CSQJZVXNBE
uses: [V1JTB52E8C, 0XC1RDBY7A, 0NEGN5CRSC, G1Z3WSTE8Q, 1JFKTEQVRX]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Fisher_information
---

## Definition

Let $H$ be a finite-dimensional complex Hilbert space and let $\Theta \subseteq \R$ be an open interval.
Let $\theta \mapsto \rho_\theta$ be a differentiable map from $\Theta$ to the [[density operators|V1JTB52E8C]] on $H$, and write $\partial_\theta \rho_\theta$ for its derivative.
A *symmetric logarithmic derivative* at $\theta$ is a [[self-adjoint operator|0NEGN5CRSC]] $L_\theta$ on $H$ with
$$\partial_\theta \rho_\theta = \frac12 \left( \rho_\theta L_\theta + L_\theta \rho_\theta \right).$$
The *quantum Fisher information* of the family at $\theta$ is
$$F_Q(\theta) = \tr\left( \rho_\theta L_\theta^2 \right).$$
It does not depend on the choice of $L_\theta$.

## Remarks

In an eigenbasis $\rho_\theta = \sum_k \lambda_k \lvert k \rangle \langle k \rvert$, one has
$$F_Q(\theta) = 2 \sum_{k, l \,:\, \lambda_k + \lambda_l > 0} \frac{\abs{\langle k \rvert \partial_\theta \rho_\theta \lvert l \rangle}^2}{\lambda_k + \lambda_l}.$$

Example: let $\rho_\theta = \lvert \psi_\theta \rangle \langle \psi_\theta \rvert$ with $\psi_\theta = e^{-i\theta A}\psi$ for a unit vector $\psi$ and a self-adjoint $A$.
Since $\rho_\theta^2 = \rho_\theta$, differentiation gives $\partial_\theta\rho_\theta = \rho_\theta (\partial_\theta\rho_\theta) + (\partial_\theta\rho_\theta)\rho_\theta$, so $L_\theta = 2\partial_\theta \rho_\theta$ works.
With $\partial_\theta \rho_\theta = -i[A, \rho_\theta]$ this gives $F_Q = 4 \left( \langle A^2 \rangle - \langle A \rangle^2 \right)$, four times the variance of $A$ in $\psi$.
For $\psi = (\lvert 0 \rangle + \lvert 1 \rangle)/\sqrt2$ and $A = \frac12 \operatorname{diag}(1, -1)$, the variance is $1/4$, so $F_Q = 1$.

Contrast: the classical [[Fisher information|G1Z3WSTE8Q]] of the outcomes of one fixed measurement is at most $F_Q(\theta)$, and it can be smaller.
In the example, a measurement in the basis $\lvert 0 \rangle, \lvert 1 \rangle$ gives probabilities $1/2, 1/2$ for every $\theta$, so its Fisher information is $0$.

The quantum Cramér–Rao bound states that every unbiased estimator of $\theta$ built from $n$ copies of $\rho_\theta$ has variance at least $1/(n F_Q(\theta))$; compare the classical [[Cramér–Rao bound|1JFKTEQVRX]].
Up to a constant factor, $F_Q$ is the Bures metric on the manifold of density operators.
