---
tag: Y2MYV7ZDM7
kind: definition
name: Projection method
msc: [76M20, 76D05, 65M06]
defines: V265MVHF6M
uses: [18KXZHVF4M, C75W88ZVNY, DWK5N5SKTK, T4ZFKBZRYK, 2JZ0C15A9C]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_method_(fluid_dynamics)
---

## Definition

Consider the [[incompressible|2JZ0C15A9C]] [[Navier–Stokes equations|18KXZHVF4M]] on a bounded domain $\Omega \subset \R^d$ with constant density $\rho$, kinematic viscosity $\nu$ and the no-slip boundary condition:
$$\partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{\rho} \nabla p + \nu \Delta \mathbf{u}, \qquad \nabla \cdot \mathbf{u} = 0.$$
Let $\Delta t > 0$ be a time step and $\mathbf{u}^n$ the approximation of $\mathbf{u}$ at time $n \Delta t$.
The *projection method* computes $\mathbf{u}^{n+1}$ and $p^{n+1}$ from $\mathbf{u}^n$ in three steps:

1. compute an intermediate velocity $\mathbf{u}^*$, equal to $0$ on $\partial\Omega$, from the momentum equation without pressure, for example
$$\frac{\mathbf{u}^* - \mathbf{u}^n}{\Delta t} = -(\mathbf{u}^n \cdot \nabla) \mathbf{u}^n + \nu \Delta \mathbf{u}^*;$$
2. solve the [[Poisson equation|DWK5N5SKTK]] $\Delta p^{n+1} = \frac{\rho}{\Delta t} \nabla \cdot \mathbf{u}^*$ in $\Omega$ with $\partial p^{n+1}/\partial \mathbf{n} = 0$ on $\partial \Omega$;
3. set $\mathbf{u}^{n+1} = \mathbf{u}^* - \frac{\Delta t}{\rho} \nabla p^{n+1}$.

## Remarks

Check: taking the divergence of step 3 and using step 2 gives $\nabla \cdot \mathbf{u}^{n+1} = \nabla \cdot \mathbf{u}^* - \frac{\Delta t}{\rho} \Delta p^{n+1} = 0$, and the Neumann condition gives $\mathbf{u}^{n+1} \cdot \mathbf{n} = 0$ on $\partial\Omega$.
So $\mathbf{u}^{n+1}$ is the $L^2$-orthogonal projection of $\mathbf{u}^*$ onto divergence-free fields tangent to the boundary, the Leray projection given by the [[Helmholtz decomposition|C75W88ZVNY]].
Non-example: the step $\mathbf{u}^{n+1} = \mathbf{u}^*$ alone, without steps 2 and 3, does not keep the velocity divergence-free, so it is not a projection method.
The tangential part of $\mathbf{u}^{n+1}$ does not vanish exactly on $\partial \Omega$, which creates a numerical boundary layer.
The basic scheme is first-order in time, and incremental variants that reuse $p^n$ in step 1 reach second order.
