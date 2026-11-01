---
tag: NE75TQGG79
kind: definition
name: Incidence algebra
msc: [06A11, 16S99]
defines: 1H9SFWHYEB
uses: [0QV2JS9RJ3, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_algebra
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]] that is locally finite: for all $x \le y$ in $P$, the interval $[x, y] = \set{z \in P : x \le z \le y}$ is finite.
Let $K$ be a [[commutative ring|0310REJJY8]].
The *incidence algebra* $I(P, K)$ is the set of all functions $f \colon \set{(x, y) \in P \times P : x \le y} \to K$, with pointwise addition and multiplication by scalars, and with the product
$$(f * g)(x, y) = \sum_{z \in [x, y]} f(x, z) \, g(z, y).$$

## Remarks

The product is associative, and the function $\delta$ with $\delta(x, x) = 1$ and $\delta(x, y) = 0$ for $x < y$ is the identity.
The zeta function is $\zeta(x, y) = 1$ for all $x \le y$.
An element $f$ is invertible if and only if $f(x, x)$ is a unit of $K$ for every $x$.
The inverse of $\zeta$ is the Möbius function $\mu$ of $P$, defined by $\mu(x, x) = 1$ and $\mu(x, y) = -\sum_{x \le z < y} \mu(x, z)$ for $x < y$.

Example: let $P = \set{1, \dots, n}$ with the usual order.
Every interval is finite, and $f \mapsto (f(i, j))_{i \le j}$ identifies $I(P, K)$ with the algebra of upper triangular $n \times n$ matrices over $K$; the product $*$ becomes matrix multiplication.

Non-example: $\Q$ with its usual order is not locally finite, since $[0, 1]$ is infinite.
The sum defining $(\zeta * \zeta)(0, 1)$ would have infinitely many terms equal to $1$.
