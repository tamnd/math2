---
tag: 3ANCZ518BN
kind: definition
name: Quadratic polynomial dynamics
msc: [37F10, 37F46]
defines: WDZFV2ACXR
uses: [BQQZ0ZCGQF, 1G0B73WPX8, 5M4S7P04GR, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_quadratic_polynomial
---

## Definition

For $c \in \C$ let $f_c \colon \C \to \C$ be the polynomial $f_c(z) = z^2 + c$.
The family $(f_c)_{c \in \C}$ is the *quadratic family*.
*Quadratic polynomial dynamics* is the [[complex dynamics|BQQZ0ZCGQF]] of this family.
It studies the [[iterates|AYVTR2ES5B]] $f_c^n$ for each $c$, and how they change with $c$.
The *filled Julia set* of $f_c$ is $K_c = \set{z \in \C : (f_c^n(z))_{n \ge 0} \text{ is bounded}}$.
Its boundary $\partial K_c$ is the [[Julia set|5M4S7P04GR]] $J_c$ of $f_c$.

## Remarks

Every [[polynomial|1G0B73WPX8]] $p(z) = a z^2 + b z + d$ with $a \ne 0$ is conjugate to exactly one $f_c$ by an affine map $z \mapsto \alpha z + \beta$.
This is why one parameter suffices.
The only critical point of $f_c$ in $\C$ is $0$.
The set $K_c$ is connected if and only if the orbit of $0$ is bounded, and otherwise $K_c$ is a Cantor set.
Example: for $c = 0$, $f_0^n(z) = z^{2^n}$ is bounded exactly when $\abs{z} \le 1$, so $K_0$ is the closed unit disc and $J_0$ is the unit circle.
Non-example: $z \mapsto z^3 + c$ is not in the quadratic family, since its degree is $3$.
