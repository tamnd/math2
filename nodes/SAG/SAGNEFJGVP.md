---
tag: SAGNEFJGVP
kind: example
name: Mellin transform of a theta series and the zeta function
msc: [11M06, 44A15]
instance_of: [N5PVGRJE1T]
uses: [1XWBY4N0VT, 2F5CYQJVAF, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_zeta_function
---

## Example

For $x > 0$ let $\psi(x) = \sum_{n=1}^{\infty} e^{-\pi n^2 x}$.
With the [[theta function|2F5CYQJVAF]] $\theta(x) = \sum_{n \in \Z} e^{-\pi n^2 x}$, one has $\psi(x) = (\theta(x) - 1)/2$.
For $\operatorname{Re} s > 1$, the [[Mellin transform|N5PVGRJE1T]] of $\psi$ at $s/2$ is
$$\int_0^\infty x^{s/2 - 1} \psi(x) \, dx = \pi^{-s/2} \, \Gamma\left(\frac{s}{2}\right) \zeta(s),$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]] and $\zeta$ is the [[Riemann zeta function|1XWBY4N0VT]].

Check: for each $n \ge 1$ the dilation rule gives
$$\int_0^\infty x^{s/2 - 1} e^{-\pi n^2 x} \, dx = (\pi n^2)^{-s/2} \, \Gamma\left(\frac{s}{2}\right) = \pi^{-s/2} \, \Gamma\left(\frac{s}{2}\right) n^{-s}.$$
Let $\sigma = \operatorname{Re} s > 1$.
The sum over $n$ of the integrals of the absolute values is $\pi^{-\sigma/2} \Gamma(\sigma/2) \sum_n n^{-\sigma} < \infty$.
So, by Fubini's theorem, the sum and the integral may be exchanged, and the sum of the right sides is $\pi^{-s/2} \Gamma(s/2) \zeta(s)$.

The series $\psi$ is Mellin convergent at $s/2$ exactly for $\operatorname{Re} s > 1$.
Near $\infty$, $\psi(x) \le C e^{-\pi x}$; near $0$, $\psi(x) \sim \frac{1}{2} x^{-1/2}$, which follows from the identity $\theta(1/x) = \sqrt{x}\, \theta(x)$.

## Explanations

### L1 human

The theta series adds up Gaussian bumps $e^{-\pi n^2 x}$, one for each whole number $n$.
Taking its Mellin transform turns each bump into a multiple of $n^{-s}$, so the whole series turns into the zeta function, times a gamma factor.
This is how Riemann connected the symmetry $\theta(1/x) = \sqrt{x}\, \theta(x)$ of the theta function with the [[functional equation of the zeta function|NFXKNDJX9C]].
Splitting the integral at $x = 1$ and using that symmetry gives the analytic continuation of $\zeta$ and the symmetry under $s \mapsto 1 - s$.
