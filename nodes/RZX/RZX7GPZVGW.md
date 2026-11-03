---
tag: RZX7GPZVGW
kind: definition
name: Finite-difference time-domain method
msc: [78M20, 65M06]
defines: 57XRW2119C
uses: [9BWWD4QK8Y, 7JX95QG3CZ, 8HSQHDNFEF, 3HGJCQBWVY, FQVVNYV6N8]
sources:
  - url: https://en.wikipedia.org/wiki/Finite-difference_time-domain_method
---

## Definition

Consider a source-free linear medium with constant scalar permittivity $\varepsilon$ and permeability $\mu$.
The [[Maxwell curl equations|9BWWD4QK8Y]] there are
$$\partial_t H = -\frac{1}{\mu} \nabla \times E, \qquad \partial_t E = \frac{1}{\varepsilon} \nabla \times H.$$
Fix space steps $\Delta x, \Delta y, \Delta z > 0$ and a time step $\Delta t > 0$, and write $f|^n_{i,j,k}$ for the value of $f$ at $(i \Delta x, j \Delta y, k \Delta z)$ and time $n \Delta t$.
The *finite-difference time-domain method* computes approximate fields as follows.

1. The components of $E$ and $H$ are placed at the staggered points of the [[Yee lattice|7JX95QG3CZ]].
2. $E$ is computed at the integer times $n \Delta t$, and $H$ at the half-integer times $(n + \frac12) \Delta t$.
3. Each space and time derivative in the curl equations is replaced by a [[central difference|8HSQHDNFEF]] over one step.

This gives explicit update rules of [[leapfrog|3HGJCQBWVY]] type.
First all of $H$ advances from time $n - \frac12$ to $n + \frac12$, then all of $E$ from $n$ to $n + 1$.
For instance, since $(\nabla \times H)_x = \partial_y H_z - \partial_z H_y$, the update of $E_x$ is
$$E_x|^{n+1}_{i+\frac12, j, k} = E_x|^{n}_{i+\frac12, j, k} + \frac{\Delta t}{\varepsilon} \left( \frac{H_z|^{n+\frac12}_{i+\frac12, j+\frac12, k} - H_z|^{n+\frac12}_{i+\frac12, j-\frac12, k}}{\Delta y} - \frac{H_y|^{n+\frac12}_{i+\frac12, j, k+\frac12} - H_y|^{n+\frac12}_{i+\frac12, j, k-\frac12}}{\Delta z} \right).$$

## Remarks

Example: in one dimension, with fields $E_x(z, t)$ and $H_y(z, t)$, the equations are $\partial_t H_y = -\frac{1}{\mu} \partial_z E_x$ and $\partial_t E_x = -\frac{1}{\varepsilon} \partial_z H_y$.
The method stores $E_x$ at $z = k \Delta z$ and $H_y$ at $z = (k + \frac12) \Delta z$, and updates
$$H_y|^{n+\frac12}_{k+\frac12} = H_y|^{n-\frac12}_{k+\frac12} - \frac{\Delta t}{\mu \Delta z} \left( E_x|^n_{k+1} - E_x|^n_{k} \right), \qquad E_x|^{n+1}_{k} = E_x|^{n}_{k} - \frac{\Delta t}{\varepsilon \Delta z} \left( H_y|^{n+\frac12}_{k+\frac12} - H_y|^{n+\frac12}_{k-\frac12} \right).$$
Each difference is centred at the point and time of the unknown it updates, so the scheme is second-order accurate in space and time.

Non-example: storing $E$ and $H$ at the same times and stepping both with the forward Euler rule $f^{n+1} = f^n + \Delta t \, \partial_t f^n$ fails clause 2.
That scheme is only first order in time, and it is unstable for the wave equation for every $\Delta t > 0$.

In a medium with wave speed $c = 1/\sqrt{\varepsilon \mu}$, the method is stable when
$$c \, \Delta t \le \left( \frac{1}{\Delta x^2} + \frac{1}{\Delta y^2} + \frac{1}{\Delta z^2} \right)^{-1/2},$$
which is its [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]].
If the reverse strict inequality holds, some grid modes grow without bound.

## Explanations

### L1 human

The method moves the electric and magnetic fields forward in time in turns, like two people walking by alternating steps.
Each new value is computed from old values at its neighbours, so no system of equations has to be solved.
The time step must be small enough that a wave does not jump over a grid cell in one step.
