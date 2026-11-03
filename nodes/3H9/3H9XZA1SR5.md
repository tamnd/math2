---
tag: 3H9XZA1SR5
kind: concept
name: Maximum distance separable code
msc: [94B05, 94B65]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Singleton_bound
---

## Summary

A maximum distance separable code, or MDS code, is a [[linear code|E85KREWV60]] that meets the [[Singleton bound|RAKXDDYNAM]]: its parameters $[n, k, d]$ satisfy $d = n - k + 1$.
For its length and dimension it has the largest possible minimum distance.
Any $k$ positions of a codeword determine the codeword, so the message can be recovered from any $k$ received symbols.
Reed–Solomon codes are the main examples, and they are used for this reason in storage systems and in erasure coding.

## Explanations

### L1 human

An MDS code turns $k$ symbols of data into $n$ symbols in such a way that any $k$ of the $n$ symbols are enough to rebuild the data.
So up to $n - k$ symbols can be lost without harm, and no code of the same size can do better.
For example, store two numbers $a, b$ as the three numbers $a, b, a + b$: any two of the three give back $a$ and $b$.
