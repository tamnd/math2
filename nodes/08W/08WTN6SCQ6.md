---
tag: 08WTN6SCQ6
kind: statement
role: proposition
name: Euler's four-square identity
msc: ["11E25"]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_four-square_identity
    locator: Algebraic identity
same_as:
  wikidata: Q1149225
  wikipedia: Euler's four-square identity
---

## Statement

Let $a_1, \dots, a_4$ and $b_1, \dots, b_4$ be elements of a commutative ring. Then
$$\begin{aligned} (a_1^2 + a_2^2 + a_3^2 + a_4^2)(b_1^2 + b_2^2 + b_3^2 + b_4^2) &= (a_1 b_1 - a_2 b_2 - a_3 b_3 - a_4 b_4)^2 + (a_1 b_2 + a_2 b_1 + a_3 b_4 - a_4 b_3)^2 \\ &\quad + (a_1 b_3 - a_2 b_4 + a_3 b_1 + a_4 b_2)^2 + (a_1 b_4 + a_2 b_3 - a_3 b_2 + a_4 b_1)^2. \end{aligned}$$

## Remarks

So the product of two sums of four squares is again a sum of four squares.
The signs come from the product of two quaternions: the identity says that the norm of quaternions is multiplicative.
Lagrange used it to reduce the [[four-square theorem|0KYYSMEVHH]] to the case of primes.

## History

Euler wrote about the identity in a letter to Goldbach of 4 May 1748.

## Explanations

### L1 human

This identity is the four-square analogue of the [[Brahmagupta–Fibonacci identity|0K2DMACEZ4]] for two squares.
You can check it by expanding both sides, since all the cross terms cancel.
