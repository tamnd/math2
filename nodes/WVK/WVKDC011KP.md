---
tag: WVKDC011KP
kind: statement
role: theorem
name: Riemann–Lebesgue lemma
msc: [42A38, 42B10, 42A16]
uses: [X7GTF3D98F, DWJF7ABPR1, 2Z2QVWZ262]
about: [X7GTF3D98F]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Lebesgue_lemma
same_as:
  wikidata: Q9363284
  wikipedia: Riemann–Lebesgue lemma
---

## Statement

Let $n \ge 1$ and let $f \colon \R^n \to \C$ be [[integrable|X7GTF3D98F]] for [[Lebesgue measure|2Z2QVWZ262]].
For $\xi \in \R^n$ let
$$\hat{f}(\xi) = \int_{\R^n} f(x) \, e^{-2 \pi i \, x \cdot \xi} \, dx,$$
a [[Lebesgue integral|DWJF7ABPR1]], where $x \cdot \xi$ is the dot product.
Then $\hat{f}(\xi) \to 0$ as $\abs{\xi} \to \infty$.

## Remarks

Proof idea: for the indicator function of a box, $\hat{f}$ is a product of terms like $(e^{-2\pi i b \xi_k} - e^{-2\pi i a \xi_k}) / (-2\pi i \xi_k)$, which tends to $0$.
Linear combinations of such indicators, the step functions, are dense in $L^1(\R^n)$.
Since $\abs{\hat{f}(\xi) - \hat{g}(\xi)} \le \int \abs{f - g}$ for every $\xi$, the property passes to all integrable $f$.

Example: for $f = \mathbf{1}_{[-1/2, 1/2]}$ on $\R$, $\hat{f}(\xi) = \sin(\pi \xi) / (\pi \xi)$ for $\xi \ne 0$, which tends to $0$.

The same proof gives the version for Fourier coefficients.
If $f$ is integrable on $[0, 2\pi]$, then $\int_0^{2\pi} f(x) e^{-ikx} \, dx \to 0$ as $\abs{k} \to \infty$ over the integers.
The lemma gives no rate of decay in general.

## Explanations

### L1 human

Multiplying a function by a fast oscillating wave and integrating gives almost complete cancellation.
The positive and negative parts of the wave nearly balance on each small piece where the function is almost constant.
So the Fourier transform of an integrable function becomes small at high frequencies.

### L2 human

The lemma says that the Fourier transform maps $L^1(\R^n)$ into the space $C_0(\R^n)$ of continuous functions vanishing at infinity.
In Fourier series it is a first step in the study of pointwise convergence, through the Dini and Jordan criteria.
The image of $L^1$ is a proper subset of $C_0$, so the decay at infinity alone does not characterise Fourier transforms of integrable functions.
