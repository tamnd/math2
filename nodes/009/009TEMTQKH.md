---
tag: 009TEMTQKH
kind: statement
role: theorem
name: Stars and bars
msc: [05A10]
uses: [092GEF38YD, 0YEQG3VBYC]
sources:
  - url: https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
    locator: Theorem two
same_as:
  wikidata: Q7602343
  wikipedia: Stars and bars (combinatorics)
---

## Statement

Let $n$ and $k$ be natural numbers with $n \ge 1$.
Then the number of multisets of size $k$ with elements in an $n$-element set is
$$\left(\!\binom{n}{k}\!\right) = \binom{n + k - 1}{k}.$$
Equivalently, this is the number of solutions $(x_1, \dots, x_n)$ of $x_1 + \dots + x_n = k$ in natural numbers.

## Remarks

The proof writes a multiset as a row of $k$ stars and $n - 1$ bars. The bars separate the stars into $n$ groups, one group for each element.
The number of solutions in positive integers is $\binom{k - 1}{n - 1}$ for $k \ge 1$. This is the [[number of compositions|057H72B2MB]] of $k$ into $n$ parts.

## Explanations

### L1 human

To share $k$ identical sweets among $n$ children, put the $k$ sweets in a row and insert $n - 1$ dividers.
There are $k + n - 1$ positions, and you choose which $k$ of them are sweets.
