---
tag: AS00YM4X7F
kind: concept
name: Arbitrary-precision arithmetic
msc: [65Y04, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Arbitrary-precision_arithmetic
same_as:
  wikidata: Q527381
  wikipedia: Arbitrary-precision arithmetic
---

## Summary

Arbitrary-precision arithmetic computes with numbers whose number of digits is limited only by the memory of the computer, not by a fixed hardware format.
Integers and rational numbers can then be handled exactly, and real numbers with as many correct digits as one asks for.
Unlike fixed-size [[floating-point arithmetic|RTKRSC3KPH]], each operation costs more as the numbers grow, so fast multiplication algorithms matter.
It is used in computer algebra, number theory, cryptography and to check numerical results with higher precision.

## Explanations

### L1 human

A calculator shows perhaps $12$ digits, and a computer's built-in numbers hold about $16$ decimal digits.
Arbitrary-precision arithmetic stores a number as a list of digits that can be as long as needed, just as one writes long numbers on paper.
It can compute $2^{1000}$, a number with $302$ digits, exactly, or $\pi$ to a million decimals.
The price is speed: a product of two numbers with $n$ digits each takes far more time than one machine multiplication.
