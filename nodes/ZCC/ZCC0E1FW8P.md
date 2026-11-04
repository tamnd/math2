---
kind: statement
msc:
- 11A25
name: Product formula for the totient function
role: theorem
sources:
- locator: source/s_inclusion-exclusion_euler-phi.ptx:43
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_inclusion-exclusion_euler-phi.ptx#L43
tag: ZCC0E1FW8P
uses:
- 0VV04M41AN
- 0SN0MAEKYX
---

## Statement

Let $n \ge 2$ be an integer. Suppose that $p_1, \dots, p_m$ are the distinct [[prime numbers|0SN0MAEKYX]] that divide $n$.
Then
$$\varphi(n) = n \prod_{i=1}^{m} \frac{p_i - 1}{p_i},$$
where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

Each factor equals $1 - 1/p_i$, so only the set of primes dividing $n$ matters, not their exponents.
For example, $12 = 2^2 \cdot 3$ gives $\varphi(12) = 12 \cdot \frac{1}{2} \cdot \frac{2}{3} = 4$.
