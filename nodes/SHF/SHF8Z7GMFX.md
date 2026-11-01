---
tag: SHF8Z7GMFX
kind: concept
name: Order of an entire function
msc: ["30D15", "30D20"]
sources:
  - url: https://en.wikipedia.org/wiki/Entire_function
---

## Summary

The order of an [[entire function|0419794R0T]] measures how fast its maximum modulus grows, on the scale of functions $\exp(r^\lambda)$.
It is the least exponent $\rho$ such that $\abs{f(z)}$ is at most about $\exp(\abs{z}^{\rho})$ for large $\abs{z}$.
Polynomials have order $0$, $e^z$ has order $1$, and $e^{z^2}$ has order $2$.
The order controls the number of zeros of the function and the shape of its factorization, as in the [[Hadamard factorization theorem|KYSR7NHNFQ]].

## Explanations

### L1 human

Entire functions can grow at very different speeds as $\abs{z}$ grows.
To compare them, one looks at the largest value $M(r)$ of $\abs{f}$ on the circle of radius $r$ and asks which power $r^\rho$ appears in the exponent.
For $e^z$, $M(r) = e^r$, so the order is $1$.
For $\cos \sqrt{z}$ the growth is like $e^{\sqrt{r}}$, so the order is $1/2$.
A function such as $e^{e^z}$ grows faster than every $\exp(r^\rho)$ and has infinite order.
