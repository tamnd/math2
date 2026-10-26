---
tag: 0XM8ZA9RNM
kind: concept
name: Sieve of Eratosthenes
msc: [11Y11]
sources:
  - url: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    locator: Overview
same_as:
  wikidata: Q177898
  wikipedia: Sieve of Eratosthenes
---

## Summary

The sieve of Eratosthenes is an algorithm that finds all the [[prime numbers|0SN0MAEKYX]] up to a given bound $N$.
It writes the integers from $2$ to $N$. It takes the smallest number that is not crossed out, which is a prime $p$, and crosses out the multiples $p^2, p^2 + p, p^2 + 2p, \dots$ up to $N$.
It repeats this step while $p^2 \le N$. The numbers that are not crossed out at the end are the primes up to $N$.

## Remarks

It is enough to start at $p^2$, because a smaller multiple of $p$ has a smaller prime factor, and an earlier step crossed it out.
The algorithm needs about $N \log \log N$ operations.
The idea of the sieve is the basis of sieve methods in analytic number theory.

## Explanations

### L1 human

For $N = 30$, cross out the multiples of $2$ from $4$, then the multiples of $3$ from $9$, then the multiples of $5$ from $25$.
Then $7^2 = 49 > 30$, so you stop.
The numbers left are $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$.
