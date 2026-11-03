---
tag: RNC7X1FQM1
kind: statement
name: Laws of exponents for nonnegative powers of a nonzero integer
role: theorem
msc:
  - 11A99
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_background_prop-integers.ptx#L122
    locator: source/s_background_prop-integers.ptx:122
---

## Statement

Let $x$ be a nonzero integer, and let $m$ and $n$ be nonnegative integers.
Then multiplying a power of $x$ by another power of $x$ adds the exponents: $x^m x^n = x^{m+n}$.
Raising a power of $x$ to a power multiplies the exponents: $(x^m)^n = x^{mn}$.

## Remarks

Here $x^0 = 1$, and $x^{k+1} = x^k x$ for $k \geq 0$.
Both laws follow by induction on $n$.
