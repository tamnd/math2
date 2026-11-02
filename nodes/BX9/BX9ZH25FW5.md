---
tag: BX9ZH25FW5
kind: definition
name: Absolutely convergent Fourier series
msc: [42A20, 42A16]
defines: HHBGB5R5S2
uses: [G12KXDHPPS, 5NN2YZZR3V, X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_algebra
---

## Definition

Let $f \colon \R \to \C$ be a $2\pi$-periodic function that is [[integrable|X7GTF3D98F]] on $[-\pi, \pi]$.
For $n \in \Z$ let $\hat f(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) e^{-int} \, dt$ be its [[Fourier coefficients|5NN2YZZR3V]].
The [[Fourier series|G12KXDHPPS]] of $f$ is *absolutely convergent* if
$$\sum_{n \in \Z} \abs{\hat f(n)} < \infty.$$

## Remarks

If the series converges absolutely, then $\sum_n \hat f(n) e^{inx}$ converges uniformly on $\R$ to a continuous function $g$.
The function $g$ has the same Fourier coefficients as $f$, so $g = f$ almost everywhere.
One often says simply that $f$ has an absolutely convergent Fourier series.

Example: let $f(x) = \abs{x}$ for $-\pi \le x \le \pi$, extended with period $2\pi$.
Integration by parts gives $\hat f(0) = \pi/2$ and $\hat f(n) = \frac{(-1)^n - 1}{\pi n^2}$ for $n \ne 0$.
So $\abs{\hat f(n)} \le 2/(\pi n^2)$, and the sum $\sum_n \abs{\hat f(n)}$ is finite.

Non-example: the square wave equal to $1$ on $(0, \pi)$ and $-1$ on $(-\pi, 0)$ has $\abs{\hat f(n)} = \frac{2}{\pi \abs{n}}$ for odd $n$.
The sum of these over odd $n$ diverges like the harmonic series.
This also follows from the remark above: the square wave is not equal almost everywhere to a continuous function.
