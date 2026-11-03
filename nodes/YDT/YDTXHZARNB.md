---
tag: YDTXHZARNB
kind: definition
name: Groundwater flow equation
msc: [76S05, 86A05, 35K05]
defines: 64DSSBPT5E
uses: [DX8RV2XG6H, FD4NR553YR, VP2HN86VAG, S8RG6N1PRT, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Groundwater_flow_equation
---

## Definition

Let $\Omega \subset \R^3$ be the region of a saturated aquifer, and let $h(x, t)$ be the hydraulic head at $x \in \Omega$ and time $t$.
Let $K(x) > 0$ be the hydraulic conductivity and $Q(x, t)$ a volumetric source rate per unit volume.
Let $S_s(x) > 0$ be the specific storage, the volume of water released from a unit volume of aquifer per unit decline of head.
By [[Darcy's law|DX8RV2XG6H]] the specific discharge is $q = -K \nabla h$.
The *groundwater flow equation* is the [[mass balance|FD4NR553YR]]
$$S_s \frac{\partial h}{\partial t} = \nabla \cdot (K \nabla h) + Q \quad \text{in } \Omega.$$

For a confined aquifer of thickness $b$ treated in two dimensions, with transmissivity $T = K b$, storativity $S = S_s b$ and source $R$ per unit area, it reads
$$S \frac{\partial h}{\partial t} = \nabla \cdot (T \nabla h) + R.$$

## Remarks

Example: for constant $K$ and $S_s$ and no source, the equation is the [[heat equation|VP2HN86VAG]] $\partial_t h = D \nabla^2 h$ with hydraulic diffusivity $D = K / S_s$, where $\nabla^2$ is the [[Laplacian|0E0B6RA8K0]].
The steady linear head $h(x) = h_0 - J x_1$ satisfies it, since $\nabla^2 h = 0$; it describes a uniform flow $q = K J e_1$ along the first axis.

Non-example: in an unconfined aquifer the thickness of the saturated zone is the head itself, and the storage comes from draining pores at the water table.
The equation then becomes nonlinear, as in the Boussinesq equation obtained from the Dupuit–Forchheimer assumption, and it is not of the linear form above.

In steady state the equation is $\nabla \cdot (K \nabla h) = -Q$, which is [[Laplace's equation|S8RG6N1PRT]] when $K$ is constant and $Q = 0$.
Boundary conditions prescribe the head (Dirichlet), the normal flux (Neumann), or a relation between them at rivers and lakes.
