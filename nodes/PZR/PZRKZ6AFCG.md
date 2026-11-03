---
tag: PZRKZ6AFCG
kind: definition
name: Shell theory
msc: [74K25, 74B05]
defines: DF7RPJHHY1
uses: [782XMC21FH, VGJJVBZ1MQ, MAJ3DH7MZS, 9KHQR16P1B]
sources:
  - url: https://en.wikipedia.org/wiki/Plate_theory
---

## Definition

Let $\omega \subset \R^2$ be a bounded domain and $\varphi \colon \overline{\omega} \to \R^3$ a smooth injective immersion, whose image $S$ is the middle [[surface|VGJJVBZ1MQ]].
Let $a_3(y)$ be the unit normal of $S$ at $\varphi(y)$.
Let $h > 0$ be a thickness that is small compared with the size of $S$ and with its radii of curvature.
A *shell* is an elastic body occupying $\set{\varphi(y) + z \, a_3(y) : y \in \omega, \ \abs{z} < h/2}$.
A *shell theory* is a model of the shell in which:

1. The unknown is a displacement field $u$ of the middle surface, possibly with rotation fields of the normals.
2. The strains are the change of metric $\gamma_{\alpha\beta}(u)$ and the change of curvature $\rho_{\alpha\beta}(u)$.
   Here $\gamma$ is half the change of the [[first fundamental form|MAJ3DH7MZS]] of $S$, and $\rho$ is the change of its [[second fundamental form|9KHQR16P1B]].
3. The equilibrium equations or the energy are written on $\omega$ through $\gamma$, $\rho$ and the stress resultants.
   These are the membrane forces $N^{\alpha\beta}$, bending moments $M^{\alpha\beta}$ and, in some theories, transverse shear forces.

## Remarks

Example: if $\varphi(y) = (y_1, y_2, 0)$, the second fundamental form of $S$ is zero.
In the linear case $\gamma$ is the in-plane strain and $\rho_{\alpha\beta}$ is $\partial_\alpha \partial_\beta u_3$, and a shell theory then becomes a [[plate theory|782XMC21FH]].

Non-example: a solid ball is not a shell, since there is no middle surface with a small thickness around it.

Important shell theories are the [[membrane theory of shells|1ND17AY99Y]], which keeps only $\gamma$ and $N$, and the [[Koiter shell model|F91VK64QRZ]], which keeps both $\gamma$ and $\rho$.
