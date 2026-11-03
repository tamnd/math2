---
tag: Z6QVMQSHZE
kind: definition
name: Goldreich–Tremaine theory of disk–satellite interaction
msc: [85A05, 70F15, 85A30]
defines: NQ9ENS3YHK
uses: [FJR64ZRB4E, GK34V4WF2V, 3N68DNRF3W, 9G3VNW5ZP0, 7147M98XNR, 9636MFFSGC, YMDCDFBTQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Planetary_migration
---

## Definition

Consider a thin disk with surface density $\Sigma(r)$, angular velocity $\Omega(r)$ and [[epicyclic frequency|GK34V4WF2V]] $\kappa(r)$.
A satellite of small mass moves on a circular orbit of radius $r_s$ in the plane of the disk, with angular velocity $\Omega_s = \Omega(r_s)$.
The *Goldreich–Tremaine theory* treats the response of the disk to the satellite by linear perturbation theory, as follows.

1. The potential of the satellite is expanded in Fourier components $\Phi_m(r) \cos\big(m(\theta - \Omega_s t)\big)$, $m = 1, 2, \dots$, each rotating with the pattern speed $\Omega_s$.
2. The torque of each component is concentrated at its resonances: the [[Lindblad resonances|FJR64ZRB4E]], where $m\,(\Omega(r) - \Omega_s) = \pm \kappa(r)$, and the corotation resonance, where $\Omega(r) = \Omega_s$.
3. At a Lindblad resonance the satellite launches a spiral [[density wave|9G3VNW5ZP0]] that carries [[angular momentum|7147M98XNR]] away.
   The torque deposited in the disk is fixed by $\Sigma$, $\Phi_m$ and the local rotation curve.
   It does not depend on how the wave is finally damped.
4. The total [[torque|9636MFFSGC]] on the satellite is the sum of the Lindblad and corotation torques over all $m$.

## Remarks

The disk outside the orbit gains angular momentum from the satellite, and the disk inside loses angular momentum to it.
So the satellite repels the disk on both sides.
The corotation torque is proportional to the radial derivative of $\Sigma/B$, where $B$ is the [[Oort constant|3N68DNRF3W]] $B$ of the local rotation, so it vanishes when $\Sigma/B$ is constant.

Example: a small moon inside a narrow gap of a planetary ring has ring material on both sides.
The outer edge is pushed outward and the inner edge inward, so the moon keeps the gap open.
Shepherd satellites on both sides of a narrow ring, as for Saturn's F ring, confine it in the same way.

Non-example: a massive planet that strongly perturbs the disk violates the linear assumption of the theory, so the torque must be computed by nonlinear or numerical methods.

The difference between the outer and inner Lindblad torques is the source of Type I [[planetary migration|YMDCDFBTQ1]]; for typical disks the outer torque is larger and the planet drifts inward.
