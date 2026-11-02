---
tag: ZN4NMX1DB4
kind: statement
role: theorem
name: Ramanujan's master theorem
msc: [44A15, 33B15]
uses: [N5PVGRJE1T, 0H5SYBSED9, 0NAHXR1FRH, 0M3YQJ81NB]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan%27s_master_theorem
same_as:
  wikidata: Q7288993
  wikipedia: Ramanujan's master theorem
---

## Statement

Let $0 < \delta < 1$, and let $C > 0$, $P \in \R$ and $0 \le A < \pi$.
Let $\varphi$ be a [[holomorphic|0NAHXR1FRH]] function on an open set containing the closed half-plane $H = \set{v + iw : v \ge -\delta}$, such that
$$\abs{\varphi(v + iw)} \le C e^{P v + A \abs{w}} \qquad \text{for all } v + iw \in H.$$
Then the series $f(x) = \sum_{k=0}^{\infty} \varphi(k) (-x)^k$ converges for $0 < x < e^{-P}$, and $f$ has an [[analytic continuation|0M3YQJ81NB]] along $(0, \infty)$.
For every $s \in \C$ with $0 < \operatorname{Re} s < \delta$, the [[Mellin transform|N5PVGRJE1T]] of this continuation converges and
$$\int_0^\infty x^{s-1} f(x) \, dx = \frac{\pi}{\sin(\pi s)} \, \varphi(-s).$$

## Remarks

This is the form of the theorem proved by G. H. Hardy.
The idea is to write $f$ as a Mellin–Barnes integral: by the residue theorem, $f(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \frac{\pi}{\sin(\pi s)} \varphi(-s) x^{-s} \, ds$ for $0 < c < \delta$, since $\pi / \sin(\pi s)$ has residue $(-1)^k$ at $s = -k$.
The growth bound with $A < \pi$ beats the decay $e^{-\pi \abs{w}}$ of $1/\sin(\pi s)$ and makes the integral converge; Mellin inversion then gives the formula.
Writing $\varphi(k) = \lambda(k) / \Gamma(k + 1)$ and using $\Gamma(s)\Gamma(1 - s) = \pi / \sin(\pi s)$ gives the classical form: if $f(x) = \sum_{k \ge 0} \lambda(k) (-x)^k / k!$, then $\int_0^\infty x^{s-1} f(x) \, dx = \Gamma(s) \lambda(-s)$, under the corresponding conditions on $\lambda$.
Example: $\varphi = 1$ gives $f(x) = 1/(1 + x)$ and $\int_0^\infty x^{s-1}/(1 + x) \, dx = \pi / \sin(\pi s)$ for $0 < \operatorname{Re} s < 1$.
Example: $\lambda = 1$ gives $f(x) = e^{-x}$ and the formula $\int_0^\infty x^{s-1} e^{-x} \, dx = \Gamma(s)$.
The growth condition is needed: $\varphi(z) = \sin(\pi z)$ vanishes at all integers, so $f = 0$, but $\varphi(-s) \ne 0$ for non-integer $s$; here $A = \pi$ and the bound with $A < \pi$ fails.

## Explanations

### L1 human

The theorem computes the Mellin transform of a function from the coefficients of its power series.
If the $k$-th coefficient is $\varphi(k)$ times $(-1)^k$, then the transform is essentially $\varphi$ evaluated at $-s$.
So a formula valid for the whole numbers $k = 0, 1, 2, \dots$ is pushed to negative and complex values.
Ramanujan used it, without a full proof, to evaluate a great many definite integrals.

### L2 human

The growth conditions make the passage from integers to all complex numbers legitimate.
By Carlson's theorem, a function of this type is determined by its values at the non-negative integers.
The proof is an instance of the general Mellin method.
A Mellin–Barnes integral, shifted to the left, gives the power series at $0$, and its inverse transform is the right side.
The theorem yields at once the Mellin transforms of the binomial series $(1 + x)^{-a}$, of Bessel functions and of many hypergeometric functions.
