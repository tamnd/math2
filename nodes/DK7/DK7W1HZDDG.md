---
kind: statement
name: Solvability of a linear Diophantine equation in two unknowns
role: theorem
msc:
- 11D04
- 11A05
sources:
- locator: source/s_induction_recursion.ptx:270
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_induction_recursion.ptx#L270
tag: DK7W1HZDDG
uses:
- 02WF878BH1
- 0R9GF3JD0K
about:
- 0R9GF3JD0K
---

## Statement

Let $m$, $n$ and $c$ be positive integers. Consider the [[linear Diophantine equation|0R9GF3JD0K]] $a m + b n = c$ in the unknowns $a$ and $b$, where $a$ and $b$ may be any integers, negative ones included.

This equation has an integer solution $(a, b)$ if and only if $c$ is a multiple of the [[greatest common divisor|02WF878BH1]] of $m$ and $n$.

## Remarks

One direction is easy. The number $\gcd(m, n)$ divides $a m + b n$ for all integers $a$ and $b$, so it divides $c$ when a solution exists.

The other direction follows from [[Bézout's identity|0DQVHMYAGA]]. If $c = k \gcd(m, n)$, multiply a Bézout pair by $k$.

For example, $6a + 10b = 7$ has no solution, since $\gcd(6, 10) = 2$ does not divide $7$. But $6a + 10b = 8$ has the solution $a = -2$, $b = 2$.
