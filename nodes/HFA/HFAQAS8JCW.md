---
tag: HFAQAS8JCW
kind: definition
name: Weyl–Lewis–Papapetrou coordinates
msc: [83C15, 83C20]
defines: ASWJNB3804
uses: [BY4QYYS788, 5AKNNW3W4Z, JRV1T69FYJ]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl–Lewis–Papapetrou_coordinates
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] with two commuting [[Killing vector fields|5AKNNW3W4Z]] $\xi$ and $\eta$.
Assume $\xi$ is timelike in some region and $\eta$ generates an action of the circle group.
*Weyl–Lewis–Papapetrou coordinates* are coordinates $(t, \phi, \rho, z)$ with $\xi = \partial_t$, $\eta = \partial_\phi$, $\rho > 0$, in which
$$g = -f\left(dt - \omega\, d\phi\right)^2 + f^{-1}\left(e^{2\gamma}\left(d\rho^2 + dz^2\right) + \rho^2 d\phi^2\right),$$
where $f > 0$, $\omega$ and $\gamma$ are smooth functions of $(\rho, z)$ only.

## Remarks

In these coordinates the Gram matrix of the Killing fields has determinant
$$g_{tt} g_{\phi\phi} - g_{t\phi}^2 = (-f)\left(-f\omega^2 + \frac{\rho^2}{f}\right) - f^2\omega^2 = -\rho^2.$$
So $\rho$ is fixed by the geometry: $\rho^2 = -\left(g(\xi,\xi) g(\eta,\eta) - g(\xi,\eta)^2\right)$.

Existence: let $(M, g)$ be a [[vacuum solution|JRV1T69FYJ]], and assume that $\eta$ vanishes somewhere, on a rotation axis.
Then the planes orthogonal to $\xi$ and $\eta$ are integrable, and the function $\rho$ just defined is harmonic on the two-dimensional orbit space.
Where $d\rho \ne 0$ one can take $\rho$ and a harmonic conjugate $z$ as coordinates.
This gives the form above.

Example: Minkowski space in cylindrical coordinates, $g = -dt^2 + d\rho^2 + dz^2 + \rho^2 d\phi^2$, has this form with $f = 1$, $\omega = 0$, $\gamma = 0$.

Non-example: the usual coordinates $(t, r, \theta, \phi)$ of the [[Schwarzschild metric|6Y50T68WKY]] are not of this form with $\rho = r\sin\theta$.
Indeed $-g_{tt} g_{\phi\phi} = (1 - 2m/r) r^2\sin^2\theta$, so the Weyl coordinate is $\rho = \sqrt{r^2 - 2mr}\,\sin\theta$, with $z = (r - m)\cos\theta$.

If $\omega = 0$ the spacetime is static and these are *Weyl coordinates*.
For vacuum with $\omega = 0$, write $f = e^{2U}$.
Then the Einstein equations say that $U$ is an axisymmetric harmonic function on flat $\R^3$ with cylindrical coordinates $(\rho, z, \phi)$.
The function $\gamma$ is then found by a line integral.
