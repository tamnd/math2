---
tag: T8EN3CAEQF
kind: concept
name: Multivariate division algorithm
msc: [13P10, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Gröbner_basis
---

## Summary

The multivariate division algorithm divides a polynomial in several variables by an ordered list of polynomials, with respect to a fixed [[monomial order|E874NARWPV]].
It writes the polynomial as a combination of the divisors plus a remainder.
No term of the remainder is divisible by the leading term of a divisor.
It extends the [[division algorithm for polynomials|0MES3KS0ZC]] in one variable.
In general the remainder depends on the order of the divisors, but for a [[Gröbner basis|C83KPT47R0]] it is unique, and it then decides ideal membership.

## Explanations

### L1 human

In one variable, long division removes the leading term of the dividend again and again until the degree is too small.
With several variables one does the same.
Whenever the leading term of what is left is a multiple of the leading term of some divisor, subtract a suitable multiple of that divisor.
When no divisor fits, move the leading term to the remainder and go on.
For example, dividing $xy^2 + 1$ by $xy + 1$ and then $y + 1$ gives $xy^2 + 1 = y(xy + 1) - (y + 1) + 2$, with remainder $2$.
