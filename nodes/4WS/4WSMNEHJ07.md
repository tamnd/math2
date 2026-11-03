---
tag: 4WSMNEHJ07
kind: definition
name: Aharonov–Bohm effect
msc: [81Q70, 78A25]
defines: Y4FPXY8MDM
uses: [8PEMR2J7EF, XRED3C547P, 6XPSV47R56, EPZR6H2WJN, WHDZ3MK56B]
sources:
  - url: https://en.wikipedia.org/wiki/Aharonov%E2%80%93Bohm_effect
---

## Definition

Let $\hbar > 0$ be the reduced Planck constant.
Let $\Omega \subseteq \R^3$ be an open set, and let $A$ be a smooth [[magnetic vector potential|8PEMR2J7EF]] on $\Omega$ with zero [[magnetic field|XRED3C547P]] there, $\nabla \times A = 0$ on $\Omega$.
Let a quantum particle of [[charge|6XPSV47R56]] $q$ move in $\Omega$ according to the [[Schrödinger equation|EPZR6H2WJN]] with the momentum operator $-i\hbar\nabla$ replaced by $-i\hbar\nabla - qA$.
For a closed loop $\gamma$ in $\Omega$, the *Aharonov–Bohm phase* of $\gamma$ is
$$\frac{q}{\hbar} \oint_\gamma A \cdot dl.$$
The *Aharonov–Bohm effect* is the fact that this phase can be nonzero modulo $2\pi$ when $\Omega$ is not simply connected.
A nonzero phase then shifts the interference between the parts of the wave function that pass on the two sides of the hole.

## Remarks

By Stokes' theorem, the phase is $q \Phi / \hbar$, where $\Phi$ is the magnetic flux through any surface spanned by $\gamma$, including the flux in the excluded region.
Since $\nabla \times A = 0$, the phase depends only on the homotopy class of $\gamma$ in $\Omega$; it is the [[holonomy|WHDZ3MK56B]] of the flat $U(1)$ connection given by $A$.
A gauge change $A \mapsto A + \nabla \chi$ does not change it modulo $2\pi$ when $e^{iq\chi/\hbar}$ is single-valued.

Example: an infinite solenoid of radius $a$ along the $z$-axis carrying the flux $\Phi$.
Outside it, in cylindrical coordinates, $A = \frac{\Phi}{2 \pi r} e_\theta$ for $r > a$.
Then $(\nabla \times A)_z = \frac{1}{r} \frac{d}{dr} \left( r \cdot \frac{\Phi}{2 \pi r} \right) = 0$, while a loop once around the axis gives $\oint A \cdot dl = \frac{\Phi}{2 \pi r} \cdot 2 \pi r = \Phi$ and the phase $q \Phi / \hbar$.

Non-example: if $\Omega$ is simply connected, then $A = \nabla \chi$ on $\Omega$ for a function $\chi$, every loop integral vanishes, and there is no effect.
The effect also vanishes when $q \Phi / \hbar$ is an integer multiple of $2\pi$.

## Explanations

### L1 human

The particle's wave function carries a phase that changes along its path by the line integral of the vector potential.
Around a closed loop this phase equals the enclosed magnetic flux, scaled by $q / \hbar$.
When the loop surrounds a region with flux that the particle cannot enter, the phase is still there, and interference reveals it.
