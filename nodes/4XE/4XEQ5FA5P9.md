---
tag: 4XEQ5FA5P9
kind: statement
role: theorem
name: Clausius–Clapeyron relation
msc: [80A22, 80A10]
uses: [WVH4PVW64P, FN6Z9QKAH5, SPY89W0RJ7, VXVGVDSJ0W, 6WJ0NADBT4, R6XCQYXKRP]
about: [6WJ0NADBT4, R6XCQYXKRP]
sources:
  - url: https://en.wikipedia.org/wiki/Clausius%E2%80%93Clapeyron_relation
same_as:
  wikidata: Q745416
  wikipedia: Clausius–Clapeyron relation
---

## Statement

Let two [[phases|6WJ0NADBT4]] $\alpha$ and $\beta$ of a pure substance coexist along a curve $p = p(T)$ in the [[phase diagram|R6XCQYXKRP]].
Let $s_\alpha, s_\beta$ be their molar [[entropies|SPY89W0RJ7]] and $v_\alpha, v_\beta$ their molar volumes on the curve, and assume $v_\beta \ne v_\alpha$.
Let $L = T(s_\beta - s_\alpha)$ be the molar [[latent heat|FN6Z9QKAH5]] of the transition from $\alpha$ to $\beta$.

1. (Clapeyron equation) Along the curve,
$$\frac{dp}{dT} = \frac{L}{T (v_\beta - v_\alpha)}.$$
2. (Clausius–Clapeyron approximation) If $\beta$ is a vapour that obeys the [[ideal gas law|VXVGVDSJ0W]] $p v_\beta = RT$, and $v_\alpha$ is negligible compared with $v_\beta$, then
$$\frac{d \ln p}{dT} = \frac{L}{R T^2}.$$

## Remarks

On the curve the [[chemical potentials|WVH4PVW64P]] are equal, $\mu_\alpha(T, p(T)) = \mu_\beta(T, p(T))$.
Differentiating along the curve and using $d\mu = -s\, dT + v\, dp$ gives $(s_\beta - s_\alpha)\, dT = (v_\beta - v_\alpha)\, dp$, which is part 1.
Part 2 follows by putting $v_\beta - v_\alpha \approx RT/p$.
If $L$ is also constant, integration gives $\ln(p_2/p_1) = -\frac{L}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$.
For melting of ice, $L > 0$ but $v_{\text{liquid}} < v_{\text{ice}}$, so the melting curve has negative slope: higher pressure lowers the melting point.
The hypothesis $v_\beta \ne v_\alpha$ is needed; at a critical point both $L$ and $v_\beta - v_\alpha$ tend to $0$.

## Explanations

### L1 human

The relation tells how the boiling or melting temperature moves when the pressure changes.
The more heat a transition needs, and the smaller the change in volume, the steeper the boundary between the two phases.
It explains why water boils at a lower temperature high in the mountains, where the pressure is lower.

### L2 human

Part 1 is exact and holds for any first-order transition of a pure substance, including solid–solid ones.
Part 2 is the form used for vapour pressure curves: plotting $\ln p$ against $1/T$ gives nearly a straight line of slope $-L/R$.
This is a standard way to measure latent heats.
For continuous transitions, where $L = 0$ and $\Delta v = 0$, the relation becomes $0/0$, and it is replaced by the [[Ehrenfest equations|DAWS652192]].
