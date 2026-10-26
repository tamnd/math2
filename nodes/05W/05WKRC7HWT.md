---
tag: 05WKRC7HWT
kind: statement
role: proposition
name: Jacobian of spherical coordinates
aliases: [spherical-volume-element]
msc: [26B15]
uses: [0RW8KPMXF6, 03W6Q1MFR5, 00N5FHP1CV]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_integral
    locator: Spherical coordinates
  - url: https://en.wikipedia.org/wiki/Spherical_coordinate_system
    locator: Integration and differentiation in spherical coordinates
---

## Statement

Let $S(\rho, \varphi, \theta) = (\rho \sin \varphi \cos \theta, \ \rho \sin \varphi \sin \theta, \ \rho \cos \varphi)$ be the [[spherical coordinate map|0RW8KPMXF6]].
Its [[Jacobian determinant|03W6Q1MFR5]] is
$$\det DS(\rho, \varphi, \theta) = \rho^2 \sin \varphi.$$
Hence, for a continuous function $f$ on a region $E \subseteq \mathbb{R}^3$ described by a region $E'$ of $(\rho, \varphi, \theta)$ with $\rho \ge 0$, $0 \le \varphi \le \pi$, $0 \le \theta \le 2\pi$,
$$\iiint_E f \, dV = \iiint_{E'} f(S(\rho, \varphi, \theta)) \, \rho^2 \sin \varphi \, d\rho \, d\varphi \, d\theta.$$

## Remarks

The Jacobian matrix has rows $(\sin \varphi \cos \theta, \ \rho \cos \varphi \cos \theta, \ -\rho \sin \varphi \sin \theta)$, $(\sin \varphi \sin \theta, \ \rho \cos \varphi \sin \theta, \ \rho \sin \varphi \cos \theta)$ and $(\cos \varphi, \ -\rho \sin \varphi, \ 0)$. Expansion along the last row gives $\rho^2 \sin \varphi$.
The integral formula follows from the [[change of variables theorem|00N5FHP1CV]]. The set where $S$ is not injective, or where the determinant vanishes, has volume zero.
Since $0 \le \varphi \le \pi$, the factor $\rho^2 \sin \varphi$ is non-negative, so no absolute value is needed.
Example: the volume of the ball of radius $a$ is $\int_0^{2\pi} \int_0^\pi \int_0^a \rho^2 \sin \varphi \, d\rho \, d\varphi \, d\theta = \tfrac{4}{3} \pi a^3$.

## Explanations

### L1 human

A small spherical box has sides $d\rho$, $\rho \, d\varphi$ and $\rho \sin \varphi \, d\theta$.
Its volume is about $\rho^2 \sin \varphi \, d\rho \, d\varphi \, d\theta$, and this factor appears in integrals in spherical coordinates.
