---
tag: 5DD48BF6CM
kind: statement
role: theorem
name: Division theorem for positive integers
aliases: [division-theorem-positive-integers]
msc: [11A05]
uses: [096PW7Q014]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_recursion.ptx#L163
    locator: source/s_induction_recursion.ptx:163
---

## Statement

Take two positive integers $m$ and $n$.
Then exactly one pair of integers $(q, r)$ satisfies both $m = qn + r$ and $0 \le r < n$.

## Remarks

The integer $q$ is the quotient and $r$ is the remainder when $m$ is divided by $n$.
The remainder is $0$ exactly when $n$ [[divides|096PW7Q014]] $m$.
For example, with $m = 17$ and $n = 5$ we get $q = 3$ and $r = 2$, since $17 = 3 \cdot 5 + 2$.
This is the case of the general division algorithm in which both numbers are positive.
