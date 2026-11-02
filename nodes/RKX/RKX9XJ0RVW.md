---
tag: RKX9XJ0RVW
kind: statement
role: fact
name: Fermat's principle
msc: [78A05, 49S05]
uses: [PQ25NHV0KS, PS0VV149ET, NSYMQMHPDN]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_principle
same_as:
  wikidata: Q331041
  wikipedia: Fermat's principle
---

## Statement

Let $\Omega \subseteq \R^3$ be a region filled with an isotropic optical medium of refractive index $n \colon \Omega \to (0, \infty)$.
For a piecewise smooth curve $\gamma \colon [a, b] \to \Omega$ define the *optical path length*
$$\mathcal{L}[\gamma] = \int_a^b n(\gamma(s))\, \abs{\gamma'(s)} \, ds.$$
Let $A$ and $B$ be two points of $\Omega$.
In geometric optics, the path of a light ray from $A$ to $B$ is a critical point of $\mathcal{L}$ among curves from $A$ to $B$.

## Remarks

Since light has speed $c/n$ in the medium, $\mathcal{L}[\gamma]/c$ is the travel time along $\gamma$, so the principle says the ray makes the travel time stationary.
The ray need not minimise the time: a ray reflected by a concave mirror can be a saddle point or a maximum.
When $n$ is smooth, the rays are the solutions of the [[Euler–Lagrange equation|PS0VV149ET]] of $\mathcal{L}$, which in arc length $\sigma$ reads $\frac{d}{d\sigma}\big(n\, \frac{dx}{d\sigma}\big) = \nabla n$.
Equivalently, the rays are the [[geodesics|NSYMQMHPDN]] of the metric $n^2 \abs{dx}^2$.
In a homogeneous medium ($n$ constant) the rays are straight lines.
Take two homogeneous media with indices $n_1, n_2$ separated by a plane.
Minimising $\mathcal{L}$ over broken lines gives Snell's law $n_1 \sin \theta_1 = n_2 \sin \theta_2$.
Here $\theta_i$ is the angle between the ray and the normal of the plane.
The principle is a statement of physics, not a theorem.
In wave optics it is recovered in the limit of short wavelength, where the phase solves the [[eikonal equation|HGMX1QGTAZ]] and the rays are its characteristic curves.

## Explanations

### L1 human

Light travelling from one point to another follows the path that takes the least time.
More exactly, its travel time does not change to first order under small changes of the path.
This explains why light goes straight in air, why it bends when it enters water, and why angles of incidence and reflection are equal at a mirror.

### L2 human

Fermat's principle is the model for all variational principles of physics.
The ray equations are the Euler–Lagrange equations of the optical length, and the rays are geodesics of the optical metric $n^2 \abs{dx}^2$.
The same formalism appears in mechanics through [[Maupertuis's principle|ZXY0AYKMXZ]], whose Jacobi metric plays the role of $n^2 \abs{dx}^2$.
