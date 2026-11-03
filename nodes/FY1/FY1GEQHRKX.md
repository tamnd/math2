---
tag: FY1GEQHRKX
kind: definition
name: Strömgren sphere
msc: [85A25]
defines: 3MRX3F8M0Z
uses: [EH021K5438]
sources:
  - url: https://en.wikipedia.org/wiki/Str%C3%B6mgren_sphere
---

## Definition

Let a star emit $Q > 0$ hydrogen-ionising photons per second into an infinite, static, uniform gas of pure hydrogen.
Let $n$ be the number density of hydrogen nuclei.
Let $\alpha_B > 0$ be the case-B coefficient of [[recombination|EH021K5438]] of hydrogen at the temperature of the ionised gas.
Assume that inside a ball around the star the gas is fully ionised, so the electron and proton densities both equal $n$.
Assume also that every ionising photon is absorbed in the ball.
The *Strömgren sphere* is this ball, and its radius $R_S$ is fixed by the balance of ionisations and recombinations:
$$Q = \frac{4\pi}{3} R_S^3 \, n^2 \alpha_B, \qquad R_S = \left( \frac{3 Q}{4 \pi n^2 \alpha_B} \right)^{1/3}.$$

## Remarks

Example: if the density $n$ is multiplied by $8$ and $Q$ and $\alpha_B$ are unchanged, then $R_S$ is multiplied by $8^{-2/3} = 1/4$.
Non-example: around a source of hard X-rays, whose photons have a long mean free path, the gas is only partly ionised throughout.
That region is not a Strömgren sphere, because the assumption of full ionisation with a sharp edge fails.
The case-B coefficient omits recombinations directly to the ground state, because the photon they emit is ionising and is absorbed again nearby.
The transition layer is about one mean free path of an ionising photon in neutral gas thick.
For typical H II regions this is much smaller than $R_S$.
