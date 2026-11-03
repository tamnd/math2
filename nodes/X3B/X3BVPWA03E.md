---
tag: X3BVPWA03E
kind: definition
name: Brewster's angle
msc: [78A40, 78A10]
defines: KBBFZ97KPK
uses: [ARTBZGVY72, 9VGK0SP6EQ, PJ8ZSJ0QDW]
sources:
  - url: https://en.wikipedia.org/wiki/Brewster%27s_angle
---

## Definition

Let a flat interface separate two lossless, isotropic, non-magnetic media with [[refractive indices|9VGK0SP6EQ]] $n_1 > 0$ (incident side) and $n_2 > 0$, with $n_1 \neq n_2$.
*Brewster's angle* is the angle of incidence $\theta_B = \arctan(n_2/n_1)$.
It is the unique angle in $(0, \pi/2)$ at which the $p$-reflection coefficient $r_p$ of the [[Fresnel equations|ARTBZGVY72]] vanishes.

## Remarks

Check: $r_p = 0$ means $n_2 \cos\theta_i = n_1 \cos\theta_t$; together with $n_1 \sin\theta_i = n_2 \sin\theta_t$ this gives $\sin\theta_i \cos\theta_i = \sin\theta_t \cos\theta_t$ with $\theta_i \neq \theta_t$, so $\theta_i + \theta_t = \pi/2$ and $\tan\theta_i = n_2/n_1$.
Example: from air ($n_1 = 1$) to glass ($n_2 = 1.5$), $\theta_B = \arctan 1.5 \approx 56.3^\circ$.
From glass to air, $\theta_B = \arctan(1/1.5) \approx 33.7^\circ$, below the critical angle $41.8^\circ$.
Non-example: for $s$-[[polarization|PJ8ZSJ0QDW]], $r_s$ never vanishes when $n_1 \neq n_2$, since $n_1 \cos\theta_i = n_2 \cos\theta_t$ and Snell's law would force $n_1 = n_2$.
So no Brewster angle exists for $s$-polarized light at a non-magnetic interface.
