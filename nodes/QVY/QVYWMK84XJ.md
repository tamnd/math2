---
tag: QVYWMK84XJ
kind: definition
name: Chemostat model
msc: [92C70, 92D25, 34C60]
defines: E6FPS400MA
uses: [0NT64JV96A, 6E26A54JG8, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Chemostat
---

## Definition

Let $S(t) \ge 0$ be the concentration of the limiting nutrient and $x(t) \ge 0$ the concentration of biomass in a vessel of constant volume.
Let $D > 0$ be the dilution rate, $S^0 > 0$ the nutrient concentration of the inflowing medium, and $Y > 0$ the yield.
Let $\mu \colon [0, \infty) \to [0, \infty)$ be a specific growth rate function.
The *chemostat model* is the system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dS}{dt} = D\, (S^0 - S) - \frac{1}{Y}\, \mu(S)\, x, \qquad \frac{dx}{dt} = \big(\mu(S) - D\big)\, x.$$
The standard choice of $\mu$ is the [[Monod equation|6E26A54JG8]] $\mu(S) = \mu_{\max} S/(K_s + S)$.

## Remarks

The *washout* state $(S, x) = (S^0, 0)$ is always an [[equilibrium|0N8NGKDZDZ]].
Example: with the Monod law and $D < \mu(S^0)$, there is a second equilibrium with $\mu(S^*) = D$, that is $S^* = K_s D/(\mu_{\max} - D)$, and $x^* = Y (S^0 - S^*) > 0$; one checks that both right sides vanish, since $D(S^0 - S^*) = D x^* / Y$.
In that case solutions with $x(0) > 0$ tend to $(S^*, x^*)$; if $D > \mu(S^0)$ they tend to washout.
Non-example: the batch culture $dS/dt = -\mu(S) x / Y$, $dx/dt = \mu(S) x$ has no inflow or outflow, so it is not a chemostat model; there the nutrient is used up.
The quantity $S + x/Y$ satisfies $\frac{d}{dt}(S + x/Y) = D(S^0 - S - x/Y)$, so it tends to $S^0$; this reduces the system to one equation.
