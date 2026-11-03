---
tag: CKG9PVBTMA
kind: definition
name: Hurwitz polynomial
msc: [26C10, 93D20, 30C15]
defines: Y631JTMMT5
uses: [019MA1VTR2, 1G0B73WPX8]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz_polynomial
---

## Definition

A nonconstant [[polynomial|1G0B73WPX8]] $p$ with real or complex coefficients is a *Hurwitz polynomial* (or *stable polynomial*) if every [[root|019MA1VTR2]] $\lambda \in \C$ of $p$ satisfies $\operatorname{Re} \lambda < 0$.

## Remarks

If $p(s) = a_0 s^n + a_1 s^{n-1} + \cdots + a_n$ is a real Hurwitz polynomial with $a_0 > 0$, then all its coefficients are positive.
Indeed $p$ is $a_0$ times a product of factors $s + r$ with $r > 0$ and $s^2 + 2as + a^2 + b^2$ with $a > 0$, all with positive coefficients.
For degree $1$ and $2$ the converse holds, but not for degree $3$ and higher.

Example: $p(s) = s^2 + 3s + 2 = (s + 1)(s + 2)$ has roots $-1$ and $-2$, both with negative real part, so it is Hurwitz.

Non-example: $p(s) = s^3 + s^2 + s + 1 = (s + 1)(s^2 + 1)$ has positive coefficients, but its roots $\pm i$ have real part $0$, so it is not Hurwitz.
