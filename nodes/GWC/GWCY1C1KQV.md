---
tag: GWCY1C1KQV
kind: statement
role: theorem
name: Bohr's approximation theorem
msc: [42A75, 42A10, 43A60]
uses: [ED69H4C3PK, 0X3WGX95FE]
about: [ED69H4C3PK]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Statement

Let $f \colon \R \to \C$ be a [[continuous function|0X3WGX95FE]].
Then $f$ is [[Bohr almost periodic|ED69H4C3PK]] if and only if the following holds.
For every $\varepsilon > 0$ there are $N \ge 1$, reals $\lambda_1, \dots, \lambda_N$ and complex numbers $c_1, \dots, c_N$ such that
$$\sup_{x \in \R} \Big| f(x) - \sum_{k=1}^{N} c_k e^{i \lambda_k x} \Big| < \varepsilon.$$

## Remarks

The sums $\sum c_k e^{i\lambda_k x}$ are called generalized trigonometric polynomials.
One direction is the easier one.
Each $e^{i\lambda x}$ is periodic, and a finite sum of Bohr almost periodic functions is again almost periodic, for example by Bochner's criterion with sequences of translates.
A uniform limit of almost periodic functions is almost periodic, by an $\varepsilon/3$ argument on almost periods.

The other direction is the substance of the theorem.
Every Bohr almost periodic function has a mean value $M(g) = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} g(x) \, dx$.
So $f$ has Fourier coefficients $a(\lambda) = M(f(x) e^{-i\lambda x})$, and $a(\lambda) \ne 0$ for at most countably many $\lambda$.
Bohr proved the Parseval identity $M(\abs{f}^2) = \sum_\lambda \abs{a(\lambda)}^2$, and approximating sums can then be built from these frequencies, for example by the Bochner–Fejér summation method.
A modern proof uses the [[Bohr compactification|G852FHZ3W1]] of $\R$ and the [[Stone–Weierstrass theorem|1P8D3MK79H]] or the Peter–Weyl theorem on that compact group.

Example: $\cos x + \cos(\sqrt{2} x) = \frac12 \big( e^{ix} + e^{-ix} + e^{i\sqrt2 x} + e^{-i\sqrt2 x} \big)$ is itself a generalized trigonometric polynomial, hence almost periodic.
The theorem is a uniform analogue for all real frequencies of the density of [[trigonometric polynomials|J3NJQ5FZJ5]] among continuous periodic functions.

## Explanations

### L1 human

A Bohr almost periodic function is one that nearly repeats itself.
The theorem says these are exactly the functions that can be approximated, uniformly on the whole line, by finite sums of waves $e^{i\lambda x}$ with any real frequencies.
So almost periodic functions are built from pure waves, just as periodic functions are built from the harmonics of one basic frequency.

### L2 human

For a continuous periodic function, the Weierstrass approximation theorem for trigonometric polynomials gives uniform approximation by harmonics of the period.
Bohr's theorem removes the restriction that all frequencies are multiples of one frequency.
The approximating frequencies can be taken among the $\lambda$ with $a(\lambda) \ne 0$, which makes the Fourier series of $f$ a faithful description of $f$.
Equivalently, the space of Bohr almost periodic functions is the closure in the uniform norm of the span of the characters $x \mapsto e^{i\lambda x}$ of $\R$.
