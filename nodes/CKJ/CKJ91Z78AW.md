---
tag: CKJ91Z78AW
kind: definition
name: Earth's rotation
msc: [86A30, "70E15", 70F15]
defines: EF1Q2JF8QH
uses: [2FTZ7D8Z0F, EZ9P9ERKNE]
sources:
  - url: https://en.wikipedia.org/wiki/Earth%27s_rotation
---

## Definition

Let $\mathcal{T}$ be a terrestrial reference frame: an orthonormal frame attached to the Earth's crust, with origin at the centre of mass.
Let $\mathcal{C}$ be a celestial reference frame: an orthonormal frame whose axes are fixed relative to distant extragalactic sources.
For each time $t$, let $R(t) \in SO(3)$ map the coordinates of a vector in $\mathcal{T}$ at time $t$ to its coordinates in $\mathcal{C}$.
The *rotation of the Earth* is the function $t \mapsto R(t)$.
Its [[angular velocity|2FTZ7D8Z0F]] vector $\omega(t) \in \R^3$, in celestial coordinates, is defined by
$$\dot R(t)\, R(t)^{T} v = \omega(t) \times v \quad \text{for all } v \in \R^3.$$

## Remarks

Example: a uniform rotation about the third axis with rate $\Omega$ is $R(t) = \begin{pmatrix} \cos\Omega t & -\sin\Omega t & 0 \\ \sin\Omega t & \cos\Omega t & 0 \\ 0 & 0 & 1 \end{pmatrix}$, and one checks that $\dot R R^T v = (0, 0, \Omega) \times v$, so $\omega = (0, 0, \Omega)$.
For the Earth, $\Omega \approx 7.292115 \cdot 10^{-5}$ rad/s.
Non-example: the orbital motion of the Earth around the Sun is a translation of the origin, not part of $R(t)$.
In practice $R(t)$ is factored into precession–nutation, the Earth rotation angle, and [[polar motion|QTRK8GS2Y1]], whose parameters are published by the International Earth Rotation and Reference Systems Service.
The model treats the crust as a [[rigid body|EZ9P9ERKNE]]; the frame $\mathcal{T}$ is defined so that the crust has no net rotation relative to it.
