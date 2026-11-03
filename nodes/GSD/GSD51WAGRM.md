---
tag: GSD51WAGRM
kind: definition
name: Lindblad resonance
msc: [85A05, 70F15]
defines: FJR64ZRB4E
uses: [GK34V4WF2V, 2FTZ7D8Z0F, 4F812GHFZK]
sources:
  - url: https://en.wikipedia.org/wiki/Lindblad_resonance
---

## Definition

Let a disc have circular [[angular velocity|2FTZ7D8Z0F]] $\Omega(R)$ and [[epicyclic frequency|GK34V4WF2V]] $\kappa(R)$.
Let a perturbation have $m$-fold symmetry, $m \ge 1$ an integer, and rotate rigidly with pattern speed $\Omega_p$.
So it depends on the angle $\varphi$ and the time $t$ only through $m (\varphi - \Omega_p t)$.
A *Lindblad resonance* is a radius $R$ at which
$$m \left( \Omega(R) - \Omega_p \right) = \pm \kappa(R).$$
With the sign $+$ it is the *inner Lindblad resonance*; with the sign $-$ it is the *outer Lindblad resonance*.
The radius where $\Omega(R) = \Omega_p$ is the *corotation resonance*.

## Remarks

Meaning: a star on a nearly circular orbit at radius $R$ meets the crests of the pattern with frequency $m \abs{\Omega(R) - \Omega_p}$.
At a Lindblad resonance this forcing frequency equals the natural frequency $\kappa$ of radial oscillation, a [[resonance|4F812GHFZK]].

Example: take a flat rotation curve $\Omega = v_0 / R$, so $\kappa = \sqrt{2} \, \Omega$, and a two-armed pattern, $m = 2$.
The inner Lindblad resonance solves $2(\Omega - \Omega_p) = \sqrt{2} \, \Omega$, that is $R = (1 - 1/\sqrt{2}) \, v_0 / \Omega_p$.
The outer one is at $R = (1 + 1/\sqrt{2}) \, v_0 / \Omega_p$, and corotation is at $R = v_0 / \Omega_p$.

Non-example: an axisymmetric perturbation, $m = 0$, does not rotate in angle, and the condition reduces to $\kappa = 0$; it gives no Lindblad resonance in a stable disc.

In planetary rings the pattern is the gravitational forcing of a moon, and Lindblad resonances in the rings excite spiral density waves.
