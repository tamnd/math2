---
tag: WQ3PJ4NWAG
kind: definition
name: Angular spectrum method
msc: [78A45, 42B10, 35J05]
defines: WBPGRQ6RJE
uses: [DPVM34ADZV, MNXKTXJ35G, NM024G378A, VT8YK4WC0H]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_spectrum_method
---

## Definition

Let $k = 2\pi/\lambda > 0$, and let $u$ solve the [[Helmholtz equation|MNXKTXJ35G]] $\Delta u + k^2 u = 0$ in the half-space $z > 0$, with waves travelling away from the plane $z = 0$.
The *angular spectrum* of $u$ in the plane $z = 0$ is the two-dimensional [[Fourier transform|DPVM34ADZV]]
$$A(f_x, f_y) = \iint u(x, y, 0) \, e^{-2\pi i (f_x x + f_y y)} \, dx \, dy.$$
Let $\gamma(f_x, f_y) = \sqrt{1/\lambda^2 - f_x^2 - f_y^2}$ when $f_x^2 + f_y^2 \le 1/\lambda^2$, and $\gamma(f_x, f_y) = i \sqrt{f_x^2 + f_y^2 - 1/\lambda^2}$ otherwise.
The *angular spectrum method* computes the field in the plane at height $z > 0$ by
$$u(x, y, z) = \iint A(f_x, f_y) \, e^{2\pi i \gamma(f_x, f_y) z} \, e^{2\pi i (f_x x + f_y y)} \, df_x \, df_y.$$

## Remarks

Each term $e^{2\pi i (f_x x + f_y y + \gamma z)}$ solves the Helmholtz equation, since $f_x^2 + f_y^2 + \gamma^2 = 1/\lambda^2$.
For $f_x^2 + f_y^2 < 1/\lambda^2$ it is a [[plane wave|NM024G378A]] with direction cosines $(\lambda f_x, \lambda f_y, \lambda \gamma)$; for $f_x^2 + f_y^2 > 1/\lambda^2$ it is an [[evanescent wave|VT8YK4WC0H]] that decays like $e^{-2\pi \abs{\gamma} z}$.
Example: $u(x, y, 0) = e^{2\pi i x \sin\alpha / \lambda}$ has its spectrum concentrated at $f_x = \sin\alpha/\lambda$, $f_y = 0$, and the method returns the tilted plane wave $e^{ik(x \sin\alpha + z \cos\alpha)}$.
The choice of the sign of $\gamma$ is what selects waves travelling away from the plane; the other choice gives incoming waves and growing exponentials.
Propagation is thus a Fourier multiplier with transfer function $H(f_x, f_y) = e^{2\pi i \gamma z}$; expanding $\gamma$ to second order in $f_x, f_y$ gives the Fresnel approximation.

## Explanations

### L1 human

The method turns propagation into multiplication: in Fourier space, moving the field forward by a distance $z$ multiplies each spatial frequency by a known phase or decay factor.
This makes it fast to compute with the fast Fourier transform.
