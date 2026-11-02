---
tag: 6HMT17DVX7
kind: concept
name: Quantum dilogarithm
msc: ["33B30", "33D05"]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_dilogarithm
same_as:
  wikidata: Q7269036
  wikipedia: Quantum dilogarithm
---

## Summary

The quantum dilogarithm is a [[q-analog|GFSDMJHHVA]] of the [[dilogarithm|G0X0NWSDB7]].
In its basic form it is the infinite product $(x; q)_\infty = \prod_{n \ge 0} (1 - x q^n)$, whose logarithm is a deformed dilogarithm series.
It satisfies a pentagon identity for $q$-commuting variables, a quantum version of the five-term relation.
It appears in quantum groups, quantum Teichmüller theory, cluster algebras and knot invariants.

## Explanations

### L1 human

The ordinary dilogarithm is the series $\sum_{n \ge 1} x^n / n^2$.
Replace one factor $n$ in the denominator by the "$q$-number" $1 - q^n$, and you get the series $\sum_{n \ge 1} x^n / \big(n (1 - q^n)\big)$.
Its exponential is a simple product, $\prod_{n \ge 0} (1 - x q^n)^{-1}$.
As $q$ tends to $1$, the deformed series times $1 - q$ tends back to the dilogarithm, so the classical function is a limit of the quantum one.
For example, with $q = 0$ the product $(x; q)_\infty$ is just $1 - x$, since every factor after the first equals $1$.
