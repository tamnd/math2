---
tag: 0Z962ECCXR
kind: concept
name: Trial division
msc: [11Y05]
specializes: [0EGJZHZ02C]
sources:
  - url: https://en.wikipedia.org/wiki/Trial_division
    locator: Method
same_as:
  wikidata: Q1333681
  wikipedia: Trial division
---

## Summary

Trial division is the simplest method to factor an integer $n > 1$ or to test whether it is prime.
It divides $n$ by the integers $d = 2, 3, 4, \dots$ in turn, and it stops at the first $d$ that divides $n$, or when $d^2 > n$.
If no $d$ with $d^2 \le n$ divides $n$, then $n$ is prime.

## Remarks

The method is correct because [[a composite number has a prime factor at most its square root|0EB6BBMQMC]].
It is enough to test the primes $d$, but a test of all integers $d$ is also correct.
For a number $n$ with $k$ digits, the method can need about $\sqrt{n} \approx 10^{k/2}$ divisions. Thus it is slow for large $n$.

## Explanations

### L1 human

To test whether $91$ is prime, try to divide it by $2$, $3$, $5$ and $7$. You can stop after $9$, because $10^2 > 91$.
The division by $7$ works: $91 = 7 \cdot 13$. So $91$ is not prime.
