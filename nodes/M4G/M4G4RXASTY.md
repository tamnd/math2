---
tag: M4G4RXASTY
kind: concept
name: Brun sieve
msc: [11N35, 11N36]
sources:
  - url: https://en.wikipedia.org/wiki/Brun_sieve
same_as:
  wikidata: Q17003952
  wikipedia: Brun sieve
---

## Summary

The Brun sieve is a combinatorial sieve method of Viggo Brun.
It counts the integers of a set that have no prime factor below a bound $z$.
It uses a truncated inclusion–exclusion, which gives upper and lower bounds with a controllable error.
It was the first sieve to give nontrivial results on problems such as twin primes.
There the [[sieve of Eratosthenes|0XM8ZA9RNM]] with full inclusion–exclusion produces too large an error.
With it Brun proved that the sum of the reciprocals of the twin primes converges.

## Explanations

### L1 human

To count numbers with no small prime factor, inclusion–exclusion subtracts the multiples of each prime, adds back the multiples of each product of two primes, and so on.
With many primes this formula has a huge number of terms, and the small rounding errors add up to something larger than the answer.
Brun's idea is to stop the formula early.
Stopping after an even number of steps gives an upper bound, stopping after an odd number gives a lower bound.
For example, the numbers up to $10$ with no factor $2$ or $3$ are $1, 5, 7$; stopping after the first step gives the lower bound $10 - 5 - 3 = 2 \le 3$.
