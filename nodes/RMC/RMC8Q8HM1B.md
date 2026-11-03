---
tag: RMC8Q8HM1B
kind: statement
role: theorem
name: Ornstein–Zernike correlation decay
msc: [82B20, 82B27, 60K35]
uses: [ENWMTRJRND, R0KGM32QN6]
about: [ENWMTRJRND]
sources:
  - url: https://en.wikipedia.org/wiki/Ornstein%E2%80%93Zernike_equation
---

## Statement

Let $d \ge 2$, and consider a ferromagnetic [[Ising model|R0KGM32QN6]] on $\Z^d$ with finite-range couplings and zero field.
Let $\beta_c$ be its critical inverse temperature, and let $\beta < \beta_c$.
Let $\langle \sigma_0 \sigma_x \rangle_\beta$ be its two-point [[correlation function|ENWMTRJRND]] in the unique Gibbs state.
Then there are a norm $\tau_\beta$ on $\R^d$ and a positive function $\psi_\beta$ on the unit sphere such that
$$\langle \sigma_0 \sigma_x \rangle_\beta = \frac{\psi_\beta(x / \abs{x})}{\abs{x}^{(d-1)/2}} \, e^{-\tau_\beta(x)} \, \big(1 + o(1)\big) \quad \text{as } \abs{x} \to \infty.$$

## Remarks

Ornstein and Zernike predicted this form in the early twentieth century from their equation for fluids, and Campanino, Ioffe and Velenik proved it for these Ising models in 2003.
The heuristic: if the Fourier transform of the correlation function is close to $1/(k^2 + \xi^{-2})$ for small $k$, then its inverse transform decays like $\abs{x}^{-(d-1)/2} e^{-\abs{x}/\xi}$.
In $d = 3$ this is the Yukawa form $e^{-r/\xi} / r$.
The rigorous proof writes the correlation as a sum over random paths and shows that these paths behave like a directed random walk with a mass gap.

Example: $\tau_\beta(x) = \abs{x} / \xi$ along a lattice axis, where $\xi$ is the correlation length in that direction.
The prefactor $\abs{x}^{-(d-1)/2}$ is the same as for the Green function of a massive random walk.

The hypothesis $\beta < \beta_c$ is necessary.
At $\beta = \beta_c$ the decay is a power law with no exponential factor.
For $\beta > \beta_c$ in $d = 2$, the truncated correlation of the plus state decays with the prefactor $\abs{x}^{-2}$ instead of $\abs{x}^{-1/2}$.

## Explanations

### L1 human

Above the critical temperature, the influence of one spin on a far spin dies out exponentially fast.
The Ornstein–Zernike law gives the exact shape: an exponential times a power of the distance.
The power is $(d - 1)/2$, the same in every model of this kind, while the rate of the exponential depends on the model and on the direction.

### L2 human

The result links the [[Ornstein–Zernike equation|29T4NC87AR]] of liquid theory with lattice spin systems.
It is proved by showing that long correlation paths split into many independent pieces, so that a local limit theorem applies.
The same method gives Ornstein–Zernike asymptotics for subcritical percolation connectivities and for self-avoiding walks with a mass.
The norm $\tau_\beta$ is the inverse correlation length as a function of direction.
