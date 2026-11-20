---
tag: S76RB8WCZ0
kind: definition
name: Small theory
msc: ["03C15", "03C50"]
topics: [6XEXRME4C1]
audience: grad
defines: W6XM5NVNRP
uses: [655K8Y7VS8, 9V71Q3SD1G, 01TQB88H4C]
sources:
  - book: isbn:9780387987606
---

## Definition

Let $L$ be a countable signature and $T$ a [[complete|655K8Y7VS8]] $L$-theory with infinite models.
For $n \ge 1$, let $S_n(T)$ be the set of complete $n$-[[types|9V71Q3SD1G]] of $T$: maximal sets of formulas in $x_1, \dots, x_n$ that are consistent with $T$.
The theory $T$ is *small* if $S_n(T)$ is [[countable|01TQB88H4C]] for every $n \ge 1$.

## Notation

Some books write $S_n^T$ or $S_n(\emptyset)$ for $S_n(T)$, and some say "$T$ has countably many types" instead of "small".

## Remarks

The definition counts types over the empty set.
Counting types over each finite set of parameters in a model gives the same notion, since a type over a tuple of length $m$ corresponds to a type of $T$ in $m$ more variables.
This is the definition of the concept [[small theory|W6XM5NVNRP]].

## Explanations

### L1 human

A theory is small when, for each number $n$, there are only countably many complete descriptions of $n$ elements.

### L2 human

For the theory of an infinite set, an $n$-type is fixed by which variables are equal.
There are finitely many such patterns, so the theory is small.
A trap is to count formulas instead of types: there are always countably many formulas, so the question is how many maximal consistent sets they form.
