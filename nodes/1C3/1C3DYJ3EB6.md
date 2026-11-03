---
tag: 1C3DYJ3EB6
kind: definition
name: Semiclassical gravity
msc: [83C47, 81T20]
defines: Q0W4SSDWKB
uses: [BY4QYYS788, P13KTBC7MH, REDZ92MKXX, JNK7GJ3AKE, W031YNVRE3]
sources:
  - url: https://en.wikipedia.org/wiki/Semiclassical_gravity
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]].
Let a [[quantum field theory|W031YNVRE3]] of matter be defined on $(M, g)$, with a state $\psi$ and a renormalized [[stress–energy tensor|REDZ92MKXX]] operator $\hat T_{\mu\nu}$.
In *semiclassical gravity*, the pair $(g, \psi)$ satisfies the semiclassical Einstein equations
$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8 \pi G}{c^4} \langle \psi | \hat T_{\mu\nu} | \psi \rangle.$$
Here $G_{\mu\nu}$ is the [[Einstein tensor|P13KTBC7MH]] of $g$ and $\Lambda$ is the cosmological constant.
The right side is the [[expectation value|JNK7GJ3AKE]] of $\hat T_{\mu\nu}$ in $\psi$.
At the same time the matter fields evolve by their quantum field equations on $(M, g)$.

## Remarks

Example: let $\psi$ be a coherent state of a field that is sharply peaked around a classical configuration.
Then $\langle \hat T_{\mu\nu} \rangle$ is close to the classical stress–energy tensor, and the equations reduce to the classical Einstein equations.
Non-example: a matter state that is a superposition of a mass in two places is a poor fit.
The metric responds only to the average, so it places half the mass at each spot.
This is a known limitation of the approximation.
The expectation value must be renormalized, for instance by point splitting, and this introduces local curvature terms that make the equations ambiguous up to higher-derivative terms.
Quantum field theory on a fixed curved background is the special case in which the back-reaction of the matter on $g$ is neglected.
