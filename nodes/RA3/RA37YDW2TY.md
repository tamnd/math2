---
tag: RA37YDW2TY
kind: concept
name: One-way function
msc: [94A60, 68Q17, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/One-way_function
same_as:
  wikidata: Q720931
  wikipedia: One-way function
---

## Summary

A one-way function is a function that is easy to compute but hard to invert on random inputs.
Its existence is the basic assumption of modern cryptography: it is equivalent to the existence of pseudorandom generators, secure private-key encryption and digital signatures.
No function is proved to be one-way, since this would imply $\mathrm{P} \ne \mathrm{NP}$.
Multiplication of two random primes is a standard candidate, through the hardness of [[integer factorization|YPE65X5HJ4]].

## Explanations

### L1 human

Some operations are easy to do and hard to undo.
Mixing two paints is easy, but separating them again is not.
In mathematics, multiplying two large primes takes a computer a fraction of a second.
Given only the product, no known method finds the two primes in a reasonable time when they have hundreds of digits.
A one-way function is a function with this property, made precise with probabilities and running times.
