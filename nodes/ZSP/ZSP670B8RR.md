---
tag: ZSP670B8RR
kind: statement
role: proposition
name: Kármán–Howarth equation
msc: [76F05, 76D05]
uses: [18KXZHVF4M, VY307F8Z0S, NM5Q4845Z4, A2X0FXC6HK, YQ2KYDWRD0]
about: [VY307F8Z0S]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A1rm%C3%A1n%E2%80%93Howarth_equation
same_as:
  wikidata: Q16910971
  wikipedia: Kármán–Howarth equation
---

## Statement

Let $\mathbf{u}(x, t)$ be a statistically homogeneous and isotropic velocity field in $\R^3$ that solves the incompressible [[Navier–Stokes equations|18KXZHVF4M]] with kinematic [[viscosity|NM5Q4845Z4]] $\nu$ and no forcing.
Write $\langle \cdot \rangle$ for the ensemble average, $u_1$ for the first component of $\mathbf{u}$, $\mathbf{e}_1$ for the first unit vector, and $u'^2 = \langle u_1^2 \rangle$.
Define the longitudinal correlation functions $f(r, t)$ and $k(r, t)$ for $r > 0$ by
$$u'^2 f(r, t) = \langle u_1(x, t)\, u_1(x + r\mathbf{e}_1, t) \rangle, \qquad u'^3 k(r, t) = \langle u_1(x, t)^2\, u_1(x + r\mathbf{e}_1, t) \rangle.$$
Then
$$\frac{\partial}{\partial t}\bigl(u'^2 f\bigr) = u'^3 \left(\frac{\partial k}{\partial r} + \frac{4k}{r}\right) + 2\nu u'^2 \left(\frac{\partial^2 f}{\partial r^2} + \frac{4}{r} \frac{\partial f}{\partial r}\right).$$

## Remarks

The proof takes the Navier–Stokes equations at the two points $x$ and $x + r\mathbf{e}_1$, multiplies them and averages.
Isotropy then writes every two- and three-point tensor in terms of $f$ and $k$.
Incompressibility removes the pressure terms, because in isotropic turbulence the pressure–velocity correlation vanishes.
The equation is not closed: it is one equation for the two unknowns $f$ and $k$, an instance of the [[turbulence closure problem|A2X0FXC6HK]].
At $r = 0$ it gives $\frac{d}{dt} u'^2 = 10 \nu u'^2 f''(0) = -\frac{2}{3}\varepsilon$, where $\varepsilon$ is the mean dissipation rate.
In the inertial range, where the viscous term and the time derivative of $f$ are negligible, integration gives Kolmogorov's four-fifths law $\langle \delta u(r)^3 \rangle = -\frac{4}{5} \varepsilon r$ for the longitudinal increment $\delta u(r)$.

## Explanations

### L1 human

In turbulence one cannot follow every eddy, so one studies how velocities at two points separated by a distance $r$ are related on average.
The Kármán–Howarth equation says how this two-point correlation changes in time.
It has a term that moves energy between scales, through a correlation of three velocities, and a term for viscous loss.
It is exact, but it does not determine the three-velocity term, so on its own it cannot be solved.

### L2 human

The equation is the main exact dynamical relation of homogeneous isotropic turbulence.
Written for the second and third order structure functions, it yields the four-fifths law, one of the few exact results in the theory.
Its Fourier transform is the equation for the energy spectrum, in which the triple correlation becomes the energy transfer term of the [[energy cascade|YQ2KYDWRD0]].
