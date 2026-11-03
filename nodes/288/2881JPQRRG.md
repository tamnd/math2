---
tag: 2881JPQRRG
kind: definition
name: Prandtl–Meyer function
msc: [76J20, 76N15]
defines: 88XSF5YV97
uses: [GFHJ858AN1, G4EN6Y0ZZ2, C5QBSMGHCR, SH8FHGTMSE]
sources:
  - url: https://en.wikipedia.org/wiki/Prandtl%E2%80%93Meyer_function
---

## Definition

Let $\gamma > 1$ be the ratio of specific heats of an ideal gas.
The *Prandtl–Meyer function* is the function $\nu \colon [1, \infty) \to \R$ of the [[Mach number|GFHJ858AN1]] $M$ given by
$$\nu(M) = \sqrt{\frac{\gamma + 1}{\gamma - 1}}\, \arctan\sqrt{\frac{\gamma - 1}{\gamma + 1}\,(M^2 - 1)} - \arctan\sqrt{M^2 - 1}.$$
It is the solution of $d\nu = \frac{\sqrt{M^2 - 1}}{1 + \frac{\gamma - 1}{2}M^2}\, \frac{dM}{M}$ with $\nu(1) = 0$.

## Remarks

Consider a plane, steady, [[isentropic|SH8FHGTMSE]] [[supersonic flow|G4EN6Y0ZZ2]] turned through a small angle $d\theta$ across a [[Mach wave|C5QBSMGHCR]].
In an expansion its Mach number changes so that $d\nu = d\theta$, and this is where the function comes from.
Example: for $\gamma = 1.4$ and $M = 2$, one has $\sqrt{6}\arctan\sqrt{1/2} - \arctan\sqrt{3} \approx 2.449 \cdot 35.26^\circ - 60^\circ \approx 26.38^\circ$.
The function is strictly increasing, and $\nu(M) \to \nu_{\max} = \frac{\pi}{2}\left(\sqrt{\frac{\gamma + 1}{\gamma - 1}} - 1\right)$ as $M \to \infty$, which is about $130.45^\circ$ for $\gamma = 1.4$.
Non-example: for $M < 1$ the expression is not defined over the reals, since $\sqrt{M^2 - 1}$ is imaginary; subsonic flows do not turn by simple waves.
