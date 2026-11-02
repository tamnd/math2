---
tag: TPJZCSXSVN
kind: statement
role: theorem
name: Fejér's theorem
msc: ["42A24", "40G05"]
uses: [G12KXDHPPS, DCCA2T9GKH, N8ZGG7EW6J, 0P0DJHBGBB, 089KWVYD69, 0P27W9RW0G, 08FPABDQ4C]
about: [G12KXDHPPS, N8ZGG7EW6J]
sources:
  - url: https://en.wikipedia.org/wiki/Fejér%27s_theorem
same_as:
  wikidata: Q571154
  wikipedia: Fejér's theorem
---

## Statement

Let $f \colon \R \to \C$ be a [[continuous|0P27W9RW0G]] [[periodic function|089KWVYD69]] with period $2\pi$.
For $n \ge 0$ let $S_n f(x) = \sum_{k=-n}^{n} c_k e^{ikx}$ be the partial sums of its [[Fourier series|G12KXDHPPS]], where $c_k = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(t) e^{-ikt} \, dt$.
For $N \ge 1$ let
$$\sigma_N f(x) = \frac{1}{N} \sum_{n=0}^{N-1} S_n f(x)$$
be their [[Cesàro means|0P0DJHBGBB]].
Then $\sigma_N f \to f$ [[uniformly|08FPABDQ4C]] on $\R$ as $N \to \infty$.

## Remarks

The proof writes $\sigma_N f(x) = \frac{1}{2\pi} \int_{-\pi}^{\pi} F_N(t) f(x - t) \, dt$ with the [[Fejér kernel|DCCA2T9GKH]] $F_N$.
Since $F_N \ge 0$ and $F_N$ has mean $1$, the error $\sigma_N f(x) - f(x)$ is a weighted average of $f(x - t) - f(x)$.
For small $\abs{t}$ this is small by uniform continuity of $f$, and for $\abs{t} \ge \delta$ the weight $F_N(t)$ is uniformly small for large $N$.

Example: the theorem shows that trigonometric polynomials are uniformly dense in the continuous $2\pi$-periodic functions, since each $\sigma_N f$ is one.
It also shows that two continuous periodic functions with the same Fourier coefficients are equal.

Continuity is needed for uniform convergence: each $\sigma_N f$ is continuous, so a uniform limit of them is continuous, and a function with a jump cannot be such a limit.
The theorem cannot be improved to the partial sums $S_n f$ themselves: there are continuous periodic functions whose Fourier series diverges at a point.

## Explanations

### L1 human

The Fourier series of a continuous periodic function may fail to converge.
Fejér's theorem says that averaging its partial sums always repairs this: the averages converge to the function, evenly over the whole line.
So a continuous periodic function is always recovered from its Fourier coefficients, by Cesàro summation of the series.

### L2 human

Fejér's theorem is the model case of summability methods applied to Fourier series.
Its proof uses only three properties of the Fejér kernel: positivity, unit mean and concentration at $0$.
Any kernel with these properties gives a similar theorem, such as [[Abel–Poisson summation|RZZ78GXP5F]] with the Poisson kernel.
Versions for integrable functions say that $\sigma_N f \to f$ in mean and at every point of continuity.
