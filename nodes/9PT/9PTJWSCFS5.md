---
tag: 9PTJWSCFS5
kind: definition
name: Riemann solver
msc: [65M08, 35L65]
defines: ZY4GY93C4B
uses: [XN081NCPF5, GJWKX22VVE, 1A01A3EJRX]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_solver
---

## Definition

Let $\Omega \subseteq \R^m$ be open and let $F \colon \Omega \to \R^m$ be the $C^1$ flux of a [[hyperbolic conservation law|XN081NCPF5]] $u_t + F(u)_x = 0$.
A *Riemann solver* for $F$ is a map $H \colon \Omega \times \Omega \to \R^m$.
Its value $H(u_l, u_r)$ is the numerical flux at an interface between a left state $u_l$ and a right state $u_r$.
It is obtained from an exact or approximate solution of the [[Riemann problem|GJWKX22VVE]] with data $u_l, u_r$.
It is required to be:

1. consistent: $H(u, u) = F(u)$ for all $u \in \Omega$;
2. locally Lipschitz continuous in both arguments.

The *exact Riemann solver* is $H(u_l, u_r) = F(w(0; u_l, u_r))$, where $w(x/t; u_l, u_r)$ is the self-similar [[entropy solution|1A01A3EJRX]] of the Riemann problem, when it exists and is unique.

## Remarks

Example: the HLL solver uses two estimates $S_L < S_R$ of the slowest and fastest wave speeds.
It sets $H = F(u_l)$ if $0 \le S_L$, $H = F(u_r)$ if $S_R \le 0$, and otherwise
$$H(u_l, u_r) = \frac{S_R F(u_l) - S_L F(u_r) + S_L S_R (u_r - u_l)}{S_R - S_L}.$$
For $u_l = u_r = u$ every case gives $F(u)$, so this solver is consistent.

Non-example: $H(u_l, u_r) = F(u_l) + F(u_r)$ fails clause 1, since $H(u, u) = 2F(u)$.
A scheme with such a flux approximates the wrong equation.

For the scalar equation $u_t + a u_x = 0$, the exact solver gives $H(u_l, u_r) = a u_l$ if $a > 0$ and $a u_r$ if $a < 0$, which is the upwind flux.
