---
tag: QCGAG68T5Z
kind: definition
name: Precession
msc: ["70E05", "70E17"]
defines: CFE9SNEHMP
uses: [EZ9P9ERKNE, 7WGBNTRQ2S, 2FTZ7D8Z0F]
sources:
  - url: https://en.wikipedia.org/wiki/Precession
---

## Definition

Let a [[rigid body|EZ9P9ERKNE]] turn about a fixed point $O$.
Let $e_3$ be a unit vector fixed in the body, such as a symmetry axis.
Let $u$ be a fixed unit vector in space, such as the upward vertical.
Describe the orientation of the body by [[Euler angles|7WGBNTRQ2S]] $(\varphi, \theta, \psi)$ with respect to $u$.
Here $\theta \in [0, \pi]$ is the angle between $u$ and $e_3$, and $\varphi$ is the azimuth of $e_3$ about $u$.
The angle $\psi$ is the angle of rotation of the body about $e_3$.
The *precession* of the body is the change of the angle $\varphi$ in time, that is, the rotation of the axis $e_3$ about $u$.
Its rate $\dot\varphi$ is the *precession rate*.

## Remarks

The [[angular velocity|2FTZ7D8Z0F]] of the body is $\dot\varphi\, u + \dot\theta\, n + \dot\psi\, e_3$, where $n$ is the unit vector along the line of nodes, perpendicular to $u$ and $e_3$.
So the motion splits into precession $\dot\varphi$, nutation $\dot\theta$ and spin $\dot\psi$.
The angle $\varphi$ is defined only when $e_3 \ne \pm u$.

Example: a symmetric top with mass $m$, centre of mass at distance $\ell$ from $O$ on its axis, and moment $I_3$ about the axis, spinning fast with rate $\omega_3$.
For a fast top in steady motion the precession rate is approximately $\dot\varphi \approx m g \ell / (I_3 \omega_3)$.

Non-example: a body spinning about a fixed axis $e_3$ has constant $\varphi$, so it does not precess.

## Explanations

### L1 human

Precession is the circling of a spinning body's axis about a fixed direction.
In the language of Euler angles it is the change of the first angle, the one measured around the fixed direction.
