---
tag: VDX0PQ2GJ4
kind: definition
name: Asymptotic analysis
msc: [41A60, "34E05"]
defines: Q26QN6GYZX
uses: [0TGV80E6A4, 00T5EPFQB9, 0QR92XBV6H]
sources:
  - url: https://en.wikipedia.org/wiki/Asymptotic_analysis
---

## Definition

Let $D \subseteq \R$ and let $x_0$ be a limit point of $D$, possibly $\pm\infty$.
A sequence of functions $\varphi_0, \varphi_1, \varphi_2, \ldots$ on $D$ is an *asymptotic sequence* as $x \to x_0$ if $\varphi_{n+1}(x) = o(\varphi_n(x))$ as $x \to x_0$ for every $n$.
Let $f$ be a function on $D$ and let $a_0, a_1, \ldots$ be numbers.
The formal series $\sum_{n \ge 0} a_n \varphi_n$ is an *asymptotic expansion* of $f$ as $x \to x_0$, written
$$f(x) \sim \sum_{n=0}^{\infty} a_n \varphi_n(x) \quad (x \to x_0),$$
if for every $N \ge 0$,
$$f(x) - \sum_{n=0}^{N} a_n \varphi_n(x) = o(\varphi_N(x)) \quad (x \to x_0).$$
*Asymptotic analysis* is the study of such expansions and of [[asymptotic equivalence|0QR92XBV6H]] $f \sim g$, meaning $f / g \to 1$.
Its estimates are written with [[big O|0TGV80E6A4]] and [[little o|00T5EPFQB9]] notation.

## Remarks

Example: $f(x) = 1 / (x - 1)$ on $(1, \infty)$ as $x \to \infty$, with $\varphi_n(x) = x^{-n-1}$.
Here $f(x) - \sum_{n=0}^{N} x^{-n-1} = x^{-N-1} / (x - 1) = o(x^{-N-1})$, so $f(x) \sim \sum_{n \ge 0} x^{-n-1}$.

A divergent example: as $x \to 0^+$, $\int_0^\infty \frac{e^{-t}}{1 + x t} \, dt \sim \sum_{n \ge 0} (-1)^n n! \, x^n$, although the series converges for no $x \neq 0$.

Non-example: $\varphi_n(x) = x^n$ is not an asymptotic sequence as $x \to \infty$, since $x^{n+1}$ is not $o(x^n)$ there; it is one as $x \to 0$.

Given the asymptotic sequence, the coefficients $a_n$ are unique.
Different functions can have the same expansion: $e^{-x}$ has all coefficients $0$ with respect to $x^{-n}$ as $x \to \infty$.

## Explanations

### L1 human

An asymptotic expansion is a list of terms of decreasing size.
Stopping after any term leaves an error smaller than the last term kept, when $x$ is close enough to the limit point.
