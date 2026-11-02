---
tag: 7EJCYBPYNN
kind: concept
name: Quantum calculus
msc: [05A30, 39A13]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_calculus
same_as:
  wikidata: Q7269016
  wikipedia: Quantum calculus
---

## Summary

Quantum calculus is calculus without limits.
It replaces the derivative by a difference quotient taken at a fixed scale.
The [[q-derivative|PMJT3FZE0Y]] compares $f(qx)$ with $f(x)$, and the $h$-derivative compares $f(x + h)$ with $f(x)$.
The matching antiderivatives are the [[Jackson integral|7EMPA6M8S7]] and finite sums.
It is the natural language for [[q-analogs|GFSDMJHHVA]] in combinatorics, for basic hypergeometric series and for [[q-difference equations|FQPYGXJJN0]].
It recovers ordinary calculus in the limit $q \to 1$ or $h \to 0$.

## Explanations

### L1 human

In ordinary calculus the slope of $f$ at $x$ is the limit of $(f(x + h) - f(x))/h$ as $h$ shrinks to zero.
In quantum calculus one stops before the limit and keeps a fixed step.
With the multiplicative step $x \mapsto qx$, the function $x^n$ has $q$-derivative $[n]_q x^{n-1}$, where $[n]_q = 1 + q + \cdots + q^{n-1}$.
This number $[n]_q$ is the $q$-analog of $n$, and it becomes $n$ when $q = 1$.
Many formulas of calculus keep a $q$-version, which often counts objects with an extra weight.
