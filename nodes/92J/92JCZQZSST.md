---
tag: 92JCZQZSST
kind: definition
name: Finite field arithmetic
msc: ["12E20", 11T71, "12-08"]
defines: YG3HWE6GEX
uses: [08RTDHX1SK, 00X2A9G9W3, 0Q9EZS90GY, 0VFW4Y69BT, 0DPF6WRZW6, D6D0SR1FK3, 0TRNT4X7J0]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field_arithmetic
---

## Definition

Let $p$ be a prime, let $n \ge 1$, and let $f \in \F_p[x]$ be a monic [[irreducible polynomial|00X2A9G9W3]] of [[degree|0DPF6WRZW6]] $n$.
The [[quotient ring|0VFW4Y69BT]] $\F_p[x]/(f)$ of the [[polynomial ring|0Q9EZS90GY]] is a [[finite field|08RTDHX1SK]] with $p^n$ elements.
*Finite field arithmetic* in this representation computes with the polynomials $a(x)$ of degree less than $n$ over $\F_p$, one for each element, as follows.

1. The sum $a + b$ is the coefficientwise sum modulo $p$.
2. The product $a \cdot b$ is the remainder of the polynomial product $a(x) b(x)$ under [[division|D6D0SR1FK3]] by $f$.
3. The inverse of $a \ne 0$ is the polynomial $u$ of degree less than $n$ with $u a + v f = 1$ for some $v \in \F_p[x]$, found by the extended [[Euclidean algorithm|0TRNT4X7J0]].

## Remarks

Take $p = 2$ and $f = x^3 + x + 1$, which has no root in $\F_2$ and so is irreducible.
Then $(x^2 + 1)(x + 1) = x^3 + x^2 + x + 1$, and its remainder modulo $f$ is $x^2$.
The inverse of $x$ is $x^2 + 1$, since $x(x^2 + 1) = x^3 + x = f + 1$.
The polynomial $x^2 + 1$ over $\F_2$ cannot serve as $f$, since $x^2 + 1 = (x + 1)^2$, and then $x + 1$ has no inverse.
Over $\F_2$, an element is stored as the bit string of its coefficients, and addition is the bitwise exclusive or.
The inverse can also be computed as $a^{p^n - 2}$, since $a^{p^n - 1} = 1$ for $a \ne 0$.
