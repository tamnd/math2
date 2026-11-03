---
tag: CV9R40QRHH
kind: definition
name: Total internal reflection
msc: [78A40, 78A05]
defines: GS6CP71X4K
uses: [9VGK0SP6EQ, QDV9SBK6W0, ARTBZGVY72]
sources:
  - url: https://en.wikipedia.org/wiki/Total_internal_reflection
---

## Definition

Let a flat interface separate two lossless, isotropic media with real [[refractive indices|9VGK0SP6EQ]] $n_1 > n_2 > 0$.
Let a plane wave in medium $1$ hit the interface at angle of incidence $\theta_i \in [0, \pi/2)$.
The *critical angle* is
$$\theta_c = \arcsin\frac{n_2}{n_1}.$$
*Total internal reflection* is the situation $\theta_c < \theta_i < \pi/2$.
In this situation [[Snell's law|QDV9SBK6W0]] $n_1 \sin\theta_i = n_2 \sin\theta_t$ has no real solution $\theta_t$, and the reflection coefficients of the [[Fresnel equations|ARTBZGVY72]] satisfy $\abs{r_s} = \abs{r_p} = 1$.

## Remarks

Check: for $\theta_i > \theta_c$ one has $\sin\theta_i > n_2/n_1$, so the required $\sin\theta_t = (n_1/n_2)\sin\theta_i$ exceeds $1$.
Then $\cos\theta_t = i\sqrt{(n_1/n_2)^2 \sin^2\theta_i - 1}$ is purely imaginary, and $r_s$, $r_p$ become quotients of a complex number by its conjugate, of modulus $1$.
Example: glass with $n_1 = 1.5$ against air with $n_2 = 1$ has $\theta_c = \arcsin(2/3) \approx 41.8^\circ$, so a ray at $45^\circ$ inside a right-angle prism is totally reflected.
Non-example: light going from air into glass ($n_1 < n_2$) is never totally reflected, since $\arcsin(n_2/n_1)$ is not defined and a refracted ray exists for every angle.
The reflected wave acquires a phase shift that differs for $s$ and $p$ polarization, and the field beyond the interface is an [[evanescent field|VT8YK4WC0H]].
