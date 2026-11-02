---
tag: DBEGF38V9H
kind: statement
role: theorem
name: Karamata's Tauberian theorem
msc: ["40E05", "44A10", "26A12"]
uses: [D6XWK1NRY1, EHJ7D5CRZS, 0WFF6AZPBP, 8NMH42GJRK, 0V3FZMVB4K, 0QR92XBV6H]
about: [D6XWK1NRY1, EHJ7D5CRZS]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy–Littlewood_Tauberian_theorem
---

## Statement

Let $U \colon \R \to \R$ be a nondecreasing, right-continuous [[monotone function|0WFF6AZPBP]] with $U(x) = 0$ for $x < 0$.
Assume that its Laplace–Stieltjes transform
$$\widehat{U}(s) = \int_{[0, \infty)} e^{-sx} \, dU(x),$$
a [[Riemann–Stieltjes integral|8NMH42GJRK]] over $[0, \infty)$ that includes a possible jump of $U$ at $0$, is finite for every $s > 0$.
Let $\rho \ge 0$ and $c > 0$ be real numbers, let $L$ be a [[slowly varying function|EHJ7D5CRZS]], and let $\Gamma$ be the [[gamma function|0V3FZMVB4K]].
Then the following are equivalent:

1. $\widehat{U}(s) \sim c \, s^{-\rho} L(1/s)$ as $s \to 0^+$;
2. $U(x) \sim \dfrac{c}{\Gamma(1 + \rho)} \, x^{\rho} L(x)$ as $x \to \infty$.

Here $\sim$ denotes [[asymptotic equivalence|0QR92XBV6H]].

## Remarks

The direction from 2 to 1 is an Abelian statement and follows by integration by parts and standard estimates for slowly varying functions.
The direction from 1 to 2 is the Tauberian part, where monotonicity of $U$ is essential.
Karamata's proof shows that $\int_0^\infty g(e^{-sx}) \, dU(x)$ has the expected behaviour for polynomials $g$, then for the indicator function of $[e^{-1}, 1]$ by one-sided polynomial approximation, which recovers $U(1/s)$.

Example: let $a_n \ge 0$ and $U(x) = \sum_{n \le x} a_n$.
Then $\widehat{U}(s) = \sum_{n \ge 0} a_n e^{-sn}$, and the case $\rho = 1$, $c = 1$, $L = 1$ is the [[Hardy–Littlewood Tauberian theorem|N42JDBT0VA]] with $x = e^{-s}$.

Monotonicity cannot be dropped in the Tauberian direction: the counterexample to the Hardy–Littlewood theorem with $a_n = 1 + (-1)^n n$ also violates statement 2 here.

## Explanations

### L1 human

The Laplace transform turns a growing function into a function of $s$ that blows up as $s \to 0$.
Karamata's theorem says that, for a nondecreasing function, a power-law growth (up to a slowly varying factor) of one side is exactly matched by a power-law blow-up of the other.
So one can read off the growth of $U$ from its transform near $0$, and back.

### L2 human

The theorem is the standard form of Tauberian theorems for Laplace–Stieltjes transforms, and it is central in the theory of regular variation.
In probability it relates the tail of a distribution or the growth of a renewal function to the behaviour of its Laplace transform near $0$.
Its proof by polynomial approximation, through the [[Weierstrass approximation theorem|0JQE130DHW]], gave a short route to the Hardy–Littlewood theorem.
