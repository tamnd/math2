---
tag: H11X2TCMAZ
kind: definition
name: Painlevé transcendents
msc: ["33E17", 34M55]
defines: AZ17JCMRKB
uses: [8EV1G2Y6CC, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Painlev%C3%A9_transcendents
---

## Definition

Let $\alpha, \beta, \gamma, \delta$ be complex constants, and let $y$ be a function of a complex variable $t$.
The six *Painlevé equations* are the [[ordinary differential equations|0NT64JV96A]]:

1. $\mathrm{P_I}$: $y'' = 6y^2 + t$;
2. $\mathrm{P_{II}}$: $y'' = 2y^3 + ty + \alpha$;
3. $\mathrm{P_{III}}$: $y'' = \frac{(y')^2}{y} - \frac{y'}{t} + \frac{\alpha y^2 + \beta}{t} + \gamma y^3 + \frac{\delta}{y}$;
4. $\mathrm{P_{IV}}$: $y'' = \frac{(y')^2}{2y} + \frac32 y^3 + 4ty^2 + 2(t^2 - \alpha) y + \frac{\beta}{y}$;
5. $\mathrm{P_V}$: $y'' = \left( \frac{1}{2y} + \frac{1}{y - 1} \right) (y')^2 - \frac{y'}{t} + \frac{(y - 1)^2}{t^2} \left( \alpha y + \frac{\beta}{y} \right) + \frac{\gamma y}{t} + \frac{\delta y (y + 1)}{y - 1}$;
6. $\mathrm{P_{VI}}$: $y'' = \frac12 \left( \frac1y + \frac{1}{y - 1} + \frac{1}{y - t} \right) (y')^2 - \left( \frac1t + \frac{1}{t - 1} + \frac{1}{y - t} \right) y' + \frac{y (y - 1)(y - t)}{t^2 (t - 1)^2} \left( \alpha + \frac{\beta t}{y^2} + \frac{\gamma (t - 1)}{(y - 1)^2} + \frac{\delta t (t - 1)}{(y - t)^2} \right)$.

A *Painlevé transcendent* is a solution of one of these six equations.

## Remarks

Each equation has the [[Painlevé property|8EV1G2Y6CC]]: the only movable singularities of its solutions are poles.
Example: for $\alpha = 1$, the function $y = -\frac1t$ solves $\mathrm{P_{II}}$.
Check: $y'' = -\frac{2}{t^3}$, and $2y^3 + ty + 1 = -\frac{2}{t^3} - 1 + 1 = -\frac{2}{t^3}$.
This solution is rational, so for special parameters some Painlevé transcendents are classical functions; the generic solution is not.
Non-example: a solution of $y'' = 6y^2$ is not a Painlevé transcendent, since this equation is not one of the six; its nonconstant solutions are translates of the Weierstrass function $\wp(t; 0, g_3)$.
Each of $\mathrm{P_I}$ to $\mathrm{P_V}$ is a limit of $\mathrm{P_{VI}}$ under a suitable coalescence of singular points and parameters.
