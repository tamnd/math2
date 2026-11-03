---
tag: AD8SVX0ZZ4
kind: conjecture
name: Finite-time blowup for the 3D Euler equations
msc: [76B03, 35Q31, 35B44]
uses: [RW0JK9VDZE, CG9JEATW3Q, 0MWV6ZTK6S, 0V33BNKZ9S, B3SXT9TWFA]
about: [RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_equations_(fluid_dynamics)
history:
  posed_by: "unknown"
  first_stated: "20th century"
---

## Statement

Consider the incompressible [[Euler equations|RW0JK9VDZE]] on $\R^3$ with no external force:
$$\partial_t u + (u \cdot \nabla) u = - \nabla p, \qquad \nabla \cdot u = 0.$$
Here $u \colon \R^3 \times [0, T) \to \R^3$ is the velocity and $p \colon \R^3 \times [0, T) \to \R$ is the pressure.
The conjecture says that there is an initial velocity $u_0 \colon \R^3 \to \R^3$ with the following properties.

1. Each component of $u_0$ lies in the [[Schwartz space|CG9JEATW3Q]] of $\R^3$.
2. The [[divergence|0MWV6ZTK6S]] of $u_0$ vanishes: $\nabla \cdot u_0 = 0$.
3. The [[smooth|0V33BNKZ9S]] solution $(u, p)$ with $u(\cdot, 0) = u_0$ exists only on a finite maximal time interval $[0, T^*)$, with $T^* < \infty$, and $\sup_{t < T^*} \norm{\nabla u(\cdot, t)}_{L^\infty} = \infty$.

## Remarks

The question is open: neither blowup nor global smoothness is known for such data.
For data in the Sobolev space $H^s(\R^3)$ with $s > 5/2$ and zero divergence, a unique solution exists on some interval $[0, T)$ with $T > 0$, and it stays smooth if $u_0$ is smooth.
The Beale–Kato–Majda criterion (1984) says that such a solution can be continued past $T^*$ if and only if $\int_0^{T^*} \norm{\omega(\cdot, t)}_{L^\infty} \, dt < \infty$, where $\omega = \nabla \times u$ is the [[vorticity|B3SXT9TWFA]].
So a blowup must make the vorticity unbounded.
In two space dimensions the vorticity is carried along by the flow, so its maximum is conserved, and smooth solutions exist for all time.
Tarek Elgindi proved finite-time blowup in $\R^3$ for velocities of class $C^{1,\alpha}$ with finite energy, for axisymmetric flows without swirl; these data are not smooth.
Jiajie Chen and Thomas Hou gave a computer-assisted proof of blowup from smooth data for axisymmetric flows in a cylinder with a solid boundary.
The viscous analogue is the problem of [[Navier–Stokes existence and smoothness|46Z1TVS2K6]].

## Explanations

### L1 human

The Euler equations describe a fluid with no internal friction.
Swirling motion in such a fluid can be stretched by the flow, and stretching makes the spin faster.
The question is whether this effect can make the spin infinite at some point after a finite time, starting from a calm and smooth flow in all of space.
In a flat, two-dimensional fluid this cannot happen, because there is no stretching.
In three dimensions nobody knows the answer, although blowup has been proved for rough initial flows and for flows inside a container with walls.
