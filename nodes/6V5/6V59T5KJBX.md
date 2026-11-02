---
tag: 6V59T5KJBX
kind: definition
name: Fourier transform
msc: [42B10, 42A38, 35A22]
defines: DPVM34ADZV
uses: [X7GTF3D98F, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform
---

## Definition

Let $n \ge 1$ and let $f \colon \R^n \to \C$ be a Lebesgue [[integrable function|X7GTF3D98F]].
The *Fourier transform* of $f$ is the function $\hat f \colon \R^n \to \C$ given by the [[Lebesgue integral|DWJF7ABPR1]]
$$\hat f(\xi) = \int_{\R^n} f(x)\, e^{-2\pi i\, x \cdot \xi} \, dx, \qquad \xi \in \R^n,$$
where $x \cdot \xi = x_1 \xi_1 + \dots + x_n \xi_n$.
It is also written $\mathcal{F} f$.

## Remarks

The integral converges absolutely because $\abs{f(x) e^{-2\pi i x \cdot \xi}} = \abs{f(x)}$.
So $\abs{\hat f(\xi)} \le \int \abs{f}$, and $\hat f$ is continuous by dominated convergence.
By the Riemann–Lebesgue lemma, $\hat f(\xi) \to 0$ as $\abs{\xi} \to \infty$.
Other common conventions are $\int f(x) e^{-i x \cdot \xi}\, dx$ and $(2\pi)^{-n/2} \int f(x) e^{-i x \cdot \xi}\, dx$; they change the constants in the formulas below.

With the convention above, if $f$ and $\partial_j f$ are integrable, then $\widehat{\partial_j f}(\xi) = 2\pi i \xi_j \hat f(\xi)$.
If $\hat f$ is also integrable, the inversion formula $f(x) = \int \hat f(\xi) e^{2\pi i x \cdot \xi}\, d\xi$ holds for almost every $x$.
Plancherel's theorem extends $\mathcal F$ to a unitary map of $L^2(\R^n)$, and duality extends it to [[tempered distributions|AES2T5JPFP]].

Example: $f(x) = e^{-\pi \abs{x}^2}$ satisfies $\hat f = f$.
For $n = 1$, completing the square gives $\hat f(\xi) = e^{-\pi \xi^2} \int_\R e^{-\pi (x + i\xi)^2}\, dx$, and the last integral equals $\int_\R e^{-\pi x^2}\, dx = 1$ by a contour shift.

Non-example: the constant function $f = 1$ on $\R$ is not integrable, and the integral $\int_\R e^{-2\pi i x \xi}\, dx$ diverges for every $\xi$.
Its Fourier transform exists only as a tempered distribution, namely the Dirac delta at $0$.

## Explanations

### L1 human

The transform measures how strongly $f$ oscillates with each frequency $\xi$.
It is the continuous analogue of the list of coefficients of a Fourier series.
