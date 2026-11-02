---
tag: DFM7NJTX3J
kind: definition
name: Minimal surface
msc: [53A10]
defines: 41X0YW2R9N
uses: [6080X3FAD4, PA78NFEPCF]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_surface
---

## Definition

Let $S \subset \R^3$ be a [[regular surface|6080X3FAD4]] with [[mean curvature|PA78NFEPCF]] $H \colon S \to \R$.
The surface $S$ is *minimal* if $H(p) = 0$ for every point $p \in S$.

## Remarks

The [[catenoid|6NN1HP54GB]] $x(u, v) = (\cosh v \cos u, \cosh v \sin u, v)$ is minimal.
Its principal curvatures are $\pm 1/\cosh^2 v$, so $H = 0$.
The sphere of radius $r$ is not minimal: both principal curvatures equal $1/r$ for the inward normal, so $H = 1/r \neq 0$.

Equivalent forms:

1. $S$ is minimal if and only if, for every compact region $R \subset S$ and every smooth normal variation of $R$ fixed on $\partial R$, the first variation of area is zero.
2. If $x$ is a conformal parametrization of $S$, then $S$ is minimal if and only if each coordinate function of $x$ is harmonic.
3. The graph of a smooth function $u(x, y)$ is minimal if and only if $(1 + u_y^2) u_{xx} - 2 u_x u_y u_{xy} + (1 + u_x^2) u_{yy} = 0$, the minimal surface equation.

A minimal surface need not minimize area among all surfaces with the same boundary; it is only a critical point.

## Explanations

### L1 human

A minimal surface is a surface whose mean curvature vanishes everywhere.
At every point the bending in one principal direction cancels the bending in the other.
