---
tag: 0BFMR2FQ8B
kind: statement
role: theorem
name: Number of k-element subsets
msc: [05A10]
uses: [05099E1NMJ, 0JZSRWRBZE, 092GEF38YD]
sources:
  - url: https://en.wikipedia.org/wiki/Combination
    locator: Number of k-combinations
---

## Statement

Let $X$ be a finite set with $|X| = n$ and let $k$ be a natural number.
Then the number of subsets of $X$ with exactly $k$ elements is the [[binomial coefficient|092GEF38YD]] $\binom{n}{k}$.

## Remarks

A proof by induction on $n$ fixes an element $x \in X$. A $k$-subset either omits $x$ or contains $x$, and this gives [[Pascal's rule|0YRG241HQQ]].
For $k > n$ both sides are $0$.

## Explanations

### L1 human

To pick a committee of $k$ people from $n$, first count the ordered lists of $k$ people. Then divide by the $k!$ orders of each committee.
This gives $\frac{n (n-1) \cdots (n-k+1)}{k!}$, which is $\binom{n}{k}$.
