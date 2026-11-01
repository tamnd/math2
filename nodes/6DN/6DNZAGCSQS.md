---
tag: 6DNZAGCSQS
kind: concept
name: Ramanujan tau function
msc: [11F30, 11F11, 11A25]
sources:
  - url: https://en.wikipedia.org/wiki/Ramanujan_tau_function
same_as:
  wikidata: Q3535240
  wikipedia: Ramanujan tau function
---

## Summary

The Ramanujan tau function $\tau(n)$ gives the Fourier coefficients of the [[cusp form|A50Y012RBP]] $\Delta = q \prod_{n \ge 1} (1 - q^n)^{24}$ of weight $12$.
Ramanujan studied it in 1916 and conjectured that it is multiplicative, which Mordell proved in 1917.
Its properties come from the theory of [[Hecke operators|S4SV3QZ8B1]].
The bound $\abs{\tau(p)} \le 2 p^{11/2}$ for primes $p$ is the [[Ramanujan–Petersson conjecture|4CDFWST967]], proved by Deligne.

## Explanations

### L1 human

Multiply out the infinite product $q(1 - q)^{24}(1 - q^2)^{24}(1 - q^3)^{24} \cdots$ and read off the coefficient of $q^n$; that is $\tau(n)$.
The first values are $\tau(1) = 1$, $\tau(2) = -24$, $\tau(3) = 252$, $\tau(4) = -1472$ and $\tau(5) = 4830$.
These numbers look random, yet $\tau(6) = \tau(2)\tau(3)$, and in general $\tau(mn) = \tau(m)\tau(n)$ when $m$ and $n$ share no factor.
They also satisfy the congruence $\tau(n) \equiv \sigma_{11}(n) \pmod{691}$.
