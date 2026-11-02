---
tag: JEQVZXHE6A
kind: statement
role: theorem
name: Newman's theorem on rational approximation of the absolute value
msc: [41A20, 41A25]
uses: [EHFQK1WXKS, 0FFXKTKKQC, 0WCZH4AFMT]
about: [EHFQK1WXKS]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_function
---

## Statement

Let $n \ge 5$ be an integer, let $\xi = e^{-1/\sqrt{n}}$, and let
$$p(x) = \prod_{k=0}^{n-1} (x + \xi^k), \qquad r(x) = x \, \frac{p(x) - p(-x)}{p(x) + p(-x)}.$$
Then $r$ is a [[rational function|0WCZH4AFMT]] whose numerator and denominator have degree at most $n + 1$, its denominator has no zero on $[-1, 1]$, and
$$\max_{-1 \le x \le 1} \big| \abs{x} - r(x) \big| \le 3 e^{-\sqrt{n}}.$$

## Remarks

For $0 \le x \le 1$ one has $p(x) > 0$ and $\abs{p(-x)} \le p(x)$, so the denominator is positive there, and by evenness on all of $[-1, 1]$.
Then $x - r(x) = 2x\, \frac{p(-x)}{p(x) + p(-x)}$, and the proof bounds the ratio $\abs{p(-x)/p(x)} = \prod_k \abs{\xi^k - x}/(\xi^k + x)$ separately for $x$ near $0$ and for $x$ in $[\xi^n, 1]$, where some factor $\abs{\xi^k - x}/(\xi^k + x)$ is small.
Newman also showed a lower bound of the form $e^{-c\sqrt{n}}$ for every rational approximation of type $(n, n)$, so the rate $e^{-c\sqrt{n}}$ is the true order.
By contrast, the best uniform approximation of $\abs{x}$ on $[-1, 1]$ by polynomials of degree $n$ has error of order $1/n$, a result of S. N. Bernstein.
Herbert Stahl later found the exact asymptotics of the best rational error, $8 e^{-\pi \sqrt{n}}$.
Example: for $n = 100$ the bound is $3 e^{-10} \approx 1.4 \cdot 10^{-4}$, while the best polynomial approximation of degree $100$ has error about $2.8 \cdot 10^{-3}$, roughly $0.28/n$.

## Explanations

### L1 human

The function $\abs{x}$ has a corner at $0$, and polynomials, which are smooth, approximate it poorly near the corner.
Donald J. Newman showed in 1964 that quotients of polynomials do much better, with an error that shrinks like $e^{-\sqrt{n}}$ instead of like $1/n$.
The trick uses the points $\xi^k = e^{-k/\sqrt{n}}$, which crowd geometrically toward the corner at $0$.

### L2 human

This theorem started the modern study of [[rational approximation|EHFQK1WXKS]] of nonsmooth functions.
It shows that rational functions are far stronger than polynomials near singularities, which is why rational methods are used for functions with corners, branch points and boundary layers.
The geometric clustering of poles near the singularity reappears in many later constructions, for example in rational methods for problems on domains with corners.
