---
tag: HSR1BM0PEP
kind: definition
name: Buckling
msc: [74G60, 74K10]
defines: 4GAM4KXSM8
uses: [50W7AQMS5Z, D9TW46P19Y]
sources:
  - url: https://en.wikipedia.org/wiki/Buckling
---

## Definition

Consider an elastic structure under a compressive load $\lambda \ge 0$ with total potential energy $\Pi(u, \lambda)$.
Suppose there is a *fundamental* branch of equilibria $u_0(\lambda)$ which is stable for small $\lambda$.
Examples are the straight state of a column and the flat state of a plate.
The structure *buckles* at $\lambda_c$ if, at $\lambda = \lambda_c$:

1. the fundamental branch loses stability, so that $\lambda_c$ is a critical load in the sense of [[elastic instability|50W7AQMS5Z]], and
2. a second branch of equilibria, different from $u_0$, passes through $(u_0(\lambda_c), \lambda_c)$.

The smallest such $\lambda_c$ is the *buckling load*, and the kernel of the second variation $D_u^2 \Pi(u_0(\lambda_c), \lambda_c)$ consists of the *buckling modes*.

## Remarks

Example: a straight elastic column pinned at both ends, of length $L$ and bending stiffness $EI$, under an axial compressive force $P$.
The straight state is an equilibrium for every $P$.
The linearized equation $EI w'' + P w = 0$, $w(0) = w(L) = 0$, has the nonzero solution $w = \sin(\pi x / L)$ exactly when $P = \pi^2 EI / L^2$, which is the buckling load.

Non-example: the same column under tension, $P < 0$.
The equation $EI w'' + P w = 0$ with these end conditions has only the solution $w = 0$, and the straight state stays stable, so no buckling occurs.

When the load reaches a maximum on a single equilibrium path without a bifurcation, as for a shallow arch, one speaks of snap-through or limit-point instability instead.
