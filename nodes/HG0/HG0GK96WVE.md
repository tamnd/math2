---
tag: HG0GK96WVE
kind: example
name: Lamé problem of a thick-walled cylinder
msc: [74G05, 74B05]
illustrates: [6W00ZECYT0]
uses: [6W00ZECYT0, KG2XWEMJ30, 0BSW4T7THS]
sources:
  - url: https://en.wikipedia.org/wiki/Cylinder_stress
---

## Example

Consider a long hollow circular cylinder of homogeneous isotropic material in [[linear elasticity|6W00ZECYT0]], with inner radius $a$ and outer radius $b$, where $0 < a < b$.
A pressure $p_i$ acts on the inner surface and a pressure $p_o$ on the outer surface, and there is no body force.
In [[polar coordinates|0BSW4T7THS]] $(r, \theta)$, $a \le r \le b$, the Lamé solution for the in-plane [[stresses|KG2XWEMJ30]] is
$$\sigma_{rr} = A - \frac{B}{r^2}, \qquad \sigma_{\theta\theta} = A + \frac{B}{r^2}, \qquad \sigma_{r\theta} = 0,$$
with
$$A = \frac{p_i a^2 - p_o b^2}{b^2 - a^2}, \qquad B = \frac{(p_i - p_o) a^2 b^2}{b^2 - a^2}.$$

Check of equilibrium: for a radially symmetric stress the only nontrivial balance equation is $\frac{d \sigma_{rr}}{dr} + \frac{\sigma_{rr} - \sigma_{\theta\theta}}{r} = 0$, and here $\frac{2B}{r^3} - \frac{2B}{r^3} = 0$.
Check of the boundary conditions: $\sigma_{rr}(a) = \frac{p_i a^2 - p_o b^2 - (p_i - p_o) b^2}{b^2 - a^2} = -p_i$ and $\sigma_{rr}(b) = \frac{p_i a^2 - p_o b^2 - (p_i - p_o) a^2}{b^2 - a^2} = -p_o$.
Compatibility holds because the stresses come from the radial displacement $u_r = C r + D / r$ for suitable constants $C$ and $D$.
The sum $\sigma_{rr} + \sigma_{\theta\theta} = 2A$ is constant across the wall.

For internal pressure only ($p_o = 0$), the largest stress is the hoop stress at the inner surface, $\sigma_{\theta\theta}(a) = p_i \frac{b^2 + a^2}{b^2 - a^2}$.
For a thin wall, $b = a + t$ with $t$ small, this is close to $p_i a / t$, the thin-walled hoop stress formula.

## Explanations

### L1 human

A gun barrel or a high-pressure pipe has a thick wall pushed outward by the pressure inside.
The Lamé solution tells how the stress varies through the wall.
The material is pulled hardest around the circumference at the inner surface, and the pull decreases towards the outside.
So making the wall thicker helps less and less: the inner layer always carries more than its share.
