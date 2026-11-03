---
tag: RN26SA4HW1
kind: definition
name: Yee lattice
msc: [78M20, 65M06]
defines: 7JX95QG3CZ
uses: [9BWWD4QK8Y, 8HSQHDNFEF]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-difference_time-domain_method
---

## Definition

Fix steps $\Delta x, \Delta y, \Delta z > 0$.
Write $(i, j, k)$ for the point $(i \Delta x, j \Delta y, k \Delta z)$ of $\R^3$, where $i, j, k$ may be integers or half-integers.
The *Yee lattice* places the components of the electric field $E$ and the magnetic field $H$ as follows, for all integers $i, j, k$:

1. $E_x$ at $(i + \frac12, j, k)$, $E_y$ at $(i, j + \frac12, k)$ and $E_z$ at $(i, j, k + \frac12)$, the midpoints of the edges of the grid cubes;
2. $H_x$ at $(i, j + \frac12, k + \frac12)$, $H_y$ at $(i + \frac12, j, k + \frac12)$ and $H_z$ at $(i + \frac12, j + \frac12, k)$, the centres of the faces of the grid cubes.

## Remarks

Check that the curl of $E$ is a [[central difference|8HSQHDNFEF]] at the points of $H$.
At the point $(i + \frac12, j + \frac12, k)$ of $H_z$, the [[Maxwell equation|9BWWD4QK8Y]] for $\partial_t H_z$ needs $(\nabla \times E)_z = \partial_x E_y - \partial_y E_x$.
The values $E_y$ at $(i, j + \frac12, k)$ and $(i + 1, j + \frac12, k)$ give a difference in $x$ centred at $i + \frac12$.
The values $E_x$ at $(i + \frac12, j, k)$ and $(i + \frac12, j + 1, k)$ give a difference in $y$ centred at $j + \frac12$.
So both differences are centred at the point of $H_z$, and the approximation is second order.

Non-example: a collocated grid, which stores all six components at the points $(i, j, k)$, is not a Yee lattice.
There a centred first difference must use the points $i - 1$ and $i + 1$, and the grid splits into decoupled sublattices that carry spurious modes.

The cubes may be replaced by rectangular boxes, and in two dimensions the lattice splits into a TE and a TM arrangement.

## Explanations

### L1 human

The Yee lattice is a rule for where to store each field component on a grid.
The electric field lives on the edges of the cubes and the magnetic field on their faces.
This choice makes every derivative that Maxwell's equations need a difference of two neighbouring values, centred exactly where it is needed.
