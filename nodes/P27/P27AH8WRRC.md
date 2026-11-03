---
tag: P27AH8WRRC
kind: example
name: Poiseuille flow
msc: [76D05, 76D07]
illustrates: [18KXZHVF4M]
uses: [18KXZHVF4M, DF0M8YNQ3D, NM5Q4845Z4, T4ZV12BVHN]
sources:
  - url: https://en.wikipedia.org/wiki/Hagen–Poiseuille_equation
---

## Example

Consider a [[Newtonian fluid|T4ZV12BVHN]] of density $\rho > 0$ and dynamic [[viscosity|NM5Q4845Z4]] $\mu > 0$ in the straight pipe $\set{(x, y, z) : x^2 + y^2 < R^2}$ of radius $R > 0$.
Let $G > 0$ be a constant and let $r = \sqrt{x^2 + y^2}$.
*Poiseuille flow* is the velocity field and pressure
$$u = \frac{G}{4 \mu} (R^2 - r^2) \, e_z, \qquad p = p_0 - G z,$$
where $e_z = (0, 0, 1)$ and $p_0$ is a constant.
It solves the steady [[Navier–Stokes equations|18KXZHVF4M]] $\rho (u \cdot \nabla) u = -\nabla p + \mu \Delta u$, $\nabla \cdot u = 0$.

Check: $u$ has only a $z$-component $w(r)$, which does not depend on $z$, so $\nabla \cdot u = \partial_z w = 0$ and $(u \cdot \nabla) u = w \, \partial_z u = 0$.
In polar form $\Delta w = \frac{1}{r} \frac{d}{dr}\big( r w'(r) \big) = \frac{1}{r} \frac{d}{dr}\Big( -\frac{G r^2}{2 \mu} \Big) = -\frac{G}{\mu}$.
So $\mu \Delta u = -G e_z = \nabla p$, and the momentum equation holds.
On the wall $r = R$ the velocity is zero, so the [[no-slip condition|DF0M8YNQ3D]] holds.

## Remarks

The volume flux through a cross-section is $Q = \int_0^R w(r) \, 2 \pi r \, dr = \frac{\pi G R^4}{8 \mu}$.
For a pipe of length $L$ with pressure drop $\Delta p = G L$, this is the Hagen–Poiseuille law $\Delta p = \frac{8 \mu L Q}{\pi R^4}$.
The flux grows like the fourth power of the radius.
The plane analogue between walls $y = \pm h$ is $u = \frac{G}{2 \mu} (h^2 - y^2) e_x$.
Real pipe flow follows this profile only at moderate Reynolds numbers; at large ones it becomes turbulent.

## Explanations

### L1 human

Push a liquid through a straight pipe and it flows fastest in the middle and not at all at the wall.
The speed profile is a parabola across the pipe.
Halving the radius cuts the flow rate by a factor of sixteen at the same pressure, which is why narrow blood vessels matter so much.
