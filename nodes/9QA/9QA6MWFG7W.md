---
tag: 9QA6MWFG7W
kind: definition
name: Magnetostriction
msc: [74F15]
defines: BZPZQRFJ24
uses: [8QS6QMJF5Z, KG2XWEMJ30]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetostriction
---

## Definition

Consider a sample of a magnetic material at zero applied [[stress|KG2XWEMJ30]], and let its magnetization be changed, for example by an applied magnetic field.
*Magnetostriction* is the [[strain|8QS6QMJF5Z]] of the sample caused by this change of magnetization.
The *magnetostriction* $\lambda = \Delta L / L$ along a given direction is the relative change of length in that direction, measured from the demagnetized state.
The *saturation magnetostriction* $\lambda_s$ is the value of $\lambda$ along the magnetization direction when the material is magnetized to saturation.

## Remarks

Example: consider an isotropic polycrystal magnetized to saturation.
If the magnetization makes the angle $\theta$ with the direction of measurement, the standard model gives
$$\lambda(\theta) = \frac{3}{2} \lambda_s \left( \cos^2\theta - \frac13 \right),$$
which equals $\lambda_s$ for $\theta = 0$ and $-\lambda_s/2$ for $\theta = \pi/2$.
The volume is unchanged to first order, since $\lambda(0) + 2\lambda(\pi/2) = 0$.
Non-example: thermal expansion of a magnetic material in zero field is a strain caused by a change of temperature, not of magnetization, so it is not magnetostriction.
The saturation magnetostriction can be positive (the material lengthens along the field) or negative, as for nickel.
For small changes around a bias field, the effect is often written in a linear form like piezoelectricity, $S = s^H T + d^{t} H$ and $B = d T + \mu^T H$, with a piezomagnetic coefficient tensor $d$.
