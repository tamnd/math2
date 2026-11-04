---
kind: statement
msc:
- 39A06
name: Solutions of an advancement operator equation with distinct roots
role: theorem
sources:
- locator: source/s_recurrence_rigorous.ptx:103
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rigorous.ptx#L103
tag: X2YNES3X3K
uses:
- 0BWDJGQYST
- 0ZV2YKKZ58
---

## Statement

Let $A$ be the advancement operator on sequences, so that $(Af)(n) = f(n+1)$. Let $r_1, \dots, r_k$ be distinct non-zero constants. Consider the equation $(A - r_1)(A - r_2)\cdots(A - r_k) f = 0$.

Then every [[solution|0ZV2YKKZ58]] $f$ of this equation can be written as $f(n) = c_1 r_1^n + c_2 r_2^n + \dots + c_k r_k^n$ for some constants $c_1, \dots, c_k$.

## Remarks

The polynomial $p(A) = (A - r_1)\cdots(A - r_k)$ is the [[characteristic polynomial|0BWDJGQYST]] of the recurrence, and $r_1, \dots, r_k$ are its roots. The statement says that the sequences $r_i^n$ span all solutions.
