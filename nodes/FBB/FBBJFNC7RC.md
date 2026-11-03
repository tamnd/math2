---
tag: FBBJFNC7RC
kind: statement
role: theorem
name: Magnetorotational instability
msc: ["76E25", 85A30, 76W05]
uses: [T8JWCBK9M6, 8CQDTE19FW, R5P8M6SBG7, GK34V4WF2V, E5GR4K48B5]
about: [T8JWCBK9M6, 6ADKW56QGV]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetorotational_instability
same_as:
  wikidata: Q381093
  wikipedia: Magnetorotational instability
---

## Statement

Consider an incompressible, perfectly conducting fluid in ideal [[magnetohydrodynamics|T8JWCBK9M6]], rotating about the $z$-axis with angular velocity $\Omega(R)$ that depends only on the cylindrical radius $R$.
Let a uniform weak magnetic field $B \hat z$ thread the fluid, with [[Alfvén speed|8CQDTE19FW]] $v_A = B/\sqrt{\mu_0 \rho}$, where $\rho$ is the density and $\mu_0$ the vacuum permeability.
Let $\kappa^2 = 4\Omega^2 + d\Omega^2/d\ln R$ be the square of the [[epicyclic frequency|GK34V4WF2V]].
Assume $\kappa^2 \ge 0$, so that without a field the flow is stable by the Rayleigh criterion.
Consider local axisymmetric perturbations proportional to $e^{i(k z - \omega t)}$ with $k$ real.
Then the [[dispersion relation|R5P8M6SBG7]] is
$$\left(\omega^2 - k^2 v_A^2\right)^2 - \kappa^2 \left(\omega^2 - k^2 v_A^2\right) - 4\Omega^2 k^2 v_A^2 = 0.$$
It has a root with $\omega^2 < 0$, an exponentially growing mode, if and only if
$$0 < k^2 v_A^2 < -\frac{d\Omega^2}{d \ln R}.$$
So unstable modes exist for some $k$ exactly when $d\Omega^2/dR < 0$, that is, when the angular velocity decreases outward.
The largest growth rate is $\frac{1}{2} \abs{d\Omega/d\ln R}$.

## Remarks

The relation is a quadratic equation in $\omega^2$ with real roots, since its discriminant is $\kappa^4 + 16 \Omega^2 k^2 v_A^2 \ge 0$.
Its two roots have sum $2 k^2 v_A^2 + \kappa^2 \ge 0$ and product $k^2 v_A^2 (k^2 v_A^2 + d\Omega^2/d\ln R)$, so one root is negative exactly when this product is negative.
Physically, the field acts like a spring between two fluid elements at different radii.
The inner element is pulled back, loses angular momentum and sinks further in, while the outer element gains angular momentum and moves out.

For a Keplerian disk, $\Omega \propto R^{-3/2}$, so $d\ln\Omega/d\ln R = -3/2$ and the largest growth rate is $\frac{3}{4}\Omega$.
The instability therefore acts in every weakly magnetized [[accretion disk|6ADKW56QGV]] and is believed to drive the turbulence that transports angular momentum.

Without the field the Rayleigh criterion applies: the flow is stable to axisymmetric perturbations when $\kappa^2 > 0$, and a Keplerian disk is stable.
The limit $B \to 0$ is singular, because the band of unstable $k$ only moves to larger wavenumbers as $v_A \to 0$.
In a real fluid, resistivity and viscosity damp these short waves, so the field must not be too weak.

## Explanations

### L1 human

A disk of gas whose inner parts spin faster than its outer parts looks stable without a magnetic field.
A weak magnetic field changes this completely: it ties neighbouring bits of gas together like springs, and the spring makes them drift apart even faster.
The disk then becomes turbulent.
This explains how gas in disks around stars and black holes can lose angular momentum and fall inward.

### L2 human

The result is a local linear stability analysis in the spirit of the Rayleigh criterion for rotating flows.
Compared with Rayleigh, the stability condition changes from "specific angular momentum increases outward" to "angular velocity increases outward".
Its growth rate is of the order of the orbital frequency, so it is fast on astrophysical scales.
It gives a physical basis to the turbulent viscosity in the [[Shakura–Sunyaev alpha disk model|E5GR4K48B5]], and numerical simulations of its nonlinear stage are used to estimate $\alpha$.
