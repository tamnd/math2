---
tag: WPJYRY9PEV
kind: definition
name: Method of moments in electromagnetics
msc: [78M05, 65R20]
defines: YXKZYG618P
uses: [R3SG1SN7JQ, CPF9Q1GR10, Y5B0PEBKE8, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_moments_(electromagnetics)
---

## Definition

Let $S$ be a surface in $\R^3$.
Let $\mathcal{L}$ be a linear integral operator acting on vector fields $J$ on $S$, as in the [[electric field integral equation|CPF9Q1GR10]].
Consider the [[integral equation|R3SG1SN7JQ]] $\mathcal{L} J = g$, where $g$ is given by the incident field.
Write $\ip{u}{v} = \int_S u \cdot v \, dS$.
The *method of moments* with $N$ unknowns is the following procedure.

1. Choose basis functions $f_1, \dots, f_N$ and testing functions $w_1, \dots, w_N$ on $S$.
2. Seek $J_N = \sum_{n=1}^{N} a_n f_n$ with $\ip{w_m}{\mathcal{L} J_N - g} = 0$ for $m = 1, \dots, N$.
3. Solve the resulting linear system $Z a = b$, where $Z_{mn} = \ip{w_m}{\mathcal{L} f_n}$ and $b_m = \ip{w_m}{g}$.

The [[matrix|0VD9ZSWWJG]] $Z$ is called the impedance matrix.

## Remarks

Example: for a perfectly conducting body whose surface is cut into triangles, the Rao–Wilton–Glisson functions are a common basis.
Each one lives on a pair of triangles that share an edge.
Its component normal to that edge is continuous across it, so the current has no line charge there.
With $w_m = f_m$ the procedure is the [[Galerkin method|Y5B0PEBKE8]].

Non-example: point matching asks $\mathcal{L} J_N = g$ only at $N$ chosen points.
It fits the definition only in a generalised sense, with Dirac masses as testing functions, which are not functions on $S$.

The kernel couples every pair of points of $S$, so $Z$ is dense.
Direct solution then costs $O(N^2)$ memory and $O(N^3)$ operations, which is what fast methods such as the fast multipole method reduce.

## Explanations

### L1 human

The method replaces an unknown function by a list of $N$ numbers, the coefficients in a chosen basis.
It then asks that the error be orthogonal to $N$ test functions.
This gives an $N \times N$ linear system, which a computer solves.
