---
tag: R1HDJFZJ5F
kind: example
name: Elastic pendulum
msc: [70K30, 70K55, 70H07]
instance_of: [0EDKGA2FAK]
uses: [0YG0ZJPTWG, 0EDKGA2FAK, 4F812GHFZK, DBKXCGDKTD]
sources:
  - url: https://en.wikipedia.org/wiki/Elastic_pendulum
same_as:
  wikidata: Q12714444
  wikipedia: Elastic pendulum
---

## Example

Let $g > 0$ be the acceleration of gravity, and let $m, k, \ell_0 > 0$.
A point mass $m$ hangs from a fixed pivot on a massless spring with stiffness $k$ and rest length $\ell_0$.
It moves without friction in a vertical plane.
Let $r$ be the length of the spring and $\theta$ its angle from the downward vertical.
The Lagrangian is
$$L = \frac{m}{2} \left( r'^2 + r^2 \theta'^2 \right) - \frac{k}{2} (r - \ell_0)^2 + m g r \cos \theta.$$
So the elastic pendulum is a [[Hamiltonian system|0EDKGA2FAK]] with two degrees of freedom.
Its equilibrium hangs straight down with length $\ell = \ell_0 + m g / k$.
Check: at $\theta = 0$ and $r' = 0$, the radial equation $m r'' = m r \theta'^2 - k (r - \ell_0) + m g \cos \theta$ gives $r'' = 0$ exactly when $k (r - \ell_0) = m g$.

## Remarks

Linearising at the equilibrium gives two uncoupled [[harmonic oscillators|0YG0ZJPTWG]].
The spring mode has angular frequency $\omega_s = \sqrt{k/m}$, and the swinging mode, like a pendulum of length $\ell$, has angular frequency $\omega_p = \sqrt{g/\ell}$.
The nonlinear terms couple the two modes.
In the [[resonance|4F812GHFZK]] case $\omega_s = 2 \omega_p$, the energy passes back and forth between bouncing and swinging.
For general parameters and energies the motion can be [[chaotic|DBKXCGDKTD]].

## Explanations

### L1 human

An elastic pendulum is a weight on a spring that can both bounce up and down and swing from side to side.
The bouncing changes the length of the pendulum, and the swinging stretches the spring, so the two motions feed each other.
When the bouncing is exactly twice as fast as the swinging, a pure bounce slowly turns into a swing and back again.
