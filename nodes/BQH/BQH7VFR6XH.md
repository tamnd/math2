---
tag: BQH7VFR6XH
kind: definition
name: Paraxial approximation
msc: [78A05]
defines: N111BHFQ2H
uses: [QDV9SBK6W0, 0225QPWRRE]
sources:
  - url: https://en.wikipedia.org/wiki/Paraxial_approximation
---

## Definition

Let an optical system have an optical axis.
Describe a ray at a plane perpendicular to the axis by its height $y$ above the axis and its angle $\theta$ with the axis.
The *paraxial approximation* keeps only the terms of first order in $y$ and $\theta$ in the laws of ray propagation.
In particular it uses
$$\sin\theta \approx \theta, \qquad \tan\theta \approx \theta, \qquad \cos\theta \approx 1.$$
A ray is called *paraxial* when these replacements are accurate.
This means that $\abs{\theta} \ll 1$ and that $y$ is small compared with the radii of curvature and the apertures.

## Remarks

The replacements are the first terms of the [[Taylor series|0225QPWRRE]]: $\sin\theta = \theta - \theta^3/6 + \cdots$, $\tan\theta = \theta + \theta^3/3 + \cdots$, $\cos\theta = 1 - \theta^2/2 + \cdots$.
Under the approximation, [[Snell's law|QDV9SBK6W0]] becomes $n_1 \theta_1 = n_2 \theta_2$.
The third-order terms give the Seidel aberrations.

Example: $\theta = 0.1$ rad.
Check: $\sin 0.1 \approx 0.09983$, so the relative error of $\sin\theta \approx \theta$ is about $0.17\%$.

Non-example: $\theta = 1$ rad, about $57^\circ$.
Here $\sin 1 \approx 0.841$, so replacing it by $1$ gives an error near $19\%$, and $\tan 1 \approx 1.557$; the ray is not paraxial.
