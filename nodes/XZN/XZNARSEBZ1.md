---
tag: XZNARSEBZ1
kind: definition
name: Electrical resistivity tomography
msc: [86A22, 35R30, 35J25]
defines: QE5PACCS74
uses: [C54MFNX576, R8Y8DDTWBM, SH6JY9RN2E]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_resistivity_tomography
---

## Definition

Let $\Omega$ be the subsurface, with conductivity $\sigma(x) > 0$ and resistivity $\rho = 1/\sigma$.
A current $I$ injected at electrode $A$ and withdrawn at electrode $B$ produces a potential $\varphi$.
It solves the following equation, with no normal current through the ground surface:
$$\nabla \cdot (\sigma \nabla \varphi) = -I\, \delta_A + I\, \delta_B \quad \text{in } \Omega.$$
Here $\delta_A$ and $\delta_B$ are point sources at the electrodes.
A measurement records the voltage $\Delta V = \varphi(M) - \varphi(N)$ between two other electrodes $M$ and $N$.
The *apparent resistivity* of the configuration is $\rho_a = K\, \Delta V / I$, where the geometric factor $K$ is chosen so that $\rho_a = \rho$ for a homogeneous half-space.
*Electrical resistivity tomography* is the [[geophysical inversion|C54MFNX576]] that recovers $\sigma$ on $\Omega$ from the values $\Delta V / I$ of many electrode configurations $(A, B, M, N)$.

## Remarks

In a homogeneous half-space a single surface electrode with current $I$ gives $\varphi(x) = \rho I / (2 \pi \abs{x - A})$, a [[Green's function|SH6JY9RN2E]] of the problem with the image of the source in the surface.
Example: the Wenner array has $A, M, N, B$ on a line with equal spacings $a$; then $\Delta V = \frac{\rho I}{2\pi}\bigl(\frac{1}{a} - \frac{1}{2a} - \frac{1}{2a} + \frac{1}{a}\bigr) = \frac{\rho I}{2\pi a}$, so $K = 2 \pi a$.
Non-example: a single resistance measurement with one fixed configuration gives one number, which cannot separate depth from lateral changes, so it is not a tomography.
With all current and voltage pairs on the boundary of a bounded body, the data form the Neumann-to-Dirichlet map of the [[Calderón problem|R8Y8DDTWBM]].
This map carries the same information as the Dirichlet-to-Neumann map.
Field surveys collect a finite subset and use regularised inversion.

## Explanations

### L1 human

Current is pushed between two electrodes and the voltage is read at two others, for many choices of the four.
Inverting all these readings gives a map of how resistive the ground is.
