---
tag: 23G7N7WZBH
kind: definition
name: Primitive polynomial over a finite field
msc: [11T06, "12E20"]
defines: HQ7KMZYPSQ
uses: [08RTDHX1SK, 00X2A9G9W3, 0YAA9CJQXF, 0GK1WB9R98, 0JPYSD5E0B, 0VV04M41AN]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_polynomial_(field_theory)
---

## Definition

Let $\F_q$ be a [[finite field|08RTDHX1SK]] and let $m \ge 1$.
A polynomial $f \in \F_q[x]$ of degree $m$ is *primitive* if it is [[irreducible|00X2A9G9W3]] and has a root $\alpha$ in $\F_{q^m}$ that is a [[primitive element|0YAA9CJQXF]].
That is, $\alpha$ has multiplicative [[order|0JPYSD5E0B]] $q^m - 1$.

## Remarks

Equivalently, $f$ is a scalar multiple of the [[minimal polynomial|0GK1WB9R98]] over $\F_q$ of a primitive element of $\F_{q^m}$.
Then all roots of $f$ are primitive elements, since they are the conjugates $\alpha^{q^i}$, which have the same order as $\alpha$.
Another standard form: an irreducible $f$ of degree $m$ with $f(0) \ne 0$ is primitive if and only if the least $e \ge 1$ such that $f$ divides $x^e - 1$ is $q^m - 1$.
There are $\varphi(q^m - 1)/m$ monic primitive polynomials of degree $m$ over $\F_q$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].
Example: over $\F_2$, the polynomial $x^3 + x + 1$ is irreducible, and a root $\alpha$ has order dividing $7$ but not $1$, so its order is $7 = 2^3 - 1$, and the polynomial is primitive.
Non-example: over $\F_2$, the polynomial $x^4 + x^3 + x^2 + x + 1$ is irreducible, but it divides $x^5 - 1$, so a root has order $5$, not $15$, and the polynomial is not primitive.
