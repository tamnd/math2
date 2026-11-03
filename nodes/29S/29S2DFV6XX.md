---
tag: 29S2DFV6XX
kind: definition
name: Biological neuron model
msc: [92C20, 37N25]
defines: RMWR3MDW0T
uses: [0NT64JV96A, BBZP1R872N]
sources:
  - url: https://en.wikipedia.org/wiki/Biological_neuron_model
---

## Definition

A *single-compartment neuron model* is a system of [[ordinary differential equations|0NT64JV96A]] of the following form.
$$C \frac{dV}{dt} = I(t) - I_{\mathrm{ion}}(V, w), \qquad \frac{dw}{dt} = G(V, w).$$
Here $V(t) \in \R$ is the membrane potential, $C > 0$ is the membrane capacitance and $I(t)$ is the input current.
The vector $w(t) \in \R^k$ ($k \ge 0$) collects auxiliary variables such as gating variables.
The function $I_{\mathrm{ion}}$ is the total ionic current, and $G$ gives the dynamics of $w$.
The model may also include a reset rule: when $V$ reaches a threshold $V_{\mathrm{th}}$, a spike is recorded and $(V, w)$ is reset to prescribed values.
A *biological neuron model* is such a model, or a spatially extended version of it.
In a spatially extended model, $V$ also depends on position along the cell and obeys a partial differential equation.

## Remarks

Example: with $k = 0$, $I_{\mathrm{ion}}(V) = (V - E_L)/R$ and a reset rule, one gets the leaky integrate-and-fire model.
Example: the Hodgkin–Huxley model has $k = 3$ gating variables and no reset rule; spikes arise from the smooth dynamics.
Non-example: a perceptron maps an input vector $x$ to $\sgn(a \cdot x - \theta)$ with no time dependence.
It has no membrane potential evolving in time, so it is not a neuron model in this sense.
The equation for $V$ is Kirchhoff's current law for the membrane viewed as a capacitor in parallel with ionic conductances.
