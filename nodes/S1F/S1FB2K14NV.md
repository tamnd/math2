---
tag: S1FB2K14NV
kind: statement
role: theorem
name: Uncertainty principle in Fourier analysis
msc: ["42B10", "42A38"]
uses: [DPVM34ADZV, SASP14MA1Z, 0G4F0XB9X2]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
    locator: Uncertainty principle
---

## Statement

Let $n \ge 1$ and let $f \in L^1(\R^n)$.
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi}\, dx$ be its [[Fourier transform|DPVM34ADZV]].
Suppose that $f$ vanishes almost everywhere outside a bounded set and that $\hat f$ vanishes outside a bounded set.
Then $f = 0$ almost everywhere.

## Remarks

If $f$ vanishes outside a ball of radius $R$, then the integral $\int f(x) e^{-2\pi i x \cdot z}\, dx$ makes sense for every $z \in \C^n$.
It defines an [[entire function|0G4F0XB9X2]] of $z$ that extends $\hat f$.
An entire function that vanishes on a nonempty open subset of $\R^n$ vanishes identically, so $\hat f = 0$, and then $f = 0$ by injectivity of the transform.

The statement is the simplest of a family of results that say a nonzero function and its Fourier transform cannot both be sharply concentrated.
The Heisenberg inequality bounds the product of the variances of $\abs{f}^2$ and $\abs{\hat f}^2$ from below.
Hardy's uncertainty principle is about Gaussian decay, and the entropic uncertainty principle measures spread by entropy.
Benedicks' theorem replaces bounded sets by sets of finite measure.

Example: $\operatorname{rect}$, the indicator of $[-\frac12, \frac12]$, has compact support, and its transform $\sin(\pi\xi)/(\pi\xi)$ has zeros only at the nonzero integers, so it does not vanish outside any bounded set.

## Explanations

### L1 human

A signal cannot be both short in time and limited to a finite band of frequencies.
If it lasts only a finite time, it must contain arbitrarily high frequencies, and if all its frequencies lie in a bounded band, it must go on forever.

### L2 human

The proof uses the Paley–Wiener idea that compact support in $x$ makes $\hat f$ analytic, indeed entire of exponential type.
Analyticity is very rigid, and this rigidity is the source of all qualitative uncertainty principles.
In signal processing the statement says that no nonzero band-limited signal has finite duration, so every real filter or sampling scheme is a compromise between the two.
