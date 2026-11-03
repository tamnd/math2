---
tag: VJ752BFSQF
kind: example
name: Blasius boundary layer
msc: [76D10, 34B40]
instance_of: [XXDE4YP722]
uses: [XXDE4YP722, 579J5K9K5Z, 6DZC6HPDH2]
sources:
  - url: https://en.wikipedia.org/wiki/Blasius_boundary_layer
same_as:
  wikidata: Q4925317
  wikipedia: Blasius boundary layer
---

## Example

Consider the steady [[Prandtl boundary layer equations|XXDE4YP722]] over a flat plate $y = 0$, $x > 0$, with constant outer speed $U > 0$ and kinematic viscosity $\nu > 0$.
Set $\eta = y \sqrt{U / (\nu x)}$ and look for a stream function $\psi = \sqrt{\nu U x} \, f(\eta)$, with $u = \partial_y \psi$ and $v = -\partial_x \psi$.
Then $u = U f'(\eta)$ and $v = \frac12 \sqrt{\nu U / x} \, (\eta f' - f)$, and the boundary layer equations become the *Blasius equation*
$$2 f''' + f f'' = 0, \qquad f(0) = f'(0) = 0, \qquad f'(\eta) \to 1 \text{ as } \eta \to \infty.$$
The *Blasius boundary layer* is the flow given by its solution.

Check: continuity holds automatically for a stream function.
The conditions $f(0) = f'(0) = 0$ give $u = v = 0$ on the plate, and $f' \to 1$ gives $u \to U$ outside the layer.
Substituting into $u \, \partial_x u + v \, \partial_y u = \nu \, \partial_y^2 u$ and dividing by $U^2 / (2x)$ gives $-f f'' = 2 f'''$.

## Remarks

The boundary value problem has a unique solution, which is computed numerically: $f''(0) \approx 0.332$.
So the wall shear stress is $\tau_w \approx 0.332 \, \mu U \sqrt{U / (\nu x)}$, which decays like $x^{-1/2}$.
The [[displacement thickness|6DZC6HPDH2]] is $\delta^* \approx 1.72 \sqrt{\nu x / U}$, so the layer grows like the square root of the distance from the leading edge.
This is a [[similarity solution|579J5K9K5Z]]: the profiles at different $x$ are all the same after rescaling.

## Explanations

### L1 human

A stream flows along a thin flat plate, starting at its front edge.
Near the plate the fluid is slowed down, in a layer that gets thicker further back, like the square root of the distance.
The shape of the speed profile is the same everywhere along the plate, only stretched.
This makes the problem reduce to one ordinary differential equation, solved once and for all.
