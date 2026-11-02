---
tag: 9C4MPVMTA7
kind: statement
role: theorem
name: Edgeworth expansion
msc: ["62E20", "60F05"]
uses: [0EPZC4Z1FC, 0AJN7WHBJZ, 07RXBVTVZB, 0ZT24EC90K, 0JDAQHWA9N]
about: [0EPZC4Z1FC]
sources:
  - url: https://en.wikipedia.org/wiki/Edgeworth_series
---

## Statement

Let $X_1, X_2, \dots$ be [[independent and identically distributed|0AJN7WHBJZ]] real random variables with mean $\mu$, variance $\sigma^2 > 0$ and $E\abs{X_1}^3 < \infty$.
Let $\mu_3 = E\big((X_1 - \mu)^3\big)$ be the third [[central moment|0ZT24EC90K]].
Assume that the distribution of $X_1$ is not a lattice distribution.
That is, it is not concentrated on a set of the form $\set{a + kh : k \in \Z}$ with $h > 0$.
Let $F_n$ be the distribution function of $S_n = \big(\sum_{i=1}^n X_i - n\mu\big)/(\sigma\sqrt{n})$, and let $\Phi$ and $\varphi$ be the distribution function and the density of the standard [[normal distribution|07RXBVTVZB]].
Then
$$F_n(x) = \Phi(x) - \frac{\mu_3}{6 \sigma^3 \sqrt{n}} (x^2 - 1)\, \varphi(x) + o\!\left(\frac{1}{\sqrt{n}}\right)$$
uniformly in $x \in \R$.

## Remarks

The proof compares characteristic functions.
The characteristic function of $S_n$ is $e^{-t^2/2}\big(1 + \frac{\mu_3}{6\sigma^3\sqrt{n}}(it)^3\big) + o(n^{-1/2})$ for $t$ in ranges of order $\sqrt{n}$, and the correction term is the Fourier transform of the correction in the statement.
A smoothing inequality turns closeness of characteristic functions into closeness of distribution functions; the non-lattice hypothesis controls the characteristic function away from $0$.

The [[central limit theorem|0EPZC4Z1FC]] says $F_n(x) \to \Phi(x)$; the expansion gives the first correction, of order $1/\sqrt{n}$, which comes from skewness.
For a symmetric distribution, $\mu_3 = 0$ and the error of the normal approximation is $o(1/\sqrt{n})$.
Under stronger moment conditions and Cramér's condition $\limsup_{\abs{t} \to \infty} \abs{E e^{itX_1}} < 1$, one gets further terms in powers of $1/\sqrt{n}$ with Hermite polynomials and higher cumulants.

The non-lattice hypothesis cannot be dropped.
For Bernoulli($1/2$) variables, $F_n$ has jumps of size of order $1/\sqrt{n}$, while the right side is continuous in $x$, so the error cannot be $o(1/\sqrt{n})$ uniformly.

## Explanations

### L1 human

The central limit theorem says that a standardized sum is approximately normal.
The Edgeworth expansion says how the first error looks.
If the summands are skewed, the distribution of the sum is a little skewed too, by an amount that shrinks like $1/\sqrt{n}$.
The formula gives the shape of this correction.

### L2 human

The Berry–Esseen theorem bounds the error of the normal approximation by $C\, E\abs{X_1 - \mu}^3/(\sigma^3\sqrt{n})$; the Edgeworth expansion identifies the leading term of that error.
Expansions of this kind explain why the bootstrap is often more accurate than the normal approximation for studentized statistics.
They also give corrected quantiles, through the Cornish–Fisher expansion, and corrected confidence intervals.
