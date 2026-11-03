---
tag: 7FKWYYQPW7
kind: definition
name: Linear elasticity
msc: [74B05, 35Q74]
defines: 6W00ZECYT0
uses: [8QS6QMJF5Z, KG2XWEMJ30, SX32X1D537, 0MWV6ZTK6S, GQ3K59MRJP]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_elasticity
    locator: Mathematical formulation
---

## Definition

Let $\Omega \subseteq \R^3$ be a bounded open set, the reference shape of a body.
Let $\mathsf{C}$ be an [[elasticity tensor|SX32X1D537]] field on $\Omega$, let $\rho > 0$ be the mass density and let $f \colon \Omega \to \R^3$ be a body force per unit volume.
The equations of *linear elasticity* for a displacement field $u \colon \Omega \times [0, T] \to \R^3$ are the following.

1. Strain–displacement relation: the [[strain tensor|8QS6QMJF5Z]] is $\varepsilon = \tfrac12 (\nabla u + (\nabla u)^T)$.
2. Constitutive law: the [[Cauchy stress tensor|KG2XWEMJ30]] is $\sigma = \mathsf{C} : \varepsilon$, that is $\sigma_{ij} = C_{ijkl} \varepsilon_{kl}$ with summation over repeated indices.
3. Equation of motion: $\nabla \cdot \sigma + f = \rho \, \partial_t^2 u$ in $\Omega$, where $(\nabla \cdot \sigma)_i = \partial_j \sigma_{ij}$ is the row-wise [[divergence|0MWV6ZTK6S]].

In the static case the right side of clause 3 is $0$.
A boundary value problem adds conditions on $\partial \Omega$.
The displacement $u$ is prescribed on one part of the boundary.
The traction $\sigma n$ is prescribed on the rest, where $n$ is the outward unit normal.

## Remarks

Example: let $\mathsf{C}$ be isotropic with Lamé parameters $\lambda, \mu$, let $f = 0$, and let $u(x) = a x_1 e_1$ for a small constant $a$.
The strain is $\varepsilon = a \, e_1 \otimes e_1$ and the stress is constant, so $\nabla \cdot \sigma = 0$ and the static equations hold.
This is a uniform stretch of the body.

Non-example: $u(x) = a x_1^2 e_1$ with $a \ne 0$ and $f = 0$ does not solve the static isotropic equations, because $\nabla \cdot \sigma = 2a(\lambda + 2\mu) e_1 \ne 0$.

For an isotropic homogeneous material, substituting clauses 1 and 2 into clause 3 gives the [[Lamé equations|GQ3K59MRJP]] for $u$ alone.
The model is valid when $\abs{\nabla u}$ is small, so that the reference and deformed shapes may be identified.
