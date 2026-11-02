---
tag: SDCKNWSWNM
kind: concept
name: Weierstrass polynomial
msc: [32B05, 13J07]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem
---

## Summary

A Weierstrass polynomial is a monic polynomial in one variable $z_n$ whose other coefficients are holomorphic germs in $z_1, \dots, z_{n-1}$ vanishing at the origin.
The [[Weierstrass preparation theorem|49JSD49P7X]] says that every holomorphic germ that does not vanish identically on the $z_n$-axis is a unit times such a polynomial.
This reduces many local questions about holomorphic functions of $n$ variables to questions about polynomials over the ring of germs in $n - 1$ variables.

## Explanations

### L1 human

Near the origin, the zeros of a Weierstrass polynomial of degree $d$ in $z_n$ behave like the $d$ roots of an ordinary polynomial.
For each fixed $z' = (z_1, \dots, z_{n-1})$ near $0$, there are exactly $d$ roots $z_n$, counted with multiplicity, and they all tend to $0$ as $z' \to 0$.
For example, $z_2^2 - z_1$ is a Weierstrass polynomial in $z_2$ of degree $2$, and its roots are the two square roots of $z_1$.
