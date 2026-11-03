---
tag: SRGSR8X5SF
kind: problem
name: Sommerfeld's half-plane diffraction problem
msc: [78A45, 35J05]
uses: [MNXKTXJ35G, D0TQ9F2ZDW, H4NXEY6QTZ]
about: [FSCTVTQQF2]
sources:
  - url: https://en.wikipedia.org/wiki/Diffraction
history:
  posed_by: "Arnold Sommerfeld"
  first_stated: "1896"
---

## Problem

Let $k > 0$, let $\Gamma = \set{(x, 0) : x \ge 0}$ be a half-line in $\R^2$, and let $u_i(x, y) = e^{i k (x \cos\alpha + y \sin\alpha)}$ be an incident plane wave with $0 < \alpha < \pi$.
Find $u = u_i + u_s$ on $\R^2 \setminus \Gamma$ such that:

1. $u$ solves the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u + k^2 u = 0$ in $\R^2 \setminus \Gamma$;
2. $u = 0$ on both sides of $\Gamma$ (the Dirichlet case), or $\partial u / \partial y = 0$ on both sides of $\Gamma$ (the Neumann case);
3. the scattered field $u_s$ is outgoing: away from the directions of the reflected wave and of the shadow boundary, it satisfies the Sommerfeld radiation condition;
4. $u$ has finite energy near the edge: $u$ and $\nabla u$ are square integrable on every bounded set.

## Remarks

The half-line is the cross-section of a thin, perfectly conducting half-plane, and the two boundary conditions correspond to the two polarisations of the electromagnetic wave.
Sommerfeld solved the problem exactly in 1896, with a method of solutions on a two-sheeted Riemann surface; the solution is unique under conditions 1 to 4.
The solution can be written with the [[Fresnel integrals|D0TQ9F2ZDW]], and it shows a smooth transition from light to shadow across the shadow boundary instead of a sharp edge.
The problem can also be solved by the [[Wiener–Hopf method|H4NXEY6QTZ]].
Its far-field asymptotics give the edge diffraction coefficient used in [[Keller's geometrical theory of diffraction|ES9KPGJAGS]].

## Explanations

### L1 human

A plane wave hits a thin straight wall that ends at a sharp edge.
The problem is to compute exactly how the wave bends around the edge into the region behind the wall.
It is one of the very few diffraction problems with an exact solution, so it serves as a test case and a building block for approximate methods.
