---
tag: D7PH59MNTV
kind: definition
name: Fourier analysis
msc: [42A16, 42A38, 42B10]
defines: FAYWXJ68SB
uses: [7QNRC9SJVV, G12KXDHPPS, DPVM34ADZV, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_analysis
---

## Definition

*Fourier analysis* is the part of [[harmonic analysis|7QNRC9SJVV]] that studies the decomposition of functions into [[complex exponentials|07GJV36896]] and the reconstruction of functions from these components.
It covers the following transforms:

1. the [[Fourier series|G12KXDHPPS]] of a $2\pi$-periodic function, with components $e^{inx}$ for $n \in \Z$;
2. the [[Fourier transform|DPVM34ADZV]] of a function on $\R^n$, with components $e^{2\pi i x \cdot \xi}$ for $\xi \in \R^n$;
3. the discrete Fourier transform of a function on $\Z / N\Z$, with components $e^{2\pi i jk/N}$ for $k \in \Z / N\Z$.

## Remarks

Example: the $2\pi$-periodic function $f(x) = \sin^3 x$ satisfies $f(x) = \frac{3}{4} \sin x - \frac{1}{4} \sin 3x$, by the identity $\sin 3x = 3 \sin x - 4 \sin^3 x$.
So its Fourier decomposition has only the frequencies $\pm 1$ and $\pm 3$.
Non-example: writing a function as a power series $\sum a_n x^n$ is an expansion into monomials, not into exponentials, so it is not Fourier analysis.
The word analysis refers to the decomposition step, and the word synthesis to the reconstruction step.
