---
tag: B8W0Z2Q0JM
kind: definition
name: Poisson's ratio
msc: [74B05]
defines: NWYZ9QBA84
uses: [80737NDZ4V, 8QS6QMJF5Z, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson%27s_ratio
---

## Definition

Let a homogeneous isotropic linear elastic material have [[Lamé parameters|80737NDZ4V]] $\lambda$ and $\mu$, with $\mu > 0$ and $3\lambda + 2\mu > 0$, so that $\lambda + \mu > 0$ as well.
Consider the state of uniaxial stress $\sigma = s \, e_1 \otimes e_1$ with $s \ne 0$, where $\sigma$ is the [[Cauchy stress tensor|KG2XWEMJ30]], and let $\varepsilon$ be the [[strain|8QS6QMJF5Z]] that produces it.
The *Poisson's ratio* of the material is
$$\nu = -\frac{\varepsilon_{22}}{\varepsilon_{11}} = \frac{\lambda}{2(\lambda + \mu)}.$$

## Remarks

Example: for $\sigma = s \, e_1 \otimes e_1$ one finds $\varepsilon_{11} = \frac{s(\lambda + \mu)}{\mu(3\lambda + 2\mu)}$ and $\varepsilon_{22} = \varepsilon_{33} = -\frac{s \lambda}{2\mu(3\lambda + 2\mu)}$, and the quotient gives the formula.
For $\lambda = 120$ and $\mu = 80$ (in GPa, steel) it gives $\nu = 120/400 = 0.3$.

Non-example: in uniaxial strain the sides are held fixed, $\varepsilon_{22} = 0$, and the quotient $-\varepsilon_{22}/\varepsilon_{11} = 0$ is not Poisson's ratio; the lateral faces must be free of stress.

Positivity of the elasticity tensor, $\mu > 0$ and $3\lambda + 2\mu > 0$, is equivalent to $E > 0$ and $-1 < \nu < 1/2$.
The value $\nu = 1/2$ is the incompressible limit, and materials with $\nu < 0$ are called auxetic.
The volume change in uniaxial tension is $\tr \varepsilon = (1 - 2\nu) \varepsilon_{11}$.
