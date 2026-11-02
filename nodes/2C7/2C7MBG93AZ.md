---
tag: 2C7MBG93AZ
kind: definition
name: Ordinal arithmetic
msc: ["03E10"]
defines: KAEDCQ8RM6
uses: [0RDJK7EQYY, 0ZHQMQ2C1N, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_arithmetic
---

## Definition

Let $\alpha$ and $\beta$ be [[ordinal numbers|0RDJK7EQYY]].
In the clauses below, $\lambda$ is a nonzero limit ordinal, and $\sup$ is the [[supremum|0BTMQ04556]] of a set of ordinals, which is its union.
The sum, product and power of ordinals are defined by [[transfinite recursion|0ZHQMQ2C1N]] on $\beta$:

1. $\alpha + 0 = \alpha$, $\alpha + (\beta + 1) = (\alpha + \beta) + 1$, and $\alpha + \lambda = \sup_{\beta < \lambda} (\alpha + \beta)$.
2. $\alpha \cdot 0 = 0$, $\alpha \cdot (\beta + 1) = \alpha \cdot \beta + \alpha$, and $\alpha \cdot \lambda = \sup_{\beta < \lambda} \alpha \cdot \beta$.
3. $\alpha^0 = 1$, $\alpha^{\beta + 1} = \alpha^\beta \cdot \alpha$, and $\alpha^\lambda = \sup_{\beta < \lambda} \alpha^\beta$ when $\alpha > 0$, with $0^\lambda = 0$.

Here $\beta + 1 = \beta \cup \set{\beta}$ is the successor of $\beta$.

## Remarks

Example: $\omega + 1$ is the successor of $\omega$, and $\omega \cdot 2 = \omega + \omega$ by clauses 2 and 1.
Non-example of commutativity: $1 + \omega = \sup_{n < \omega} (1 + n) = \omega$, while $\omega + 1 \ne \omega$.
Likewise $2 \cdot \omega = \sup_n 2n = \omega$, while $\omega \cdot 2 = \omega + \omega > \omega$.
Equivalently, $\alpha + \beta$ is the order type of $\alpha$ followed by $\beta$.
And $\alpha \cdot \beta$ is the order type of the pairs $(b, a)$ with $b < \beta$ and $a < \alpha$, compared first by $b$ and then by $a$.
Addition and multiplication are associative, and $\alpha \cdot (\beta + \gamma) = \alpha \cdot \beta + \alpha \cdot \gamma$, but the other distributive law fails.
On finite ordinals the operations agree with those of the natural numbers.
Ordinal exponentiation differs from cardinal exponentiation: $2^\omega = \omega$ as ordinals, while $2^{\aleph_0} > \aleph_0$ as cardinals.
