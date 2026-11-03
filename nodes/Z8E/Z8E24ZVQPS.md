---
tag: Z8E24ZVQPS
kind: statement
role: fact
name: Gravitational memory effect
msc: [83C35, 83C30]
uses: [SJ0A4TZTFR, AH62KSWA6Y, 3HTF65XMF7]
about: [SJ0A4TZTFR]
sources:
  - url: https://en.wikipedia.org/wiki/Gravitational_memory_effect
same_as:
  wikidata: Q97943607
  wikipedia: Gravitational memory effect
---

## Statement

Work in units with $G = c = 1$, in an [[asymptotically flat|3HTF65XMF7]] spacetime in the weak-field regime of [[linearized gravity|AH62KSWA6Y]].
Let a burst of [[gravitational waves|SJ0A4TZTFR]] pass a pair of freely falling test masses at a large distance $r$ from the source.
Let $h^{TT}_{jk}$ be the transverse-traceless metric perturbation at the masses.
Then $h^{TT}_{jk}$ need not return to its initial value after the burst.
There can be a permanent change
$$\Delta h^{TT}_{jk} = h^{TT}_{jk}(\text{after}) - h^{TT}_{jk}(\text{before}) \neq 0,$$
and the proper distance between the test masses changes permanently by an amount proportional to $\Delta h^{TT}_{jk}$.
Suppose the source emits or absorbs unbound bodies of masses $M_A$ and velocities $\mathbf{v}_A$.
The linear part of the change is then
$$\Delta h^{TT}_{jk} = \Delta \sum_A \left[ \frac{4 M_A}{r \sqrt{1 - \abs{\mathbf{v}_A}^2}} \, v_A^j v_A^k \right]^{TT}.$$
Here $\Delta$ is the difference between the final and the initial sums.
The symbol $[\,\cdot\,]^{TT}$ is the transverse-traceless part with respect to the direction to the observer.

## Remarks

The linear memory comes from a net change of the second time derivative of the moments of the source between early and late times.
Zel'dovich and Polnarev found it in 1974.
Christodoulou showed in 1991 that there is also a nonlinear memory, sourced by the energy carried off by the gravitational waves themselves.
The nonlinear memory is present even for a bound system such as a binary that merges, because the radiated waves act as an unbound outgoing flux of energy.
The memory is a zero-frequency effect: it grows during the burst and then stays.
It is linked to the asymptotic symmetries of asymptotically flat spacetimes.

## Explanations

### L1 human

A gravitational wave stretches and squeezes space as it passes.
One might expect everything to return to its old place afterwards.
The memory effect says that this need not happen: two free masses can end up at a slightly different distance from each other than before the wave arrived.
The wave leaves a permanent record of its passage.

### L2 human

In linearized theory the far-field wave form is a time derivative of source moments.
So a net change of those derivatives between early and late times leaves a step in $h^{TT}_{jk}$.
Such steps arise when masses fly apart, as in a hyperbolic encounter or an explosion.
In full general relativity the radiated gravitational energy adds a further step, the nonlinear memory, which is of the same order for compact binary mergers.
Detecting the memory in gravitational-wave data is an active goal of observation.
