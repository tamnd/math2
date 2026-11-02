---
tag: TRC892PJNN
kind: concept
name: Closure of an operator
msc: [47A05, 47B25]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
---

## Summary

The closure of a closable operator is its smallest closed extension.
Its graph is the closure of the graph of the original operator.
Taking closures lets one define an operator on a simple domain and then pass to a closed operator, to which the main theorems apply.

## Explanations

### L1 human

An operator given by a formula on nice inputs can be extended by limits: if $x_n \to x$ and $T x_n \to y$, declare $Tx = y$.
For a closable operator this rule is consistent, and the result is the closure.
For example, starting with differentiation on polynomials in $C[0, 1]$, the closure is differentiation on all continuously differentiable functions.
It is the most economical way to make an operator closed without changing what it does on the old domain.
