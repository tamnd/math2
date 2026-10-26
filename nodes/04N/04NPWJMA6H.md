---
tag: 04NPWJMA6H
kind: statement
role: theorem
name: Sum of two squares theorem
msc: ["11E25"]
uses: [043B3ENSTY, 0K2DMACEZ4, 04VCPS30ZE]
sources:
  - url: https://en.wikipedia.org/wiki/Sum_of_two_squares_theorem
    locator: lead section
same_as:
  wikidata: Q25303848
  wikipedia: Sum of two squares theorem
---

## Statement

Let $n$ be a positive integer.
Then $n = x^2 + y^2$ for some integers $x$ and $y$ if and only if $\nu_p(n)$ is even for each prime $p \equiv 3 \pmod 4$.
Here $\nu_p$ is the [[p-adic valuation|04VCPS30ZE]].

## Remarks

For example, $45 = 3^2 \cdot 5 = 6^2 + 3^2$, but $21 = 3 \cdot 7$ is not a sum of two squares.
The "if" part follows from [[Fermat's theorem on sums of two squares|043B3ENSTY]] and the [[Brahmagupta–Fibonacci identity|0K2DMACEZ4]].
Zero squares are allowed, so each square and each double of a square is a sum of two squares.

## Explanations

### L1 human

To decide whether $n$ is a sum of two squares, factor $n$ into primes.
Look only at the primes that leave remainder $3$ on division by $4$. Each of them must appear an even number of times.
