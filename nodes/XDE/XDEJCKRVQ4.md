---
tag: XDEJCKRVQ4
kind: statement
role: theorem
name: Fubini's theorem on differentiation
msc: [26A24, 26A48]
uses: [0WFF6AZPBP, 0F1WR9C83K]
about: [0WFF6AZPBP]
sources:
  - url: https://en.wikipedia.org/wiki/Fubini%27s_theorem_on_differentiation
same_as:
  wikidata: Q1841237
  wikipedia: Fubini's theorem on differentiation
---

## Statement

Let $a < b$ be real numbers and let $f_n \colon [a, b] \to \R$, for $n \ge 1$, be nondecreasing functions.
Assume that the series $F(x) = \sum_{n=1}^{\infty} f_n(x)$ converges for every $x \in [a, b]$.
Then for almost every $x \in [a, b]$, with respect to Lebesgue measure, the [[derivatives|0F1WR9C83K]] $F'(x)$ and $f_n'(x)$ exist for all $n$, and
$$F'(x) = \sum_{n=1}^{\infty} f_n'(x).$$

## Remarks

Replacing $f_n$ by $f_n - f_n(a)$ changes nothing, so one may assume $f_n \ge 0$.
By [[Lebesgue's theorem|1Y4N1DDQNR]], $F$ and all $f_n$ are differentiable almost everywhere.
Since $F$ minus a partial sum is nondecreasing, the partial sums of $\sum f_n'$ are bounded by $F'$ almost everywhere, so the series of derivatives converges.
Choosing partial sums $S_{n_k}$ with $F(b) - S_{n_k}(b) < 2^{-k}$ and applying the same argument to $\sum_k (F - S_{n_k})$ shows that the terms $F' - S_{n_k}'$ tend to $0$ almost everywhere.
Monotonicity is essential: take $f_1(x) = \sin x$ and $f_n(x) = \sin(n^2 x)/n^2 - \sin((n-1)^2 x)/(n-1)^2$ for $n \ge 2$; the partial sums $\sin(n^2 x)/n^2$ converge uniformly to $0$, but their derivatives $\cos(n^2 x)$ do not converge to $0$.

## Explanations

### L1 human

A convergent series of increasing functions can be differentiated term by term, except on a set of length zero.
No uniform convergence and no smoothness is needed, only that each term is increasing.

### L2 human

The theorem is a tool in the theory of monotone functions and functions of [[bounded variation|A8251BHCMP]].
It shows, for example, that a jump function, a convergent sum of step functions, has derivative $0$ almost everywhere.
It contrasts with the classical termwise differentiation theorem, which asks for uniform convergence of the derivatives.
