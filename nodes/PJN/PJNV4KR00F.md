---
tag: PJNV4KR00F
kind: definition
name: Short-time Fourier transform
msc: [42A38, 94A12]
defines: 3DHNP5NEWH
uses: [SASP14MA1Z, DPVM34ADZV, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Short-time_Fourier_transform
---

## Definition

Let $g \in L^2(\R)$ be a nonzero function, the *window*, and let $f \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
The *short-time Fourier transform* of $f$ with respect to $g$ is the function $V_g f \colon \R^2 \to \C$,
$$V_g f(x, \omega) = \int_{\R} f(t) \, \overline{g(t - x)} \, e^{-2\pi i t \omega} \, dt,$$
for $x \in \R$ (time) and $\omega \in \R$ (frequency).

## Remarks

The integral converges absolutely, since $f \cdot \overline{g(\cdot - x)}$ is integrable by the Cauchy–Schwarz inequality.
So $V_g f(x, \cdot)$ is the [[Fourier transform|DPVM34ADZV]] of $f \cdot \overline{g(\cdot - x)}$.
In inner product form, $V_g f(x, \omega) = \ip{f}{M_\omega T_x g}$, where $T_x g(t) = g(t - x)$ and $M_\omega g(t) = e^{2\pi i \omega t} g(t)$.
Moyal's formula states $\norm{V_g f}_{L^2(\R^2)} = \norm{f}_2 \norm{g}_2$.
The squared modulus $\abs{V_g f}^2$ is the *spectrogram*.
In engineering texts the variable $\omega$ often denotes angular frequency, and the kernel is $e^{-i \omega t}$.

Example: let $f = g = 1_{[0, 1]}$.
For $0 \le x \le 1$, the product $f \cdot g(\cdot - x)$ is the indicator of $[x, 1]$, so $V_g f(x, 0) = 1 - x$.
For $\abs{x} > 1$ the supports are disjoint and $V_g f(x, \omega) = 0$.

Non-example: with the constant window $g = 1$, which is not in $L^2(\R)$, the formula gives $\hat f(\omega)$ for every $x$.
It carries no time information, and this choice is excluded by the definition.
