---
tag: GC2S8E05YP
kind: definition
name: Epicyclic frequency
msc: [85A05, 70F15]
defines: GK34V4WF2V
uses: [V4FYBDSGMT, 2FTZ7D8Z0F]
sources:
  - url: https://en.wikipedia.org/wiki/Epicyclic_frequency
---

## Definition

Let $\Phi(R, z)$ be an axisymmetric potential with circular speed $v_c(R)$ in the plane $z = 0$, as in the [[rotation curve|V4FYBDSGMT]].
Let $\Omega(R) = v_c(R)/R$ be the [[angular velocity|2FTZ7D8Z0F]] of circular orbits.
The *epicyclic frequency* $\kappa(R) \ge 0$ is defined, where the right-hand side is nonnegative, by
$$\kappa^2(R) = R \frac{d \Omega^2}{d R} + 4 \Omega^2 = \frac{\partial^2 \Phi}{\partial R^2}(R, 0) + \frac{3}{R} \frac{\partial \Phi}{\partial R}(R, 0).$$

## Remarks

Meaning: a planar orbit with angular momentum $L = R_g^2 \Omega(R_g)$ moves in the effective potential $\Phi(R, 0) + L^2 / (2 R^2)$.
Its minimum is at the guiding radius $R_g$, and its second derivative there is $\kappa^2(R_g)$.
So small radial deviations $x = R - R_g$ obey $\ddot x = -\kappa^2 x$ and oscillate with frequency $\kappa$.

Example: for a point mass, $\Omega^2 = GM/R^3$, so $R \, d\Omega^2/dR = -3 \Omega^2$ and $\kappa = \Omega$.
For a flat rotation curve, $\Omega^2 = v_0^2 / R^2$, so $\kappa = \sqrt{2} \, \Omega$.
For a rigid rotation, $\Omega$ is constant and $\kappa = 2 \Omega$.

Non-example: if $\Omega^2$ decreases faster than $R^{-4}$, then $\kappa^2 < 0$; circular orbits are then unstable to radial perturbations and no real epicyclic frequency exists.
That instability criterion, $\kappa^2 < 0$, is the Rayleigh criterion for rotating flows.
