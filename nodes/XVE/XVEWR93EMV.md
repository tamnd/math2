---
tag: XVEWR93EMV
kind: definition
name: Lebesgue integral
msc: [28A25, 26A42]
defines: DWJF7ABPR1
uses: [X7GTF3D98F, DG76G5Z6XW]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_integral
---

## Definition

Let $(X, \Sigma, \mu)$ be a measure space and let $f \colon X \to \R$ be an [[integrable function|X7GTF3D98F]].
Let $f^+ = \max(f, 0)$ and $f^- = \max(-f, 0)$, so that $f = f^+ - f^-$.
The *Lebesgue integral* of $f$ is
$$\int_X f \, d\mu = \int_X f^+ \, d\mu - \int_X f^- \, d\mu,$$
where both terms are [[integrals of non-negative functions|DG76G5Z6XW]] and are finite.
For an integrable $f \colon X \to \C$, the integral is $\int_X f \, d\mu = \int_X \operatorname{Re} f \, d\mu + i \int_X \operatorname{Im} f \, d\mu$.

## Remarks

Example: on $[-1, 1]$ with Lebesgue measure, let $f(x) = x$.
Then $f^+ = x \mathbf{1}_{[0, 1]}$ and $f^- = -x \mathbf{1}_{[-1, 0]}$ both have integral $1/2$, so $\int f = 0$.

Non-example: $g(x) = x$ on all of $\R$ is not integrable.
Both $\int g^+$ and $\int g^-$ are infinite, so the difference $\infty - \infty$ has no meaning.

The same formula is used when only one of $\int f^+$ and $\int f^-$ is finite, with value $\pm \infty$.
The integral is linear and monotone on integrable functions, and it satisfies $\abs{\int_X f \, d\mu} \le \int_X \abs{f} \, d\mu$.
On a bounded interval, every Riemann integrable function is Lebesgue integrable and the two integrals agree.
Common notations are $\int f \, d\mu$, $\int f(x) \, d\mu(x)$ and $\int f(x) \, \mu(dx)$.
