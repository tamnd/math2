---
tag: YEKN6DDY6W
kind: definition
name: Earth tide
msc: [86A30, 70F15, 86A04]
defines: JFX02GA88H
uses: [2E2KCFNMHE, C8HCN8NEQP, 3F32Y21HP4]
sources:
  - url: https://en.wikipedia.org/wiki/Earth_tide
---

## Definition

Model the Earth as a spherically symmetric, non-rotating, elastic body of radius $a$ with surface gravity $g$.
Let $W = \sum_{n \ge 2} W_n$ be the [[tide-generating potential|2E2KCFNMHE]] of the Moon and the Sun at the surface, split into terms $W_n$ of degree $n$ in [[spherical harmonics|3F32Y21HP4]].
The *Earth tide* is the displacement field $u$ of the solid Earth produced by $W$.
Let $\theta$ be the colatitude and $\varphi$ the longitude.
At the surface the Earth tide is
$$u_r = \sum_n \frac{h_n}{g} W_n, \qquad u_\theta = \sum_n \frac{l_n}{g} \frac{\partial W_n}{\partial \theta}, \qquad u_\varphi = \sum_n \frac{l_n}{g \sin\theta} \frac{\partial W_n}{\partial \varphi},$$
and the deformation adds the potential $\sum_n k_n W_n$ to the external gravity field.
The dimensionless constants $h_n$, $l_n$ and $k_n$ are the [[Love numbers|C8HCN8NEQP]] of degree $n$.

## Remarks

The degree $2$ terms dominate, with $h_2 \approx 0.6$, $k_2 \approx 0.3$ and $l_2 \approx 0.08$ for the real Earth.
Example: a gravimeter at a fixed point measures the tidal change of gravity multiplied by the gravimetric factor $\delta_2 = 1 + h_2 - \tfrac32 k_2 \approx 1.16$.
Here $h_2$ comes from the lift of the station, which moves it away from the centre, and $k_2$ from the attraction of the redistributed mass.
The tilt of the ground relative to the vertical is reduced by the diminishing factor $\gamma_2 = 1 + k_2 - h_2 \approx 0.7$.
Non-example: the ocean tide is the motion of the sea surface relative to the sea floor, not the deformation of the solid Earth.
The weight of the moving ocean water deforms the ground too; this load tide is usually treated separately from the body tide.
For a perfectly rigid Earth all Love numbers vanish and there is no Earth tide.
