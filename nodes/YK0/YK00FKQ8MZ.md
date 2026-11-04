---
tag: YK00FKQ8MZ
kind: proof
name: Proof that congruence is compatible with powers
msc: [11A07]
proves: 0J5VGJYYC3
uses: [0TPW25CBN6, 096PW7Q014, 072D5G4SK6]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: Basic properties
---

## Proof

We argue by induction on $k$.

1. Let $n$ be a positive integer, and let $a$ and $b$ be integers with $a \equiv b \pmod n$.
2. Base case $k = 0$: we have $a^0 = 1 = b^0$. Since $n$ [[divides|096PW7Q014]] $1 - 1 = 0$, we get $a^0 \equiv b^0 \pmod n$ by the definition of [[congruence|0TPW25CBN6]].
3. Induction step: let $k \ge 0$ and assume $a^k \equiv b^k \pmod n$.
4. By step 3, by step 1 and by [[compatibility with multiplication|072D5G4SK6]], $a^k \cdot a \equiv b^k \cdot b \pmod n$.
5. That is, $a^{k+1} \equiv b^{k+1} \pmod n$.
6. By steps 2 to 5 and induction, $a^k \equiv b^k \pmod n$ for each natural number $k$.

## Idea

A power is a repeated product. Each new factor $a$ can be replaced by $b$ without changing the class modulo $n$, by compatibility with multiplication, so induction on the exponent finishes the proof.
