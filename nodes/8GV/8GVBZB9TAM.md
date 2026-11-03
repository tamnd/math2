---
tag: 8GVBZB9TAM
kind: definition
name: Entropy production
msc: [82C35, 80A17]
defines: STR73R5MX4
uses: [SPY89W0RJ7, CY4GJQGF06, T11MGWEKJ3, J027RJ924H, 0MWV6ZTK6S]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_production
---

## Definition

Let a closed system with [[entropy|SPY89W0RJ7]] $S(t)$ exchange [[heat|CY4GJQGF06]] with its surroundings through boundary parts $j$ at temperatures $T_j$, at rates $\dot Q_j$.
Split the rate of change of entropy as
$$\frac{dS}{dt} = \sum_j \frac{\dot Q_j}{T_j} + \Sigma.$$
The first term is the entropy exchange rate, and $\Sigma$ is the *rate of entropy production* of the system.

Now let a continuous system be in [[local thermodynamic equilibrium|J027RJ924H]], with mass density $\rho$ and specific entropy $s$.
The local form is the balance law
$$\rho \frac{ds}{dt} = -\nabla \cdot J_s + \sigma.$$
Here $\frac{d}{dt}$ is the material derivative, $J_s$ is the entropy flux and $\nabla \cdot$ is the [[divergence|0MWV6ZTK6S]].
The term $\sigma$ is the *local entropy production* per unit volume and time.

## Remarks

The [[second law|T11MGWEKJ3]] states $\Sigma \ge 0$ and $\sigma \ge 0$, with equality exactly for reversible processes.
Example: in a solid with heat flux $J_q$ and no other process, $J_s = J_q / T$ and
$$\sigma = J_q \cdot \nabla \frac{1}{T}.$$
With Fourier's law $J_q = -k \nabla T$ and $k > 0$, this gives $\sigma = k \abs{\nabla T}^2 / T^2 \ge 0$, as the second law requires.
In general $\sigma = \sum_k J_k \cdot X_k$, a sum of products of fluxes $J_k$ and conjugate forces $X_k$, such as $\nabla(1/T)$ for heat or $-\nabla(\mu_k/T)$ for diffusion.
Non-example: the full rate $dS/dt$ is not the entropy production, because it also contains the exchange term, and it can be negative when a body cools.
