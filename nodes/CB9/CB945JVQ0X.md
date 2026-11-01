---
tag: CB945JVQ0X
kind: definition
name: q-derivative
msc: [05A30, 39A13]
defines: PMJT3FZE0Y
uses: [0V1EJCT8G6, AZBDB5F4M4, GFSDMJHHVA]
sources:
  - url: https://en.wikipedia.org/wiki/Q-derivative
---

## Definition

Let $q$ be a real number with $q \ne 0$ and $q \ne 1$.
Let $A \subseteq \R$ be a set with $qx \in A$ for every $x \in A$, and let $f \colon A \to \R$.
For $x \in A$ with $x \ne 0$, the *$q$-derivative* of $f$ at $x$ is
$$D_q f(x) = \frac{f(qx) - f(x)}{(q - 1) x}.$$
If $0 \in A$, one sets $D_q f(0) = f'(0)$ when the ordinary [[derivative|0V1EJCT8G6]] $f'(0)$ exists.

## Remarks

It is a [[difference quotient|AZBDB5F4M4]] of $f$ between $x$ and $qx$.
Example: for an integer $n \ge 1$ and $f(x) = x^n$ on $\R$, one gets $D_q x^n = \frac{q^n - 1}{q - 1} x^{n-1} = [n]_q \, x^{n-1}$, where $[n]_q = 1 + q + \cdots + q^{n-1}$ is the $q$-analog of $n$.
As $q \to 1$, $[n]_q \to n$, and more generally $D_q f(x) \to f'(x)$ at each $x \ne 0$ where $f$ is differentiable.
Non-example: with $q = 2$ and $f$ defined only on $A = [1, 2]$, the point $qx$ lies outside $A$ for $x > 1$, so $D_2 f(x)$ is not defined there.
The operator is linear and satisfies the product rule $D_q (fg)(x) = f(qx) \, D_q g(x) + g(x) \, D_q f(x)$.
