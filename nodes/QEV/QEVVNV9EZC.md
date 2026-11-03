---
tag: QEVVNV9EZC
kind: definition
name: P-wave
msc: [74J10, 74J05, 86A15]
defines: EEPJJHC5JZ
uses: [T1PYEBKBAJ, 80737NDZ4V, 0NF6GQNXMY, 5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/P_wave
---

## Definition

Let a homogeneous isotropic linear elastic solid have density $\rho > 0$ and [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu > 0$ with $\lambda + 2\mu > 0$.
Let $u(x, t)$ solve the [[elastodynamic|T1PYEBKBAJ]] equation $\rho \, \partial_t^2 u = (\lambda + \mu) \nabla (\nabla \cdot u) + \mu \Delta u$.
The field $u$ is a *P-wave* (compressional, longitudinal or primary wave) if it is irrotational, $\nabla \times u = 0$.
Here $\nabla \times$ is the [[curl|0NF6GQNXMY]].
For such fields the equation reduces to the [[wave equation|5EHD2XBQDG]]
$$\partial_t^2 u = c_P^2 \, \Delta u, \qquad c_P = \sqrt{\frac{\lambda + 2\mu}{\rho}}.$$

## Remarks

The reduction uses the identity $\Delta u = \nabla (\nabla \cdot u) - \nabla \times (\nabla \times u)$, which gives $\nabla (\nabla \cdot u) = \Delta u$ when $\nabla \times u = 0$.

Example: the plane wave $u = n \, F(n \cdot x - c_P t)$ with a unit vector $n$ and a twice differentiable function $F$.
Its curl is $n \times n \, F' = 0$, and $\Delta u = n F''$ while $\partial_t^2 u = c_P^2 n F''$, so it is a P-wave travelling in direction $n$.

Non-example: $u = m \, F(n \cdot x - c t)$ with $m$ a unit vector perpendicular to $n$ and $F'' \ne 0$.
Its curl $n \times m \, F'$ is not zero, so it is not a P-wave; it is an [[S-wave|GZ7E9GHQYB]] when $c = \sqrt{\mu/\rho}$.
