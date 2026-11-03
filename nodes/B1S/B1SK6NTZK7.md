---
tag: B1SK6NTZK7
kind: definition
name: Large eddy simulation
msc: [76F65]
defines: 1708HMRRSW
uses: [18KXZHVF4M, VY307F8Z0S, 4K9W1VP58R, P1KWMQG4NZ, V47TX9AFKF]
sources:
  - url: https://en.wikipedia.org/wiki/Large_eddy_simulation
---

## Definition

Consider an incompressible fluid with constant density $\rho$ and kinematic viscosity $\nu$ in $\R^3$, whose velocity $u_i$ and pressure $p$ satisfy the [[Navier–Stokes equations|18KXZHVF4M]].
Let $G_\Delta$ be a filter kernel of width $\Delta > 0$, an integrable function with $\int G_\Delta = 1$, and write $\tilde f = G_\Delta * f$ for the filtered field.
Filtering the equations gives
$$\frac{\partial \tilde u_i}{\partial t} + \frac{\partial (\tilde u_i \tilde u_j)}{\partial x_j} = -\frac{1}{\rho} \frac{\partial \tilde p}{\partial x_i} + \nu \Delta \tilde u_i - \frac{\partial \tau_{ij}}{\partial x_j}, \qquad \frac{\partial \tilde u_i}{\partial x_i} = 0,$$
with the subgrid-scale stress $\tau_{ij} = \widetilde{u_i u_j} - \tilde u_i \tilde u_j$.
*Large eddy simulation* is the numerical solution of these filtered equations for $\tilde u_i$ and $\tilde p$ on a grid with spacing comparable to $\Delta$.
In it, $\tau_{ij}$ is replaced by a subgrid-scale model expressed in terms of the filtered fields.

## Remarks

Let $\tilde S_{ij}$ be the [[strain rate tensor|P1KWMQG4NZ]] of $\tilde u$ and $C_s$ a constant, typically between about $0.1$ and $0.2$.
The most common model is Smagorinsky's eddy viscosity model, in the spirit of the [[Boussinesq hypothesis|4K9W1VP58R]]:
$$\tau_{ij} - \tfrac13 \tau_{kk} \delta_{ij} = -2 \nu_t \tilde S_{ij}, \qquad \nu_t = (C_s \Delta)^2 \abs{\tilde S}, \qquad \abs{\tilde S} = \sqrt{2 \tilde S_{ij} \tilde S_{ij}}.$$
The filter commutes with derivatives on $\R^3$, which is why the filtered equations take this form.

Example: use a Gaussian kernel, or a sharp cutoff in Fourier space at wavenumber $\pi / \Delta$, with $\Delta$ in the inertial range of the flow.
Then the resolved field contains the energetic large eddies, and the model mainly has to drain energy at the right rate.
Non-example: solving the mean equations of the [[Reynolds decomposition|V47TX9AFKF]] with an ensemble average is not large eddy simulation.
That average removes all fluctuations, while the filter removes only scales smaller than $\Delta$.
Also, the filter in general does not satisfy $\tilde{\tilde f} = \tilde f$.
