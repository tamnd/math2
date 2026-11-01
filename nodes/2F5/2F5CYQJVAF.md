---
tag: 2F5CYQJVAF
kind: concept
name: Theta function
msc: [11F27, 14K25, "33E05"]
sources:
  - url: https://en.wikipedia.org/wiki/Theta_function
same_as:
  wikidata: Q1154787
  wikipedia: Theta function
---

## Summary

The Jacobi theta function is $\vartheta(z, \tau) = \sum_{n \in \Z} e^{\pi i n^2 \tau + 2 \pi i n z}$ for $z \in \C$ and $\tau$ in the [[upper half-plane|X6XGGH5FPW]].
It is periodic in $z$ with period $1$ and quasi-periodic with period $\tau$.
Theta functions are the building blocks of elliptic functions and of functions on abelian varieties.
In the variable $\tau$, the theta series of quadratic forms are [[modular forms|GWKN5VG78A]] that count representations of numbers.

## Explanations

### L1 human

A theta function is a sum of exponentials whose exponents grow like squares, so it converges very fast.
Shifting $z$ by $1$ changes nothing, and shifting $z$ by $\tau$ multiplies the function by a simple exponential factor.
Setting $z = 0$ gives $\theta(\tau) = \sum_{n \in \Z} e^{\pi i n^2 \tau}$.
Raising it to the $k$-th power counts the ways to write numbers as sums of $k$ squares.
This is how [[Jacobi's four-square theorem|CG17WSS64W]] can be proved.
