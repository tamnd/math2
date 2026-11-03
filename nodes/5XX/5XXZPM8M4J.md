---
tag: 5XXZPM8M4J
kind: definition
name: Hasselmann's kinetic equation for wind waves
msc: [86A05, 76B15, 35Q86]
defines: 29YAK3JEQ0
uses: [GYQCDP4VN8, R9WC0Z7Z69, R5P8M6SBG7, MH6CSWD7F0]
sources:
  - url: https://en.wikipedia.org/wiki/Wind_wave_model
---

## Definition

Consider [[surface gravity waves|R9WC0Z7Z69]] on deep water, with wavevector $k \in \R^2$ and angular frequency $\omega(k) = \sqrt{g \abs{k}}$ given by the [[dispersion relation|R5P8M6SBG7]].
Describe the sea by its wave action spectrum $N(k, x, t) \ge 0$, the energy [[spectrum|GYQCDP4VN8]] in wavenumber space divided by $\omega(k)$.
Write $N_j = N(k_j)$ and $\omega_j = \omega(k_j)$ for $j = 1, 2, 3$, and $N = N(k)$, $\omega = \omega(k)$.
*Hasselmann's kinetic equation* is
$$\frac{\partial N}{\partial t} + c_g \cdot \nabla_x N = S_{nl} + S_{in} + S_{ds}.$$
Here $c_g = \nabla_k \omega$ is the group velocity, and $S_{in}$ and $S_{ds}$ are the source terms for wind input and dissipation.
The transfer by resonant four-wave interactions is
$$S_{nl}(k) = \int T(k, k_1, k_2, k_3) \, \delta(k + k_1 - k_2 - k_3) \, \delta(\omega + \omega_1 - \omega_2 - \omega_3) \, \big[ N_1 N_2 N_3 + N N_2 N_3 - N N_1 N_3 - N N_1 N_2 \big] \, dk_1 \, dk_2 \, dk_3.$$
The kernel $T \ge 0$ is computed from the nonlinear equations of water waves.

## Remarks

Example: the bracket equals $N N_1 N_2 N_3 \big( N^{-1} + N_1^{-1} - N_2^{-1} - N_3^{-1} \big)$ when all values are positive.
For the spectrum $N(k) = 1/\omega(k)$ the bracket is $N N_1 N_2 N_3 (\omega + \omega_1 - \omega_2 - \omega_3)$, which vanishes on the resonance set.
So this spectrum is a stationary solution of $\partial_t N = S_{nl}$, like an equilibrium of the [[Boltzmann equation|MH6CSWD7F0]].

Non-example: for capillary waves, three-wave resonances $k = k_1 + k_2$, $\omega = \omega_1 + \omega_2$ are possible, and the kinetic equation has a three-wave collision term instead.
For deep-water gravity waves, with $\omega = \sqrt{g \abs{k}}$, three-wave resonances are impossible, and the four-wave term is the leading one.

The term $S_{nl}$ conserves the total action $\int N \, dk$, the total energy $\int \omega N \, dk$ and the total momentum $\int k N \, dk$.
Its exact evaluation is costly, and forecasting models use approximations such as the discrete interaction approximation.
