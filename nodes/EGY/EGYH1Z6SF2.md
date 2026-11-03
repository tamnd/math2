---
tag: EGYH1Z6SF2
kind: statement
role: theorem
name: Lagrange's planetary equations
msc: [70F15, 70M20, 70H09]
uses: [WW0JHSBE6D, KAJTW4B41Q, K6KNWEVRY4, 0ABK9V9Y64]
about: [WW0JHSBE6D]
sources:
  - url: https://en.wikipedia.org/wiki/Perturbation_(astronomy)
---

## Statement

Let $\mu > 0$ and let a body move by
$$r'' = -\frac{\mu\, r}{\norm{r}^3} + \nabla_r \mathcal{R}(r, t),$$
where the disturbing function $\mathcal{R}$ is a smooth function and $\nabla_r$ is its [[gradient|0ABK9V9Y64]] in $r$.
Assume that the [[osculating orbit|KAJTW4B41Q]] stays elliptic with $0 < e < 1$ and $0 < i < \pi$.
Let $a, e, i, \Omega, \omega$ and the mean anomaly $M$ be its [[orbital elements|K6KNWEVRY4]], and let $n = \sqrt{\mu / a^3}$ be the mean motion.
Write $\mathcal{R}$ as a function of these elements and $t$, with partial derivatives in $a$ taken at fixed $M$.
Then the elements satisfy
$$\frac{da}{dt} = \frac{2}{na} \frac{\partial \mathcal{R}}{\partial M},$$
$$\frac{de}{dt} = \frac{1 - e^2}{n a^2 e} \frac{\partial \mathcal{R}}{\partial M} - \frac{\sqrt{1 - e^2}}{n a^2 e} \frac{\partial \mathcal{R}}{\partial \omega},$$
$$\frac{di}{dt} = \frac{\cos i}{n a^2 \sqrt{1 - e^2} \sin i} \frac{\partial \mathcal{R}}{\partial \omega} - \frac{1}{n a^2 \sqrt{1 - e^2} \sin i} \frac{\partial \mathcal{R}}{\partial \Omega},$$
$$\frac{d\Omega}{dt} = \frac{1}{n a^2 \sqrt{1 - e^2} \sin i} \frac{\partial \mathcal{R}}{\partial i},$$
$$\frac{d\omega}{dt} = \frac{\sqrt{1 - e^2}}{n a^2 e} \frac{\partial \mathcal{R}}{\partial e} - \frac{\cos i}{n a^2 \sqrt{1 - e^2} \sin i} \frac{\partial \mathcal{R}}{\partial i},$$
$$\frac{dM}{dt} = n - \frac{1 - e^2}{n a^2 e} \frac{\partial \mathcal{R}}{\partial e} - \frac{2}{na} \frac{\partial \mathcal{R}}{\partial a}.$$

## Remarks

The proof is Lagrange's method of variation of constants.
The elements are functions of $(r, r')$ that are constant along Kepler motion, so along the perturbed motion their derivatives are linear in the perturbing acceleration.
Computing the Poisson brackets of the elements, or equivalently the Lagrange brackets, gives the coefficients above.
Without the term $\nabla_r \mathcal{R}$ the right sides vanish, except $dM/dt = n$, which is uniform motion on a fixed ellipse.
Example: averaging the $J_2$ term of the Earth's potential over one orbit and inserting it in the equation for $\Omega$ gives the classical regression of the node of a satellite.
The factors $1/e$ and $1/\sin i$ show why the equations break down for nearly circular or nearly equatorial orbits; other sets of elements are used there.
For forces that do not come from a potential, such as drag, one uses Gauss's form of the equations instead.

## Explanations

### L1 human

A perturbed orbit can be seen as an ellipse whose shape and tilt change slowly.
These equations tell exactly how fast each number describing the ellipse changes, given the extra force.
They turn a hard problem about positions into an easier problem about slowly drifting quantities.

### L2 human

The equations are the starting point of secular perturbation theory: one averages $\mathcal{R}$ over the fast mean anomalies and studies the slow evolution of the remaining elements.
In the averaged system $\partial \mathcal{R} / \partial M = 0$, so the semi-major axis is constant to first order, which is the Laplace–Lagrange result behind the classical stability arguments.
They are a Hamiltonian system in disguise; in Delaunay variables they take canonical form.
