---
tag: WT7K28D1CD
kind: definition
name: Wigner distribution function
msc: [81S30, 42A38, 94A12]
defines: FCHW5QGG5V
uses: [SASP14MA1Z, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_distribution_function
---

## Definition

Let $f \in L^2(\R)$ (see [[Lp space|SASP14MA1Z]]).
The *Wigner distribution* of $f$ is the function $Wf \colon \R^2 \to \C$,
$$Wf(x, \omega) = \int_{\R} f\!\left(x + \tfrac{t}{2}\right) \overline{f\!\left(x - \tfrac{t}{2}\right)} \, e^{-2\pi i t \omega} \, dt,$$
for $x \in \R$ (time) and $\omega \in \R$ (frequency).

## Remarks

The integral converges absolutely for each $x$, by the Cauchy–Schwarz inequality.
$Wf$ is real-valued, since replacing $t$ by $-t$ turns the integral into its complex conjugate.
For $f$ in the Schwartz space, $\int_\R Wf(x, \omega) \, d\omega = \abs{f(x)}^2$ and $\int_\R Wf(x, \omega) \, dx = \abs{\hat f(\omega)}^2$, where $\hat f$ is the [[Fourier transform|DPVM34ADZV]].
In quantum mechanics the Wigner function of a wave function is usually written with Planck's constant and a normalizing factor.

Example: let $f(t) = 2^{1/4} e^{-\pi t^2}$, so that $\norm{f}_2 = 1$.
Then $f(x + t/2) \overline{f(x - t/2)} = \sqrt2 \, e^{-2\pi x^2} e^{-\pi t^2/2}$, and the Fourier transform of $e^{-\pi t^2/2}$ is $\sqrt2 \, e^{-2\pi \omega^2}$.
So $Wf(x, \omega) = 2 e^{-2\pi (x^2 + \omega^2)}$, and integrating in $\omega$ gives $\sqrt2 e^{-2\pi x^2} = \abs{f(x)}^2$.

Non-example: the Wigner distribution is quadratic in $f$, not linear.
For instance $W(2f) = 4 Wf \ne 2 Wf$ when $f \ne 0$.
