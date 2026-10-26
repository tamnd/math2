---
tag: 08YERZDM9X
kind: statement
role: theorem
name: Subfields of a finite field
msc: ["12E20"]
uses: [08RTDHX1SK, 0A7KJ68XHT, 0QWR8WTZEW, 07QY5RPFBR]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Statement

Let $p$ be a prime number and let $n \ge 1$.
For each divisor $m$ of $n$, the field $\mathbb{F}_{p^n}$ has exactly one [[subfield|07QY5RPFBR]] of order $p^m$, namely $\{ a : a^{p^m} = a \}$.
It has no other subfields.

## Remarks

If $K$ is a subfield of $\mathbb{F}_{p^n}$ of order $p^m$, then $n = m \cdot [\mathbb{F}_{p^n} : K]$ by the [[tower law|0A7KJ68XHT]], so $m$ divides $n$.
For example, the subfields of $\mathbb{F}_{64} = \mathbb{F}_{2^6}$ are $\mathbb{F}_2$, $\mathbb{F}_4$, $\mathbb{F}_8$ and $\mathbb{F}_{64}$.
The subfield of order $p^m$ is the fixed field of $\varphi^m$, where $\varphi$ is the [[Frobenius automorphism|0VP4TBVJ19]].

## Explanations

### L1 human

The subfields of a finite field match the divisors of the exponent.
The field with $2^6$ elements contains the fields with $2^1$, $2^2$ and $2^3$ elements, but not one with $2^4$ elements.
