---
tag: YZHM3HSM0F
kind: concept
name: Pochhammer symbol
msc: [05A10, 33C20, 33B15]
sources:
  - url: https://en.wikipedia.org/wiki/Falling_and_rising_factorials
---

## Summary

The Pochhammer symbol $(a)_n$ is the rising factorial $a (a + 1) \cdots (a + n - 1)$, a product of $n$ consecutive terms that go up by $1$ starting at $a$.
It is the basic building block of the [[hypergeometric series|428M453CR2]], whose coefficients are quotients of Pochhammer symbols.
For $a$ not a non-positive integer it equals $\Gamma(a + n)/\Gamma(a)$, which ties it to the [[gamma function|0H5SYBSED9]].
In combinatorics the same notation $(x)_n$ often stands for the [[falling factorial|0SJNCJCCQG]] instead, so one has to check the convention of each text.

## Explanations

### L1 human

The [[factorial|0XWG0JGDFW]] $n!$ multiplies $1, 2, \ldots, n$.
The Pochhammer symbol does the same but may start at any number $a$: it multiplies $a, a + 1, \ldots$ for $n$ steps.
For example $(3)_2 = 3 \cdot 4 = 12$ and $(\tfrac12)_2 = \tfrac12 \cdot \tfrac32 = \tfrac34$.
Starting at $a = 1$ gives back the factorial: $(1)_n = n!$.
