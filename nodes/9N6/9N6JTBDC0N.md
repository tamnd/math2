---
kind: statement
msc:
- 11A05
name: Euclidean algorithm step for the greatest common divisor
role: theorem
sources:
- locator: source/s_induction_recursion.ptx:223
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_recursion.ptx#L223
tag: 9N6JTBDC0N
uses:
- 0C8WYW4KYQ
- 0CHQKZFK5S
- 096PW7Q014
---

## Statement

Let $m$ and $n$ be positive integers with $m > n$.
Divide $m$ by $n$ with the [[division algorithm|0CHQKZFK5S]]. This gives the unique integers $q$ and $r$ with $m = qn + r$ and $0 \le r < n$.

If $r > 0$, then $\gcd(m, n) = \gcd(n, r)$, where $\gcd$ is the [[greatest common divisor|0C8WYW4KYQ]].

If $r = 0$, then $n$ [[divides|096PW7Q014]] $m$, and $\gcd(m, n) = n$.

## Remarks

The first case lets us replace the pair $(m, n)$ by the smaller pair $(n, r)$ without changing the gcd.
The second case ends the process.
