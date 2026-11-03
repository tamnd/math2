---
tag: AA5EAPX2VC
kind: definition
name: Morris–Lecar model
msc: [92C20, 34C60, 37N25]
defines: Z7W7723M80
uses: [0NT64JV96A, RMWR3MDW0T, K0QGHD7E70]
sources:
  - url: https://en.wikipedia.org/wiki/Morris–Lecar_model
---

## Definition

The *Morris–Lecar model* is the following planar system of [[ordinary differential equations|0NT64JV96A]].
Its unknowns are the membrane potential $V(t)$ and the potassium gating variable $N(t) \in [0, 1]$.
$$C \frac{dV}{dt} = I - g_L (V - V_L) - g_{\mathrm{Ca}} M_\infty(V)(V - V_{\mathrm{Ca}}) - g_{\mathrm{K}} N (V - V_{\mathrm{K}}),$$
$$\frac{dN}{dt} = \frac{N_\infty(V) - N}{\tau_N(V)},$$
with
$$M_\infty(V) = \tfrac12\Bigl(1 + \tanh\frac{V - V_1}{V_2}\Bigr), \quad N_\infty(V) = \tfrac12\Bigl(1 + \tanh\frac{V - V_3}{V_4}\Bigr), \quad \tau_N(V) = \frac{1}{\varphi \cosh\frac{V - V_3}{2 V_4}}.$$
Here $C > 0$ is the membrane capacitance and $I$ the applied current.
The constants $g_L, g_{\mathrm{Ca}}, g_{\mathrm{K}} > 0$ are the leak, calcium and potassium conductances, and $V_L, V_{\mathrm{Ca}}, V_{\mathrm{K}}$ their reversal potentials.
The shape parameters are $V_1, V_3 \in \R$ and $V_2, V_4 > 0$, and $\varphi > 0$ is a rate constant.

## Remarks

The calcium activation is taken at its steady state $M_\infty(V)$, which is justified when it is much faster than $N$.
This is the same reduction that turns the [[Hodgkin–Huxley model|K0QGHD7E70]] into planar models.
Depending on the parameters, the onset of repetitive firing as $I$ increases occurs through a Hopf bifurcation or through a saddle-node bifurcation on an invariant circle.
In the second case the firing frequency starts near zero, as in many cortical neurons.
Non-example: if $N$ is also replaced by its steady state $N_\infty(V)$, the model becomes one-dimensional and cannot oscillate.
