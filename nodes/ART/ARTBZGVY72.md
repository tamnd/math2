---
tag: ARTBZGVY72
kind: statement
role: theorem
name: Fresnel equations
msc: [78A40, 78A25]
uses: [NM024G378A, 9VGK0SP6EQ, QDV9SBK6W0, EZG8N3H7QN, PJ8ZSJ0QDW]
about: [NM024G378A, 9VGK0SP6EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Fresnel_equations
same_as:
  wikidata: Q838055
  wikipedia: Fresnel equations
---

## Statement

Let the plane $z = 0$ separate two linear, isotropic, non-magnetic media with real [[refractive indices|9VGK0SP6EQ]] $n_1$ (for $z < 0$) and $n_2$ (for $z > 0$).
Let a monochromatic [[plane wave|NM024G378A]] in medium $1$ hit the plane at angle of incidence $\theta_i$, measured from the normal.
Let $\theta_t$ be the angle of refraction given by [[Snell's law|QDV9SBK6W0]] $n_1 \sin \theta_i = n_2 \sin \theta_t$, and assume $n_1 \sin \theta_i < n_2$.
Write $r$ and $t$ for the ratios of the complex amplitudes of the reflected and transmitted electric fields to that of the incident electric field.
For $s$-[[polarization|PJ8ZSJ0QDW]] (electric field perpendicular to the plane of incidence),
$$r_s = \frac{n_1 \cos\theta_i - n_2 \cos\theta_t}{n_1 \cos\theta_i + n_2 \cos\theta_t}, \qquad t_s = \frac{2 n_1 \cos\theta_i}{n_1 \cos\theta_i + n_2 \cos\theta_t}.$$
For $p$-polarization (electric field in the plane of incidence),
$$r_p = \frac{n_2 \cos\theta_i - n_1 \cos\theta_t}{n_2 \cos\theta_i + n_1 \cos\theta_t}, \qquad t_p = \frac{2 n_1 \cos\theta_i}{n_2 \cos\theta_i + n_1 \cos\theta_t}.$$
The reflectance $R = \abs{r}^2$ and the transmittance $T = \dfrac{n_2 \cos\theta_t}{n_1 \cos\theta_i} \abs{t}^2$ satisfy $R + T = 1$ for each polarization.

## Remarks

The proof writes the incident, reflected and transmitted fields as plane waves and imposes the [[interface conditions|EZG8N3H7QN]]: the tangential components of $\mathbf{E}$ and $\mathbf{H}$ are continuous across $z = 0$.
Equality of the phases along the plane gives the law of reflection and Snell's law, and the two continuity equations for each polarization give the amplitude ratios.
The sign of $r_p$ depends on the orientation chosen for the $p$ field vectors, and some books use the opposite sign.
At normal incidence both polarizations give $R = \left( \dfrac{n_1 - n_2}{n_1 + n_2} \right)^2$; for air ($n_1 = 1$) and glass ($n_2 = 1.5$) this is $0.04$, so a glass surface reflects $4\%$ of the light.
If $n_1 \sin\theta_i > n_2$, no real $\theta_t$ exists; the same formulas with a complex $\cos\theta_t$ give $\abs{r_s} = \abs{r_p} = 1$, which is [[total internal reflection|GS6CP71X4K]].
The zero of $r_p$ is [[Brewster's angle|KBBFZ97KPK]].

## Explanations

### L1 human

When light hits a glass window, part of it bounces back and part goes through.
The Fresnel equations say exactly how much of each, depending on the angle and on how the light is polarized.
At grazing angles almost all light is reflected, which is why a lake mirrors the far shore.

### L2 human

The equations are the boundary value problem for Maxwell's equations at a flat interface, solved for plane waves.
They are the building block of thin-film optics, where a stack of layers is treated by multiplying interface and propagation matrices.
They contain Snell's law, Brewster's angle, total internal reflection and the evanescent wave as special cases.
For absorbing media one replaces $n_2$ by a complex index, and the same formulas hold with complex angles.
