---
tag: VB6EHHPCPA
kind: example
name: Spherical pendulum
msc: [70H06, 70F20, 37N05]
instance_of: [N0N7CMRCMH]
uses: [0EDKGA2FAK, 0262JP0NV9, 0SHPXM2HWH]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_pendulum
same_as:
  wikidata: Q3299367
  wikipedia: Spherical pendulum
---

## Example

Let $g > 0$ be the acceleration of gravity, and let $\ell > 0$ and $m > 0$.
A point mass $m$ moves without friction on the sphere of radius $\ell$ centred at a fixed pivot, under a constant downward gravity.
Let $\theta \in [0, \pi]$ be the angle from the downward vertical and let $\varphi$ be the azimuth angle around the vertical axis.
The Lagrangian is
$$L = \frac{m \ell^2}{2} \left( \theta'^2 + \sin^2 \theta \, \varphi'^2 \right) + m g \ell \cos \theta.$$
The system has two degrees of freedom and two independent [[first integrals|0262JP0NV9]]:

1. the energy $E = \frac{m \ell^2}{2} \left( \theta'^2 + \sin^2 \theta \, \varphi'^2 \right) - m g \ell \cos \theta$;
2. the vertical component of the angular momentum $L_z = m \ell^2 \sin^2 \theta \, \varphi'$.

Check for $L_z$: the coordinate $\varphi$ does not appear in $L$, so the Euler–Lagrange equation for $\varphi$ reads $\frac{d}{dt} \frac{\partial L}{\partial \varphi'} = 0$, and $\partial L / \partial \varphi' = L_z$.
So the spherical pendulum is a [[Hamiltonian system|0EDKGA2FAK]] with two degrees of freedom and two independent first integrals in involution.
It is an [[integrable system|N0N7CMRCMH]].

## Remarks

Fixing the value of $L_z$ leaves a one-dimensional motion in $\theta$ with the effective potential $\frac{L_z^2}{2 m \ell^2 \sin^2 \theta} - m g \ell \cos \theta$.
So $\theta$ oscillates between two values, and the solutions are given by elliptic functions.
When $L_z = 0$ the motion stays in a vertical plane and is the planar pendulum, described by the [[pendulum equation|0SHPXM2HWH]].
For each $\theta_0 \in (0, \pi/2)$ there is a conical motion with $\theta = \theta_0$ and $\varphi'^2 = g / (\ell \cos \theta_0)$.

## Explanations

### L1 human

A spherical pendulum is a weight on a rod that may swing in every direction, not only back and forth in a plane.
Seen from above, the weight usually traces a rosette: it moves around the pivot while its height goes up and down.
If it is pushed sideways just right, it runs around a horizontal circle at constant height, like a conical pendulum.
