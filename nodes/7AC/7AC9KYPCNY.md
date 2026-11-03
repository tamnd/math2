---
tag: 7AC9KYPCNY
kind: definition
name: Climate sensitivity
msc: [86A08]
defines: RNXRF74VSC
uses: [B8HRNPHNZF, M49PQ7BDYN]
sources:
  - url: https://en.wikipedia.org/wiki/Climate_sensitivity
---

## Definition

Let $\Delta T$ be the change of the global mean surface temperature from its preindustrial equilibrium.
Let $N$ be the net downward radiative flux at the top of the atmosphere.
In the linear forcing-feedback model, a [[radiative forcing|B8HRNPHNZF]] $\Delta F$ gives
$$N = \Delta F - \lambda \, \Delta T,$$
where $\lambda > 0$ is the *climate feedback parameter*, in $\mathrm{W\,m^{-2}\,K^{-1}}$.

1. The *equilibrium climate sensitivity* (ECS) is the value of $\Delta T$ at equilibrium ($N = 0$) after carbon dioxide is doubled and then held fixed. In the linear model, $\mathrm{ECS} = \Delta F_{2\times} / \lambda$, with $\Delta F_{2\times}$ the forcing of the doubling.
2. The *climate sensitivity parameter* is $1/\lambda$, the equilibrium warming per unit forcing.
3. Let carbon dioxide rise by $1\%$ per year. The *transient climate response* (TCR) is the value of $\Delta T$ at the time of doubling, averaged over 20 years.

## Remarks

Example: in the zero-dimensional energy balance model with outgoing flux $\sigma T^4$ and no other feedback, $\lambda = 4 \sigma T_e^3$ at the emission temperature $T_e \approx 255$ K, so $\lambda \approx 3.8 \ \mathrm{W\,m^{-2}\,K^{-1}}$.
With $\Delta F_{2\times} \approx 3.7 \ \mathrm{W/m^2}$ this gives an ECS of about $1$ K, the no-feedback sensitivity.
Positive feedbacks lower $\lambda$ and raise the ECS.

Non-example: the warming observed while the concentration is still rising is not the ECS, since the deep ocean is still taking up heat and $N > 0$.
It is closer to the TCR, which is smaller than the ECS.

The assessment of the IPCC in 2021 gives a likely range of $2.5$ to $4$ K for the ECS, with a best estimate of $3$ kelvin.
In [[climate models|M49PQ7BDYN]] the feedback parameter is often estimated after an abrupt quadrupling of carbon dioxide.
One regresses $N$ against $\Delta T$ and reads $\lambda$ from the slope.
