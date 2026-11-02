---
tag: HJ2XQMFDS9
kind: definition
name: Jordan–Dedekind chain condition
msc: [06A07, 06B05]
defines: RW7YC3HG0S
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, 3AX549FFFM]
sources:
  - url: https://en.wikipedia.org/wiki/Graded_poset
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|0QV2JS9RJ3]].
For $x \le y$ in $P$, let $[x, y] = \set{z \in P : x \le z \le y}$.
A finite [[chain|0S8FE7ZMFM]] $z_0 < z_1 < \cdots < z_n$ has length $n$.
The poset $P$ satisfies the *Jordan–Dedekind chain condition* when the following holds for all $x \le y$ in $P$.
All [[maximal chains|3AX549FFFM]] of $[x, y]$ are finite and have the same length.

## Remarks

Example: the positive divisors of $12$ under divisibility satisfy the condition.
A maximal chain of $[a, b]$ multiplies by one prime at each step, so its length is the number of prime factors of $b / a$ counted with multiplicity.
Non-example: the pentagon with $0 < a < b < 1$ and $0 < c < 1$ fails it, since $0 < a < b < 1$ and $0 < c < 1$ are maximal chains of $[0, 1]$ with lengths $3$ and $2$.
Let $P$ be finite with a least element $\hat{0}$.
Then $P$ satisfies the condition if and only if $P$ has a rank function.
In that case, setting $\rho(x)$ equal to the length of any maximal chain of $[\hat{0}, x]$ gives a rank function.
Every modular lattice of finite length satisfies the condition.
