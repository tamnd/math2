---
tag: EQ23YX9CFG
kind: definition
name: Superharmonic potential
msc: [31B05, 31B15]
defines: AQ5RN6FFT0
uses: [X4V2S56YQQ, G0H97JZRS9, 0DEB0JMN0W, 02BH3MCBQB, CBZ20SS8RQ, 0HYPR64JM2]
sources:
  - url: https://en.wikipedia.org/wiki/Subharmonic_function
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a connected [[open set|02BH3MCBQB]].
A *potential* on $\Omega$ is a function $u$ on $\Omega$ such that:

1. $u$ is [[superharmonic|X4V2S56YQQ]] on $\Omega$.
2. $u \ge 0$ on $\Omega$.
3. The greatest harmonic minorant of $u$ is $0$; equivalently, every [[harmonic function|0DEB0JMN0W]] $h$ on $\Omega$ with $h \le u$ satisfies $h \le 0$.

## Remarks

Since $u \ge 0$, the function $0$ is a harmonic minorant, so the greatest harmonic minorant exists; it is $-h_0$, where $h_0$ is the [[least harmonic majorant|G0H97JZRS9]] of $-u$.
Let $\Omega$ have a Green function $G$.
Then the [[Riesz decomposition theorem|CBZ20SS8RQ]] shows that the potentials are exactly the functions $x \mapsto \int G(x, y)\, d\mu(y)$.
Here $\mu$ runs over the positive measures for which this function is not identically $+\infty$.
Every nonnegative superharmonic function is uniquely the sum of a potential and a nonnegative harmonic function.

Example: for $n \ge 3$ let $u(x) = \abs{x}^{2-n}$ on $\Omega = \R^n$, with $u(0) = +\infty$.
It is superharmonic and positive.
Let $h$ be harmonic with $h \le u$, and fix $a$.
By the [[mean value property|0HYPR64JM2]], $h(a)$ is the mean of $h$ over the sphere $S(a, R)$, which is at most the mean of $u$ there, namely $\max(\abs{a}, R)^{2-n}$.
Letting $R \to \infty$ gives $h(a) \le 0$, so $u$ is a potential.

Non-example: on a bounded domain the constant $u = 1$ is superharmonic and nonnegative, but $h = 1$ is a harmonic minorant with $h > 0$, so clause 3 fails.
