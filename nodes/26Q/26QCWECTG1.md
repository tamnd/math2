---
tag: 26QCWECTG1
kind: definition
name: Full waveform inversion
msc: [86A22, 35R30, 35L05]
defines: 3XQA40D91Q
uses: [JRN1693EHB, 5EHD2XBQDG, YD8SA6WS01, 0BYTQ4X1HC]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_inversion
---

## Definition

Let $\Omega \subset \R^n$ be a region and let $m$ be a model of the medium on $\Omega$, for example $m = 1/c^2$ for a sound speed $c > 0$.
For each source $s$, let $u_s(x, t; m)$ solve the [[wave equation|5EHD2XBQDG]]
$$m(x)\, \partial_t^2 u_s - \Delta u_s = f_s, \qquad u_s = \partial_t u_s = 0 \text{ at } t = 0,$$
where $f_s$ is the source term and $\Delta$ is the Laplacian.
Let $d_{s,r}(t)$ be the seismogram recorded at receiver $x_r$ for $t \in [0, T]$.
*Full waveform inversion* is the [[seismic tomography|JRN1693EHB]] that estimates $m$ by minimising the [[least squares|0BYTQ4X1HC]] waveform misfit
$$J(m) = \frac{1}{2} \sum_{s, r} \int_0^T \bigl( u_s(x_r, t; m) - d_{s,r}(t) \bigr)^2 \, dt.$$
The minimisation, usually with a regularisation term, uses local iterative methods from an initial model $m_0$.

## Remarks

The gradient of $J$ is computed by the [[adjoint state method|YD8SA6WS01]].
For each source, an adjoint wavefield is driven by the data residuals at the receivers and propagated backward in time.
The gradient at $x$ is a time integral of the product of the adjoint field with $\partial_t^2 u_s$ at $x$.
So one gradient costs about two wave simulations per source, whatever the number of model parameters.
Example of the main difficulty: take a single arrival $w(t - \tau)$ with $w(t) = \cos(\omega t)$ on a long window.
The misfit against the true arrival at $\tau = 0$ behaves like $1 - \cos(\omega \tau)$, with minima at every $\tau = 2\pi k/\omega$.
A starting model with a time error larger than half a period converges to a wrong minimum; this is called cycle skipping.
Non-example: travel-time tomography uses only the arrival times extracted from the records, not the full traces, so it is not full waveform inversion.
Elastic, viscoelastic and anisotropic versions replace the acoustic wave equation by the corresponding systems.

## Explanations

### L1 human

The method changes the model of the Earth step by step to make simulated seismograms match the recorded ones as closely as possible.
The adjoint trick gives the direction of each step at the cost of two simulations.
