---
tag: EMSWBK1SPG
kind: proof
name: Proof of the multiplicativity of the Legendre symbol from Euler's criterion
msc: [11A15]
proves: 0NW1JP7TBR
uses: [01J8AMV9RS, 0M7DEDKSYB, 072D5G4SK6, 0TPW25CBN6]
sources:
  - url: https://proofwiki.org/wiki/Legendre_Symbol_is_Multiplicative
---

## Proof

1. Let $p$ be an odd prime and $a, b$ integers. Let $e = (p-1)/2$.
2. By [[Euler's criterion|0M7DEDKSYB]], $\left(\frac{ab}{p}\right) \equiv (ab)^e \pmod p$.
3. We have $(ab)^e = a^e b^e$. By Euler's criterion for $a$ and for $b$, and [[products of congruences|072D5G4SK6]], $a^e b^e \equiv \left(\frac{a}{p}\right) \left(\frac{b}{p}\right) \pmod p$.
4. So $u = \left(\frac{ab}{p}\right)$ and $v = \left(\frac{a}{p}\right) \left(\frac{b}{p}\right)$ satisfy $u \equiv v \pmod p$.
5. By the definition of the [[Legendre symbol|01J8AMV9RS]], $u$ and $v$ lie in $\set{-1, 0, 1}$. So $\abs{u - v} \le 2$.
6. Since $p \mid u - v$ and $p \ge 3 > \abs{u - v}$, we get $u - v = 0$.
7. Hence $\left(\frac{ab}{p}\right) = \left(\frac{a}{p}\right) \left(\frac{b}{p}\right)$.

## Idea

Euler's criterion turns the Legendre symbol into the power $a^{(p-1)/2}$ modulo $p$, and powers are multiplicative. Two numbers in $\set{-1, 0, 1}$ that agree modulo an odd prime are equal.
