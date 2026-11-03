---
tag: KK33RD9TVW
kind: example
name: Jeffery–Hamel flow
msc: [76D05, 76M55]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, 579J5K9K5Z, DF0M8YNQ3D]
sources:
  - url: https://en.wikipedia.org/wiki/Jeffery–Hamel_flow
same_as:
  wikidata: Q30596183
  wikipedia: Jeffery–Hamel flow
---

## Example

Let $0 < \alpha < \pi$ and consider the plane wedge $\set{(r, \theta) : r > 0, \ \abs{\theta} < \alpha}$ in polar coordinates, filled with a fluid of density $1$ and kinematic viscosity $\nu > 0$.
Fluid flows radially out of or into the apex, as from a source or a sink.
*Jeffery–Hamel flow* is the steady flow with purely radial velocity
$$u_r = \frac{\nu}{r} F(\theta), \qquad u_\theta = 0,$$
where $F$ solves
$$F'' + 4 F + F^2 = C, \qquad F(\pm \alpha) = 0,$$
for a constant $C$, and the flux $\nu \int_{-\alpha}^{\alpha} F(\theta) \, d\theta$ is prescribed.

Check: $\frac{1}{r} \partial_r (r u_r) = 0$, so the field is divergence-free.
The azimuthal [[Navier–Stokes equation|18KXZHVF4M]] gives $p = 2 \nu^2 F(\theta) / r^2 + P(r)$.
Putting this into the radial equation gives $\nu^2 (F'' + 4F + F^2) = r^3 P'(r)$.
The left side depends only on $\theta$ and the right side only on $r$, so both are a constant $\nu^2 C$.
The conditions $F(\pm \alpha) = 0$ are the [[no-slip condition|DF0M8YNQ3D]] on the walls.

## Remarks

This is a [[similarity solution|579J5K9K5Z]]: the problem reduces to an ordinary differential equation in the angle.
Multiplying by $F'$ and integrating once gives $\tfrac12 F'^2 + 2F^2 + \tfrac13 F^3 = C F + D$, so $F$ is an elliptic function.
For converging flow (a sink), the profile becomes flat in the middle with thin layers at the walls as the Reynolds number grows.
For diverging flow (a source) the symmetric outflow exists only below a critical Reynolds number, which depends on $\alpha$, and beyond it the solutions develop regions of backflow.

## Explanations

### L1 human

Think of a fluid squeezed through a V-shaped channel, either pouring out from the tip or draining into it.
Along each ray from the tip the speed falls off like one over the distance, and the shape of the speed across the channel is the same at every distance.
This turns the full flow equations into a single equation in the angle, which is one of the rare cases with an exact answer.
