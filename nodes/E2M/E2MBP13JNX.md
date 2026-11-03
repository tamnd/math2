---
tag: E2MBP13JNX
kind: definition
name: Richtmyer–Meshkov instability
msc: ["76E17", 76L05]
defines: YED33V9DS5
uses: [3ETBXHDWBM, FRVV0NHBXT, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Richtmyer–Meshkov_instability
---

## Definition

Consider a perturbed interface $z = \eta(x, t)$ between two fluids of different densities $\rho_1$ and $\rho_2$.
Suppose that at time $t = 0$ the interface is impulsively accelerated, typically by the passage of a [[shock wave|FRVV0NHBXT]].
Its mean velocity then changes by $\Delta u$ in a time much shorter than the other time scales of the flow.
The *Richtmyer–Meshkov instability* is the growth of the perturbation $\eta$ of the interface after the impulse.

## Remarks

Let $\rho_2$ be the density on the side towards which the impulse points, and $A = (\rho_2 - \rho_1) / (\rho_2 + \rho_1)$ the Atwood number.
The linear equation of the [[Rayleigh–Taylor instability|3ETBXHDWBM]] for a mode $\eta = a(t) \cos kx$ is $a'' = A k g(t) a$.
Richtmyer's impulsive model uses it with $g(t) = \Delta u \, \delta(t)$.
This gives, for $t > 0$,
$$a(t) = a_0 + A k \, \Delta u \, a_0 \, t,$$
so the amplitude grows linearly in time, where $a_0$ is the amplitude just after the impulse.
Richtmyer proposed this model, with post-shock values of $A$ and $a_0$, and Meshkov later observed the instability in experiments.

Example: when a shock passes from a light gas into a heavy gas, $A > 0$ and the perturbation grows with the same phase.
When it passes from heavy to light, $A < 0$: the amplitude first decreases through zero, so the interface inverts its phase, and then grows.
Non-example: an unperturbed flat interface, $a_0 = 0$, stays flat in this model; the instability needs an initial perturbation.
