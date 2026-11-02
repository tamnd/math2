---
tag: VD2REA47BN
kind: definition
name: Gabor transform
msc: [42A38, 94A12]
defines: 8GQRJ6TPVC
uses: [3DHNP5NEWH, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Gabor_transform
---

## Definition

Let $f \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
The *Gabor transform* of $f$ is the function $G f \colon \R^2 \to \C$,
$$G f(\tau, \omega) = \int_{\R} f(t) \, e^{-\pi (t - \tau)^2} \, e^{-2\pi i \omega t} \, dt,$$
for $\tau \in \R$ (time) and $\omega \in \R$ (frequency).

## Remarks

It is the [[short-time Fourier transform|3DHNP5NEWH]] $V_g f$ with the Gaussian window $g(t) = e^{-\pi t^2}$.
Some authors allow a Gaussian $e^{-\alpha \pi (t - \tau)^2}$ of any width $\alpha > 0$, or normalize the window to have $L^2$ norm $1$.

Example: let $f(t) = e^{-\pi t^2}$.
Then $f(t) e^{-\pi (t - \tau)^2} = e^{-\pi \tau^2/2} e^{-2\pi (t - \tau/2)^2}$, and the Fourier transform of $e^{-2\pi s^2}$ at $\omega$ is $2^{-1/2} e^{-\pi \omega^2/2}$.
So $G f(\tau, \omega) = 2^{-1/2} e^{-\pi \tau^2/2} e^{-\pi \omega^2/2} e^{-\pi i \tau \omega}$, and $\abs{G f}$ is a Gaussian bump centred at the origin of the time–frequency plane.

Non-example: the short-time Fourier transform with the window $1_{[-1/2, 1/2]}$ is not a Gabor transform, since its window is not Gaussian.
