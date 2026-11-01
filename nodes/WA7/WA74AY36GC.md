---
tag: WA74AY36GC
kind: definition
name: Sidon set
msc: [11B83, 11B13, 05B10]
defines: BAADB7WHWZ
uses: [082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Sidon_sequence
---

## Definition

Let $G$ be an [[abelian group|082GHNPJ53]], for example $\Z$, and let $A$ be a subset of $G$.
The set $A$ is a *Sidon set* if for all $a, b, c, d \in A$ with $a + b = c + d$, one has $\set{a, b} = \set{c, d}$.

## Remarks

If $G$ has no elements of order $2$, as in $\Z$, the definition is equivalent to this one: the differences $a - b$ with $a, b \in A$ and $a \ne b$ are pairwise different.
The set $\set{1, 2, 4, 8}$ is a Sidon set in $\Z$.
Its sums $a + b$ with $a \le b$ are $2, 3, 4, 5, 6, 8, 9, 10, 12, 16$, and these ten numbers are distinct.
The set $\set{1, 2, 3, 4}$ is not a Sidon set, since $1 + 4 = 2 + 3$ but $\set{1, 4} \ne \set{2, 3}$.
An infinite Sidon set of positive integers, listed in increasing order, is called a Sidon sequence.
Sidon sets in $\Z$ are also called Golomb rulers when they are finite.
