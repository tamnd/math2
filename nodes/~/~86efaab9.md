---
tag: ~86efaab9
kind: concept
name: Recursively defined sequence
msc: [11B37]
uses: [~045b33ad]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Sequence
    locator: Defining a sequence by recursion
---

## Summary

A recursively defined sequence is a [[sequence|~045b33ad]] given by its first terms and a rule that computes each later term from the terms before it. A typical form is $a_0 = c$ and $a_{n+1} = f(n, a_n)$ for a given value $c$ and a given function $f$. The recursion theorem shows that exactly one sequence satisfies such a rule.

## Remarks

The factorials satisfy $0! = 1$ and $(n+1)! = (n+1) \cdot n!$.
The Fibonacci numbers satisfy $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$. Here each term needs the two terms before it.
In analysis, the sequence $a_0 = 1$, $a_{n+1} = \frac{1}{2}(a_n + 2/a_n)$ converges to $\sqrt{2}$. It is [[Newton's method|~160896df]] for $x^2 - 2$.
The rule that links the terms is a recurrence relation.

## Explanations

### L1 human

A recursive rule tells you how to get the next term from the terms you already have.
Start with $a_0 = 1$ and the rule $a_{n+1} = 2 a_n$, and you get $1, 2, 4, 8, \dots$.
