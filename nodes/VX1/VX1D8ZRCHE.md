---
tag: VX1D8ZRCHE
kind: definition
name: CMB angular power spectrum
msc: [85A40, 62P35]
defines: SJY21N1SNZ
uses: [3F32Y21HP4, QFYGJVA996, EH021K5438]
sources:
  - url: https://en.wikipedia.org/wiki/Cosmic_microwave_background
---

## Definition

Let $T(\hat n)$ be the temperature of the cosmic microwave background, released at [[recombination|EH021K5438]], in the direction $\hat n \in S^2$.
Let $\bar T$ be its mean over the sphere.
Expand the relative fluctuation in [[spherical harmonics|3F32Y21HP4]] $Y_{\ell m}$:
$$\frac{T(\hat n) - \bar T}{\bar T} = \sum_{\ell \ge 1} \sum_{m = -\ell}^{\ell} a_{\ell m} \, Y_{\ell m}(\hat n).$$
Model the fluctuation as a statistically isotropic random field with mean zero.
Then $\mathbb{E}[a_{\ell m} \overline{a_{\ell' m'}}] = C_\ell \, \delta_{\ell \ell'} \delta_{m m'}$, and the sequence $(C_\ell)_{\ell \ge 1}$ is the *angular power spectrum*.

## Remarks

The two-point correlation function is
$$C(\vartheta) = \sum_{\ell} \frac{2 \ell + 1}{4 \pi} C_\ell \, P_\ell(\cos \vartheta),$$
where $\vartheta$ is the angle between the two directions and $P_\ell$ are the [[Legendre polynomials|QFYGJVA996]].
This follows from the addition theorem for spherical harmonics.
From one sky, $C_\ell$ is estimated by $\hat C_\ell = \frac{1}{2 \ell + 1} \sum_m \abs{a_{\ell m}}^2$.
For a Gaussian field, this estimator has relative standard deviation $\sqrt{2 / (2 \ell + 1)}$, the cosmic variance.
Spectra are usually plotted as $D_\ell = \ell (\ell + 1) C_\ell / (2 \pi)$.
The dipole $\ell = 1$ is dominated by the motion of the observer and is usually removed.

Example: if $C_\ell = c / (\ell(\ell + 1))$ for a constant $c$, then $D_\ell = c / (2 \pi)$ is flat; this is roughly the shape at low $\ell$ for a scale-invariant spectrum of primordial fluctuations.

Non-example: a fixed map with a preferred direction, such as $\delta T / \bar T = \varepsilon \cos \vartheta_0$, is not statistically isotropic.
Its coefficients are not described by a variance depending only on $\ell$.
