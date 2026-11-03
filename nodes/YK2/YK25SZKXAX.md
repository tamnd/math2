---
tag: YK25SZKXAX
kind: statement
role: fact
name: Paris' law
msc: [74R99, 74R10]
uses: [8D619PN75J, A8X23QRKVF]
about: [A8X23QRKVF]
sources:
  - url: https://en.wikipedia.org/wiki/Paris%27_law
same_as:
  wikidata: Q7137166
  wikipedia: Paris' law
---

## Statement

Let a crack of length $a$ in a part grow under cyclic loading.
Let $\Delta K = K_{\max} - K_{\min}$ be the range of the mode I [[stress intensity factor|8D619PN75J]] over one cycle.
Consider the intermediate range of $\Delta K$.
It lies above the threshold below which cracks do not grow, and below the values close to the fracture toughness.
In this range the crack growth rate per cycle obeys the empirical power law
$$\frac{da}{dN} = C \, (\Delta K)^m,$$
where $N$ is the number of cycles.
The numbers $C > 0$ and $m > 0$ are constants of the material for a given load ratio and environment.

## Remarks

The law is an empirical fit to measured crack growth curves, not a consequence of the equations of mechanics; for metals the exponent $m$ is typically between $2$ and $4$.
Example: for a through crack in a wide plate, $\Delta K = \Delta\sigma \sqrt{\pi a}$, where $\Delta \sigma$ is the stress range.
For $m \ne 2$, separating variables and integrating from an initial length $a_0$ to a final length $a_f$ gives the number of cycles
$$N = \frac{a_0^{1 - m/2} - a_f^{1 - m/2}}{(m/2 - 1) \, C \, (\Delta\sigma \sqrt{\pi})^m}.$$
For $m > 2$ this depends mainly on $a_0$, which is why the detection of small initial cracks matters so much.
Outside the intermediate range the law fails: near the threshold the growth rate drops faster, and near the fracture toughness it increases faster.

## Explanations

### L1 human

Under repeated loading a crack grows by a tiny amount in every cycle.
Paris' law says that this amount is proportional to a power of the range of the stress intensity at the crack tip.
A larger crack has a larger stress intensity, so it grows faster, and the growth speeds up until the part fails.

### L2 human

Paris' law is the basis of damage-tolerant design of [[fatigue|A8X23QRKVF]]-loaded structures such as aircraft.
One estimates the largest crack that inspections might miss.
Integrating the law gives the number of cycles until the crack reaches the critical length set by the fracture toughness.
The inspection interval is chosen below that number.
It links fatigue to linear elastic fracture mechanics through $\Delta K$.
Refinements, such as the Forman equation, add the effect of the load ratio and of the approach to fracture.
