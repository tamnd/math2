---
tag: T8QYJCS3JA
kind: concept
name: q-exponential
msc: [05A30, 33D15]
sources:
  - url: https://en.wikipedia.org/wiki/Q-exponential
same_as:
  wikidata: Q1062655
  wikipedia: Q-exponential
---

## Summary

The $q$-exponential $e_q(z) = \sum_{n \ge 0} z^n / [n]_q!$ is the [[q-analog|GFSDMJHHVA]] of the [[exponential function|0J0FCWV32D]].
It is the solution of $D_q f = f$, $f(0) = 1$, for the [[q-derivative|PMJT3FZE0Y]] $D_q$, just as $e^z$ solves $f' = f$.
By the [[q-binomial theorem|VVT27RB46B]] it is an infinite product, and it tends to $e^z$ as $q \to 1$.
A second $q$-exponential $E_q$ satisfies $e_q(z) E_q(-z) = 1$, which replaces the rule $e^z e^{-z} = 1$.

## Explanations

### L1 human

Replace each factorial $n!$ in the series of $e^z$ by its $q$-analogue $[n]_q! = [1]_q [2]_q \cdots [n]_q$, where $[k]_q = 1 + q + \cdots + q^{k-1}$.
The result is the $q$-exponential.
Its first terms are $1 + z + \frac{z^2}{1 + q} + \cdots$, which become $1 + z + \frac{z^2}{2} + \cdots$ at $q = 1$.
Many familiar rules of the exponential survive in a modified form, but $e_q(x) e_q(y) = e_q(x + y)$ fails in general.
