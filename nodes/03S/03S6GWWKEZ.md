---
tag: 03S6GWWKEZ
kind: statement
role: proposition
name: Limit of a quotient of sequences
msc: [40A05]
uses: [0XKWSSY8P2, 0734RSVF2V]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Properties
---

## Statement

Let $(a_n)$ and $(b_n)$ be real sequences, and let $a$ and $b$ be real numbers with $b \ne 0$.
Assume that $a_n \to a$ and $b_n \to b$ as $n \to \infty$.
Then there is a natural number $N$ such that $b_n \ne 0$ for all $n \ge N$.
Moreover, the sequence $(a_n / b_n)_{n \ge N}$ converges to $a / b$.

## Remarks

The main step is $1/b_n \to 1/b$. For large $n$ we have $|b_n| > |b|/2$, and then $|1/b_n - 1/b| = |b - b_n| / (|b_n|\,|b|) < 2 |b_n - b| / |b|^2$.
The [[limit of a product|0734RSVF2V]] of $(a_n)$ and $(1/b_n)$ then gives the result.
The hypothesis $b \ne 0$ is needed. For $a_n = 1$ and $b_n = 1/n$, the quotient is $n$, which has no real limit.

## Explanations

### L1 human

The limit of a quotient is the quotient of the limits, when the limit of the denominator is not zero.
For example, $(3 + 1/n)/(2 + 1/n) \to 3/2$.
