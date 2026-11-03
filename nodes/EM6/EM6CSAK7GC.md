---
tag: EM6CSAK7GC
kind: example
name: Kovalevskaya top
msc: ["70E40", "70E17", 37J35]
instance_of: [N0N7CMRCMH]
uses: [PN15F4ZS8D, WVGTEH6P10, C4864H02XR]
sources:
  - url: https://en.wikipedia.org/wiki/Lagrange,_Euler,_and_Kovalevskaya_tops
---

## Example

The *Kovalevskaya top* is a heavy rigid body turning about a fixed point $O$ in a uniform gravitational field, with the following mass distribution.
Its principal moments of inertia at $O$ are $I_1 = I_2 = 2I_3$.
Its centre of mass lies in the plane of the first two principal axes, at $\ell e_1$ with $\ell \ne 0$.
Let $m$ be its mass and $g$ the gravitational acceleration, and put $c = m g \ell / I_3$.
Let $\omega$ be the angular velocity and $\gamma$ the upward unit vertical in the body frame.
The Euler–Poisson equations read
$$2\dot\omega_1 = \omega_2\omega_3, \quad 2\dot\omega_2 = -\omega_1\omega_3 + c\gamma_3, \quad \dot\omega_3 = -c\gamma_2, \qquad \dot\gamma = \gamma \times \omega.$$

Besides the energy and the vertical component of the angular momentum, it has the *Kovalevskaya integral*
$$K = (\omega_1^2 - \omega_2^2 - c\gamma_1)^2 + (2\omega_1\omega_2 - c\gamma_2)^2.$$
The check: put $z = \omega_1 + i\omega_2$ and $\xi = \gamma_1 + i\gamma_2$, so that $K = \abs{z^2 - c\xi}^2$.
The equations give $\dot z = -\tfrac{i}{2}\omega_3 z + \tfrac{i}{2}c\gamma_3$ and $\dot\xi = -i\omega_3\xi + i\gamma_3 z$.
Hence $\frac{d}{dt}(z^2 - c\xi) = -i\omega_3 (z^2 - c\xi)$, and the modulus of $z^2 - c\xi$ is constant.
With three integrals in involution it is an [[integrable system|N0N7CMRCMH]].

## Remarks

Sofia Kovalevskaya found this case and solved it by hyperelliptic functions, work for which she received the Prix Bordin of the Paris Academy in 1888.
Together with the Euler top and the [[Lagrange top|C4864H02XR]], it is one of the three cases of the heavy top that are integrable for all initial conditions.

## Explanations

### L1 human

The Kovalevskaya top is a special spinning top whose motion can be solved exactly, although its centre of mass does not lie on its axis of symmetry.
Its hidden conserved quantity $K$ is not visible from any symmetry of the body; it was found by asking when the solutions are well behaved as functions of complex time.
