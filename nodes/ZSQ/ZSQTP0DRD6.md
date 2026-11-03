---
tag: ZSQTP0DRD6
kind: definition
name: Non-Newtonian fluid
msc: [76A05, 76A10]
defines: 8DT9MB9V6R
uses: [T4ZV12BVHN, NM5Q4845Z4, P1KWMQG4NZ]
sources:
  - url: https://en.wikipedia.org/wiki/Non-Newtonian_fluid
---

## Definition

Consider an incompressible fluid with velocity field $u$.
Its Cauchy stress is written $\sigma = -p I + \tau$, where $p$ is the pressure, $I$ is the identity tensor and $\tau$ is the deviatoric (extra) stress.
Let $D = \tfrac12 (\nabla u + (\nabla u)^T)$ be the [[strain rate tensor|P1KWMQG4NZ]].
The fluid is [[Newtonian|T4ZV12BVHN]] if there is a constant $\mu > 0$, the [[viscosity|NM5Q4845Z4]], such that $\tau = 2 \mu D$ in every flow.
A *non-Newtonian fluid* is a fluid that is not Newtonian.
That is, its extra stress is not $2 \mu D$ for a single constant $\mu$.
The ratio of stress to strain rate may depend on the strain rate, or the stress may depend on the history of the deformation.

## Remarks

In a simple shear flow $u = (\dot\gamma y, 0, 0)$ with shear rate $\dot\gamma > 0$, the shear stress is $\tau_{xy}$, and the *apparent viscosity* is $\eta(\dot\gamma) = \tau_{xy} / \dot\gamma$.
A Newtonian fluid has $\eta(\dot\gamma) = \mu$ for all $\dot\gamma$.

Example: a [[power-law fluid|C6RVY7R8S6]] with $\tau_{xy} = K \dot\gamma^{1/2}$ and $K > 0$ has $\eta(\dot\gamma) = K \dot\gamma^{-1/2}$.
This is not constant, so the fluid is non-Newtonian; it is shear-thinning.

Non-example: a fluid with $\tau = 2 \mu D$ and $\mu = 10^{-3}$ (in SI units, roughly water) is Newtonian, because the ratio is the same constant in every flow.

Common classes are shear-thinning and shear-thickening fluids, viscoplastic fluids with a yield stress such as the [[Bingham plastic|FP202DPQ3D]], and viscoelastic fluids such as the [[Oldroyd-B model|VPACKRZSA8]].
