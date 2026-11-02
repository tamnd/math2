---
tag: ZTZ1FRRFM8
kind: statement
role: proposition
name: Mellin transform as a Fourier transform in logarithmic variables
msc: [44A15, 42A38]
uses: [SGZZ4Y0D36, N5PVGRJE1T, DPVM34ADZV, X7GTF3D98F]
about: [N5PVGRJE1T, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $f \colon (0, \infty) \to \C$ be measurable and let $s = \sigma + i\tau$ with $\sigma, \tau \in \R$.
Define $h_\sigma \colon \R \to \C$ by $h_\sigma(u) = e^{-\sigma u} f(e^{-u})$.
Then $f$ is [[Mellin convergent|SGZZ4Y0D36]] at $s$ if and only if $h_\sigma$ is [[integrable|X7GTF3D98F]] on $\R$.
In that case
$$\mathcal{M}f(\sigma + i\tau) = \widehat{h_\sigma}\left(\frac{\tau}{2\pi}\right),$$
where $\mathcal{M}f$ is the [[Mellin transform|N5PVGRJE1T]] and $\widehat{h}(\xi) = \int_{\R} h(u) e^{-2\pi i u \xi} \, du$ is the [[Fourier transform|DPVM34ADZV]].

## Remarks

The proof is the substitution $x = e^{-u}$, with $dx = -e^{-u} \, du$, which maps $(0, \infty)$ onto $\R$ with reversed orientation.
It gives $\int_0^\infty x^{\sigma - 1} \abs{f(x)} \, dx = \int_{\R} \abs{h_\sigma(u)} \, du$, and
$$\int_0^\infty x^{s-1} f(x) \, dx = \int_{\R} e^{-su} f(e^{-u}) \, du = \int_{\R} h_\sigma(u) e^{-i\tau u} \, du.$$
Example: $f(x) = e^{-x}$ and $\sigma = 1$ give $h_1(u) = e^{-u} e^{-e^{-u}}$, and the statement says $\widehat{h_1}(\tau/2\pi) = \Gamma(1 + i\tau)$.
Other sign conventions use $x = e^{u}$, which replaces $\tau / 2\pi$ by $-\tau / 2\pi$.
For fixed $\sigma$, the map $f \mapsto h_\sigma$ is a bijection, so every theorem on the Fourier transform on $\R$ has a Mellin version on each vertical line.

## Explanations

### L1 human

On a logarithmic scale, multiplication becomes addition, and the powers $x^{s}$ become exponentials $e^{su}$.
So the Mellin transform, which integrates against powers, becomes the Fourier transform, which integrates against exponentials.
The real part of $s$ only adds a fixed weight $e^{-\sigma u}$ to the function.

### L2 human

This dictionary transports results from Fourier analysis.
The Riemann–Lebesgue lemma gives the decay of $\mathcal{M}f(\sigma + i\tau)$ as $\abs{\tau} \to \infty$.
The Fourier inversion theorem and the Plancherel theorem give the Mellin inversion theorem and the Parseval formula for Mellin transforms.
Varying $\sigma$ as well, the same substitution identifies the Mellin transform with a two-sided Laplace transform of $u \mapsto f(e^{-u})$.
It also identifies the strip of Mellin convergence with the strip of convergence of that Laplace transform.
