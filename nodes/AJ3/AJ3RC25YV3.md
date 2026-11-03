---
tag: AJ3RC25YV3
kind: definition
name: Nyquist rate
msc: [94A20, 94A12, 42A38]
defines: AXKCWXE77N
uses: [P3T104G564, DPVM34ADZV, BMXDMHRXBG]
sources:
  - url: https://en.wikipedia.org/wiki/Nyquist_rate
---

## Definition

Let $f \in L^2(\R)$ be a nonzero function of time $t$ in seconds.
Let $\hat f$ be its [[Fourier transform|DPVM34ADZV]], with frequency $\xi$ in hertz.
It is normalized so that $\hat f(\xi) = \int_\R f(t) \, e^{-2\pi i \xi t} \, dt$ for integrable $f$.
Assume that $f$ is [[band-limited|P3T104G564]], that is, $\hat f = 0$ almost everywhere outside some bounded interval.
Let $B$ be the smallest number $B \ge 0$ such that $\hat f = 0$ almost everywhere outside $[-B, B]$.
The *Nyquist rate* of $f$ is $2B$, in samples per second.

## Remarks

Example: let $f(t) = \left(\frac{\sin \pi t}{\pi t}\right)^2$.
Its Fourier transform is the triangle $\hat f(\xi) = \max(1 - \abs{\xi}, 0)$, which is nonzero on $(-1, 1)$ and zero outside $[-1, 1]$.
So $B = 1$ and the Nyquist rate of $f$ is $2$ samples per second.

Non-example: the Gaussian $f(t) = e^{-\pi t^2}$ has $\hat f(\xi) = e^{-\pi \xi^2}$, which is nonzero everywhere.
So $f$ is not band-limited and has no Nyquist rate.

The [[Nyquist–Shannon sampling theorem|BMXDMHRXBG]] says that the samples $f(n/r)$, $n \in \Z$, determine $f$ when the sampling rate $r$ exceeds the Nyquist rate.
The Nyquist rate is a property of the signal; it should not be confused with the Nyquist frequency, which is half of a given sampling rate.
