---
tag: NZ273TPSG4
kind: statement
role: theorem
name: Principle of mathematical induction for positive integers
msc: [03F30]
uses: [0ASJVEFA9J]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_induction.ptx#L32
    locator: source/s_induction_induction.ptx:32
---

## Statement

For each positive integer $n$, let $S_n$ be a statement that is either true or false.
Suppose that $S_1$ is true.
Suppose also that for every positive integer $k$, the truth of $S_k$ forces the truth of $S_{k+1}$.
Then $S_n$ is true for every positive integer $n$.

## Remarks

This is the form of [[induction|0ASJVEFA9J]] that starts at $1$.
The proof of $S_1$ is the base case.
The proof that $S_k$ implies $S_{k+1}$ is the induction step, and the assumption $S_k$ is the induction hypothesis.
