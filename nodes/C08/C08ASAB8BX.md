---
tag: C08ASAB8BX
kind: definition
name: q-exponential
msc: [05A30, 33D15]
defines: T8QYJCS3JA
uses: [GFSDMJHHVA, 0MZB06ST2B, Y1X8ZZQ7VM]
sources:
  - url: https://en.wikipedia.org/wiki/Q-exponential
---

## Definition

Let $q \in \C$ with $0 < \abs{q} < 1$, and let $[n]_q! = \prod_{k=1}^{n} \frac{1 - q^k}{1 - q}$ be the $q$-factorial, a [[q-analog|GFSDMJHHVA]] of $n!$.
The *$q$-exponential* is the [[power series|0MZB06ST2B]]
$$e_q(z) = \sum_{n=0}^{\infty} \frac{z^n}{[n]_q!},$$
for $z \in \C$ with $\abs{z} < \frac{1}{\abs{1 - q}}$.
The second $q$-exponential is
$$E_q(z) = \sum_{n=0}^{\infty} \frac{q^{\binom{n}{2}} z^n}{[n]_q!}, \qquad z \in \C.$$

## Remarks

Since $\frac{z^n}{[n]_q!} = \frac{((1 - q) z)^n}{(q; q)_n}$, the [[q-binomial theorem|VVT27RB46B]] gives the products $e_q(z) = \frac{1}{((1 - q) z; q)_\infty}$ and $E_q(z) = (-(1 - q) z; q)_\infty$, with the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].
The ratio test gives the radius of convergence $\frac{1}{\abs{1-q}}$ of $e_q$, since $[n+1]_q \to \frac{1}{1 - q}$.
With $D_q f(z) = \frac{f(qz) - f(z)}{(q - 1) z}$, one has $D_q z^n = [n]_q z^{n-1}$, hence $D_q e_q(z) = e_q(z)$.

Example: the products show $e_q(z) E_q(-z) = \frac{((1-q)z; q)_\infty}{((1-q)z; q)_\infty} = 1$.
Check on the first terms: $e_q(z) E_q(-z) = (1 + z + \cdots)(1 - z + \cdots) = 1 + 0 \cdot z + \cdots$.

Non-example: $e_q(x) e_q(y) \ne e_q(x + y)$ in general.
The coefficient of $xy$ is $1$ on the left, and on the right it is $\frac{2}{[2]_q} = \frac{2}{1 + q}$, which differs from $1$ for $q \ne 1$.

Some authors use $\sum_n z^n / (q; q)_n$ instead, which is $e_q\left(\frac{z}{1-q}\right)$.
