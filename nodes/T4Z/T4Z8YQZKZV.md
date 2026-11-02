---
tag: T4Z8YQZKZV
kind: statement
role: theorem
name: Fourier inversion theorem
msc: [42B10, 42A38]
uses: [DPVM34ADZV, JB8QMT8DCH, X7GTF3D98F, RARTMA0ZEC]
about: [DPVM34ADZV, JB8QMT8DCH]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_inversion_theorem
same_as:
  wikidata: Q3984053
  wikipedia: Fourier inversion theorem
---

## Statement

Let $n \ge 1$ and let $f \colon \R^n \to \C$ be [[integrable|X7GTF3D98F]].
Let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$ be its [[Fourier transform|DPVM34ADZV]], and assume that $\hat f$ is also integrable.
Then
$$f(x) = \int_{\R^n} \hat f(\xi) \, e^{2\pi i x \cdot \xi} \, d\xi$$
for [[almost every|RARTMA0ZEC]] $x \in \R^n$, that is, $f$ equals the [[inverse Fourier transform|JB8QMT8DCH]] of $\hat f$ almost everywhere.
If moreover $f$ is continuous, the equality holds for every $x \in \R^n$.

## Remarks

Proof idea: insert the Gaussian factor $e^{-\pi \varepsilon^2 \abs{\xi}^2}$ into the inversion integral.
With this factor the double integral converges absolutely.
Since the Gaussian is its own Fourier transform, Fubini's theorem turns it into the convolution of $f$ with a Gaussian of width $\varepsilon$ and total mass $1$.
As $\varepsilon \to 0$, the left side tends to the inversion integral by dominated convergence, since $\hat f$ is integrable.
The convolutions tend to $f$ in $L^1$, and hence almost everywhere along a subsequence.

Example: $f(x) = e^{-\abs{x}}$ on $\R$ has $\hat f(\xi) = \frac{2}{1 + 4\pi^2 \xi^2}$, which is integrable.
Since $f$ is continuous, $e^{-\abs{x}} = \int_\R \frac{2 e^{2\pi i x \xi}}{1 + 4\pi^2 \xi^2} \, d\xi$ for every $x$.

The integrability of $\hat f$ is needed for the integral to make sense.
For $f = \mathbf{1}_{[-1/2, 1/2]}$, $\hat f(\xi) = \frac{\sin \pi \xi}{\pi \xi}$ is not integrable, so the theorem does not apply as stated.
Then $f$ is recovered only by the symmetric limits $\lim_{R \to \infty} \int_{-R}^{R}$, which give $f(x)$ for $\abs{x} \ne 1/2$ and $1/2$ at the jumps.
A consequence of the theorem is uniqueness: if $f$ is integrable and $\hat f = 0$, then $f = 0$ almost everywhere.

## Explanations

### L1 human

The Fourier transform breaks a function into waves of all frequencies.
The inversion theorem says that adding these waves back together gives the original function.
So no information is lost in passing to the frequency side.

### L2 human

The theorem lets one solve problems on the frequency side, where derivatives become multiplications, and then return.
It is the basis of the Fourier method for linear differential equations with constant coefficients.
On the Schwartz space the transform is a bijection and inversion holds everywhere without extra hypotheses.
The [[Plancherel theorem|HPZHRZ0502]] gives the corresponding statement in $L^2$, where the inverse transform is the adjoint of the transform.
