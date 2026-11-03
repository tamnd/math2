---
tag: 4PGX7PHJCK
kind: concept
name: Circuit complexity
msc: [68Q06, 68Q17, 94C11]
sources:
  - url: https://en.wikipedia.org/wiki/Circuit_complexity
same_as:
  wikidata: Q1055112
  wikipedia: Circuit complexity
---

## Summary

Circuit complexity measures how hard a [[Boolean function|0X05GS525E]] is by the size or depth of the smallest [[Boolean circuit|SQXNFGVADX]] that computes it.
A language is studied through the family of circuits that decide it on each input length.
Lower bounds on circuit size are a route to separating complexity classes, since every problem in [[P|GVT2NKN37K]] has circuits of polynomial size.
Strong lower bounds are known for restricted circuits, such as constant-depth and monotone circuits, but not for general ones.

## Explanations

### L1 human

A Boolean circuit is a wiring diagram of AND, OR and NOT gates that computes an output bit from input bits.
The size of a circuit is its number of gates, and its depth is the length of the longest path from an input to the output.
The circuit complexity of a function is the size of the smallest circuit for it.
For example, the AND of $n$ bits needs exactly $n - 1$ gates of fan-in two.
Most functions need about $2^n / n$ gates, but for explicit functions in NP the best known lower bounds are only a small constant times $n$.
