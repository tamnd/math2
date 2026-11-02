---
tag: QY8ETVDA1Z
kind: statement
role: theorem
name: Convolution theorem
msc: ["42B10", "42A85", "42A38"]
uses: [DPVM34ADZV, 2Z29JN3VES, SASP14MA1Z, 0R0T1VWH5X]
about: [DPVM34ADZV, 2Z29JN3VES]
sources:
  - url: https://en.wikipedia.org/wiki/Convolution_theorem
same_as:
  wikidata: Q2638931
  wikipedia: Convolution theorem
---

## Statement

Let $n \ge 1$ and let $f, g \in L^1(\R^n)$.
Let $f * g$ be their [[convolution|2Z29JN3VES]], $(f * g)(x) = \int_{\R^n} f(y)\, g(x - y)\, dy$.
Let $\hat h(\xi) = \int_{\R^n} h(x) e^{-2\pi i x \cdot \xi}\, dx$ denote the [[Fourier transform|DPVM34ADZV]] of $h \in L^1(\R^n)$.
Then $f * g$ lies in [[$L^1(\R^n)$|SASP14MA1Z]], and
$$\widehat{f * g}(\xi) = \hat f(\xi)\, \hat g(\xi) \quad \text{for every } \xi \in \R^n.$$

## Remarks

The proof is one application of [[Fubini's theorem|0R0T1VWH5X]].
Write $e^{-2\pi i x \cdot \xi} = e^{-2\pi i y \cdot \xi} e^{-2\pi i (x - y) \cdot \xi}$ inside the double integral of $f(y) g(x - y) e^{-2\pi i x \cdot \xi}$.
The double integral converges absolutely because $\int\int \abs{f(y)} \abs{g(x - y)}\, dy\, dx = \norm{f}_1 \norm{g}_1$.
Integrating first in $x$ and then in $y$ gives $\hat f(\xi) \hat g(\xi)$.

Example: on $\R$, let $f = g = \mathbf{1}_{[-1/2, 1/2]}$.
Then $\hat f(\xi) = \sin(\pi \xi)/(\pi \xi)$, and $f * g$ is the triangle function $\max(1 - \abs{x}, 0)$.
So the Fourier transform of the triangle function is $\sin^2(\pi \xi)/(\pi \xi)^2$.

There is a dual form: for $f, g$ in the Schwartz space, $\widehat{f g} = \hat f * \hat g$.
The same identity holds for Fourier series, where the convolution on the circle becomes the product of Fourier coefficients.

## Explanations

### L1 human

Convolution is a kind of moving weighted average of one function against another.
On the frequency side it becomes plain multiplication.
So to smooth a signal with a filter, one can multiply its spectrum by the spectrum of the filter.

### L2 human

The theorem is why the Fourier transform solves linear equations with constant coefficients: such equations are convolution equations, and the transform makes them algebraic.
It also shows that $L^1(\R^n)$ with convolution is a commutative algebra, and that $f \mapsto \hat f$ is an algebra homomorphism into bounded continuous functions with pointwise product.
Fast convolution of long sequences uses the discrete version of the theorem together with the fast Fourier transform.
