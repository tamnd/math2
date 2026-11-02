---
tag: FA5V5KRWDF
kind: statement
role: theorem
name: Compactness of the spectrum
msc: [46H05, 47A10]
uses: [EH0CZ19RKP, X0243CZD9D, 0R6EWFKRCF, 4DJ4V5VBSH]
about: [EH0CZ19RKP]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
---

## Statement

Let $\mathbb{K}$ be $\R$ or $\C$, and let $A$ be a Banach algebra over $\mathbb{K}$ with unit $1$, so that $\norm{xy} \le \norm{x} \norm{y}$ for all $x, y \in A$.
Let $a \in A$.
Then the [[spectrum|EH0CZ19RKP]] $\sigma(a)$ is a [[compact subset|0R6EWFKRCF]] of $\mathbb{K}$, and $\abs{\lambda} \le \norm{a}$ for every $\lambda \in \sigma(a)$.

## Remarks

If $\abs{\lambda} > \norm{a}$, then $a - \lambda 1 = -\lambda (1 - a/\lambda)$, and the Neumann series $\sum_{n \ge 0} (a/\lambda)^n$ converges to an inverse of $1 - a/\lambda$.
So $\sigma(a)$ lies in the closed disc of radius $\norm{a}$.
If $u$ is invertible and $\norm{b} < 1/\norm{u^{-1}}$, then $u - b = u(1 - u^{-1} b)$ is invertible by the same series.
Hence the invertible elements form an open set, the [[resolvent set|X0243CZD9D]] is open, and $\sigma(a)$ is closed and bounded.

Completeness is necessary.
In the [[normed algebra|4DJ4V5VBSH]] of complex polynomials with the sup norm on $[0,1]$, only nonzero constants are invertible.
So the element $t$ has spectrum $\C$, which is not bounded.

For a complex Banach algebra the spectrum is also nonempty.
For instance, for $a \in M_n(\C)$ with the operator norm, the theorem says that every eigenvalue has modulus at most $\norm{a}$.

## Explanations

### L1 human

The numbers $\lambda$ for which $a - \lambda$ is not invertible form a closed and bounded set, and they are never larger than the size of $a$.
The reason is that $1 - x$ is invertible as soon as $x$ is small, by the geometric series $1 + x + x^2 + \cdots$.

### L2 human

This is the first basic fact of spectral theory in Banach algebras.
Together with the holomorphy of the resolvent and [[Liouville's theorem|0EHKVRF4J6]], it gives the [[nonemptiness of the spectrum|QWQC5SV0SD]] in the complex case.
It is refined by [[Gelfand's spectral radius formula|T4RFYT8HDN]], $\max \set{\abs{\lambda} : \lambda \in \sigma(a)} = \lim_n \norm{a^n}^{1/n}$, which can be smaller than $\norm{a}$.
The compactness allows the continuous functional calculus, which needs $\sigma(a)$ to be a compact space.
