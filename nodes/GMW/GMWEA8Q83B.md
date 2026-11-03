---
tag: GMWEA8Q83B
kind: statement
role: proposition
name: Parker solar wind model
msc: [85A30, 76N15, 35Q85]
uses: [RW0JK9VDZE, SN4J6KP03C, 29WRN5J730, 0YTCMFB4HC]
about: [RW0JK9VDZE]
sources:
  - url: https://en.wikipedia.org/wiki/Solar_wind
---

## Statement

Let a star of mass $M$ be surrounded by a steady, spherically symmetric, isothermal flow of gas, described by the [[Euler equations|RW0JK9VDZE]] with [[Newtonian gravity|29WRN5J730]].
Let $c_s > 0$ be the constant isothermal [[speed of sound|SN4J6KP03C]] and $G$ the gravitational constant.
Let $v(r)$ be the radial velocity and $\rho(r)$ the density at distance $r$ from the centre.
Mass conservation $\rho v r^2 = \text{const}$ and the momentum equation $v \, v' = -c_s^2 \rho'/\rho - GM/r^2$ give
$$\left( v - \frac{c_s^2}{v} \right) \frac{dv}{dr} = \frac{2 c_s^2}{r} - \frac{GM}{r^2}.$$
Let $r_c = GM/(2 c_s^2)$ be the critical radius.
Then every solution with $v > 0$ satisfies, for some constant $C$,
$$\frac{v^2}{c_s^2} - \ln \frac{v^2}{c_s^2} = 4 \ln \frac{r}{r_c} + \frac{4 r_c}{r} + C.$$
Exactly two solutions pass through the [[critical point|0YTCMFB4HC]] $(r, v) = (r_c, c_s)$, both with $C = -3$.
One of them, the *Parker wind*, increases with $r$: it is subsonic for $r < r_c$, supersonic for $r > r_c$, and $v(r) \sim 2 c_s \sqrt{\ln(r/r_c)}$ as $r \to \infty$.

## Remarks

Dividing the momentum equation by $v$ and using $\rho'/\rho = -v'/v - 2/r$ gives the first equation; separating variables and integrating gives the second.
At $r = r_c$ the right-hand side vanishes, and a smooth solution can change from subsonic to supersonic flow only there, where the factor $v - c_s^2/v$ also vanishes.
Inserting $r = r_c$ and $v = c_s$ gives $1 - 0 = 0 + 4 + C$, so $C = -3$.
The other transonic solution decreases with $r$ and describes spherical accretion onto the star.

For the solar corona, with a temperature of about $10^6$ kelvin, $r_c$ is a few solar radii.
The model then predicts a supersonic wind of some hundreds of kilometres per second near the Earth.
Parker argued that a static isothermal atmosphere would keep a finite pressure at infinity, far above the pressure of the interstellar medium.
So the corona cannot be static and must expand.
In the wind solution, $\rho = \text{const}/(v r^2)$ tends to $0$, so the pressure tends to $0$ at infinity.

## Explanations

### L1 human

The outer atmosphere of the Sun is so hot that gravity cannot hold it.
Parker showed that it must flow away as a wind that starts slowly, passes the speed of sound a few solar radii out, and then keeps speeding up.
The prediction was confirmed by spacecraft, which measure the solar wind streaming past the Earth.

### L2 human

The model is the simplest example of a transonic flow through a critical point, a structure that appears again in Bondi accretion and in the de Laval nozzle.
The steady Euler equations become a single ordinary differential equation that is singular at the sonic point, and the physical solution is the one that crosses this singularity smoothly.
More realistic models add rotation and magnetic fields, which lead to the Parker spiral and to the magnetic braking of stars.
