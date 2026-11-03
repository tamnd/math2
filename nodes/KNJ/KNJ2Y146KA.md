---
tag: KNJ2Y146KA
kind: statement
role: fact
name: Sachs–Wolfe effect
msc: [83F05, 85A40]
uses: [XMH5RQCJYT, ECJMS4VDTF]
about: [XMH5RQCJYT]
sources:
  - url: https://en.wikipedia.org/wiki/Sachs%E2%80%93Wolfe_effect
same_as:
  wikidata: Q1617362
  wikipedia: Sachs–Wolfe effect
---

## Statement

Consider a spatially flat [[Friedmann–Lemaître–Robertson–Walker|ECJMS4VDTF]] universe.
Take scalar [[cosmological perturbations|XMH5RQCJYT]] in the Newtonian gauge,
$$ds^2 = a(\eta)^2 \left[ -(1 + 2\Psi)\, d\eta^2 + (1 - 2\Phi)\, \delta_{ij}\, dx^i dx^j \right],$$
where $\eta$ is conformal time and $\Psi, \Phi$ are small functions of $(\eta, x)$.
Assume that the photons decouple instantaneously at conformal time $\eta_*$ and then travel freely to the observer at time $\eta_0$.
Neglect the Doppler term from the velocity of the emitting matter.
Let $\Theta_0 = \delta T / T$ be the fractional temperature perturbation of the photons at the emission point.
Drop the terms at the observer, which only add a monopole and a dipole.
Then the fractional temperature perturbation seen in the direction $\hat n$ is, to first order,
$$\frac{\delta T}{T}(\hat n) = \left[ \Theta_0 + \Psi \right](\eta_*, x_*) + \int_{\eta_*}^{\eta_0} \left( \partial_\eta \Psi + \partial_\eta \Phi \right)(\eta, x(\eta))\, d\eta,$$
where $x(\eta) = (\eta_0 - \eta)\, \hat n$ is the photon path and $x_* = x(\eta_*)$.
For adiabatic perturbations on scales larger than the horizon at decoupling, in a matter-dominated era, $\Theta_0 = -\tfrac{2}{3} \Psi$, so the first term becomes $\tfrac{1}{3} \Psi(\eta_*, x_*)$.

## Remarks

The formula comes from the geodesic equation for photons in the perturbed metric.
The photon energy changes when it climbs out of the potential $\Psi$ and when the potentials change in time along its path.
The first term is the ordinary Sachs–Wolfe effect, and the integral is the integrated Sachs–Wolfe effect.
In an overdense region $\Psi < 0$, so the photon loses more energy climbing out of the well than it had gained in intrinsic temperature, and the region appears colder by $\abs{\Psi}/3$.
In a matter-dominated universe with no anisotropic stress, $\Phi = \Psi$ is constant in time on linear scales, so the integrated term vanishes.
It becomes nonzero when radiation is still important just after decoupling, and at late times when a cosmological constant or spatial curvature makes the potentials decay.
The effect dominates the temperature anisotropy of the cosmic microwave background at large angular scales.

## Explanations

### L1 human

Light from the early universe has to climb out of the gravitational wells and hills made by clumps of matter.
Light that climbs out of a well loses energy and looks a little colder; light coming from a hill looks a little warmer.
The Sachs–Wolfe effect is this link between the gravity of early clumps and small temperature differences across the sky.
It lets astronomers read the largest early clumps of matter from a map of the cosmic microwave background.

### L2 human

In linear [[cosmological perturbation theory|XMH5RQCJYT]] the observed temperature anisotropy is a sum of a few terms along each line of sight.
The Sachs–Wolfe terms are the gravitational ones: the potential at last scattering and the time change of the potentials afterwards.
On large angular scales they give a nearly flat angular power spectrum $\ell(\ell + 1) C_\ell$ for a nearly scale-invariant spectrum of initial perturbations.
The late integrated term correlates with the large-scale distribution of galaxies, and this correlation is a test for dark energy.
Sign conventions for $\Phi$ and $\Psi$ differ between textbooks, so the formula must be read together with the metric above.
