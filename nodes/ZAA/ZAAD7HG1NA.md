---
tag: ZAAD7HG1NA
kind: definition
name: S-wave
msc: [74J10, 74J05, 86A15]
defines: GZ7E9GHQYB
uses: [T1PYEBKBAJ, 80737NDZ4V, 0MWV6ZTK6S, 5EHD2XBQDG, NWYZ9QBA84]
sources:
  - url: https://en.wikipedia.org/wiki/S_wave
---

## Definition

Let a homogeneous isotropic linear elastic solid have density $\rho > 0$ and [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu > 0$.
Let $u(x, t)$ solve the [[elastodynamic|T1PYEBKBAJ]] equation $\rho \, \partial_t^2 u = (\lambda + \mu) \nabla (\nabla \cdot u) + \mu \Delta u$.
The field $u$ is an *S-wave* (shear, transverse or secondary wave) if it is divergence-free, $\nabla \cdot u = 0$.
Here $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]].
For such fields the equation reduces to the [[wave equation|5EHD2XBQDG]]
$$\partial_t^2 u = c_S^2 \, \Delta u, \qquad c_S = \sqrt{\frac{\mu}{\rho}}.$$

## Remarks

Example: the plane wave $u = m \, F(n \cdot x - c_S t)$ with unit vectors $m \perp n$ and a twice differentiable function $F$.
Its divergence is $(m \cdot n) F' = 0$, and $\mu \Delta u = \mu m F'' = \rho c_S^2 m F'' = \rho \, \partial_t^2 u$, so it is an S-wave travelling in direction $n$ and polarized along $m$.

Non-example: the plane wave $u = n \, F(n \cdot x - c t)$ with $F'' \ne 0$ has divergence $F' \ne 0$ somewhere, so it is not an S-wave; it is a [[P-wave|EEPJJHC5JZ]] when $c = \sqrt{(\lambda + 2\mu)/\rho}$.

The ratio of the two speeds is $c_P / c_S = \sqrt{2(1 - \nu)/(1 - 2\nu)}$, where $\nu$ is [[Poisson's ratio|NWYZ9QBA84]], so $c_S < c_P$ for every admissible $\nu$.
An S-wave whose polarization is horizontal is called SH, and one polarized in the vertical plane through the direction of travel is called SV.
