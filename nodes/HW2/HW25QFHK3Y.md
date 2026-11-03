---
tag: HW25QFHK3Y
kind: definition
name: Integrate-and-fire model
msc: [92C20, 34C60]
defines: D1E7NK903C
uses: [RMWR3MDW0T, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Biological_neuron_model
---

## Definition

Let $\tau_m > 0$, $R > 0$, and let $E_L < V_{\mathrm{th}}$ and $V_r < V_{\mathrm{th}}$ be real numbers.
The *leaky integrate-and-fire model* with input current $I(t)$ is the following rule for the membrane potential $V(t)$.

1. While $V(t) < V_{\mathrm{th}}$, it obeys the [[ordinary differential equation|0NT64JV96A]] $\tau_m \dfrac{dV}{dt} = -(V - E_L) + R\, I(t)$.
2. When $V$ reaches $V_{\mathrm{th}}$ at a time $t_k$, a spike is emitted at $t_k$ and $V$ is reset to $V_r$; then clause 1 applies again.

Here $\tau_m$ is the membrane time constant, $R$ the membrane resistance, $E_L$ the resting potential, $V_{\mathrm{th}}$ the threshold and $V_r$ the reset value.
More generally, an *integrate-and-fire model* replaces the right side of clause 1 by $f(V) + R\, I(t)$ for a function $f$, keeping the threshold and reset rule.

## Remarks

Example: for constant input $I$ with $E_L + R I > V_{\mathrm{th}}$, the solution after a reset is $V(t) = E_L + R I + (V_r - E_L - R I) e^{-t/\tau_m}$.
It reaches $V_{\mathrm{th}}$ after the time
$$T = \tau_m \ln \frac{E_L + R I - V_r}{E_L + R I - V_{\mathrm{th}}},$$
so the neuron fires periodically with period $T$.
If $E_L + R I \le V_{\mathrm{th}}$, the potential tends to $E_L + R I$ and never fires.
Variants add a refractory period after each spike, or use $f(V)$ quadratic or exponential, which gives the quadratic and exponential integrate-and-fire models.
Non-example: the Hodgkin–Huxley model has no threshold and reset rule; its spikes come from the continuous dynamics of its gating variables.
