---
tag: 0EFYCFHYFG
kind: concept
name: Proof by infinite descent
aliases: [infinite-descent, method-of-descent]
msc: [11D99]
topics: [G9JFJGY4TQ]
specializes: [0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_infinite_descent
    locator: lead section
same_as:
  wikidata: Q619388
  wikipedia: Proof by infinite descent
---

## Summary

A proof by infinite descent shows that a statement has no solution in positive integers.
It assumes a solution, and from it constructs a strictly smaller solution in positive integers.
This gives an infinite decreasing sequence of positive integers, which is impossible.

## Remarks

The method rests on the well-ordering of the natural numbers: each nonempty set of natural numbers has a least element.
A classic use shows that $\sqrt{2}$ is irrational: a solution of $a^2 = 2 b^2$ in positive integers gives a smaller one, $(2b - a, a - b)$.
Fermat used the method to prove [[Fermat's right triangle theorem|086BE0J3FZ]].

## Explanations

### L1 human

You cannot go down forever in the positive integers: you reach the bottom after finitely many steps.
So if each solution gives a smaller one, there can be no solution at all.
