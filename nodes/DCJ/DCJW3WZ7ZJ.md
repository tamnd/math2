---
tag: DCJW3WZ7ZJ
kind: example
name: Ricker wavelet
msc: [42C40, 94A12]
illustrates: [57FR21NDGV, 2BBB8NY5ZA]
uses: [4PZ35C0GV3, 57FR21NDGV, 2BBB8NY5ZA, 7QERXM0C52]
sources:
  - url: https://en.wikipedia.org/wiki/Ricker_wavelet
same_as:
  wikidata: Q1019202
  wikipedia: Ricker wavelet
---

## Example

Fix a width $\sigma > 0$.
The *Ricker wavelet*, also called the Mexican hat wavelet, is
$$\psi(t) = \frac{2}{\sqrt{3\sigma} \, \pi^{1/4}} \left(1 - \frac{t^2}{\sigma^2}\right) e^{-t^2/(2\sigma^2)}, \qquad t \in \R.$$
Up to a negative constant factor, it is the second derivative of the Gaussian $e^{-t^2/(2\sigma^2)}$.

Check of the zero mean, with $\sigma = 1$.
Since $\int_{\R} e^{-t^2/2} \, dt = \sqrt{2\pi}$ and $\int_{\R} t^2 e^{-t^2/2} \, dt = \sqrt{2\pi}$, the integral of $(1 - t^2) e^{-t^2/2}$ is $0$.
Check of the norm, with $\sigma = 1$.
The integral of $(1 - t^2)^2 e^{-t^2}$ is $\sqrt{\pi}\,(1 - 1 + 3/4) = 3\sqrt{\pi}/4$, and multiplying by $4/(3\sqrt{\pi})$ gives $\norm{\psi}_2^2 = 1$.
The general case follows by the substitution $t = \sigma s$.

## Remarks

The Fourier transform of $\psi$ is a constant times $\omega^2 e^{-\sigma^2\omega^2/2}$.
It vanishes to second order at $\omega = 0$, so $\psi$ satisfies the [[admissibility condition|2BBB8NY5ZA]] and has two [[vanishing moments|7QERXM0C52]]: $\int \psi = 0$ and $\int t \psi(t) \, dt = 0$, while $\int t^2 \psi(t) \, dt \ne 0$.
It does not generate an orthonormal basis; it is used in the [[continuous wavelet transform|57FR21NDGV]].
In two variables, the analogous function is the negative Laplacian of a Gaussian, which detects blobs and edges in images.
The Ricker wavelet is also a standard model of a seismic source pulse.

## Explanations

### L1 human

Draw a bell curve, push its sides down below zero, and keep the middle as a bump: that is the Mexican hat shape.
The positive bump and the two negative dips balance, so the total area is zero.
Sliding this shape along a signal gives a strong response where the signal has a peak of matching width.
