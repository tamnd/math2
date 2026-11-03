---
tag: QZ6EPBTEHT
kind: problem
name: Gravity inversion
msc: [86A22, 86A20, 31B20]
uses: [DCMFQ01QGS, J6V1B7SP0Q, W09B9NZ9B5]
about: [C54MFNX576, PCMW7KN5P4]
sources:
  - url: https://en.wikipedia.org/wiki/Gravity_anomaly
history:
  posed_by: "George Gabriel Stokes"
  first_stated: "1867"
---

## Problem

Let $D \subset \R^3$ be a bounded domain, and let $G > 0$ be the gravitational constant.
For a bounded integrable density $\rho \colon D \to \R$, let
$$V_\rho(x) = G \int_D \frac{\rho(y)}{\abs{x - y}} \, dy$$
be its [[Newtonian potential|DCMFQ01QGS]].
The *gravity inversion problem* asks: given the gravity field $\nabla V_\rho$ on a surface or region outside $\overline{D}$, find the density $\rho$.
In practice the data are a [[gravity anomaly|J6V1B7SP0Q]] measured at finitely many points, with errors.

## Remarks

The problem has no unique solution.
If $\varphi$ is a smooth function with compact support in $D$ and $\rho = -\Delta \varphi / (4 \pi G)$, then $V_\rho = \varphi$, so $V_\rho = 0$ outside $D$.
Adding such a $\rho$ to any density does not change the exterior field.
For example, a homogeneous ball and a uniform thin shell with the same centre and the same total mass give the same field outside the ball.
Stokes noted in 1867 that a given exterior potential is produced by many different interior mass distributions.
The problem is also unstable, so it is not a [[well-posed problem|W09B9NZ9B5]].
The exterior field smooths out the fine detail of $\rho$, so small changes in the data can come from large changes in $\rho$.
Uniqueness holds in restricted classes.
P. S. Novikov proved such a result in 1938 for bodies of one constant density.
Two such bodies that are star-shaped with respect to a common point and have the same exterior potential are equal.
In applied work, gravity inversion is solved as a [[geophysical inversion|C54MFNX576]] with regularisation and prior information, such as bounds on the density or a given depth range.

## Explanations

### L1 human

Gravity is slightly stronger above heavy rock and slightly weaker above light rock.
Gravity inversion tries to work back from these small changes, measured at the surface, to a picture of the rock below.
The difficulty is that many different pictures give exactly the same measurements.
For example, a big light ball and a small heavy ball with the same centre and the same total mass give exactly the same measurements outside.
So one must add extra knowledge, such as the likely rock densities, to choose one answer.
