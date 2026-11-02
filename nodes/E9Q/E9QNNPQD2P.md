---
tag: E9QNNPQD2P
kind: statement
role: corollary
name: Convolution ring has no zero divisors
msc: [44A40, 44A35]
uses: [FCKX8KFVGN, WGY75H4VWW, 0NNRDW10RZ, MBK7NFE74S]
about: [FCKX8KFVGN]
sources:
  - url: https://en.wikipedia.org/wiki/Titchmarsh_convolution_theorem
---

## Statement

Let $\mathcal{C}$ be the set of continuous functions $[0, \infty) \to \C$, with pointwise addition and the [[convolution on the half-line|FCKX8KFVGN]]
$$(f * g)(t) = \int_0^t f(\tau) \, g(t - \tau) \, d\tau$$
as multiplication.
Then $\mathcal{C}$ is a commutative [[rng|MBK7NFE74S]], that is, a ring that need not have a unit.
It has no [[zero divisors|0NNRDW10RZ]]: if $f, g \in \mathcal{C}$ and $f * g = 0$, then $f = 0$ or $g = 0$.

## Remarks

Commutativity and associativity follow from the corresponding facts on the line, and distributivity is linearity of the integral.
For the absence of zero divisors, suppose $f * g = 0$ and $f(t_0) \ne 0$.
By continuity $f$ is nonzero near $t_0$, so $f$ does not vanish almost everywhere on $(0, \lambda)$ for any $\lambda > t_0$.
For each $T > t_0$, the [[Titchmarsh convolution theorem|WGY75H4VWW]] then gives $g = 0$ almost everywhere on $(0, T - t_0)$; letting $T \to \infty$ and using continuity gives $g = 0$.

$\mathcal{C}$ has no unit element.
If $e * f = f$ for all $f$, then $e * 1 = 1$, but $(e * 1)(0) = 0 \ne 1$.

Example: $1 * 1 = t$ and $t * t = t^3/6$, and in general no product of nonzero polynomials in $\mathcal{C}$ is $0$, in line with the formula $t^m * t^n = \frac{m!\,n!}{(m+n+1)!} t^{m+n+1}$.

## Explanations

### L1 human

In ordinary arithmetic, a product is zero only when one factor is zero.
The same rule holds when continuous functions on $[0, \infty)$ are "multiplied" by convolution.
This is far from obvious, because convolution mixes values of the two functions in a complicated way.

### L2 human

A commutative rng without zero divisors has a field of fractions, built from pairs $f/g$ as for the rational numbers.
For $\mathcal{C}$ this is the [[Mikusiński field of operators|82YAXZMMQ1]], the setting of the Mikusiński operational calculus.
The same conclusion holds for locally integrable functions, with equality almost everywhere.
