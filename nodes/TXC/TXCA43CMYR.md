---
tag: TXCA43CMYR
kind: concept
name: K-function
msc: ["33B15"]
sources:
  - url: https://en.wikipedia.org/wiki/K-function
same_as:
  wikidata: Q1541649
  wikipedia: K-function
---

## Summary

The K-function extends the hyperfactorial $1^1 \cdot 2^2 \cdots n^n$ to non-integer arguments.
It satisfies $K(1) = 1$ and $K(z + 1) = z^z K(z)$, so $K(n + 1) = 1^1 2^2 \cdots n^n$ for positive integers $n$.
It is defined through an integral of $\log \Gamma$, where $\Gamma$ is the [[gamma function|0H5SYBSED9]], and is related to the [[Barnes G-function|7E2JJWFF00]].

## Explanations

### L1 human

The factorial multiplies $1, 2, 3, \ldots, n$.
The hyperfactorial multiplies $1^1, 2^2, 3^3, \ldots, n^n$, so it grows even faster.
The K-function is a smooth curve through the values of the hyperfactorial, as the gamma function is a smooth curve through the factorials.
For example, $K(4) = 1^1 \cdot 2^2 \cdot 3^3 = 108$.
