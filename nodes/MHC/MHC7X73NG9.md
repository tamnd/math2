---
tag: MHC7X73NG9
kind: definition
name: Filtered back-projection
msc: [44A12, 92C55, 65R10]
defines: SJQDDY9FMX
uses: [VJNZJ352PC, 938SXZQS8G, KXC9KHWVGE]
sources:
  - url: https://en.wikipedia.org/wiki/Tomographic_reconstruction
---

## Definition

Let $f$ be in the Schwartz space $\mathcal{S}(\R^2)$, with [[Radon transform|VJNZJ352PC]] $R f$, and write $R_\theta f(s) = R f(\theta, s)$.
Let $\Phi \colon \R \to \R$ be an even bounded function with $\Phi(\sigma) = 0$ for $\abs{\sigma} > 1$, continuous at $0$, with $\Phi(0) = 1$.
For $b > 0$, let $w_b$ be the filter with Fourier transform $\hat w_b(\sigma) = \abs{\sigma}\, \Phi(\sigma/b)$.
Its *filtered back-projection* reconstruction with filter $w_b$ is
$$f_b(x) = \frac{1}{4\pi} R^* \left( w_b * R_\theta f \right)(x) = \frac{1}{4\pi} \int_{S^1} (w_b * R_\theta f)(x \cdot \theta)\, d\theta,$$
where $*$ is [[convolution|KXC9KHWVGE]] in the variable $s$ and $R^*$ is the [[dual Radon transform|938SXZQS8G]].

## Remarks

The Fourier convention is $\hat g(\sigma) = \int g(s)\, e^{-is\sigma}\, ds$.
The projection-slice theorem gives $\hat f_b(\xi) = \Phi(\abs{\xi}/b)\, \hat f(\xi)$, so $f_b \to f$ as $b \to \infty$, uniformly on $\R^2$.
With $\Phi$ the indicator of $[-1, 1]$ the filter is the Ram–Lak filter, a band-limited ramp.

Example: if $\Phi$ is the indicator of $[-1, 1]$ and $\hat f$ vanishes for $\abs{\xi} > b$, then $\hat f_b = \hat f$ and the reconstruction is exact: $f_b = f$.

Non-example: back-projection without filter, $\frac{1}{4\pi} R^* R f$, is not a reconstruction of $f$.
It corresponds to $\hat w(\sigma) = 1$ instead of $\abs{\sigma}$, and its Fourier transform is $\hat f(\xi)/\abs{\xi}$, a blurred image.

In practice $R f$ is known only at finitely many angles and offsets, and the integral and the convolution are replaced by sums.
