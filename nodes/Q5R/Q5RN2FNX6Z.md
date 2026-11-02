---
tag: Q5RN2FNX6Z
kind: example
name: Meyer wavelet
msc: [42C40, 65T60]
instance_of: [4PZ35C0GV3]
uses: [DPVM34ADZV, 1GHQMBR7DE]
sources:
  - url: https://en.wikipedia.org/wiki/Meyer_wavelet
same_as:
  wikidata: Q12036496
  wikipedia: Meyer wavelet
---

## Example

Use the [[Fourier transform|DPVM34ADZV]] $\hat f(\omega) = \int_{\R} f(x) e^{-i\omega x} \, dx$.
Fix an infinitely differentiable function $\nu \colon \R \to [0,1]$ with $\nu(x) = 0$ for $x \le 0$, $\nu(x) = 1$ for $x \ge 1$, and $\nu(x) + \nu(1-x) = 1$ for all $x$.
The *Meyer wavelet* $\psi$ is the function in $L^2(\R)$ whose Fourier transform is
$$\hat\psi(\omega) = \begin{cases} e^{i\omega/2} \sin\left(\frac{\pi}{2} \nu\left(\frac{3\abs{\omega}}{2\pi} - 1\right)\right) & \text{if } \frac{2\pi}{3} \le \abs{\omega} \le \frac{4\pi}{3}, \\ e^{i\omega/2} \cos\left(\frac{\pi}{2} \nu\left(\frac{3\abs{\omega}}{4\pi} - 1\right)\right) & \text{if } \frac{4\pi}{3} \le \abs{\omega} \le \frac{8\pi}{3}, \\ 0 & \text{otherwise.} \end{cases}$$
The functions $\psi_{j,k}(x) = 2^{j/2} \psi(2^j x - k)$, for $j, k \in \Z$, form an orthonormal basis of $L^2(\R)$.
So $\psi$ is an orthonormal wavelet.
It comes from a [[multiresolution analysis|1GHQMBR7DE]] whose scaling function $\varphi$ has $\hat\varphi(\omega) = 1$ for $\abs{\omega} \le 2\pi/3$ and $\hat\varphi(\omega) = 0$ for $\abs{\omega} \ge 4\pi/3$.

## Remarks

The two formulas agree at $\abs{\omega} = 4\pi/3$, since there the sine has argument $\pi/2$ and the cosine has argument $0$.
The condition $\nu(x) + \nu(1-x) = 1$ makes the values of $\abs{\hat\psi}^2$ on overlapping bands add up to $1$, which is the key to orthonormality.
Since $\hat\psi$ vanishes near $\omega = 0$, every moment $\int x^n \psi(x) \, dx$ is zero.
Since $\hat\psi$ has compact support, $\psi$ is band-limited and infinitely differentiable.
Since $\nu$ is $C^\infty$, $\hat\psi$ is $C^\infty$ with compact support, so $\psi$ decays faster than any power of $\abs{x}$.
The support of $\psi$ itself is not compact.
The Meyer wavelet can be seen as a smoothed version of the [[Shannon wavelet|6C1S8HD38Z]], whose Fourier transform is a sharp indicator function.

## Explanations

### L1 human

The Meyer wavelet is built in frequency space rather than in time.
Its spectrum lives in two bands, one on each side of the origin, and the edges of the bands are rounded off smoothly instead of being cut sharply.
Because the edges are smooth, the wavelet is concentrated in time as well: it is a smooth wave that dies out quickly away from the origin.
Shifting and dyadically stretching it gives an orthonormal basis for all finite-energy signals on the line.
