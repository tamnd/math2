---
tag: PEMQHB13Q3
kind: definition
name: Blandford–Znajek process
msc: [83C57, 85A30, 76W05]
defines: 2FJ9VNFMQJ
uses: [AHEEC3Y5JF, 9BWWD4QK8Y, 6Y50T68WKY]
sources:
  - url: https://en.wikipedia.org/wiki/Blandford%E2%80%93Znajek_process
---

## Definition

Let $G$ be the gravitational constant and $c$ the speed of light.
Let a Kerr black hole of mass $M$ have dimensionless spin $a \in (0, 1)$ and horizon radius $r_H = (GM/c^2)(1 + \sqrt{1 - a^2})$.
Its horizon angular velocity is $\Omega_H = a c / (2 r_H)$.
Let a stationary, axisymmetric magnetosphere surround the hole, and let some of its field lines cross the horizon.
Its electromagnetic field solves [[Maxwell's equations|9BWWD4QK8Y]] on the Kerr spacetime and is [[force-free|AHEEC3Y5JF]].
In such a field each field line rotates rigidly with an angular velocity $\Omega_F$, constant along the line.
The *Blandford–Znajek process* is the outward flux of electromagnetic energy through the horizon along the field lines with $0 < \Omega_F < \Omega_H$.
The rotational energy of the hole pays for this flux.

## Remarks

On a field line crossing the horizon the outward energy flux is proportional to $\Omega_F (\Omega_H - \Omega_F)$, so it is positive exactly when $0 < \Omega_F < \Omega_H$ and is largest for $\Omega_F = \Omega_H / 2$.
For a magnetic flux $\Phi$ through the horizon, the total power has the form $P \approx \kappa \, \Phi^2 \Omega_H^2 / c$ in Gaussian units, with a dimensionless factor $\kappa$ that depends on the field geometry.

Example: in the slowly rotating split monopole field of the original paper, the field lines rotate at about $\Omega_H/2$, and energy flows out to infinity along all of them.

Non-example: a non-rotating hole, with the [[Schwarzschild metric|6Y50T68WKY]], has $\Omega_H = 0$; no $\Omega_F$ satisfies $0 < \Omega_F < 0$, so there is no Blandford–Znajek power.

The process is often compared with the Penrose process, since both draw on the rotational energy of the hole.
