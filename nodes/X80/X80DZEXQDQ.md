---
tag: X80DZEXQDQ
kind: definition
name: Summability method
msc: [40C99, 40A05]
defines: 8X25Q4XYMN
uses: [0QE8STGJH2, 0JH4MN4K1C, 0NB643K60Q]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $\mathbb{K}^{\N}$ be the set of all [[sequences|0QE8STGJH2]] in $\mathbb{K}$.
A *summability method* $M$ consists of a set $D_M \subseteq \mathbb{K}^{\N}$ and a map $M \colon D_M \to \mathbb{K}$.
A sequence $s$ is *$M$-summable* (or *$M$-limitable*) to $M(s)$ if $s \in D_M$.
A [[series|0JH4MN4K1C]] $\sum a_n$ is $M$-summable with $M$-sum $L$ if its sequence of [[partial sums|0NB643K60Q]] $s_n = a_0 + \cdots + a_n$ is $M$-summable to $L$.

## Remarks

Example: the ordinary limit, with $D_M$ the set of convergent sequences and $M(s) = \lim s_n$, is a summability method; it sums exactly the convergent series.
Example: Cesàro summation takes $D_M$ to be the sequences whose [[Cesàro means|0P0DJHBGBB]] converge, and $M(s)$ the limit of these means; it sums $1 - 1 + 1 - \cdots$ to $\frac12$.
Non-example: "take the limit of some convergent subsequence" is not a summability method.
The sequence $0, 1, 0, 1, \dots$ would get both $0$ and $1$, so the rule does not define a map.
Some authors define methods directly on series $(a_n)$ instead of on partial sums; the two points of view are equivalent.

## Explanations

### L1 human

A summability method is any well-defined rule that turns certain sequences into numbers.
Further conditions, such as agreement with the ordinary limit, single out the useful methods.
