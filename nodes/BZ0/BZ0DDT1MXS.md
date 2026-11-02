---
tag: BZ0DDT1MXS
kind: definition
name: Poincaré's functional equation
msc: [39B32, 30D05, 37F10]
defines: 3384ZV3PWM
uses: [0NAHXR1FRH, R6QVS6P21N, SRAN4EKWS0, VTJV7JVJEA, 0G4F0XB9X2]
sources:
  - url: https://en.wikipedia.org/wiki/Schr%C3%B6der%27s_equation
---

## Definition

Let $U \subseteq \C$ be an open set containing $0$, and let $f \colon U \to \C$ be [[holomorphic|0NAHXR1FRH]] with $f(0) = 0$.
Let $\lambda = f'(0)$.
*Poincaré's functional equation* for $f$ is the [[functional equation|SRAN4EKWS0]]
$$\Psi(\lambda z) = f(\Psi(z)) \quad \text{for all } z \text{ near } 0.$$
The unknown is a holomorphic function $\Psi$ on a neighbourhood of $0$ with $\Psi(0) = 0$ and $\Psi'(0) = 1$.

## Remarks

Example: $f(w) = w^2 + 2w$ has $f(0) = 0$ and $\lambda = f'(0) = 2$.
The function $\Psi(z) = e^z - 1$ satisfies $\Psi(0) = 0$, $\Psi'(0) = 1$ and $f(\Psi(z)) = (e^z - 1)^2 + 2(e^z - 1) = e^{2z} - 1 = \Psi(2z)$.

Non-example: for the same $f$, the function $\Psi(z) = z$ fails, since $f(z) = z^2 + 2z \ne 2z$ for $z \ne 0$.

If $\Phi$ is a solution of [[Schröder's equation|VTJV7JVJEA]] $\Phi \circ f = \lambda \Phi$ with $\Phi(0) = 0$ and $\Phi'(0) = 1$, then its local inverse $\Psi = \Phi^{-1}$ solves Poincaré's equation.
So for $\abs{\lambda} > 1$ a unique solution exists, by the Koenigs linearization theorem applied to $f$.
Assume moreover that $f$ is [[entire|0G4F0XB9X2]].
Then the formula $\Psi(z) = f^n(\Psi(z / \lambda^n))$, with $n$ so large that $z / \lambda^n$ lies in the domain of $\Psi$, extends $\Psi$ to an entire function.
This function is the Poincaré function of $f$ at $0$.
