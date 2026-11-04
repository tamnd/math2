---
tag: NFGYSXBH72
kind: proof
name: Proof that the order modulo p divides p − 1
msc: [11A07]
proves: 0Y4B7P0GS8
uses: [0SBRX5CZ5R, 0M25PRN3WQ, 0CHQKZFK5S, 0SN0MAEKYX, 0GFKP8F8AG, 0J5VGJYYC3, 072D5G4SK6]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplicative_order
    locator: Properties
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$ be an integer with $p \nmid a$.
2. The only positive divisors of $p$ are $1$ and $p$, and $p \nmid a$. So $\gcd(a, p) = 1$, and $a$ is [[coprime|0GFKP8F8AG]] to $p$.
3. So the [[multiplicative order|0SBRX5CZ5R]] $k = \operatorname{ord}_p(a)$ is defined. It is the least positive integer with $a^k \equiv 1 \pmod p$.
4. By [[Fermat's little theorem|0M25PRN3WQ]], $a^{p-1} \equiv 1 \pmod p$.
5. By the [[division algorithm|0CHQKZFK5S]], there are integers $q$ and $r$ with $p - 1 = qk + r$ and $0 \le r < k$. Here $q \ge 0$, because $p - 1 \ge 0$ and $r < k$.
6. Then $a^{p-1} = (a^k)^q \cdot a^r$. Since $a^k \equiv 1$, [[powers|0J5VGJYYC3]] and [[products|072D5G4SK6]] of congruences give $a^{p-1} \equiv 1^q \cdot a^r = a^r \pmod p$.
7. With step 4 this gives $a^r \equiv 1 \pmod p$.
8. If $r > 0$, then $r$ is a positive integer less than $k$ with $a^r \equiv 1 \pmod p$. This contradicts the minimality of $k$.
9. So $r = 0$, and $p - 1 = qk$. Hence $\operatorname{ord}_p(a)$ divides $p - 1$.

## Idea

Fermat's little theorem says that the exponent $p - 1$ brings $a$ back to $1$. Any exponent that does so is a multiple of the order, since the remainder on division by the order would be a smaller such exponent.
