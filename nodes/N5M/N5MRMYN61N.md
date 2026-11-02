---
tag: N5MRMYN61N
kind: definition
name: Elliptic hypergeometric series
msc: [33D15, "33E05"]
defines: FQYSKP388T
uses: [FF9ZPCZ59K, Y1X8ZZQ7VM, EB4N9RQR51]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_hypergeometric_series
---

## Definition

Let $\sum_{n \ge 0} c_n$ be a series of nonzero complex numbers.
View the term ratio $c_{n+1} / c_n$ as a function of $n$ extended to complex values.
The series is an *elliptic hypergeometric series* if this ratio is an [[elliptic function|FF9ZPCZ59K]] of $n$.

In the usual explicit form, fix complex numbers $p, q$ with $\abs{p} < 1$ and $q \ne 0$.
The *modified theta function* is $\theta(x; p) = (x; p)_\infty \, (p/x; p)_\infty$ for $x \ne 0$, where $(\cdot\,; p)_\infty$ is the infinite [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
The *elliptic shifted factorial* is $(a; q, p)_n = \prod_{k=0}^{n-1} \theta(a q^k; p)$.
For nonzero parameters $a_1, \ldots, a_{r+1}$, $b_1, \ldots, b_r$ and $z$, the series
$${}_{r+1}E_r(a_1, \ldots, a_{r+1}; b_1, \ldots, b_r; q, p; z) = \sum_{n \ge 0} \frac{(a_1; q, p)_n \cdots (a_{r+1}; q, p)_n}{(q; q, p)_n \, (b_1; q, p)_n \cdots (b_r; q, p)_n} z^n$$
is an elliptic hypergeometric series when the balancing condition $a_1 a_2 \cdots a_{r+1} = q \, b_1 b_2 \cdots b_r$ holds.

## Remarks

Why the balancing condition: write $q = e^{2\pi i \sigma}$ and $p = e^{2\pi i \tau}$, and view the term ratio as a function of a complex variable $n$.
The shift $n \mapsto n + 1/\sigma$ leaves $q^n$ unchanged.
The shift $n \mapsto n + \tau/\sigma$ replaces $q^n$ by $p q^n$, and the rule $\theta(px; p) = -x^{-1}\theta(x; p)$ shows that it multiplies the ratio by $q b_1 \cdots b_r / (a_1 \cdots a_{r+1})$.
So the ratio is elliptic with periods $1/\sigma$ and $\tau/\sigma$ exactly when this factor is $1$.

Example: for $p = 0$ one has $\theta(x; 0) = 1 - x$ and $(a; q, 0)_n = (a; q)_n$, so the series becomes the [[basic hypergeometric series|EB4N9RQR51]] ${}_{r+1}\phi_r$ with the same parameters.

Non-example: $\sum_n n! \, z^n$ has term ratio $(n + 1) z$, a nonconstant polynomial in the complex variable $n$.
A nonconstant elliptic function must have poles, so the series is not elliptic hypergeometric.
