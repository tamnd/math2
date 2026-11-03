---
tag: X32JRW8WWT
kind: definition
name: Oblique shock
msc: [76L05, 76J20]
defines: DSYRY5HCDD
uses: [FRVV0NHBXT, GFHJ858AN1, C5QBSMGHCR, G4EN6Y0ZZ2]
sources:
  - url: https://en.wikipedia.org/wiki/Oblique_shock
---

## Definition

Consider a steady planar flow of a polytropic gas with adiabatic exponent $\gamma > 1$.
Upstream the flow is uniform with [[Mach number|GFHJ858AN1]] $M_1 > 1$.
Let $\mu_1 \in (0, \pi/2)$ be the Mach angle, defined by $\sin \mu_1 = 1/M_1$.
An *oblique shock* is a straight [[shock wave|FRVV0NHBXT]] that makes an angle $\beta$ with the upstream velocity, where $\mu_1 < \beta < \pi/2$.
Across it, the velocity component tangent to the shock is continuous.
The normal component obeys the normal shock relations with upstream normal Mach number $M_1 \sin\beta$.

## Remarks

The flow is turned towards the shock by a deflection angle $\theta$, given by the $\theta$-$\beta$-$M$ relation
$$\tan\theta = 2 \cot\beta \, \frac{M_1^2 \sin^2\beta - 1}{M_1^2 (\gamma + \cos 2\beta) + 2}.$$
For given $M_1$, the deflection $\theta$ has a maximum $\theta_{\max}$.
A wedge of half-angle less than $\theta_{\max}$ carries an attached oblique shock, and there are two possible shock angles, the weak and the strong solution.
For a larger wedge angle the shock detaches from the tip and is curved.
The case $\beta = \pi/2$ is the normal shock, with $\theta = 0$.

Example: for $\gamma = 1.4$, $M_1 = 2$ and $\beta = \pi/4$, one has $\mu_1 = \pi/6 < \beta$ and normal Mach number $\sqrt 2 > 1$.
The relation gives $\tan\theta = 2 \cdot 1 \cdot \dfrac{2 - 1}{4 \cdot 1.4 + 2} = \dfrac{2}{7.6}$, so $\theta \approx 14.7^\circ$.

Non-example: if $\beta < \mu_1$, then $M_1 \sin\beta < 1$, the normal component is subsonic and no shock is possible at that angle.
The limit $\beta = \mu_1$ gives $\theta = 0$ and a jump of zero strength, a [[Mach wave|C5QBSMGHCR]].
