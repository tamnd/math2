---
tag: 4N2KN8HTRB
kind: statement
role: fact
name: Tresca yield criterion
msc: [74C05]
uses: [CWWCEXZ8BH, M6ZWV4Y29A]
about: [CWWCEXZ8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Yield_surface
---

## Statement

Let an isotropic ductile material have yield stress $\sigma_y > 0$ in uniaxial tension.
Let $\sigma_1, \sigma_2, \sigma_3$ be the [[principal stresses|M6ZWV4Y29A]] at a point.
The Tresca criterion states that the material begins to yield at the point when the maximum shear stress reaches $\sigma_y / 2$:
$$\max\left(\abs{\sigma_1 - \sigma_2}, \abs{\sigma_2 - \sigma_3}, \abs{\sigma_3 - \sigma_1}\right) = \sigma_y.$$

## Remarks

The criterion is a constitutive assumption, the maximum shear stress hypothesis, not a theorem.
The maximum shear stress at a point is half the largest difference of principal stresses, which explains the factor $2$.
Its [[yield surface|CWWCEXZ8BH]] in principal stress space is an infinite regular hexagonal prism about the line $\sigma_1 = \sigma_2 = \sigma_3$, so hydrostatic pressure has no effect.
Check in uniaxial tension, $\sigma_1 = \sigma$, $\sigma_2 = \sigma_3 = 0$: the maximum is $\abs{\sigma}$, so yielding starts at $\sigma = \sigma_y$.
In pure shear, $\sigma_1 = \tau$, $\sigma_2 = 0$, $\sigma_3 = -\tau$: the maximum is $2\abs{\tau}$, so the shear yield stress is $\sigma_y / 2$, smaller than the value $\sigma_y/\sqrt{3}$ of the von Mises criterion.
When the two are matched in uniaxial tension, the Tresca hexagon is inscribed in the von Mises circle.

## Explanations

### L1 human

The Tresca rule says that a metal starts to flow when the largest shear stress inside it reaches a fixed limit.
Shear is the stress that makes layers of atoms slide over each other, which is how metals deform permanently.

### L2 human

The Tresca criterion is piecewise linear in the principal stresses.
So it often gives simple closed-form answers in limit analysis and in hand calculations, for example for thick tubes.
Its corners make the flow rule non-unique there, which is a nuisance in numerical work.
It is the special case of the Mohr–Coulomb criterion with zero friction angle.
