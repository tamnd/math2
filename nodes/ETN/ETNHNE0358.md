---
tag: ETNHNE0358
kind: proof
name: Proof of Fermat's little theorem in the form a^p = a
msc: [11A07]
proves: 0BMXWXDVJZ
uses: [0M25PRN3WQ, 0SN0MAEKYX, 0TPW25CBN6, 096PW7Q014, 072D5G4SK6]
methods: [0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_little_theorem
    locator: lead section
---

## Proof

We argue by cases on whether $p$ divides $a$.

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $a$ be an integer.
2. Case $p \mid a$. Write $a = p s$ with an integer $s$. Since $p \ge 2$, we have $a^p - a = p s (a^{p-1} - 1)$.
3. So $p$ [[divides|096PW7Q014]] $a^p - a$, and $a^p \equiv a \pmod p$ by the definition of [[congruence|0TPW25CBN6]].
4. Case $p \nmid a$. By [[Fermat's little theorem|0M25PRN3WQ]], $a^{p-1} \equiv 1 \pmod p$.
5. Since $a \equiv a \pmod p$, [[compatibility with multiplication|072D5G4SK6]] gives $a^{p-1} \cdot a \equiv 1 \cdot a \pmod p$, that is, $a^p \equiv a \pmod p$.
6. In both cases, $a^p \equiv a \pmod p$.

## Idea

When $p$ divides $a$, both sides are multiples of $p$. Otherwise, multiply Fermat's congruence $a^{p-1} \equiv 1$ by $a$.
