---
tag: 6WGT43N6KT
kind: example
name: Gamma function as Mellin transform of the exponential
msc: [44A15, 33B15]
instance_of: [N5PVGRJE1T]
uses: [0H5SYBSED9, SGZZ4Y0D36, Z8D1CZFTWP]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Example

Let $f(x) = e^{-x}$ for $x > 0$.
Its [[Mellin transform|N5PVGRJE1T]] is the [[gamma function|0H5SYBSED9]]:
$$\mathcal{M}f(s) = \int_0^\infty x^{s-1} e^{-x} \, dx = \Gamma(s), \qquad \operatorname{Re} s > 0.$$
The right side is [[Euler's integral|Z8D1CZFTWP]], which is the usual definition of $\Gamma$ on the half-plane $\operatorname{Re} s > 0$.

Check of [[Mellin convergence|SGZZ4Y0D36]]: let $\sigma = \operatorname{Re} s$.
On $(0, 1]$, $x^{\sigma - 1} e^{-x} \le x^{\sigma - 1}$, which is integrable exactly when $\sigma > 0$.
On $[1, \infty)$, $x^{\sigma - 1} e^{-x} \le C_\sigma e^{-x/2}$ for a constant $C_\sigma$, which is integrable for every $\sigma$.
For $\sigma \le 0$, $x^{\sigma - 1} e^{-x} \ge e^{-1} x^{\sigma - 1}$ on $(0, 1]$, which is not integrable.
So $f$ is Mellin convergent exactly on the half-plane $\operatorname{Re} s > 0$.

Integration by parts gives $\Gamma(s + 1) = s \Gamma(s)$, and $\Gamma(1) = \int_0^\infty e^{-x} \, dx = 1$, so $\Gamma(n + 1) = n!$.
By the dilation rule, $\int_0^\infty x^{s-1} e^{-ax} \, dx = a^{-s} \Gamma(s)$ for $a > 0$.
By the [[Mellin inversion theorem|XJWC13NY9E]], for every $c > 0$ and $x > 0$,
$$e^{-x} = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \Gamma(s) x^{-s} \, ds.$$

## Explanations

### L1 human

The gamma function, which extends the factorial, is the simplest Mellin transform.
One weighs the decaying exponential $e^{-x}$ against the powers $x^{s-1}$ and integrates.
At $s = 1, 2, 3, \dots$ the answers are $0!, 1!, 2!, \dots$.
The integral only makes sense when $\operatorname{Re} s > 0$, because otherwise the power blows up too fast at $0$.
