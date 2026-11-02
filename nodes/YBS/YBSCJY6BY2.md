---
tag: YBSCJY6BY2
kind: definition
name: q-gamma function
msc: ["33D05"]
defines: 68P2VKSEP5
uses: [Y1X8ZZQ7VM, 0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Q-gamma_function
---

## Definition

Let $0 < q < 1$, and let $(a; q)_\infty = \prod_{k=0}^\infty (1 - a q^k)$ be the infinite [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
For a real number $x$ that is not in $\set{0, -1, -2, \ldots}$, the *$q$-gamma function* is
$$\Gamma_q(x) = (1 - q)^{1 - x} \frac{(q; q)_\infty}{(q^x; q)_\infty}.$$

## Remarks

The products converge because $\sum q^k < \infty$, and $(q^x; q)_\infty \ne 0$ because $q^{x+k} \ne 1$ for all $k \ge 0$.

Example: $\Gamma_q(1) = 1$, since the two products are equal.
Also $\Gamma_q(2) = (1-q)^{-1} \frac{(q;q)_\infty}{(q^2;q)_\infty} = \frac{1 - q}{1 - q} = 1$ and $\Gamma_q(3) = \frac{(1-q)(1-q^2)}{(1-q)^2} = 1 + q$.
In general $\Gamma_q(x + 1) = [x]_q\, \Gamma_q(x)$ with $[x]_q = \frac{1 - q^x}{1 - q}$, so $\Gamma_q(n + 1) = [1]_q [2]_q \cdots [n]_q$.

Non-example of a valid argument: for $x = -1$ the factor $1 - q^{x+1}$ of $(q^x; q)_\infty$ is $0$, so $\Gamma_q$ has a pole there.

For each fixed $x$, $\Gamma_q(x) \to \Gamma(x)$ as $q \to 1^-$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
A related definition exists for $q > 1$.
