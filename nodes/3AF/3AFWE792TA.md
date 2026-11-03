---
tag: 3AFWE792TA
kind: definition
name: Stagnation pressure
msc: [76N15, 76G25]
defines: SYS9BF1K2N
uses: [SH8FHGTMSE, GFHJ858AN1, 7XFWQVWPG1, JSDMGGTG7G]
sources:
  - url: https://en.wikipedia.org/wiki/Stagnation_pressure
---

## Definition

Consider a fluid particle with static pressure $p$, density $\rho$ and speed $u$.
Its *stagnation pressure* $p_0$ is the pressure it would have after being brought to rest by an [[isentropic|SH8FHGTMSE]] process, that is, adiabatically and reversibly.

1. For an incompressible fluid, $p_0 = p + \frac{1}{2}\rho u^2$.
2. For an ideal gas with constant ratio of specific heats $\gamma$, at [[Mach number|GFHJ858AN1]] $M$,
$$p_0 = p \left(1 + \frac{\gamma - 1}{2} M^2\right)^{\gamma/(\gamma - 1)}.$$

## Remarks

Example: air at $p = 100\ \mathrm{kPa}$ moving at $M = 1$ with $\gamma = 1.4$ has $p_0 = 100 \cdot 1.2^{3.5} \approx 189\ \mathrm{kPa}$.
For small $M$ the binomial expansion gives $p_0 \approx p + \frac{1}{2}\rho u^2 (1 + M^2/4)$, which recovers formula 1 as $M \to 0$.
In steady inviscid flow without heat exchange $p_0$ is constant along streamlines, which is a form of [[Bernoulli's principle|7XFWQVWPG1]].
Non-example: the static pressure $p$ is not a stagnation pressure, because it is measured moving with the fluid and does not include the kinetic energy.
Across a [[shock wave|JSDMGGTG7G]] the stagnation pressure drops, since the process is not reversible.
