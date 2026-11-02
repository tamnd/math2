---
tag: QP0MY1E9RK
kind: definition
name: Symplectomorphism
msc: [53D05, 53D22]
defines: A8TS2SNX9Z
uses: [CAN490EPRT, 0KZZ70ZHXP, 0E3G0GRPZ6, X12FS2JAP0, C5EH3B4BEP]
sources:
  - url: https://en.wikipedia.org/wiki/Symplectomorphism
---

## Definition

Let $(M, \omega)$ and $(N, \eta)$ be [[symplectic manifolds|CAN490EPRT]].
A *symplectomorphism* from $M$ to $N$ is a [[diffeomorphism|0KZZ70ZHXP]] $\phi \colon M \to N$ such that $\phi^* \eta = \omega$, that is
$$\eta_{\phi(p)}\big(d\phi_p(v), d\phi_p(w)\big) = \omega_p(v, w)$$
for all $p \in M$ and $v, w \in T_p M$.

## Remarks

Example: on $\R^2$ with $\omega = dx \wedge dy$, let $\phi(x, y) = (x, y + f(x))$ for a smooth function $f$.
It is a diffeomorphism with inverse $(x, y) \mapsto (x, y - f(x))$, and $\phi^* \omega = dx \wedge (dy + f'(x)\, dx) = dx \wedge dy$.

Non-example: $\psi(x, y) = (2x, y)$ on the same plane is a diffeomorphism, but $\psi^* \omega = 2\, dx \wedge dy \ne \omega$.

A linear map of $(\R^{2n}, \omega_0)$ is a symplectomorphism exactly when it lies in the [[symplectic group|X12FS2JAP0]] $Sp(2n, \R)$.
The flow of a [[Hamiltonian vector field|C5EH3B4BEP]] consists of symplectomorphisms.
A symplectomorphism preserves the volume form $\omega^n / n!$, so it preserves volume; in dimension $2$ the converse holds for orientation-preserving diffeomorphisms.
