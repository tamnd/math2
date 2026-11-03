---
tag: XJNTZZ7MM5
kind: definition
name: Geometric phase
msc: [81Q70, 53C29]
defines: 7BJM2TRPK2
uses: [HM2HHE3J51, 0NEGN5CRSC, 0N6960W0BV, WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_phase
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]], and let $M$ be a smooth manifold of parameters.
Let $R \mapsto H(R)$, $R \in M$, be a smooth family of [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}$.
Let $E(R)$ be a simple eigenvalue of $H(R)$ depending smoothly on $R$.
Let $R \colon [0, 1] \to M$ be a smooth closed loop, $R(0) = R(1)$.
Choose a smooth curve $u \colon [0, 1] \to \mathcal{H}$ of unit [[eigenvectors|0N6960W0BV]], $H(R(t)) u(t) = E(R(t)) u(t)$, that satisfies the parallel transport condition
$$\ip{u(t)}{u'(t)} = 0 \quad \text{for all } t.$$
Then $u(1) = e^{i\gamma} u(0)$ for a real number $\gamma$, and $\gamma$ modulo $2\pi$ is the *geometric phase* (or *Berry phase*) of the loop.

## Remarks

Such a curve $u$ exists and is unique up to a constant phase, so $\gamma$ is well defined modulo $2\pi$.
Let $n(R)$ be a smooth choice of unit eigenvector on a neighbourhood of the loop.
Then $\gamma = i \oint \ip{n}{dn}$, the integral of the Berry connection $\mathcal{A} = i\ip{n}{dn}$, a real 1-form.
Changing $n$ to $e^{i\chi(R)} n$ changes $\gamma$ by a multiple of $2\pi$.
When the loop bounds a surface $S$, $\gamma = \int_S d\mathcal{A}$, the flux of the Berry curvature.
In geometric terms $\gamma$ is the [[holonomy|WHDZ3MK56B]] of the loop for the connection induced on the line bundle of eigenvectors.

Example: let $H(R) = -R \cdot \sigma$ for $R$ on the unit sphere $S^2$, where $\sigma = (\sigma_x, \sigma_y, \sigma_z)$ are the Pauli matrices, and take the lower eigenvalue $E(R) = -1$.
For a loop enclosing the solid angle $\Omega$, $\gamma \equiv \pm \Omega/2 \pmod{2\pi}$, the sign depending on the orientation of the loop.

Non-example: let every $H(R)$ be a real symmetric matrix.
Then the eigenvectors can be chosen real, and $\ip{n}{dn} = \frac12 d\ip{n}{n} = 0$.
So the only possible phases are $0$ and $\pi$, the latter when $n$ returns as $-n$.
An open path also has no well-defined geometric phase, since the phase of $u(1)$ relative to $u(0)$ depends on the choices made.
