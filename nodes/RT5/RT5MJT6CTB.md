---
tag: RT5MJT6CTB
kind: statement
role: theorem
name: Apéry's theorem
msc: [11J72, 11M06]
uses: [1XWBY4N0VT, 0DZXAXEJQ9, 007NPQX34K]
about: [1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Ap%C3%A9ry%27s_theorem
same_as:
  wikidata: Q1095330
  wikipedia: Apéry's theorem
---

## Statement

The number
$$\zeta(3) = \sum_{n=1}^{\infty} \frac{1}{n^3}$$
is [[irrational|0DZXAXEJQ9]].
Here $\zeta$ is the [[Riemann zeta function|1XWBY4N0VT]].

## Remarks

The proof constructs two sequences of rational numbers $a_n$ and $b_n$, where the $b_n$ and the $2 d_n^3 a_n$ are integers, with $d_n$ the [[least common multiple|007NPQX34K]] of $1, 2, \dots, n$.
The differences $b_n \zeta(3) - a_n$ are nonzero and tend to $0$ so fast that $2 d_n^3 (b_n \zeta(3) - a_n)$ still tends to $0$.
If $\zeta(3) = p/q$, then $2 q d_n^3 (b_n \zeta(3) - a_n)$ would be a nonzero integer tending to $0$, which is impossible.
A useful series in the proof is
$$\zeta(3) = \frac{5}{2} \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^3 \binom{2n}{n}}.$$
For even arguments much more is known: $\zeta(2k)$ is a rational multiple of $\pi^{2k}$, so it is transcendental, as in the [[Basel problem|0DMY75D6FV]].
It is not known whether $\zeta(5)$ is irrational, and it is not known whether $\zeta(3)$ is transcendental.

## Explanations

### L1 human

The sum $1 + 1/8 + 1/27 + 1/64 + \cdots$ of the reciprocals of the cubes is about $1.202$.
Apéry's theorem says that this number is not a fraction.
Unlike the sum of the reciprocals of the squares, which equals $\pi^2/6$, no closed form for it is known.

### L2 human

Apéry's sequences satisfy a three-term recurrence with polynomial coefficients, and their growth controls the speed of approximation.
Later work gave other proofs, for example with Beukers' integrals over the unit cube.
Rivoal proved that infinitely many of the values $\zeta(2k+1)$ are irrational, and Zudilin proved that at least one of $\zeta(5), \zeta(7), \zeta(9), \zeta(11)$ is irrational.
