---
tag: VYB03ZZ8H6
kind: example
name: Wilson–Cowan neural field equation
msc: [92C20, 45K05]
instance_of: [YRKW2KX2CW]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson%E2%80%93Cowan_model
---

## Example

A neural field describes the activity of a sheet of neurons, with a position variable $x \in \R^d$ and time $t$.
Let $u_e(x, t)$ and $u_i(x, t)$ be the mean activities of the excitatory and the inhibitory populations, with time constants $\tau_e, \tau_i > 0$.
Let $w_{ab} \colon \R^d \to [0, \infty)$ be integrable connectivity kernels, let $S_e, S_i$ be increasing sigmoid firing-rate functions, and let $h_e, h_i$ be external inputs.
A commonly used form of the Wilson–Cowan neural field equations, with refractory terms neglected, is
$$\tau_e \, \partial_t u_e = -u_e + S_e\big(w_{ee} * u_e - w_{ei} * u_i + h_e\big), \qquad \tau_i \, \partial_t u_i = -u_i + S_i\big(w_{ie} * u_e - w_{ii} * u_i + h_i\big),$$
where $(w * u)(x, t) = \int_{\R^d} w(x - y) \, u(y, t) \, dy$.
Each equation has a time derivative of the unknowns and a space integral of them, so the system is a nonlinear [[integro-differential equation|YRKW2KX2CW]].

Check: for constant inputs, a spatially constant state $(\bar u_e, \bar u_i)$ is a steady state exactly when
$$\bar u_e = S_e\big(W_{ee} \bar u_e - W_{ei} \bar u_i + h_e\big), \qquad \bar u_i = S_i\big(W_{ie} \bar u_e - W_{ii} \bar u_i + h_i\big),$$
where $W_{ab} = \int_{\R^d} w_{ab}(z) \, dz$, because $w * \bar u = W \bar u$ for a constant $\bar u$.
These are the equations of the space-clamped [[Wilson–Cowan model|98XX53BC3S]].

## Remarks

The convolution structure makes the linearization at a homogeneous steady state diagonal in Fourier modes $e^{i k \cdot x}$.
This gives conditions for pattern-forming (Turing-type) instabilities, used to model visual hallucination patterns and travelling waves of cortical activity.
A single-population version $\tau \partial_t u = -u + w * S(u) + h$ is also widely studied, under the name Amari equation.

## Explanations

### L1 human

Neurons in the cortex excite or inhibit other neurons, more strongly when they are close.
The model follows the average activity at each point of the cortex.
This activity decays on its own and is driven by a weighted sum of the activity at all other points.
The weighted sum is an integral over space, so the model is an integro-differential equation, whose solutions can form bumps, stripes and waves.
