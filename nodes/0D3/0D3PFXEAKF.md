---
tag: 0D3PFXEAKF
kind: statement
role: theorem
name: Consecutive Fibonacci numbers are coprime
msc: [11B39]
uses: [0GFKP8F8AG, 02WF878BH1, 0TRNT4X7J0]
sources:
  - url: https://en.wikipedia.org/wiki/Fibonacci_sequence
    locator: Divisibility properties
---

## Statement

Let $(F_n)_{n \ge 0}$ be the Fibonacci sequence, given by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$ for $n \ge 0$.
Then $F_n$ and $F_{n+1}$ are [[coprime|0GFKP8F8AG]] for each $n \ge 0$, that is, $\gcd(F_n, F_{n+1}) = 1$.

## Remarks

A proof by induction: $\gcd(F_{n+1}, F_{n+2}) = \gcd(F_{n+1}, F_{n+2} - F_{n+1}) = \gcd(F_{n+1}, F_n)$, and $\gcd(F_0, F_1) = 1$.
A stronger fact is $\gcd(F_m, F_n) = F_{\gcd(m, n)}$ for all $m, n \ge 0$.
The [[Euclidean algorithm|0TRNT4X7J0]] on $F_{n+1}$ and $F_n$ takes many steps, and consecutive Fibonacci numbers give its worst case.

## Explanations

### L1 human

Two neighbours in the Fibonacci sequence $0, 1, 1, 2, 3, 5, 8, 13, \dots$ never have a common factor larger than $1$.
A common factor of two neighbours would also divide the term before them, and so on down to $F_1 = 1$.
