---
tag: XVVHKCYF2Z
kind: statement
role: theorem
name: Balian–Low theorem
msc: [42C15, 42A38]
uses: [M9WHY8E2PM, ZYDYD7FB1Z, DPVM34ADZV, SASP14MA1Z]
about: [M9WHY8E2PM]
sources:
  - url: https://en.wikipedia.org/wiki/Balian%E2%80%93Low_theorem
same_as:
  wikidata: Q3527008
  wikipedia: Balian–Low theorem
---

## Statement

Let $g \in L^2(\R)$, and let $\hat g(\xi) = \int_\R g(t) e^{-2\pi i t \xi} \, dt$ be its [[Fourier transform|DPVM34ADZV]].
Suppose that the [[Gabor system|M9WHY8E2PM]] $\left(e^{2\pi i n t} g(t - k)\right)_{k, n \in \Z}$ is a [[Riesz basis|ZYDYD7FB1Z]] of $L^2(\R)$.
Then
$$\left( \int_\R \abs{t \, g(t)}^2 \, dt \right) \left( \int_\R \abs{\xi \, \hat g(\xi)}^2 \, d\xi \right) = \infty.$$

## Remarks

So a window of a Gabor Riesz basis at the critical density $ab = 1$ cannot be well localized both in time and in frequency.
Roger Balian and, independently, Francis Low stated the result for orthonormal bases; later work completed their proofs and extended it to Riesz bases.
A standard route uses the [[Zak transform|S026HQSGY9]]: the system is a Riesz basis exactly when $Zg$ is bounded above and below by positive constants almost everywhere.
On the other hand $Zg$ is quasi-periodic, and a continuous quasi-periodic function must vanish somewhere; when $g$ is well localized this contradicts the lower bound.
The hypothesis $ab = 1$ matters: for $ab < 1$ the Gaussian $e^{-\pi t^2}$, which is as well localized as possible, generates a Gabor frame.

Example: $g = 1_{[0, 1)}$ generates an orthonormal basis.
Here $\int \abs{t g(t)}^2 \, dt = \tfrac13$ is finite, but $\abs{\hat g(\xi)} = \abs{\sin(\pi \xi)}/(\pi \abs{\xi})$, so $\abs{\xi \hat g(\xi)}^2 = \sin^2(\pi \xi)/\pi^2$ is not integrable.

## Explanations

### L1 human

A Gabor basis builds every signal from shifted and modulated copies of one window, placed on a grid as sparse as possible.
The theorem says that this window cannot be nice: it must be badly spread out either in time or in frequency.
The box function is sharp in time but its spectrum decays too slowly.
It is a strong form of the uncertainty principle for bases.

### L2 human

The theorem explains why practical Gabor expansions are redundant frames with $ab < 1$ rather than bases.
It is proved with the [[Zak transform|S026HQSGY9]], which turns the Gabor system at $a = b = 1$ into multiplication by a quasi-periodic function, and the question becomes one about zeros of that function.
It contrasts with wavelets: there exist orthonormal wavelet bases, such as the Meyer wavelets, whose generator is smooth and decays fast together with its Fourier transform.
Compare with the [[uncertainty principle in Fourier analysis|S1FB2K14NV]], which bounds the product of the two integrals from below for one function.
