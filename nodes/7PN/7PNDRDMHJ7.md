---
tag: 7PNDRDMHJ7
kind: definition
name: Rayleigh–Bénard convection
msc: ["76E06", 76R10]
defines: GKVRHF9E43
uses: [18KXZHVF4M, TXQQQG9T2S, CEKBV27MP0, C4KSBMR413, H028A17Z55]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh–Bénard_convection
---

## Definition

Consider a fluid layer $0 < z < d$, unbounded in the horizontal directions, under gravity $g$ in the direction $-z$.
Let $\nu$ be its kinematic viscosity, $\kappa$ its thermal diffusivity and $\alpha$ its thermal expansion coefficient.
The bottom plate is held at temperature $T_0 + \Delta T$ and the top plate at $T_0$, with $\Delta T > 0$.
Let $\rho_0$ be a reference density and $\mathbf{e}_z$ the upward unit vector.
In the [[Boussinesq approximation|TXQQQG9T2S]], the velocity $\mathbf{u}$, pressure $p$ and temperature $T$ satisfy
$$\partial_t \mathbf{u} + (\mathbf{u} \cdot \nabla) \mathbf{u} = -\frac{1}{\rho_0} \nabla p + \nu \Delta \mathbf{u} + g \alpha (T - T_0) \mathbf{e}_z, \qquad \nabla \cdot \mathbf{u} = 0,$$
$$\partial_t T + \mathbf{u} \cdot \nabla T = \kappa \Delta T.$$
These equations have the conduction solution $\mathbf{u} = 0$, $T = T_0 + \Delta T (1 - z/d)$.
*Rayleigh–Bénard convection* is the flow with $\mathbf{u} \neq 0$ that this system develops when the conduction solution is unstable.

## Remarks

The control parameters are the [[Rayleigh number|CEKBV27MP0]] $\mathrm{Ra} = g \alpha \Delta T d^3 / (\nu \kappa)$ and the [[Prandtl number|C4KSBMR413]] $\mathrm{Pr} = \nu / \kappa$.
Linear stability theory shows that the conduction state is unstable exactly when $\mathrm{Ra}$ exceeds a critical value $\mathrm{Ra}_c$ that does not depend on $\mathrm{Pr}$.
For two rigid no-slip plates, $\mathrm{Ra}_c \approx 1708$ with critical wavenumber $k_c d \approx 3.12$.
For two stress-free plates, Rayleigh's case, $\mathrm{Ra}_c = 27 \pi^4 / 4 \approx 657.5$ with $k_c d = \pi / \sqrt{2}$.

Example: just above $\mathrm{Ra}_c$, with rigid plates, the observed flow consists of steady parallel convection rolls with wavelength close to $2\pi d / k_c \approx 2d$.
Non-example: a layer heated from above, $\Delta T < 0$, is stably stratified, and the conduction solution is stable for every value of $\abs{\Delta T}$.
The hexagonal cells in Bénard's original experiments with a free upper surface are now attributed mainly to surface tension gradients, the Marangoni effect, rather than to buoyancy.
