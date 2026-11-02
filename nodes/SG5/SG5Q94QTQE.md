---
tag: SG5Q94QTQE
kind: definition
name: Fourier coefficient
msc: [42A16]
defines: 5NN2YZZR3V
uses: [089KWVYD69, X7GTF3D98F, DWJF7ABPR1, TZYSW0975T]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Definition

Let $f \colon \R \to \C$ be a [[periodic function|089KWVYD69]] of period $2\pi$ that is Lebesgue [[integrable|X7GTF3D98F]] on $[-\pi, \pi]$, and let $n \in \Z$.
The $n$-th *Fourier coefficient* of $f$ is the complex number
$$\hat f(n) = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) e^{-inx} \, dx,$$
where the integral is the [[Lebesgue integral|DWJF7ABPR1]].

## Remarks

In terms of the [[Fourier monomials|TZYSW0975T]] $e_n$, $\hat f(n) = \langle f, e_n \rangle$ for the inner product $\langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} f \overline{g}$.
By periodicity the integral may be taken over any interval of length $2\pi$.
The bound $\abs{\hat f(n)} \le \frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{f}$ holds for every $n$.
Example: for $f(x) = \cos x$, the formula $\cos x = \frac{1}{2}(e^{ix} + e^{-ix})$ and the orthogonality of the $e_n$ give $\hat f(1) = \hat f(-1) = \frac{1}{2}$ and $\hat f(n) = 0$ for $\abs{n} \ne 1$.
Non-example: the $2\pi$-periodic function equal to $1/x$ on $(0, 2\pi]$ is not integrable on a period, so its Fourier coefficients are not defined.
The real coefficients $a_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos nx \, dx$ and $b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin nx \, dx$ satisfy $a_n = \hat f(n) + \hat f(-n)$ and $b_n = i(\hat f(n) - \hat f(-n))$.
Other notations are $c_n$ and $\mathcal{F}f(n)$; for period $T$ the coefficient is $\frac{1}{T} \int_0^T f(x) e^{-2\pi i n x / T} \, dx$.
