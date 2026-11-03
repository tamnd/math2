---
tag: KVRVGFMAYJ
kind: definition
name: Newtonian fluid
msc: [76A02, 76D05]
defines: T4ZV12BVHN
uses: [NM5Q4845Z4, P1KWMQG4NZ, 0XC1RDBY7A, 2JZ0C15A9C, 18KXZHVF4M]
sources:
  - url: https://en.wikipedia.org/wiki/Newtonian_fluid
---

## Definition

Consider a fluid with pressure $p$, velocity field $\mathbf{u}$ and [[strain rate tensor|P1KWMQG4NZ]] $E$.
Let $I$ be the $3 \times 3$ identity matrix, and note that the [[trace|0XC1RDBY7A]] of $E$ is $\tr E = \nabla \cdot \mathbf{u}$.
The fluid is *Newtonian* if its Cauchy stress tensor $\sigma$ has the form
$$\sigma = -p I + 2 \mu E + \lambda \, (\tr E) \, I.$$
Here $\mu$ is the dynamic [[viscosity|NM5Q4845Z4]] and $\lambda$ is a second coefficient.
Both may depend on the thermodynamic state but not on $E$.

## Remarks

The form is the general isotropic stress that is linear in $E$.
For an [[incompressible flow|2JZ0C15A9C]], $\tr E = 0$ and the law becomes $\sigma = -p I + 2 \mu E$.
Example: in the simple shear flow $\mathbf{u} = (\dot\gamma y, 0, 0)$, $E_{12} = \dot\gamma / 2$, so the shear stress is $\sigma_{12} = \mu \dot\gamma$, proportional to the shear rate.
Non-example: a power-law fluid with shear stress $\tau = K \dot\gamma^{m}$ for a constant $m \ne 1$ is not Newtonian, since its stress is not linear in the shear rate.
Substituting the Newtonian law into the balance of momentum gives the [[Navier–Stokes equations|18KXZHVF4M]].
