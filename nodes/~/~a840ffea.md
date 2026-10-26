---
tag: ~a840ffea
kind: statement
role: theorem
name: Number of nth roots of unity
msc: [11R18]
uses: [~219e078f]
sources:
  - url: https://en.wikipedia.org/wiki/Root_of_unity
    locator: Elementary properties
---

## Statement

Let $n$ be a positive integer.
Then there are exactly $n$ complex $n$th [[roots of unity|~c96389e8]].

## Remarks

The [[list of the nth roots of unity|~219e078f]] has $n$ numbers $e^{2 \pi i k / n}$ with $0 \le k < n$.
They are pairwise different, because their arguments are different numbers in $[0, 2\pi)$.
A polynomial of degree $n$ has at most $n$ roots in a field, so $X^n - 1$ has no other roots.
In other fields there can be fewer: in $\mathbb{R}$, the only $4$th roots of unity are $1$ and $-1$.

## Explanations

### L1 human

The equation $z^n = 1$ has exactly $n$ complex solutions.
Over the real numbers, it has only one or two solutions, so most of the solutions are not real.
