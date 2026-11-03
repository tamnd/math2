---
tag: NGRNGHQK8V
kind: example
name: Foucault pendulum
msc: [70J30, 70B05, 70F15]
illustrates: [6HZRX3WSQD]
uses: [HNXK6CJ5B2, 6HZRX3WSQD]
sources:
  - url: https://en.wikipedia.org/wiki/Foucault_pendulum
same_as:
  wikidata: Q178841
  wikipedia: Foucault pendulum
---

## Example

A Foucault pendulum is a long pendulum that is free to swing in every direction.
It is set up at a place of the Earth with latitude $\phi$.
Let $\Omega$ be the angular velocity of the Earth, and let $\Omega_z = \Omega \sin \phi$ be its vertical component.
In the [[rotating frame|HNXK6CJ5B2]] of the Earth, the [[Coriolis force|6HZRX3WSQD]] acts on the swinging mass.
For small swings, let $x$ and $y$ be the horizontal displacements to the east and to the north.
Let $\omega_0 = \sqrt{g/\ell}$, where $\ell$ is the length of the pendulum and $g$ is the acceleration of gravity.
Keeping only the vertical component of the rotation, the equations of motion are
$$x'' - 2 \Omega_z \, y' + \omega_0^2 x = 0, \qquad y'' + 2 \Omega_z \, x' + \omega_0^2 y = 0.$$
With $z = x + i y$ they become $z'' + 2 i \Omega_z \, z' + \omega_0^2 z = 0$.
Check: substituting $z(t) = e^{-i \Omega_z t} w(t)$ gives $w'' + (\omega_0^2 + \Omega_z^2) w = 0$.
So $w$ is a planar harmonic swing that does not turn.
In the northern hemisphere the factor $e^{-i \Omega_z t}$ turns it clockwise, seen from above, at the angular rate $\Omega_z = \Omega \sin \phi$.

## Remarks

At a pole the plane of swing turns once per sidereal day, about $23$ hours $56$ minutes.
At latitude $\phi$ it turns once in a sidereal day divided by $\abs{\sin \phi}$.
At the equator $\sin \phi = 0$, and the plane does not turn.
In the southern hemisphere $\sin \phi < 0$, and the plane turns anticlockwise.
Léon Foucault showed the effect in Paris in 1851, as a visible proof of the rotation of the Earth.

## Explanations

### L1 human

A heavy weight on a long wire keeps swinging back and forth in a fixed direction relative to the stars.
The Earth turns underneath it, so to people in the room the line of swing slowly rotates over the hours.
How fast it rotates depends on the latitude: fastest at the poles, not at all on the equator.
