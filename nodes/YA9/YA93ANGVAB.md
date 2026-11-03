---
kind: statement
msc:
- 05A10
name: Recurrence for the falling factorial
role: lemma
sources:
- locator: source/s_genfunction_binom-app.ptx:6
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_genfunction_binom-app.ptx#L6
tag: YA93ANGVAB
uses:
- 0N5M924N3P
---

## Statement

Let $p$ be a number, and write $P(p,k)$ for the [[falling factorial|0N5M924N3P]] of $p$ of order $k$, that is, $P(p,k) = p(p-1)\cdots(p-k+1)$.
Then for every integer $k \ge 0$,
$$P(p,k+1) = P(p,k)\,(p-k).$$

## Remarks

Going from order $k$ to order $k+1$ adds one more factor, namely $p-k$, at the end of the product.
For $k = 0$ the claim reads $P(p,1) = p$, since the empty product is $1$.
