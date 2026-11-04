---
kind: statement
msc:
- 39A06
name: General solution of a recurrence with a repeated root
role: lemma
sources:
- locator: source/s_recurrence_rigorous.ptx:152
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rigorous.ptx#L152
tag: AGXA4Q7E5J
uses:
- 91QMF4R1CY
- 0BWDJGQYST
---

## Statement

Let $A$ be the [[shift operator|91QMF4R1CY]] on sequences, so that $(Af)(n) = f(n+1)$. Let $r$ be a constant and let $k \ge 1$ be an integer.

Consider the recurrence $(A - r)^k f = 0$. Its [[characteristic polynomial|0BWDJGQYST]] is $(x - r)^k$, so $r$ is its only root, with multiplicity $k$.

Then the general solution is
$$f(n) = c_1 r^n + c_2 n r^n + c_3 n^2 r^n + \dots + c_k n^{k-1} r^n,$$
where $c_1, \dots, c_k$ are arbitrary constants. That is, each sequence of this form solves the recurrence, and each solution has this form for some constants.

## Remarks

For $k = 1$ the recurrence is $f(n+1) = r f(n)$, and the solutions are $c_1 r^n$.

For $k = 2$ the solutions are $(c_1 + c_2 n) r^n$.

The shape matches the differential equation case, where a root of multiplicity $m$ gives $x^j e^{rx}$ for $0 \le j < m$.
