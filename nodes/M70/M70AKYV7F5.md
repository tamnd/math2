---
tag: M70AKYV7F5
kind: definition
name: Rate–distortion theory
msc: [94A34, 94A29]
defines: PFJER4FMJ5
uses: [00MRN0FARV, 0WQNRCNY3M, RABRP2KG81]
sources:
  - url: https://en.wikipedia.org/wiki/Rate%E2%80%93distortion_theory
---

## Definition

Let $\mathcal{X}$ and $\hat{\mathcal{X}}$ be finite [[alphabets|RABRP2KG81]], the source and reproduction alphabets.
Let $X_1, X_2, \dots$ be [[i.i.d.|00MRN0FARV]] random variables with values in $\mathcal{X}$.
Let $d \colon \mathcal{X} \times \hat{\mathcal{X}} \to [0, \infty)$ be a *distortion measure*.
For strings of length $n$, put $d(x^n, \hat{x}^n) = \frac{1}{n} \sum_{i=1}^{n} d(x_i, \hat{x}_i)$.

1. A *lossy source code* with parameters $(M, n)$ is a pair of maps $f \colon \mathcal{X}^n \to \set{1, \dots, M}$ and $g \colon \set{1, \dots, M} \to \hat{\mathcal{X}}^n$.
2. Its *distortion* is the [[expected value|0WQNRCNY3M]] $\mathbb{E}\, d\big(X^n, g(f(X^n))\big)$.
3. A pair $(R, D)$ of non-negative reals is *achievable* if there are codes with parameters $(\ceil{2^{nR}}, n)$ whose distortions $D_n$ satisfy $\limsup_{n \to \infty} D_n \le D$.

*Rate–distortion theory* studies the set of achievable pairs.
In particular it studies the *operational rate–distortion function* $D \mapsto \inf\set{R : (R, D) \text{ achievable}}$.

## Remarks

Example: let $X_i$ be uniform bits, $\hat{\mathcal{X}} = \set{0, 1}$, and let $d$ be the Hamming distortion, $d(x, \hat{x}) = 0$ if $x = \hat{x}$ and $1$ otherwise.
The pair $(1/2, 1/4)$ is achievable for even $n$.
Send the first $n/2$ bits exactly, and reproduce the other bits as $0$; half of those are wrong on average, so the distortion is $1/4$.
Non-example: $(0, 1/4)$ is not achievable for this source.
With rate $0$ the code has one reproduction string, and each source bit disagrees with it with probability $1/2$, so the distortion is $1/2$.
Shannon's rate–distortion theorem computes the operational function as a minimum of mutual information.
