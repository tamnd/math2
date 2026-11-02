---
tag: PYEN6SFS9P
kind: statement
role: theorem
name: Nekhoroshev estimates
msc: [37J40, 70H08]
uses: [0EDKGA2FAK, M3T81YNSKC, N0N7CMRCMH]
about: [N0N7CMRCMH]
sources:
  - url: https://en.wikipedia.org/wiki/Nekhoroshev_estimates
same_as:
  wikidata: Q6989812
  wikipedia: Nekhoroshev estimates
---

## Statement

Let $n \ge 2$, let $D \subseteq \R^n$ be a bounded open set and let $\mathbb{T}^n = \R^n / 2\pi \Z^n$.
Use [[action-angle coordinates|M3T81YNSKC]] $(I, \theta)$ on $D \times \mathbb{T}^n$.
Consider the [[Hamiltonian system|0EDKGA2FAK]] with Hamiltonian
$$H_\varepsilon(I, \theta) = h(I) + \varepsilon f(I, \theta).$$
Assume that $h$ and $f$ are real-analytic on a complex neighbourhood of $\overline{D} \times \mathbb{T}^n$.
Assume that $h$ is steep, for example strictly convex.
Then there are constants $a, b, C, \varepsilon_0 > 0$ with the following property.
Let $0 < \varepsilon < \varepsilon_0$, and take a solution with $I(0)$ in $D$, away from the boundary of $D$.
Then
$$\abs{I(t) - I(0)} \le C \varepsilon^b \quad \text{for} \quad \abs{t} \le C \exp\left(\varepsilon^{-a}\right).$$

## Remarks

The proof has two parts.
The analytic part builds, near each resonance, a normal form in which the angle dependence that does not belong to the resonance is exponentially small in $1/\varepsilon$.
The geometric part uses steepness to show that an orbit cannot move far along the directions allowed by a resonance before it leaves the resonance zone.

For strictly convex $h$ one can take $a = b = \frac{1}{2n}$.

Unlike the [[KAM theorem|3ZZSXKM16Z]], the estimate holds for all initial conditions, not only for most of them, but only for a finite, exponentially long time.
Together with the existence of [[Arnold diffusion|ZVY046R4XB]], it shows that instability can occur in nearly integrable systems but only on exponentially long time scales.

Some steepness condition is needed.
For $n = 2$, $h(I) = I_1^2 - I_2^2$, which is not steep, and $f = \sin(\theta_1 + \theta_2)$, the equations give $(\theta_1 + \theta_2)' = 2(I_1 - I_2)$ and $I_1' = I_2' = -\varepsilon \cos(\theta_1 + \theta_2)$.
The solution with $I_1(0) = I_2(0)$ and $\theta_1(0) + \theta_2(0) = 0$ has $I_1(t) = I_1(0) - \varepsilon t$ and $I_2(t) = I_2(0) - \varepsilon t$, so the actions drift by order one in time of order $1/\varepsilon$.

## Explanations

### L1 human

Take an [[integrable system|N0N7CMRCMH]], where the actions never change, and add a small perturbation of size $\varepsilon$.
The theorem says that the actions then change only by a small amount for an extremely long time, longer than any power of $1/\varepsilon$.
So even when a system is not stable forever, it can be stable for times much longer than the age of the universe.

### L2 human

The Nekhoroshev estimates complement KAM theory.
KAM gives stability forever on a large set of invariant tori, but says nothing about the orbits between them.
Nekhoroshev gives stability for all orbits, over times that are exponentially long in a power of $1/\varepsilon$.
They are used in celestial mechanics, for example to discuss the long-time stability of asteroids near the Lagrange points.
