---
tag: AENSRM0ZMD
kind: definition
name: Deconvolution of seismic data
msc: [86A22, 94A12, 62M10]
defines: BWBB42GNEH
uses: [2Z29JN3VES, 5FY0JQGHYZ, GKY2WSHE26, DT0QXJE705]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_inversion
---

## Definition

Model a seismic trace as a discrete time series
$$x_n = (w * r)_n + e_n = \sum_{k} w_k\, r_{n-k} + e_n.$$
Here $w$ is the source wavelet, $r$ is the reflectivity series, $e$ is noise and $*$ is [[convolution|2Z29JN3VES]].
*Deconvolution of seismic data* is the deconvolution problem of estimating $r$ from $x$.
Usually one designs a filter $f$ of finite length with $f * w \approx \delta$, where $\delta$ is the unit spike at time $0$, and takes $\hat r = f * x$.
In Wiener (spiking) deconvolution, the coefficients $f_0, \dots, f_{L-1}$ minimise the expected squared error $E\bigl[\abs{(f * x)_n - r_n}^2\bigr]$.
When $r$ is white, this leads to the normal equations
$$\sum_{j=0}^{L-1} \phi_{i-j}\, f_j = c\, \delta_{i0}, \qquad i = 0, \dots, L-1.$$
Here $\phi$ is the autocorrelation of the [[stationary|DT0QXJE705]] trace and $c$ is a constant fixed by the wavelet.

## Remarks

The matrix $(\phi_{i-j})$ is a symmetric [[Toeplitz matrix|GKY2WSHE26]], so the system is solved in $O(L^2)$ operations by Levinson recursion.
Example: $w = (1, -\tfrac{1}{2})$, that is, $W(z) = 1 - z/2$ in [[$z$-transform|5FY0JQGHYZ]] notation.
The filter $f_k = 2^{-k}$ has $F(z) = 1/(1 - z/2)$, so $F W = 1$ and $f * w = \delta$; truncating $f$ after $L$ terms leaves an error $-2^{-L}$ at lag $L$.
Non-example: for $w = (1, -2)$ the formal causal inverse $\sum_k 2^k z^k$ diverges.
The wavelet is not minimum phase, since the root $z = 1/2$ of $W$ lies inside the unit disc.
A stable inverse exists only as a non-causal filter, and the autocorrelation alone cannot tell this wavelet from $(-2, 1)$.
Predictive deconvolution uses a prediction lag larger than one sample to remove periodic reverberations, such as multiples in a water layer.

## Explanations

### L1 human

The trace is the wavelet smeared over the reflectivity.
Deconvolution finds a filter that undoes the smearing, so each reflection becomes a spike.
