---
tag: WVJQXA3K2E
kind: example
name: Morlet wavelet
msc: [42C40, 94A12]
illustrates: [57FR21NDGV, 2BBB8NY5ZA]
uses: [4PZ35C0GV3, 57FR21NDGV, 2BBB8NY5ZA]
sources:
  - url: https://en.wikipedia.org/wiki/Morlet_wavelet
same_as:
  wikidata: Q3505077
  wikipedia: Morlet wavelet
---

## Example

Fix a parameter $\sigma > 0$ and put $\kappa_\sigma = e^{-\sigma^2/2}$.
The *Morlet wavelet* is the complex-valued function
$$\psi_\sigma(t) = c_\sigma \, \pi^{-1/4} e^{-t^2/2} \left(e^{i\sigma t} - \kappa_\sigma\right), \qquad t \in \R,$$
where $c_\sigma > 0$ is the constant that makes $\norm{\psi_\sigma}_2 = 1$.
It is a plane wave $e^{i\sigma t}$ under a Gaussian envelope, with a small correction term.

Check of the zero mean.
Since $\int_{\R} e^{-t^2/2} e^{i\sigma t} \, dt = \sqrt{2\pi} \, e^{-\sigma^2/2}$ and $\int_{\R} e^{-t^2/2} \, dt = \sqrt{2\pi}$, the integral of $\psi_\sigma$ is $c_\sigma \pi^{-1/4} \sqrt{2\pi} \left(e^{-\sigma^2/2} - \kappa_\sigma\right) = 0$.
Its Fourier transform is a combination of two Gaussians and vanishes at frequency $0$.
Together with the Gaussian decay, this gives the [[admissibility condition|2BBB8NY5ZA]], so $\psi_\sigma$ can be used in the [[continuous wavelet transform|57FR21NDGV]].

## Remarks

The correction $\kappa_\sigma$ is tiny when $\sigma$ is large; for $\sigma \ge 5$ it is below $10^{-5}$, and in practice it is often dropped.
Without the correction, the function $e^{-t^2/2} e^{i\sigma t}$ has nonzero integral, so it is not admissible in the strict sense.
The Morlet wavelet does not generate an orthonormal basis; it is used for the continuous transform and for time–frequency analysis of signals.
Its real part is even and its imaginary part is odd.
Since the wavelet is complex-valued, the modulus of the transform gives an amplitude and the argument gives a phase.

## Explanations

### L1 human

The Morlet wavelet is a short burst of oscillation: a wave of frequency $\sigma$ that fades out like a bell curve on both sides.
Comparing a signal with stretched and shifted copies of it tells how much of each frequency is present near each time.
The small constant subtracted from the wave makes the average of the function exactly zero, which a wavelet needs.
