---
tag: ACSF58HYDH
kind: concept
name: Weierstrass product
msc: ["30D20", "30D10"]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_factorization_theorem
---

## Summary

A Weierstrass product is an infinite product of elementary factors $E_{p_n}(z/a_n)$ that converges to an [[entire function|0419794R0T]] with zeros exactly at the points $a_n$.
Each elementary factor is $1 - z/a_n$ times an exponential correction that makes the product converge.
Weierstrass products show that any sequence of nonzero complex numbers tending to infinity is the zero set of an entire function.
They are the building blocks of the [[Weierstrass factorization theorem|11VC51YHQJ]] and the [[Hadamard factorization theorem|KYSR7NHNFQ]].

## Explanations

### L1 human

To build a polynomial with given roots, multiply the factors $1 - z/a$.
With infinitely many roots, this product may diverge, as for $\prod_{n \ge 1} (1 - z/n)$.
Weierstrass multiplies each factor by $\exp(z/a + z^2/(2a^2) + \cdots + z^p/(p a^p))$, which equals $1$ at $z = 0$ and has no zeros.
This correction removes the first terms of $\log(1 - z/a)$ and makes the product converge.
For the roots $n = 1, 2, 3, \dots$, the product $\prod_n (1 - z/n) e^{z/n}$ converges, and it is closely related to the gamma function.
