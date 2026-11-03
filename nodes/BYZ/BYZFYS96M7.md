---
tag: BYZFYS96M7
kind: example
name: Ashkin–Teller model
msc: [82B20, 82B23]
instance_of: [PAEME5EQRM]
uses: [R0KGM32QN6, 5GY2J6ZGXJ]
sources:
  - url: https://en.wikipedia.org/wiki/Potts_model
---

## Example

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], let $J_1, J_2, J_4$ be real constants and let $\beta \ge 0$ be the inverse temperature.
A configuration assigns to each vertex $x$ two Ising spins $\sigma_x, \tau_x \in \set{-1, +1}$.
Its energy is
$$H(\sigma, \tau) = -\sum_{\set{x, y} \in E} \left( J_1 \sigma_x \sigma_y + J_2 \tau_x \tau_y + J_4 \sigma_x \sigma_y \tau_x \tau_y \right).$$
The *Ashkin–Teller model* is the probability measure on $(\set{-1, +1}^2)^V$ proportional to $e^{-\beta H(\sigma, \tau)}$.

## Remarks

If $J_4 = 0$, the model is two independent [[Ising models|R0KGM32QN6]], one for $\sigma$ and one for $\tau$.
If $J_1 = J_2 = J_4 = J$, the bond energy is $-3J$ when $(\sigma_x, \tau_x) = (\sigma_y, \tau_y)$ and $+J$ otherwise.
So it equals $J - 4J \delta_{(\sigma_x, \tau_x), (\sigma_y, \tau_y)}$, and the model is the four-state [[Potts model|5GY2J6ZGXJ]] with coupling $4J$.
Ashkin and Teller introduced it in 1943 as a model of a four-component system.
On the square lattice it has a line of critical points along which the critical exponents vary continuously.

## Explanations

### L1 human

Put two Ising spins at each site instead of one.
Each kind of spin likes to agree with its neighbours, and an extra term couples the two kinds.
Tuning the extra term moves the model between two separate Ising models and the four-state Potts model.
