---
tag: NSS3XW4BYZ
kind: statement
role: theorem
name: Cantor's uniqueness theorem for trigonometric series
msc: [42A63, 42A20]
uses: [FZK2M8KGXQ, 8Z55VMJSEX]
about: [FZK2M8KGXQ, K7CNWXF9SN]
sources:
  - url: https://en.wikipedia.org/wiki/Set_of_uniqueness
---

## Statement

Let $(c_n)_{n \in \Z}$ be complex numbers, and consider the [[trigonometric series|FZK2M8KGXQ]] $\sum_{n \in \Z} c_n e^{inx}$.
Assume that for every $x \in \R$ its symmetric partial sums converge to $0$:
$$\lim_{N \to \infty} \sum_{n=-N}^{N} c_n e^{inx} = 0.$$
Then $c_n = 0$ for every $n \in \Z$.

## Remarks

Equivalently, if two trigonometric series converge at every point to the same sum, then they have the same coefficients.
So a function has at most one representation by an everywhere convergent trigonometric series.

Proof idea, following Riemann's method.
First, the terms $c_n e^{inx} + c_{-n} e^{-inx}$ tend to $0$ for every $x$, so $c_n \to 0$ as $\abs{n} \to \infty$ by the [[Cantor–Lebesgue theorem|8Z55VMJSEX]].
Then the function $F(x) = \frac{c_0 x^2}{2} - \sum_{n \ne 0} \frac{c_n}{n^2} e^{inx}$ is continuous, and Riemann's first lemma shows that its second symmetric derivative at $x$ equals the sum of the series at $x$, which is $0$.
A lemma of Schwarz says that a continuous function with vanishing second symmetric derivative is linear, so $F(x) = ax + b$.
Comparing with the periodic part gives $c_0 = 0$, $a = 0$, and then $c_n = 0$ for all $n \ne 0$ by uniqueness of the coefficients of a uniformly convergent series.

Cantor proved the theorem in 1870 and soon allowed finitely many exceptional points.
In the language of [[sets of uniqueness|K7CNWXF9SN]], the theorem says that the empty set is a set of uniqueness.
The hypothesis of convergence at all points cannot be replaced by convergence almost everywhere.
Menshov constructed a nonzero trigonometric series that converges to $0$ outside a closed set of measure zero.

## Explanations

### L1 human

If a sum of waves is equal to $0$ at every point, every single wave in it must be $0$.
For finite sums this is easy linear algebra, but for infinite sums that only converge, it is a deep fact.
It means that a function can be written as a convergent trigonometric series in at most one way.

### L2 human

The theorem is about arbitrary trigonometric series, not only Fourier series, so no integral formula for the coefficients is available.
Riemann's idea of integrating the series twice turns the problem into one about continuous functions.
Trying to allow larger exceptional sets, Cantor was led to derived sets, transfinite ordinals and set theory.
The modern theory of sets of uniqueness continues this question.
