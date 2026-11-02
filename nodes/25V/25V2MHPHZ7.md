---
tag: 25V2MHPHZ7
kind: counterexample
name: Kolmogorov's everywhere divergent Fourier series
msc: [42A20, 42A16]
uses: [SASP14MA1Z, G12KXDHPPS, 5NN2YZZR3V, V6Q24CHJG8]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Counterexample

Let $\mathbb{T} = \R / 2\pi\Z$ and let $L^1(\mathbb{T})$ be the [[space|SASP14MA1Z]] of integrable $2\pi$-periodic functions.
For $f \in L^1(\mathbb{T})$ let $S_N f(x) = \sum_{\abs{k} \le N} \hat f(k) e^{ikx}$ be the partial sums of its [[Fourier series|G12KXDHPPS]], where $\hat f(k)$ are the [[Fourier coefficients|5NN2YZZR3V]].
Kolmogorov constructed a function $f \in L^1(\mathbb{T})$ such that the sequence $S_N f(x)$ diverges for every $x \in \R$.
So integrability alone gives no [[convergence of the Fourier series|V6Q24CHJG8]] at any point.

## Remarks

Kolmogorov first gave, in 1923, an integrable function whose Fourier series diverges almost everywhere, and in 1926 one whose Fourier series diverges everywhere.
The construction adds up a series of carefully chosen trigonometric polynomials.
Each has small $L^1$ norm, but some of its partial sums are very large on most of the circle.
The coefficients $\hat f(k)$ still tend to $0$, by the [[Riemann–Lebesgue lemma|WVKDC011KP]], so the divergence is not caused by large terms.
The example shows that [[Carleson's theorem|FBH6KG484Z]] and [[Hunt's extension|NAX51M6025]], which give convergence almost everywhere for $f \in L^p(\mathbb{T})$ with $1 < p < \infty$, have no analogue for $p = 1$.

## Explanations

### L1 human

A Fourier series tries to rebuild a periodic function from pure waves.
For square-integrable functions this works at almost every point.
Kolmogorov found an integrable function for which it fails at every single point: the partial sums never settle down anywhere.
So the right space for pointwise convergence questions is smaller than the space of all integrable functions.
