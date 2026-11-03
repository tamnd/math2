---
tag: SZ5JAVZM72
kind: definition
name: Hodgkin–Huxley model
msc: [92C20, 34C60]
defines: K0QGHD7E70
uses: [RMWR3MDW0T, 0NT64JV96A, B9JD74Y5C3]
sources:
  - url: https://en.wikipedia.org/wiki/Hodgkin–Huxley_model
---

## Definition

The *Hodgkin–Huxley model* is the system of [[ordinary differential equations|0NT64JV96A]] for $V(t)$ and gating variables $m(t), h(t), n(t) \in [0, 1]$
$$C_m \frac{dV}{dt} = I - \bar g_{\mathrm{Na}} m^3 h (V - E_{\mathrm{Na}}) - \bar g_{\mathrm{K}} n^4 (V - E_{\mathrm{K}}) - g_L (V - E_L),$$
$$\frac{dx}{dt} = \alpha_x(V)(1 - x) - \beta_x(V)\, x \qquad \text{for } x \in \set{m, h, n}.$$
Here $V$ is the membrane potential, $C_m > 0$ the membrane capacitance and $I$ the applied current.
The constants $\bar g_{\mathrm{Na}}, \bar g_{\mathrm{K}}, g_L > 0$ are the maximal sodium, potassium and leak conductances, and $E_{\mathrm{Na}}, E_{\mathrm{K}}, E_L$ the reversal potentials.
The functions $\alpha_x, \beta_x > 0$ are voltage-dependent rates fitted to data.

## Remarks

The reversal potentials $E_{\mathrm{Na}}$ and $E_{\mathrm{K}}$ are given by the [[Nernst equation|B9JD74Y5C3]].
For fixed $V$, each gating variable relaxes to $x_\infty(V) = \alpha_x/(\alpha_x + \beta_x)$ with time constant $\tau_x(V) = 1/(\alpha_x + \beta_x)$.
The variable $m$ (sodium activation) is fast, while $h$ (sodium inactivation) and $n$ (potassium activation) are slower; this separation of time scales produces the spike.
Example: with $I = 0$ and the original squid axon parameters, the system has a stable resting equilibrium, and a brief current pulse above a threshold produces one action potential.
For constant $I$ in a suitable range the rest state loses stability and the model fires periodically.
Non-example: replacing $m^3 h$ and $n^4$ by constants gives a linear passive membrane, which has no spikes.
