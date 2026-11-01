---
tag: 9N6R5ADJXT
kind: concept
name: Blaschke product
msc: [30J10, 30J05]
sources:
  - url: https://en.wikipedia.org/wiki/Blaschke_product
same_as:
  wikidata: Q4380191
  wikipedia: Blaschke product
---

## Summary

A Blaschke product is a bounded [[holomorphic function|0DG0Z72CQD]] on the [[unit disc|8G5ABXRK85]] built as a product of disc automorphisms, one for each prescribed zero.
It exists exactly when the zeros satisfy the Blaschke condition $\sum_n (1 - \abs{a_n}) < \infty$.
Blaschke products are the basic [[inner functions|NN8XH5RJYB]], and every nonzero function in a [[Hardy space|PNNNFJVF6W]] factors through the Blaschke product of its zeros.

## Explanations

### L1 human

Each factor $\frac{\abs{a}}{a} \frac{a - z}{1 - \bar a z}$ is a [[Möbius transformation|0B346DDAM5]] that maps the disc onto itself and vanishes only at $a$.
Multiplying such factors gives a function with exactly the chosen zeros and with modulus at most $1$.
With infinitely many zeros, the product converges only if the zeros approach the circle fast enough.
For example, the zeros $a_n = 1 - 2^{-n}$ are allowed, since $\sum 2^{-n} < \infty$.
The zeros $a_n = 1 - 1/n$ are not allowed, since $\sum 1/n = \infty$.
