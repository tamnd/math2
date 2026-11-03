---
tag: 5JVHKVT19J
kind: definition
name: Mohr–Coulomb theory
msc: [74C05, 74L10]
defines: Q5CF1Z6179
uses: [CWWCEXZ8BH, M6ZWV4Y29A, DED41X44XM]
sources:
  - url: https://en.wikipedia.org/wiki/Mohr–Coulomb_theory
---

## Definition

Let $c \ge 0$ (the cohesion) and $\phi \in [0, \pi/2)$ (the angle of internal friction) be material constants.
Take tensile stresses as positive.
For a plane through a point, let $\sigma_n$ be the normal stress and $\tau$ the shear stress on it.
The *Mohr–Coulomb criterion* states that the material fails at the point when some plane satisfies
$$\abs{\tau} = c - \sigma_n \tan \phi,$$
while no plane has $\abs{\tau} > c - \sigma_n \tan \phi$.
In terms of the [[principal stresses|M6ZWV4Y29A]] $\sigma_1 \ge \sigma_2 \ge \sigma_3$ this is
$$\frac{\sigma_1 - \sigma_3}{2} = c \cos \phi - \frac{\sigma_1 + \sigma_3}{2} \sin \phi.$$

## Remarks

The stresses on all planes lie in the largest [[Mohr's circle|DED41X44XM]], with centre $(\sigma_1 + \sigma_3)/2$ and radius $(\sigma_1 - \sigma_3)/2$.
This circle touches the line $\abs{\tau} = c - \sigma_n \tan \phi$ exactly when its radius equals the distance from its centre to the line.
This is why the two forms agree.
Example: in uniaxial compression, $\sigma_1 = \sigma_2 = 0$ and $\sigma_3 = -q$, the criterion gives the compressive strength $q = 2c \cos\phi / (1 - \sin \phi)$; in uniaxial tension the strength is $2c\cos\phi/(1 + \sin\phi)$, which is smaller when $\phi > 0$.
With $\phi = 0$ it reduces to the [[Tresca criterion|4N2KN8HTRB]] with $c = \sigma_y / 2$.
Non-example: a hydrostatic compression $\sigma_1 = \sigma_2 = \sigma_3 = -p$ with $p > 0$ never meets the criterion when $c > 0$.
The left side is $0$, and the right side is $c\cos\phi + p \sin\phi > 0$.
The [[yield surface|CWWCEXZ8BH]] in principal stress space is an irregular hexagonal pyramid with axis the line $\sigma_1 = \sigma_2 = \sigma_3$, and the intermediate stress $\sigma_2$ plays no role.

## Explanations

### L1 human

A plane in the material slips when its shear stress reaches the cohesion plus friction times the pressure across it.
Equivalently, the largest Mohr circle touches a fixed straight line.
