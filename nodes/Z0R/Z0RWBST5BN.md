---
tag: Z0RWBST5BN
kind: definition
name: Chern–Simons form
msc: [53C05, 57R20]
defines: X83ECKQ6G8
uses: [0E3G0GRPZ6, 0ZHSTAG8ZY, 0GRAATMGP1, ZAJFW1S078, 82ZPRD39J7]
sources:
  - url: https://en.wikipedia.org/wiki/Chern%E2%80%93Simons_form
---

## Definition

Let $M$ be a smooth manifold, and let $\mathfrak{gl}_n(\C)$ be the space of complex $n \times n$ matrices.
Let $A$ be a smooth $\mathfrak{gl}_n(\C)$-valued [[$1$-form|0E3G0GRPZ6]] on $M$; it is a connection form on the trivial bundle $M \times \C^n$.
Let $F = dA + A \wedge A$ be its [[curvature|ZAJFW1S078]], where $d$ is the [[exterior derivative|0ZHSTAG8ZY]] and $\wedge$ is the matrix [[wedge product|0GRAATMGP1]].
The *Chern–Simons $3$-form* of $A$ is
$$\mathrm{CS}(A) = \tr\Big(A \wedge dA + \tfrac23 \, A \wedge A \wedge A\Big).$$

## Remarks

The defining property is $d\, \mathrm{CS}(A) = \tr(F \wedge F)$.
Check: $d \tr(A \wedge dA) = \tr(dA \wedge dA)$ and $d \tr(A \wedge A \wedge A) = 3 \tr(dA \wedge A \wedge A)$ by cyclicity of the graded trace; while $\tr(F \wedge F) = \tr(dA \wedge dA) + 2 \tr(dA \wedge A \wedge A) + \tr(A^4)$ and $\tr(A^4) = 0$.
Example: if $n = 1$, then $A \wedge A = 0$, $F = dA$ and $\mathrm{CS}(A) = A \wedge dA$; on $M = \R^4$ with coordinates $x_1, \dots, x_4$ and $A = x_1 \, dx_2 + x_3 \, dx_4$, one gets $dA = dx_1 \wedge dx_2 + dx_3 \wedge dx_4$, and both $d(A \wedge dA)$ and $F \wedge F$ equal $2 \, dx_1 \wedge dx_2 \wedge dx_3 \wedge dx_4$.
Non-example: for non-abelian $A$, the form $\tr(A \wedge dA)$ alone does not have derivative $\tr(F \wedge F)$ in general, since the term $2 \tr(dA \wedge A \wedge A)$ is missing; the cubic term is needed.
More generally, let $f$ be an invariant polynomial of degree $k$ as in the [[Chern–Weil homomorphism|82ZPRD39J7]], and let $\omega$ be a connection on a principal bundle $P$.
Put $\Omega_t = t\, d\omega + \frac{t^2}{2} [\omega \wedge \omega]$ and $Tf(\omega) = k \int_0^1 f(\omega, \Omega_t, \dots, \Omega_t) \, dt$.
Then $Tf(\omega)$ is a $(2k-1)$-form on $P$ with $d \, Tf(\omega) = f(\Omega, \dots, \Omega)$.
The $3$-form above is the case $f(X, Y) = \tr(XY)$ in a trivialization.
Under a gauge transformation $A \mapsto g^{-1} A g + g^{-1} dg$, $\mathrm{CS}(A)$ changes by an exact form plus $-\frac13 \tr\big((g^{-1}dg)^3\big)$, whose integral over a closed $3$-manifold is an integer multiple of $8\pi^2$ for $G = \mathrm{SU}(n)$.
