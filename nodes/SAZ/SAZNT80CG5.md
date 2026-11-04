---
tag: SAZNT80CG5
kind: statement
role: theorem
name: Probabilistic lower bound for diagonal Ramsey numbers
msc: [05D10, 05C55, 05D40]
uses: [01DSVCRF6X]
about: [0K9QVPJYJF]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_ramsey_probability.ptx#L7
    locator: source/s_ramsey_probability.ptx:7
---

## Statement

Let $n$ be a positive integer.
Then the diagonal [[Ramsey number|01DSVCRF6X]] $R(n,n)$ satisfies

$$R(n,n) \ge \frac{n}{e\sqrt{2}}\, 2^{n/2}.$$

## Remarks

The bound shows that $R(n,n)$ grows at least exponentially in $n$, with base $\sqrt{2}$.
It is proved by the probabilistic method, which colours the edges at random.
