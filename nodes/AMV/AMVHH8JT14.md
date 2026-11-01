---
tag: AMVHH8JT14
kind: definition
name: Sigma-compact space
msc: [54D45]
defines: ZW4NFH5RNC
uses: [0CQHFPGJ45, 0R6EWFKRCF, 01TQB88H4C, 0X1GSWNBN1, SW0SN1NEJE]
sources:
  - url: https://en.wikipedia.org/wiki/Σ-compact_space
---

## Definition

A [[topological space|0CQHFPGJ45]] $X$ is *σ-compact* when there are [[compact|0R6EWFKRCF]] subsets $K_1, K_2, K_3, \ldots$ of $X$ with
$$X = \bigcup_{n \ge 1} K_n.$$

## Remarks

The family may be finite or [[countable|01TQB88H4C]]; a finite family can be padded by repeating a set.
Every σ-compact space is [[Lindelöf|SW0SN1NEJE]]: an open cover has a finite subcover of each $K_n$, and the union of these is a countable subcover.
A closed subspace and a continuous image of a σ-compact space are σ-compact.

Example: $\R^n$ is σ-compact.
It is the union of the closed balls $\set{x : \norm{x} \le m}$ for $m \ge 1$, which are compact by the Heine–Borel theorem.
Example: $\Q$ is σ-compact, as the countable union of its one-point subsets.

Non-example: an uncountable set $X$ with the discrete topology is not σ-compact.
Its compact subsets are finite, and a countable union of finite sets is countable.

Notation: σ-compact, also written sigma-compact.
