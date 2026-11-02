---
tag: RMEF8T6C0E
kind: definition
name: Tomita–Takesaki theory
msc: [46L10, 46L40]
defines: NBR81PR7E5
uses: [PSFWQVZ0FS, 1VC7EJ1ZBZ, HM2HHE3J51, KRJX5RA0PW, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Tomita–Takesaki_theory
---

## Definition

Let $M$ be a [[von Neumann algebra|PSFWQVZ0FS]] on a complex [[Hilbert space|HM2HHE3J51]] $H$, with [[commutant|1VC7EJ1ZBZ]] $M'$.
Let $\Omega \in H$ be cyclic for $M$, that is, $M\Omega$ is dense in $H$.
Assume also that $\Omega$ is separating for $M$: if $x \in M$ and $x\Omega = 0$, then $x = 0$.

1. The operator $S_0$ with domain $M\Omega$ defined by $S_0(x\Omega) = x^*\Omega$ is a well-defined, densely defined, closable antilinear [[unbounded operator|KRJX5RA0PW]]; let $S$ be its closure.
2. The *modular operator* is the positive self-adjoint operator $\Delta = S^* S$, and the *modular conjugation* is the antiunitary operator $J$ in the polar decomposition $S = J \Delta^{1/2}$.
3. The *modular automorphism group* is $\sigma_t(x) = \Delta^{it} x \Delta^{-it}$ for $t \in \R$ and $x \in M$.

*Tomita–Takesaki theory* is the study of these objects.
Its main theorem states that $J M J = M'$ and $\Delta^{it} M \Delta^{-it} = M$ for all $t \in \R$.
So each $\sigma_t$ is an automorphism of $M$.

## Remarks

Example: let $M = M_n(\C)$ act by left multiplication on $H = M_n(\C)$ with inner product $\langle \xi, \eta \rangle = \operatorname{tr}(\eta^* \xi)$, and let $\Omega = \rho^{1/2}$ for an invertible density matrix $\rho$.
Then $\Omega$ is cyclic and separating, $\Delta \xi = \rho \xi \rho^{-1}$ and $J \xi = \xi^*$.
Check: $J \Delta^{1/2}(x \rho^{1/2}) = J(\rho^{1/2} x) = x^* \rho^{1/2} = S(x\rho^{1/2})$.
Here $JMJ$ is the algebra of right multiplications, which is $M'$, and $\sigma_t(x) = \rho^{it} x \rho^{-it}$.

Non-example: let $M = B(H)$ with $\dim H \ge 2$, let $\Omega$ be a unit vector, and let $\eta$ be a unit vector orthogonal to $\Omega$.
Every nonzero vector is cyclic for $B(H)$, but $\Omega$ is not separating.
Indeed, the operator $x = \langle \cdot, \eta \rangle \Omega$ is nonzero and $x\Omega = 0$.
Its adjoint is $x^* = \langle \cdot, \Omega \rangle \eta$, so $x^*\Omega = \eta \ne 0$.
Since $x\Omega = 0\Omega$ but $x^*\Omega \ne 0^*\Omega$, the formula for $S_0$ does not define a map.

The vector state $\varphi(x) = \langle x\Omega, \Omega \rangle$ is a KMS state for the modular automorphism group, and Takesaki showed that $\sigma$ is the only one-parameter automorphism group of $M$ with this property.
