---
tag: H2EG94MRFT
kind: example
name: Von Kármán swirling flow
msc: [76D05, 76U05]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, 579J5K9K5Z, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Von_Kármán_swirling_flow
same_as:
  wikidata: Q30596026
  wikipedia: Von Kármán swirling flow
---

## Example

An infinite plane disk $z = 0$ rotates with constant angular velocity $\Omega > 0$ about the $z$-axis.
A fluid of kinematic viscosity $\nu > 0$ fills $z > 0$ and is at rest far away.
In cylindrical coordinates $(r, \theta, z)$ set $\zeta = z \sqrt{\Omega / \nu}$ and look for a velocity of the form
$$u_r = r \Omega F(\zeta), \qquad u_\theta = r \Omega G(\zeta), \qquad u_z = \sqrt{\nu \Omega} \, H(\zeta),$$
with a pressure that depends only on $z$.
*Von Kármán swirling flow* is the solution of the [[Navier–Stokes equations|18KXZHVF4M]] of this form.
The functions $F, G, H$ solve
$$2F + H' = 0, \qquad F'' = F^2 - G^2 + H F', \qquad G'' = 2 F G + H G',$$
with $F(0) = 0$, $G(0) = 1$, $H(0) = 0$ and $F, G \to 0$ as $\zeta \to \infty$.

Check: the divergence is $\frac{1}{r} \partial_r (r u_r) + \partial_z u_z = \Omega (2F + H')$, which vanishes.
In the radial momentum equation every term is $r \Omega^2$ times a function of $\zeta$.
The pressure term drops because $p$ does not depend on $r$, and this gives the equation for $F''$.
The azimuthal equation gives the equation for $G''$ in the same way.
The conditions at $\zeta = 0$ are the [[no-slip condition|DF0M8YNQ3D]] on the rotating disk.

## Remarks

This is a [[similarity solution|579J5K9K5Z]] that reduces the Navier–Stokes equations exactly to ordinary differential equations, found by von Kármán in 1921.
The disk acts as a centrifugal pump: it throws fluid outward along the disk.
Fluid is drawn toward the disk from above, so $H$ tends to a negative constant at infinity.
The layer affected by the rotation has a thickness of order $\sqrt{\nu / \Omega}$, independent of $r$.

## Explanations

### L1 human

Spin a large plate under still water.
The water touching the plate is dragged round and flung outward, and to replace it, water from above flows down toward the plate.
All of this happens in a layer of the same thickness everywhere, which makes the flow simple enough to compute exactly.
