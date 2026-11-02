---
tag: R8Y8DDTWBM
kind: problem
name: Calderón problem
msc: [35R30, 35J25, 65N21]
uses: [W783KDGT8E, PCMW7KN5P4, 8D56GQ4AG8]
about: [W783KDGT8E, PCMW7KN5P4]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_impedance_tomography
history:
  posed_by: "Alberto Calderón"
  first_stated: "1980"
---

## Problem

Let $\Omega \subset \R^n$, $n \ge 2$, be a bounded connected open set with smooth boundary.
A conductivity is a measurable function $\gamma$ on $\Omega$ with $c \le \gamma \le c^{-1}$ for some constant $c > 0$.
Let $\Lambda_\gamma$ be the [[Dirichlet-to-Neumann operator|W783KDGT8E]] of the equation $\nabla \cdot (\gamma \nabla u) = 0$ in $\Omega$.
The problem has two parts:

1. Uniqueness: if $\Lambda_{\gamma_1} = \Lambda_{\gamma_2}$, does it follow that $\gamma_1 = \gamma_2$?
2. Reconstruction: give a method that recovers $\gamma$ from $\Lambda_\gamma$.

## Remarks

This is the model [[inverse problem|PCMW7KN5P4]] behind electrical impedance tomography, where voltages are applied on the surface of a body and the resulting currents are measured.
Calderón posed it in his 1980 paper "On an inverse boundary value problem", where he proved uniqueness for the linearized problem near constant conductivities.
Sylvester and Uhlmann proved uniqueness for smooth conductivities in dimension $n \ge 3$ in 1987, using complex geometrical optics solutions.
Astala and Päivärinta proved uniqueness for all bounded measurable conductivities in dimension $n = 2$ in 2006.
In dimension $n \ge 3$ uniqueness for general bounded measurable conductivities is open.
The problem is severely ill-posed: the stability of $\gamma$ with respect to $\Lambda_\gamma$ is only logarithmic in general.

## Explanations

### L1 human

Can one see inside a body using only electrical measurements made on its skin?
Each choice of voltage pattern on the surface gives a pattern of currents flowing out, and the full list of these pairs is the data.
The Calderón problem asks whether these data determine the electrical conductivity at every point inside, and how to compute it.
Different tissues conduct differently, so a positive answer gives an imaging method that uses no radiation.
