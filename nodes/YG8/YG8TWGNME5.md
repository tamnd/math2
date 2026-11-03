---
tag: YG8TWGNME5
kind: statement
role: theorem
name: Toomre's stability criterion
msc: [85A05, "76E20"]
uses: [GK34V4WF2V, 9G3VNW5ZP0, S1PZ23YAXQ]
about: [GK34V4WF2V]
sources:
  - url: https://en.wikipedia.org/wiki/Toomre%27s_stability_criterion
same_as:
  wikidata: Q18353297
  wikipedia: Toomre's stability criterion
---

## Statement

Consider an infinitely thin, differentially rotating disc with surface density $\Sigma > 0$ and [[epicyclic frequency|GK34V4WF2V]] $\kappa > 0$ at a radius $R$, and consider tightly wound axisymmetric perturbations.

1. For a fluid disc with sound speed $c_s$, all such perturbations are stable if and only if
$$Q = \frac{c_s \kappa}{\pi G \Sigma} \ge 1.$$
2. For a disc of stars with radial velocity dispersion $\sigma_R$ and Maxwellian velocities, all such perturbations are stable if and only if
$$Q = \frac{\sigma_R \kappa}{3.36 \, G \Sigma} \ge 1.$$

## Remarks

For the fluid disc, the [[density wave|9G3VNW5ZP0]] dispersion relation with $m = 0$ reads $\omega^2 = \kappa^2 - 2 \pi G \Sigma \abs{k} + c_s^2 k^2$.
The right side is smallest at $\abs{k} = \pi G \Sigma / c_s^2$, where it equals $\kappa^2 - (\pi G \Sigma / c_s)^2$.
So $\omega^2 \ge 0$ for all $k$ if and only if $c_s \kappa \ge \pi G \Sigma$; otherwise some $\omega$ is imaginary and the mode grows exponentially.
The stellar case uses the stellar dispersion relation, and the constant $3.36$ comes from minimising its reduction factor.

The criterion combines two stabilising effects against the [[Jeans instability|S1PZ23YAXQ]] of the disc: pressure, which acts on short wavelengths, and rotation through $\kappa$, which acts on long wavelengths.
Without rotation, $\kappa = 0$, every disc with $\Sigma > 0$ is unstable at long wavelengths.
The result is due to A. Toomre (1964) for stellar discs; the fluid version is often credited to V. S. Safronov (1960) as well.
$Q \ge 1$ does not guarantee stability against non-axisymmetric perturbations.

## Explanations

### L1 human

A rotating disc of gas or stars tends to clump under its own gravity.
Two things fight the clumping: random motions, which spread small clumps, and rotation, which spins large clumps apart.
Toomre's number $Q$ compares these effects with gravity.
If $Q$ is at least one, the disc is safe against ring-shaped clumps; if it is below one, the disc fragments.

### L2 human

In galaxy discs, star formation is often observed where the gas has $Q$ near or below one, so $Q$ is a standard diagnostic.
The same criterion governs the fragmentation of massive protoplanetary and accretion discs.
It is the rotating-disc version of the Jeans criterion, with the extra $\kappa$ term coming from the epicyclic motion.
